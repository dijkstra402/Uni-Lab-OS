import numpy as np
from pymodaq.utils.daq_utils import ThreadCommand
from pymodaq.utils.data import DataFromPlugins, Axis, DataToExport
from pymodaq.control_modules.viewer_utility_classes import DAQ_Viewer_base, comon_parameters, main
from pymodaq.utils.parameter import Parameter
from pymodaq.utils.parameter import utils

from pyvisa import ResourceManager  
# Import the pywin32 library, this library allow the control of other applications.
# Used here for LeCroy.ActiveDSOCtrl.1
# The methods of ActiveDSO are described in the documentation Lecroy ActiveDSO Developers Guide
from lecroydso import ActiveDSO, LeCroyDSO
import time
# It seems important to initialize active_dso outside the class (???)
# If not pymodaq will not allow the initialization of the detector.

VISA_rm = ResourceManager()
resources = list(VISA_rm.list_resources())
usb_address = "USBTMC:" + resources[0]
activeDSO = ActiveDSO(usb_address)

# This does not work over the local network at least. Maybe with a direct connection to the scope.
#IP_adress = 'IP:169.254.137.210'
#activeDSO = ActiveDSO(IP_adress)


def numString2Int(num_string):
    num_string = num_string.replace('K','000')
    num_string = num_string.replace('MA','000000')
    return int(num_string)

class DAQ_1DViewer_LecroyWaverunner(DAQ_Viewer_base):
    """ Instrument plugin class for a 1D viewer.
    
    This object inherits all functionalities to communicate with PyMoDAQ’s DAQ_Viewer module through inheritance via
    DAQ_Viewer_base. It makes a bridge between the DAQ_Viewer module and the Python wrapper of a particular instrument.

    TODO Complete the docstring of your plugin with:
        * The set of instruments that should be compatible with this instrument plugin.
        * With which instrument it has actually been tested.
        * The version of PyMoDAQ during the test.
        * The version of the operating system.
        * Installation instructions: what manufacturer’s drivers should be installed to make it run?

    Attributes:
    -----------
    controller: object
        The particular object that allow the communication with the hardware, in general a python wrapper around the
         hardware library.
         
    # TODO add your particular attributes here if any

    """
    def makeChannelsParameterTree():
        params = []
        for i in 1+np.arange(4):
            params.append({'title': None,
                'name': f'C{i}',
                'type': 'bool',
                'value': True,
                'expanded': False,
                'renamable':True,
                'children':
                [{'title': 'Vertical/Div',
                'name': f'VScale_C{i}',
                'type': 'float',
                'value': 2,                 
                },
                {'title': 'Offset',
                'name': f'offset_C{i}',
                'type': 'float',
                'value': 0,                 
                },        
                {'title': 'Display',
                'name': f'doDisplay_C{i}',
                'type': 'bool',
                'value': True,
                }                                       
                ]             
            },                    
            )
        return params
    params = comon_parameters + [
            {'title': 'VISA:',
             'name': 'VISA_ressources',
             'type': 'list',
             'values': ''},
             {
             'title': 'Channels:',
             'name': 'channels',
             'type': 'group',
             'children': makeChannelsParameterTree()}]
    
    params += [
        {'title': 'Horizontal axis',
             'name': 'tGroup',
             'type': 'group',
            'children': [        
        {'title': 't0',
             'name': 'tOffset',
             'type': 'float',
            'limits': [-np.inf, np.inf],
            'value': -1e-6,          
            'step': 1e-9,
        },             
        {'title': 'Time/Div',
             'name': 'tDiv',
             'type': 'list',
            'limits': ['1NS','2NS','5NS','10NS','20NS','50NS','100NS','200NS','500NS','1US','2US','5US','10US','20US','50US','100US','200US','500US','1MS','2MS','5MS','10MS','20MS','50MS','100MS','200MS','500MS','1S','2S','5S','10S','20S','50S','100S'],
            'value': '100NS',
        },        
            ]  
        },                          
        {'title': 'Trigger',
             'name': 'triggerGroup',
             'type': 'group',
            'children': [      
        {'title': 'source',
             'name': 'triggerSource',
             'type': 'list',
            'limits': ["EXT","C1", "C2", "C3", "C4","EXT10"],
            'value':"EX",
        },                                    
        {'title': 'delay',
             'name': 'triggerDelay',
             'type': 'float',
            'limits': [-np.inf, np.inf],
            'value': -1e-6,          
            'step': 1e-9,
        },
        {'title': 'level',
             'name': 'triggerLevel',
             'type': 'float',
            'limits': [-4, 4],
            'value': 0.15,          
            'step': 0.01,
        'suffix': 'V',
        'finite': True,
        'dec': True,
        },                
        {'title': 'mode',
             'name': 'triggerMode',
             'type': 'list',
            'limits': ['AUTO', 'NORMAL', 'STOPPED', 'SINGLE'],
            'value': "NORMAL",
        },                   
        ],     
        },
        {'title': 'Display',
             'name': 'doDisplay',
             'type': 'bool',
            'value': False,        
        },      
        {'title': 'Persistence',
             'name': 'doPersistence',
             'type': 'bool',
            'value': True,        
        },                          
        {'title': 'Sequence',
             'name': 'number_of_segments',
             'type': 'int',
            'limits': [1, np.inf],
            'value': 1,
        },    
        {'title': 'Memory Size',
             'name': 'memorySize',
             'type': 'list',
            'limits': ['500','1000','2500','5000','10K','25K','50K','100K','250K','500K','1MA','2.5MA','5MA','10MA','25MA','50MA','100MA'],
            'value': '10K',          
        },    
        {'title': 'GrabPerSecond',
             'name': 'GPS',
             'type': 'float',
            'limits': [0, np.inf],
            'value': 0,
            'enabled':False          
        },    
        {'title': 'TreatmentPerSecond',
             'name': 'TPS',
             'type': 'float',
            'limits': [0, np.inf],
            'value': 0,
            'enabled':False          
        }, 

        {'title': 'Clear sweep',
             'name': 'clear_sweeps',
             'type': 'bool',
            'value': True,
        },        
        {'title': 'Force trigger',
             'name': 'force_trigger',
             'type': 'bool',
            'value': False,
        },                
        ]
             



    def ini_attributes(self):
        #  TODO declare the type of the wrapper (and assign it to self.controller) you're going to use for easy
        #  autocompletion
        self.controller: LeCroyDSO = None
        # TODO declare here attributes you want/need to init with a default value
        self.x_axis = None
        self.start = 0
        self.end = 0
        self.isRunning = False


    def __init__(self, parent=None, params_state=None):
        super().__init__(parent, params_state)


    def commit_settings(self, param: Parameter):
        """Apply the consequences of a change of value in the detector settings

        Parameters
        ----------
        param: Parameter
            A given parameter (within detector_settings) whose value has been changed by the user
        """
        ## TODO for your custom plugin
        self.changingSettings = True
        if param.name() == "triggerSource":
            self.controller.set_trigger_source(param.value())
        elif param.name() == "triggerMode":
            self.controller.set_trigger_mode(param.value())
        elif param.name() == "triggerLevel":
            self.controller.set_trigger_level(self.settings.child('triggerGroup','triggerSource').value(),param.value())
        elif param.name() == "triggerDelay":
            self.controller.write(f'TRIG_DELAY {param.value()}')
        elif param.name() == "number_of_segments":
            if param.value()>1:
                self.controller.set_sample_mode('SEQUENCE',param.value())
            else:
                self.controller.set_sample_mode('REALTIME')
            self.getSegArray()                
        elif param.name()[:-1] == "C":
            self.updateChannelList()
        elif param.name()[:-1] == "VScale_C":
            self.controller.set_ver_scale(f'C{int(param.name()[-1])}',param.value())
        elif param.name()[:-1] == "VOffset_C":
            self.controller.set_ver_offset(f'C{int(param.name()[-1])}',param.value())
        elif param.name()[:-1] == "doDisplay_C":
            if param.value():
                self.controller.write(f'C{int(param.name()[-1])}:TRA ON')
            else:
                self.controller.write(f'C{int(param.name()[-1])}:TRA OFF')
        elif param.name() == 'tDiv': #In seconds, convert 1NS in 1e-9
            self.controller.write(f'TDIV {param.value()}')
        elif param.name() == 'tOffset':
                self.controller.set_hor_offset(param.value())
        elif param.name() =='doDisplay':
            if param.value():
                self.controller.write('DISP ON')
            else:
                self.controller.write('DISP OFF')          
        elif param.name() == 'doPersistence':
            if param.value():
                self.controller.write('PERS ON')
            else:
                self.controller.write('PERS OFF')          
        elif param.name() =='memorySize':
            self.controller.write(f'MSIZ {param.value()}')
        elif param.name() == 'clear_sweeps':
            self.controller.clear_sweeps()
        elif param.name() == 'force_trigger':
            self.controller.write('FRTR')
        self.changingSettings = False
        if self.isRunning:
            time.sleep(0.5)

    def getSegArray(self,):
        L_seg = (numString2Int(self.settings.child('memorySize').value())+2)
        self.segArray = range(0,self.settings.child('number_of_segments').value()*L_seg,L_seg)
    def updateChannelList(self):
        channelList = []
        for i in range(4):
            if self.settings.child('channels',f'C{i+1}').value():
                channelList.append(self.settings.child('channels',f'C{i+1}').name())                
            self.settings.child('channels',f'C{i+1}',f'doDisplay_C{i+1}').setValue(self.settings.child('channels',f'C{i+1}').value())
            self.commit_settings( self.settings.child('channels',f'C{i+1}',f'doDisplay_C{i+1}'))
        self.channelList = channelList
        ##
    def ini_detector(self, controller=None):
        """Detector communication initialization

        Parameters
        ----------
        controller: (object)
            custom object of a PyMoDAQ plugin (Slave case). None if only one actuator/detector by controller
            (Master case)

        Returns
        -------
        info: str
        initialized: bool
            False if initialization failed otherwise True
        """        

        # self.controller = LeCroyDSO(activeDSO)
        self.ini_detector_init(old_controller=controller,
                            new_controller=LeCroyDSO(activeDSO))
        
        # self.controller.write('*RST')
        [self.commit_settings(param) for param in utils.iter_children_params(self.settings)]

        ## TODO for your custom plugin
        # get the x_axis (you may want to to this also in the commit settings if x_axis may have changed
        # data_x_axis = self.controller.your_method_to_get_the_x_axis()  # if possible
        # self.x_axis = Axis(data=data_x_axis, label='', units='', index=0)

        # # TODO for your custom plugin. Initialize viewers pannel with the future type of data
        # self.dte_signal_temp.emit(DataToExport(name='myplugin',
        #                                        data=[DataFromPlugins(name='Mock1',
        #                                                              data=[np.array([0., 0., ...]),
        #                                                                    np.array([0., 0., ...])],
        #                                                              dim='Data1D', labels=['Mock1', 'label2'],
        #                                                              axes=[self.x_axis])]))

        info = "Whatever info you want to log"
        initialized = True
        return info, initialized

    def close(self):
        """Terminate the communication protocol"""
        self.controller=None

    def grab_data(self, Naverage=1, **kwargs,):
        """Start a grab from the detector

        Parameters
        ----------
        Naverage: int
            Number of hardware averaging (if hardware averaging is possible, self.hardware_averaging should be set to
            True in class preamble and you should code this implementation)
        kwargs: dict
            others optionals arguments
        """
        ## TODO for your custom plugin: you should choose EITHER the synchrone or the asynchrone version following
        self.isRunning = True
        if not self.changingSettings:
            self.start = time.time()
            data_temp=[]
            L_seg = (numString2Int(self.settings.child('memorySize').value())+2)
            for i,c in enumerate(self.channelList):
                firstChannel = True
                if self.settings.child('channels',c).value():
                    if firstChannel:
                        t, wf_temp = self.controller._conn.aDSO.GetScaledWaveformWithTimes(f'C{i+1}',1e8,0) #Getting data
                        t = np.array(t)
                        firstChannel = False
                    else:
                        wf_temp = self.controller._conn.aDSO.GetScaledWaveform(c,1e8,0)

                    wf_temp = np.array(wf_temp)
                    if self.settings.child('number_of_segments').value()>1:
                        wf_temp = np.mean([wf_temp[seg:seg+L_seg] for seg in self.segArray],axis=0)
                        t=t[:L_seg]

                    data_temp.append(wf_temp) #Adding waveform to data

            self.x_axis = Axis(data=t, label='Time of flight', units='s', index=0)
            self.end = time.time()

            self.settings.child('TPS').setValue(self.end-self.start) 

            self.dte_signal.emit(DataToExport('myplugin',
                                                data=[DataFromPlugins(name='test', data=data_temp,
                                                                    dim='Data1D', labels=self.channelList,
                                                                    axes=[self.x_axis])]))
            # except Exception as e:
            #     self.emit_status(ThreadCommand('Error during grab', [f'{e}']))
            #     return
            ##asynchrone version (non-blocking function with callback)
            # self.controller.your_method_to_start_a_grab_snap(self.callback)
            #########################################################
        self.isRunning = False

    def callback(self):
        """optional asynchrone method called when the detector has finished its acquisition of data"""
        data_tot = self.controller.your_method_to_get_data_from_buffer()
        self.dte_signal.emit(DataToExport('myplugin',
                                          data=[DataFromPlugins(name='Mock1', data=data_tot,
                                                                dim='Data1D', labels=['dat0', 'data1'])]))

    def stop(self):
        """Stop the current grab hardware wise if necessary"""
        ## TODO for your custom plugin
        # raise NotImplemented  # when writing your own plugin remove this line
        # self.controller.your_method_to_stop_acquisition()  # when writing your own plugin replace this line
        # self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))
        # ##############################
        return ''


if __name__ == '__main__':
    main(__file__)
