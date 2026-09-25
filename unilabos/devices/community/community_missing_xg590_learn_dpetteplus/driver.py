import serial, time

class DPETTE():
    def __init__(self, port='/dev/ttyUSB0'):
        self.CMD = 'HELLO'
        self.CMD_TABLE = {
        # Info
        'HELLO'	      : 0xA0, # 握手 handshake
        'INFO'	      : 0xA1, # 读取仪器设置信息 read setting info of the pipette (invalid command)
        'STA'	      : 0xA2, # 读取仪器状态信息 read status  info of the pipette (invalid command)
        'EE_READ'	  : 0xA3, # 读取EEPROM参数  read parameters in EEPROM
        'EE_WRITE'	  : 0xA4, # 写入EEPROM参数  write para in EEPROM
        'DEMARCATE'	  : 0xA5, # 标定模式        calibration mode
        'DMRCT_VOLUM' : 0xA6, # 设置标定体积     calibrate the volume
        'RESET'	      : 0xA7, # 恢复出厂设置     factory reset
        'DMRCT_PULSE' : 0xA8, # 设置标定脉冲     calibrate pulse ???
        # Control
        'WOL'	      : 0xB0, # 远程            working mode (pipetting, dilusion or splitting)
        'SPEED'	      : 0xB1, # 设置速度 —吸液速度 排液度 set the speed of sucking and blowing liquid
        'PI_VOLUM'	  : 0xB2, # 设置PI体积       set the volume of pipetting
        'KEY'	      : 0xB3, # 吸排液           sucking or blowing 
        'ST_VOLUM'	  : 0xB4, # 设置ST体积       set the volume of each splitting 
        'ST_NUM'	  : 0xB5, # 设置ST次数       set the number of splitting 
        'DI1_VOLUM'	  : 0xB6, # 设置DI体积       set the volume of first dilusion 
        'DI2_VOLUM'	  : 0xB7, # 设置DI体积       set the volume of second dilusion
        }
        self.serial = serial.Serial(port     = '/dev/ttyUSB0',      # 电枪串口
                                    baudrate = 9600,                # 波特率
                                    parity   = serial.PARITY_NONE,  # 奇偶校验
                                    bytesize = serial.EIGHTBITS,    # 数据位
                                    stopbits = serial.STOPBITS_ONE) # 停止位
        self.reply = []
        return None

    def send(self, CMD, *args): 
        time.sleep(1)                                  # Give the pipette some time to rest 
        self.CMD = CMD 
        cmd = [0xFE, self.CMD_TABLE[self.CMD]]         # First two bytes
        cmd.extend(args)                               # All arguments end in the cmd
        checksum = sum(cmd[1:]) & 0xFF                 # checksum calculation
        [cmd.append(0x00) for _ in range(3-len(args))] # padding so the len of total bytes is 5 
        cmd.append(checksum)                           # append the checksum 
        #print([hex(i) for i in list(cmd)])
        self.serial.write(bytes(cmd))                  # list to byte string
        return None
    
    def receive(self, debug=False):
        time.sleep(1)                                  # Give the pipette some time to rest 
        if self.CMD in ['HELLO', 'INFO', 'WOL', 'SPEED', 'PI_VOLUM', 'KEY']:
            reply = list(self.serial.read(6)) 
            if     reply[ 0] == 0xFD                     \
               and reply[ 1] == self.CMD_TABLE[self.CMD] \
               and reply[-1] == sum(reply[1:-1]) & 0xFF:
               if debug : print('Response received')
            else:
                print('Response corrupted')
            self.reply = reply
        else:
            print('Illegal command') 
        return None
        
    def hello(self):
        self.send('HELLO')
        self.receive() 
        if   self.reply[2] == 0:
            print('Handshaking succeeded')
        elif self.reply[2] == 1:
            print('Handshaking failed')
        return None
        
    def get_pipette_info(self):
        self.send('INFO')
        self.receive() 
        if   self.reply[2] == 1:
            print('Single Channel Pipette')
        elif self.reply[2] == 2:
            print('Multiple Channel Pipette')
        print(f'Volume: {self.reply[3]<<8 | self.reply[4]}') 
        return None
        
    def set_mode(self, mode):
        if mode in ['PI', 'ST', 'DI']:
            # PI: Pipette, ST: Split, DI: Dilusion
            self.send('WOL', {'PI': 1, 'ST': 2, 'DI': 3}[mode])
            self.receive() 
            if   self.reply[2] == 0:
                print('Mode setting succeeded')
            elif self.reply[2] == 1:
                print('Mode setting failed')
        else:
            print('Mode could only be PI, ST or DI')
        return None
            
    def set_speed(self, direction, speed):
        if direction in ['Suck', 'suck', 'Blow', 'blow'] and speed in [1, 2, 3]:
            self.send('SPEED', {'Suck':1, 'suck':1, 'Blow':2, 'blow':2}[direction], speed)
            self.receive()
            if   self.reply[2] == 0:
                print('Speed setting succeeded')
            elif self.reply[2] == 1:
                print('Speed setting failed')
        else:
            print('Direction could only be Suck or Blow while speed could only be 1, 2 or 3')
        return None
            
    def set_pipette_volume(self, volume):
        if volume > 1000 or volume < 100:
            print('Volume could only be bigger than 100mL and less than 1000mL')
        else: 
            volume *= 100 
            self.send('PI_VOLUM', volume >> 16, volume >> 8 & 0xFF, volume & 0xFF)
            self.receive()
            if   self.reply[2] == 0:
                print('Pipette volume setting succeeded')
            elif self.reply[2] == 1:
                print('Pipette volume setting failed') 
        return None
         
    def action(self, direction):
        if direction in ['Suck', 'suck', 'Blow', 'blow']:
            self.send('KEY', {'Suck':1, 'suck':1, 'Blow':2, 'blow':2}[direction])
            self.receive()
            if   self.reply[2] == 0:
                print(f'Action succeeded')
            elif self.reply[2] == 1:
                print(f'Action failed')
            self.receive()
            if   self.reply[2] == 1:
                print(f'{direction}ing is done')
            elif self.reply[2] == 2:
                print(f'{direction}ing is done')
        else:
            print('Direction could only be Suck or Blow while speed could only be 1, 2 or 3')
        return None