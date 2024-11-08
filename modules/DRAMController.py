import numpy as np  

class DRAMController:
    """
    Use valid DRAM commands to create encoding
    """

    def __init__(self):
        self._address = np.zeros(18) # 18 bits, includes bits used for commands
        self._act_bar = np.zeros(1)  # 1 bit
        self._bank = np.zeros(2)     # 2 bits
        self._cs_bar = np.ones(1)       # 1 bit

    def deselect(self):
        self._address = np.zeros(18) 
        self._act_bar = np.zeros(1)  
        self._bank = np.zeros(2)     
        self._cs_bar = np.ones(1)      
        
    def activate(self, bank, address):
        pass

    def read(self, bank, bc, ap, col):
        pass

    def write(self, bank, bc, ap, col):
        pass

    def precharge(self, bank):
        pass

    def precharge_all(self):
        pass