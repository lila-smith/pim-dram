import numpy as np  

class DRAMController:
    """
    Use valid DRAM commands to create encoding
    """

    def __init__(self):
        self._encoded_command = np.zeros(1+4+1+18)

    def deselect(self):
        self.address = np.zeros(18) 
        self.act_bar = 0  
        self.bank_sel = np.zeros(4)     
        self.cs_bar = 1      
        
    def activate(self, bank, address):
        self.address = address
        self.bank_sel = bank
        self.act_bar = 0
        self.cs_bar = 0

    def read(self, bank, bc, ap, col):
        pass

    def write(self, bank, bc, ap, col):
        pass

    def precharge(self, bank):
        pass

    def precharge_all(self):
        pass

    
    
    
    
    # Named ways to read and set the bits used
    # ChatGPT assisted
    
    
    @property
    def address(self):
        return self._encoded_command[0:18]
    @address.setter
    def address(self, address):
        self._encoded_command[0:18] = np.array(address)

    @property
    def all_precharge(self):
        return self._encoded_command[10]
    @all_precharge.setter
    def all_precharge(self, all_precharge):
        self._encoded_command[10] = all_precharge

    @property
    def burst_chop(self):
        return self._encoded_command[12]
    @burst_chop.setter
    def burst_chop(self, burst_chop):
        self._encoded_command[12] = burst_chop

    @property
    def wr_en_bar(self):
        return self._encoded_command[14]
    @wr_en_bar.setter
    def wr_en_bar(self, wr_en_bar):
        self._encoded_command[14] = wr_en_bar

    @property
    def cas_bar(self):
        return self._encoded_command[15]
    @cas_bar.setter
    def cas_bar(self, cas_bar):
        self._encoded_command[15] = cas_bar

    @property
    def ras_bar(self):
        return self._encoded_command[16]
    @ras_bar.setter
    def ras_bar(self, ras_bar):
        self._encoded_command[16] = ras_bar

    @property
    def act_bar(self):
        return self._encoded_command[18]
    @act_bar.setter
    def act_bar(self, act_bar):
        self._encoded_command[18] = act_bar

    @property
    def bank_sel(self):
        return self._encoded_command[19:23]
    @bank_sel.setter
    def bank_sel(self, bank_sel):
        self._encoded_command[19:23] = bank_sel

    @property
    def cs_bar(self):
        return self._encoded_command[23]
    @cs_bar.setter
    def cs_bar(self, cs_bar):
        self._encoded_command[23] = cs_bar
    
    
    def __repr__(self):
        if self.cs_bar:
            return "Deselected"
        elif self.act_bar:
            return f" "
        else:
            return f"Activate - Bank = {self.bank_sel}, Address = {self.address}"