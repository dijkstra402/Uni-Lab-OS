# Imports from the python standard library:
import time

# Third party imports, installable via pip:
import serial

class Controller:
    '''
    Basic device adaptor for the Ohaus Explorer Semi-Micro Balance EX225D/AD.
    Many more commands are available and have not been implemented.
    '''
    def __init__(self,
                 which_port,
                 name='ohaus_EX225D/AD',
                 verbose=True,
                 very_verbose=False):
        self.name = name
        self.verbose = verbose
        self.very_verbose = very_verbose
        # open serial port:
        if self.verbose: print("%s: opening..."%name, end='')
        try:
            self.port = serial.Serial(
                port=which_port, baudrate=9600, timeout=1)
        except serial.serialutil.SerialException:
            raise IOError('No connection to %s on port %s'%(name, which_port))
        if self.verbose: print(" done.")
        # check status:
        self._get_software_version()
        self._get_serial_number()
        self._get_current_mode()

    def _send(self, cmd, response_lines):
        cmd = bytes(cmd + '\r\n', encoding='ascii')
        if self.very_verbose:
            print("%s: sending cmd = %s"%(self.name, cmd))
        self.port.write(cmd)
        responses = []
        for i in range(response_lines):
            response = self.port.readline().decode('ascii').strip()
            responses.append(response)
            if self.very_verbose:
                print("%s: response (%i) = %s"%(self.name, i, response))
        if self.port.in_waiting != 0:
                r = self.port.readline().decode('ascii').strip()
                raise Exception("%s: unexpected response = %s"%(self.name, r))
        return responses

    def _get_software_version(self):
        if self.verbose:
            print("%s: getting software version"%self.name)
        self.software_version = self._send('PV', response_lines=1)[0]
        if self.verbose:
            print("%s:  = %s "%(self.name, self.software_version))
        return self.software_version

    def _get_serial_number(self):
        if self.verbose:
            print("%s: getting software version"%self.name)
        self.serial_number = self._send('PSN', response_lines=1)[0]
        if self.verbose:
            print("%s:  = %s "%(self.name, self.serial_number))
        return self.serial_number

    def _get_current_mode(self):
        if self.verbose:
            print("%s: getting immediate weight"%self.name)
        self.current_mode = self._send('PM', response_lines=1)[0]
        if self.verbose:
            print("%s:  = %s "%(self.name, self.current_mode))
        return self.current_mode

    def move_door(self, direction, wait_s=3):
        if self.verbose:
            print("%s: moving door = %s"%(self.name, direction))
        assert direction in (
            'open_left', 'open_right', 'open_both', 'close_both')
        if direction == 'open_left':
            assert self._send('WI 1 0', response_lines=1)[0] == 'WI A'
        if direction == 'open_right':
            assert self._send('WI 0 1', response_lines=1)[0] == 'WI A'
        if direction == 'open_both':
            assert self._send('WI 1 1', response_lines=1)[0] == 'WI A'
        if direction == 'close_both':
            assert self._send('WI 0 0', response_lines=1)[0] == 'WI A'
        time.sleep(wait_s) # responds immediately but takes up to ~3s?!
        if self.verbose:
            print("%s: -> done moving door."%self.name)
        return None

    def zero(self, wait_s=10):
        if self.verbose:
            print("%s: zeroing..."%self.name)
        assert self._send('Z', response_lines=1)[0] == 'OK!'
        time.sleep(wait_s) # responds immediately but takes up to ~10s?!
        if self.verbose:
            print("%s: -> done zeroing."%self.name)
        return None

    def tare(self, wait_s=10):
        if self.verbose:
            print("%s: tareing..."%self.name)
        assert self._send('T', response_lines=1)[0] == 'OK!'
        time.sleep(wait_s) # responds immediately but takes up to ~10s?!
        if self.verbose:
            print("%s: -> done tareing."%self.name)
        return None

    def get_immediate_weight(self):
        if self.verbose:
            print("%s: getting immediate weight"%self.name)
        self.immediate_weight = self._send('IP', response_lines=4)[0].split()
        if self.verbose:
            print("%s:  = %s (%s)"%(
                self.name, self.immediate_weight[0], self.immediate_weight[1]))
        return self.immediate_weight

    def close(self):
        if self.verbose: print("%s: closing..."%self.name, end=' ')
        self.port.close()
        if self.verbose: print("done.")

if __name__ == '__main__':
    balance = Controller(which_port='COM9', verbose=True, very_verbose=False)

##    balance.move_door(direction='open_left')
##    balance.move_door(direction='close_both')

##    balance.move_door(direction='open_right')
##    balance.move_door(direction='close_both')
    
##    balance.move_door(direction='open_both')
##    balance.move_door(direction='close_both')

##    balance.zero()
##    balance.tare()

    for i in range(3): # tested to 1000 iterations
        print('iteration = %i'%i)
        immediate_weight = balance.get_immediate_weight()[0]

    balance.close()
