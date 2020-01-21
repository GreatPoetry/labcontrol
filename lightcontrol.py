
"""
Allows simple high level lighting controls
"""
import time
import random
import threading

class dmx_control:
    def __init__(self, output_light, initial_dmx=0):
        self.__dmx = initial_dmx
        self.__output = output_light
        output_file_handle = open(self.__output, 'a')
        output_file_handle.write('\nLight control activated')
        output_file_handle.write(f'\nCurrent dmx: {self.__dmx}\n')
        output_file_handle.close()
        self.__thread = threading.Thread(target=self.__show_dmx_change, args=(initial_dmx,))

    @property
    def dmx(self):
        return self.__dmx
    
    @dmx.setter
    def dmx(self, value):
        self.__thread = threading.Thread(target=self.__show_dmx_change, args=(value,))
        self.__thread.start()

    def __show_dmx_change(self,value):
        if value == self.__dmx:
            output_file_handle = open(self.__output, 'a')
            output_file_handle.write(f'\ndmx already {value}')
            output_file_handle.close()
            return True
        if value >= 0 and value <=255:
            self.__dmx = value
            for cnt in reversed(range(random.randint(3,5))):
                output_file_handle = open(self.__output, 'a')
                time.sleep(1)
                output_file_handle.write(str(cnt) + '...')
                output_file_handle.close()
            output_file_handle = open(self.__output, 'a')
            output_file_handle.write('\nLight level adjusted')
            output_file_handle.write(f'\nCurrent dmx: {self.__dmx}\n')
            output_file_handle.close()
            self.__dmx = value
            return True
        else:
            print('ERROR: bad dmx values')
            return False
    
    def lights_ready(self):
        return not self.__thread.is_alive()

    def wait_for_lights(self):
        while not self.lights_ready():
            pass