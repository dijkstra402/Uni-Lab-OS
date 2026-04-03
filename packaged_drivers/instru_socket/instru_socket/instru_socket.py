import serial

class instru_socket(serial.Serial):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def ask(self,cmd):
        self.write((cmd).encode("utf-8"))
        return(self.readline().decode())
        
    def write(self,cmd):
        self.write((cmd).encode("utf-8"))

__all__ = ["instru_socket"]
