import memory
import time
import instructions

class CPU:
    def __init__(self,memoryIn):
        self.memory = memory
        self.registers = memory.Register(64)
        self.PC = 0
        
    def tick(self):
        pass
    
    def GHALT(self):
        while(1):
            time.sleep(1)

    def GLD(self):
        print("Instruction not implmented!\n")
        
    def GST(self):
        print("Instruction not implmented!\n")
   
    def GLI(self):
        print("Instruction not implmented!\n")
        
    def GLR(self):
        print("Instruction not implmented!\n")
        
    def GSR(self):
        print("Instruction not implmented!\n")
        
    def GADD(self):
        print("Instruction not implmented!\n")
        
    def GSUB(self):
        print("Instruction not implmented!\n")
        
    def GSFR(self):
        print("Instruction not implmented!\n")
        
    def GCMP(self):
        print("Instruction not implmented!\n")
        
    def GXOR(self):
        print("Instruction not implmented!\n")
        
    def GAND(self):
        print("Instruction not implmented!\n")

    def GOR(self):
        print("Instruction not implmented!\n")
        
    def GPSH(self):
        print("Instruction not implmented!\n")
        
    def GPOP(self):
        print("Instruction not implmented!\n")
        
    def GMV(self):
        print("Instruction not implmented!\n")

    def GBRGI(self):
        print("Instruction not implmented!\n")
        
    def GBRL(self):
        print("Instruction not implmented!\n")
        
    def GBRE(self):
        print("Instruction not implmented!\n")
        
    def GBRP(self): 
        print("Instruction not implmented!\n")
        
    def GBRN(self):
        print("Instruction not implmented!\n")
        
    def GJMP(self):
        print("Instruction not implmented!\n")
        
    def GSUB(self):
        print("Instruction not implmented!\n")
        
    def GSRET(self):
        print("Instruction not implmented!\n")
        
    def GINTE(self):
        print("Instruction not implmented!\n")
        
    def GINTD(self):
        print("Instruction not implmented!\n")
        
    def GINTD(self):
        print("Instruction not implmented!\n")
        
    def GIRET(self):
        print("Instruction not implmented!\n")
