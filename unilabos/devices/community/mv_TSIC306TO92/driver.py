import io
import serial
from pyvisa_device import device
from old_code.utils import logging
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

log = logging.child_logger(__file__)

class TSIC306TO92(device):
    """
    TSIC306TO92 temperature sensor.

    Example:
    -------------

    """


    def __init__(self, port="COM7"):

        log.info("Initialising device.")

        self.port = port
        self.baudrate = 9600
        self.timeout = 0.001
        self.ser = serial.Serial(self.port,self.baudrate,timeout=self.timeout) # this should only be executed once
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))
        if self.ser.isOpen():
            log.info('TSIC306TO92 is open')
        else:
            log.warning('Failed to open TSIC306TO92')

        self.sio.flush()    # it is buffering. required to get the data out *now*

        self.pid_term0 = None
        self.pid_term1 = None
        self.pid_term2 = None

        self.start_time=None

    def create_figure(self):
        plt.ion()

        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.xss = []
        self.ys = []

        # Format plot
        self.ax.set(xticklabels=[])

        plt.ylabel('Temperature')
        plt.xlabel('Time')
        plt.subplots_adjust(bottom=0.1)

    # This function is called periodically from FuncAnimation
    def update_figure(self, temperature=None, target_temperature=-20, time_now=None, pid_terms=None):

        # Add x and y to lists
        if temperature is None:
            temperature = self.read_temperature()
        if time_now is None:
            time_now = dt.datetime.now()

        if self.start_time is None:
           self.start_time = time_now

        self.ys.append(temperature)
        self.xs.append(time_now.strftime('%H:%M:%S.%f'))

        # time_now = time_now.strftime('%H:%M:%S.%f').split(".")[0]
        # self.xss.append(time_now)

        # Limit x and y lists to 20 items
        self.xs = self.xs[-1500:]
        self.ys = self.ys[-1500:]
        
        ymin, ymax = min(self.ys), max(self.ys)
        yrange = ymax - ymin
        
        self.ax.set_xlim(self.xs[0], self.xs[-1])
        self.ax.set_ylim(ymin - max(yrange*0.1, 0.2), ymax + max(yrange*0.1,0.2))

        self.ax.plot([min(self.xs),max(self.xs)], [target_temperature, target_temperature], linestyle="--", color="black")
        
        if self.pid_term0 is not None:
            self.pid_term0.remove()
        if self.pid_term1 is not None:
            self.pid_term1.remove()
        if self.pid_term2 is not None:
            self.pid_term2.remove()

        if pid_terms and pid_terms[0] is not None:
            self.pid_term0 = self.ax.text(0.03,0.04, f"P = {round(pid_terms[0],3)}", horizontalalignment='left', verticalalignment='bottom', transform=self.ax.transAxes)
            self.pid_term1 = self.ax.text(0.03,0.08, f"I = {round(pid_terms[1],3)}", horizontalalignment='left', verticalalignment='bottom', transform=self.ax.transAxes)
            self.pid_term2 = self.ax.text(0.03,0.12, f"D = {round(pid_terms[2],3)}", horizontalalignment='left', verticalalignment='bottom', transform=self.ax.transAxes)
        
        # Draw x and y lists                          
        self.ax.plot(self.xs, self.ys, color="black")

        time_diff = (time_now - self.start_time)
        plt.title(f'Time: {time_diff}')
        
        # drawing updated values
        self.fig.canvas.draw()
    
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        self.fig.canvas.flush_events()
    
        # Set attribute functions
        # ---------------------------------


    # Read attribute functions
    # ---------------------------------
    def read_temperature(self, sample=5):
        log.debug(f"Read temperature")
        self.sio.flush()

        temps = []
        for i in range(sample):
            temp_c = ''
            while temp_c=='' or float(temp_c.split(":")[-1]) <= -50.0 or float(temp_c.split(":")[-1]) > 100:
                temp_c = self.sio.read()
            
            temps.append(float(temp_c.split(":")[-1]))

        median = np.median(temps)

        log.debug(f"Median {median}")

        # sort out values that are more than 2C away from median (probably bad measurements)
        temps = np.array([x for x in filter(lambda t, m=median: abs(t - m) < 2, temps)])

        if len(temps) == 0:
            mean = self.read_temperature()
        else:
            mean = np.mean(temps)

        log.debug(f"Mean {mean}")

        return mean
