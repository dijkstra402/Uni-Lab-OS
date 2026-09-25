# # Python Class for FLIR Systems' Blackfly USB Camera
#
# By Chris Arcadia (2021/01/11)
#
# Intended for use with the Blackfly S USB3 Camera 
#
# Inspired by the following Repositories: 
#   * "Acquisition.py" (from "Spinnaker-Python3-Examples" by FLIR Systems, in Python, in [firmware download](https://flir.custhelp.com/app/account/fl_downloads))
#   * "Enumeration.py" (from "Spinnaker-Python3-Examples" by FLIR Systems, in Python, in [firmware download](https://flir.custhelp.com/app/account/fl_downloads))

import time
import numpy
import os
import PySpin
from matplotlib import pyplot

class BlackFlyPy():

    def __init__(self):
        self.load_options()
        self.load_constants()
        self.set_path()    
        self.initialize_system()
        self.load_system_info()

    def load_options(self):
        self.verbose = True
        self.record = True # unimplemented option to save each read step or position value to text (along with a timestamp)

    def load_constants(self):
        # load constants specific to Blackfly

        self.hardware = {
            'interface':'USB 3', 
            'manufacturer': 'FLIR Systems', 
            'camera':'Blackfly S',
        } # known hardware details

        self.units = {
            'time': 's',
        }           

    def set_path(self,pathOut=None):
        self.path = dict();        
        self.path['root'] = os.path.dirname(__file__)
        if not pathOut:
            # provide default output path
            pathOut = os.path.join(self.path['root'],'__temporary__')      
            self.ensure_path(pathOut)                
        self.path['output'] = pathOut                            

    def ensure_path(self,path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def notify(self,message):
        if self.verbose:
            print('BlackFlyPy: '+message) 

    def initialize_system(self):
        self.get_system()
        self.get_interfaces()
        self.get_cameras()  

    def get_system(self):
        try:
            self.system = PySpin.System.GetInstance()
            self.loaded = True
            self.notify('System initialized with library version '+self.get_library_version())                                
        except:
            self.system = None
            self.loaded = False                                     

    def get_library_version(self):
        version = None
        if self.loaded:
            version = self.system.GetLibraryVersion()
            version = '%d.%d.%d.%d' % (version.major, version.minor, version.type, version.build)            
        return version
        
    def get_interfaces(self):
        self.interfaces = None 
        if self.loaded:    
            try:            
                self.interfaces = self.system.GetInterfaces()
                self.notify('Found %i interfaces.' % self.about_interfaces()['count'])
            except: 
                pass                
        return self.interfaces

    def about_interfaces(self):
        info = {'count':0,'name':[],'index':[]}    
        if self.loaded and self.interfaces:
            info['count'] = self.interfaces.GetSize()
            info['index'] = list(range(info['count']))
            for interface in self.interfaces:
                nodemap = interface.GetTLNodeMap()
                name = self.get_nodemap_property(nodemap,'InterfaceDisplayName')
                info['name'].append(name)
        return info   

    def clear_interfaces(self):
        if self.loaded and self.interfaces:
            self.interfaces.Clear()

    def get_nodemap_property(self,nodemap,field):
        value = None
        try:
            ptr = PySpin.CStringPtr(nodemap.GetNode(field))
            if PySpin.IsAvailable(ptr) and PySpin.IsReadable(ptr):
                value = ptr.GetValue()
        except:
            pass
        return value
    

    def get_cameras(self):
        self.cameras = None 
        if self.loaded:    
            try:            
                self.cameras = self.system.GetCameras()
                self.notify('Detected %i cameras.' % self.about_cameras()['count'])
            except: 
                pass
        return self.cameras

    def about_cameras(self):
        info = {'count':0,'name':[],'index':[],'vendor':[]}    
        if self.loaded and self.cameras:
            info['count'] = self.cameras.GetSize()
            info['index'] = list(range(info['count']))            
            for camera in self.cameras:
                nodemap = camera.GetTLDeviceNodeMap()
                vendor = self.get_nodemap_property(nodemap,'DeviceVendorName')
                model = self.get_nodemap_property(nodemap,'DeviceModelName')
                info['name'].append(model)
                info['vendor'].append(vendor)
        return info   


    def clear_cameras(self):
        if self.loaded and self.cameras:
            self.cameras.Clear()

    def get_system_info(self):
        info = dict()
        info['libraryVersion'] = self.get_library_version()
        info['interfaces'] = self.about_interfaces()
        info['cameras'] = self.about_cameras()
        return info

    def load_system_info(self):
        self.info = self.get_system_info()
            
    def release(self):
        if self.loaded:
            self.clear_cameras()
            self.clear_interfaces()
            self.system.ReleaseInstance()      

    def initialize_camera(self,index=0):
        if self.loaded and self.cameras and index<self.about_cameras()['count']:
            try:
                camera = self.cameras[index]
                camera.Init()
            except:
                pass

    def deinitialize_camera(self,index=0):
        if self.loaded and self.cameras and index<self.about_cameras()['count']:
            try:
                camera = self.cameras[index]
                camera.DeInit()
            except:
                pass

    def get_camera_information(self,index=0):
        info = dict()
        if self.loaded and self.cameras and index<self.about_cameras()['count']:
            try:
                camera = self.cameras[index]
                nodemap = camera.GetTLDeviceNodeMap()
                info_ptr = PySpin.CCategoryPtr(nodemap.GetNode('DeviceInformation'))
                if PySpin.IsAvailable(info_ptr) and PySpin.IsReadable(info_ptr):
                    features = info_ptr.GetFeatures()
                    for feature in features:
                        ptr = PySpin.CValuePtr(feature)
                        if PySpin.IsReadable(ptr):
                            field = ptr.GetName()
                            value = ptr.ToString()
                            info.update({field:value})
            except:
                pass
        return info

    def get_camera_image(self,index=0,timeout=1): # timeout specified in seconds      
        info = dict()
        data = None
        if self.loaded and self.cameras and index<self.about_cameras()['count']:
            try:
                camera = self.cameras[index]
                
                nodemap = camera.GetTLDeviceNodeMap()
                serial = self.get_nodemap_property(nodemap,'DeviceSerialNumber')
                filename = 'Image-'+str(serial)+'-'+'.jpg'
                fullfilename = os.path.join(self.path['output'],filename)

                self.notify('Starting image acquisition.')                
                camera.BeginAcquisition()

                try:
                    image = camera.GetNextImage(round(timeout*1e3))
                    if image.IsIncomplete():
                        self.notify('Image incomplete with image status %d ...' % image.GetImageStatus())
                    else:
                        info = {'width':image.GetWidth(),
                                'height':image.GetHeight(),
                                'timestamp':image.GetTimeStamp(), # time stamp is in nanoseconds
                                }
                        data = image.GetNDArray()
                        image_converted = image.Convert(PySpin.PixelFormat_Mono8, PySpin.HQ_LINEAR)
                        image_converted.Save(fullfilename)
                        self.notify('Image captured with the following details: \n' + str(info))
                    image.Release()
                except:
                    pass
                
                self.notify('Ending image acquisition.')                                                
                camera.EndAcquisition()

            except:
                pass
        return [data,info]


if __name__ == "__main__":

    # set camera ID to the first available camera
    cid = 0 
 
    # instantiate class
    blackfly = BlackFlyPy()    

    # get device info
    info = blackfly.get_camera_information(index=cid)    
    print('Selected Device Info: \n'+str(info))

    # aquire images
    blackfly.initialize_camera(index=cid)  
    result = blackfly.get_camera_image(index=cid)
    if result[0]:
        pyplot.imshow(result[0],cmap='gray')
    blackfly.deinitialize_camera(index=cid)
    
    # todo:
    # - set image acuired exposure and gain
    # - clean-up get_camera_image method
    # - append desired image metadata to image or associated text file


# -*- coding: utf-8 -*-
