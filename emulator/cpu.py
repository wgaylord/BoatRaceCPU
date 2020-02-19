import memory
import instructions

class CPU:
    def __init__(self,memoryIn):
        self.memory = memory
        self.registers = memory.Register(64)
        
    def tick(self):
        pass
    
        
