import memory
import time
import instructions

class CPU:
    def __init__(self,memoryIn):
        self.memory = memory
        self.registers = memory.Register(64)
        
    def tick(self):
        pass
    
    def GHALT(self):
        while(1):
            time.sleep(1)

    def GLD(self):
        pass
        
    def GST(self):
        pass
   
    def GLI(self):
        pass
        
    def GLR(self):
        pass
        
    def GSR(self):
        pass
        
    def GADD(self):
        pass
        
    def GSUB(self):
        pass
        
    def GSFR(self):
        pass
        
    def GCMP(self):
        pass
        
    def GXOR(self):
        pass
        
    def GAND(self):
        pass

    def GOR(self):
        pass
        
    def GPSH(self):
        pass
        
    def GPOP(self):
        pass
        
    def GMV(self):
        pass

    def GBRGI(self):
        pass
        
    def GBRL(self):
        pass
        
    def GBRE(self):
        pass
        
    def GBRP(self): 
        pass
        
    def GBRN(self):
        pass
        
    def GJMP(self):
        pass
        
    def GSUB(self):
        pass
        
    def GSRET(self):
        pass
        
    def GINTE(self):
        pass
        
    def GINTD(self):
        pass
        
    def GINTD(self):
        pass
        
    def GIRET(self):
        pass
