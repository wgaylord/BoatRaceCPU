import memory
import time
import instructions as instr

class CPU:
    def __init__(self,mem):
        self.mem = mem
        self.registers = memory.Registers(64)
        self.PC = self.mem.readAddress(0xFFFFF9)
        
    def tick(self):
        opcode = instr.decodeGenericOP(self.mem.readUByte(self.PC))
        section = instr.decodeSection(opcode)
        
        if opcode == instr.GADD:
            self.GADD(section)
        if opcode == instr.GAND:
            self.GAND(section)
        if opcode == instr.GBRE:
            self.GBRE(section)
        if opcode == instr.GBRG:
            self.GBRG(section)
        if opcode == instr.GBRL:
            self.GBRL(section)
        if opcode == instr.GBRN:
            self.GBRN(section)
        if opcode == instr.GBRP:
            self.GBRP(section)
        if opcode == instr.GCMP:
            self.GCMP(section)
        if opcode == instr.GHALT:
            self.GHALT(section)
        if opcode == instr.GHALT1:
            self.GHALT1(section)
        if opcode == instr.GINTD:
            self.GINTD(section)
        if opcode == instr.GINTE:
            self.GINTE(section)
        if opcode == instr.GIRET:
            self.GIRET(section)
        if opcode == instr.GJMP:
            self.GJMP(section)
        if opcode == instr.GLD:
            self.GLD(section)
        if opcode == instr.GLI:
            self.GLI(section)
        if opcode == instr.GLR:
            self.GLR(section)
        if opcode == instr.GMV:
            self.GMV(section)
        if opcode == instr.GOR:
            self.GOR(section)
        if opcode == instr.GPOP:
            self.GPOP(section)
        if opcode == instr.GPSH:
            self.GPSH(section)
        if opcode == instr.GSFR:
            self.GSFR(section)
        if opcode == instr.GSR:
            self.GSR(section)
        if opcode == instr.GSRET:
            self.GSRET(section)
        if opcode == instr.GST:
            self.GST(section)
        if opcode == instr.GSUB:
            self.GSUB(section)
        if opcode == instr.GXOR:
            self.GXOR(section)
            
    def GHALT(self,section):
        while(1):
            time.sleep(1)

    def GLD(self,section):
        if section == 0:
            self.PC+=1
            register = self.mem.readUByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.registers.writeUByte(register,self.mem.readUByte(address))
            return 
        if section == 1:
            self.PC+=1
            register = self.mem.readByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.registers.writeByte(register,self.mem.readByte(address))
            return 
        if section == 2:
            self.PC+=1
            register = self.mem.readUByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.registers.writeUShort(register,self.mem.readUShort(address))
            return 
        if section == 3:
            self.PC+=1
            register = self.mem.readByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.registers.writeShort(register,self.mem.readShort(address))
            return 
                
    def GST(self,section):
        if section == 0:
            self.PC+=1
            register = self.mem.readUByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.mem.writeUByte(address,self.registers.readUByte(register))
            return 
        if section == 1:
            self.PC+=1
            register = self.mem.readByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.mem.writeByte(address,self.registers.readByte(register))
            return 
        if section == 2:
            self.PC+=1
            register = self.mem.readUByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.mem.writeUShort(address,self.registers.readUShort(register))
            return 
        if section == 3:
            self.PC+=1
            register = self.mem.readByte(self.PC)
            self.PC+=1
            address = self.mem.readAddress(self.PC)
            self.PC +=6
            self.mem.writeShort(address,self.registers.readShort(register))
            return 
   
    def GLI(self,section):
        print("Instruction not implmented!\n")
        
    def GLR(self,section):
        print("Instruction not implmented!\n")
        
    def GSR(self,section):
        print("Instruction not implmented!\n")
        
    def GADD(self,section):
        print(self.PC)
        if section == 0:
            self.PC+=1
            registerA = self.mem.readUByte(self.PC)
            self.PC+=1
            registerB = self.mem.readUByte(self.PC)
            self.PC +=1
            registerC = self.mem.readUByte(self.PC)
            self.PC+=1
            answer = self.registers.readUByte(registerA) + self.registers.readUByte(registerB)
            self.registers.writeUByte(registerC,answer)
            return 
        if section == 1:
            self.PC+=1
            registerA = self.mem.readUByte(self.PC)
            self.PC+=1
            registerB = self.mem.readUByte(self.PC)
            self.PC +=1
            registerC = self.mem.readUByte(self.PC)
            self.PC+=1
            answer = self.registers.readByte(registerA) + self.registers.readByte(registerB)
            self.registers.writeByte(registerC,answer)
            return
        if section == 2:
            self.PC+=1
            registerA = self.mem.readUByte(self.PC)
            self.PC+=1
            registerB = self.mem.readUByte(self.PC)
            self.PC +=1
            registerC = self.mem.readUByte(self.PC)
            self.PC+=1
            answer = self.registers.readUShort(registerA) + self.registers.readUShort(registerB)
            self.registers.writeUShort(registerC,answer)
            return 
        if section == 3:
            self.PC+=1
            registerA = self.mem.readUByte(self.PC)
            self.PC+=1
            registerB = self.mem.readUByte(self.PC)
            self.PC +=1
            registerC = self.mem.readUByte(self.PC)
            self.PC+=1
            answer = self.registers.readShort(registerA) + self.registers.readShort(registerB)
            self.registers.writeShort(registerC,answer)
            return         
        
    def GSUB(self,section):
        print("Instruction not implmented!\n")
        
    def GSFR(self,section):
        print("Instruction not implmented!\n")
        
    def GCMP(self,section):
        print("Instruction not implmented!\n")
        
    def GXOR(self,section):
        print("Instruction not implmented!\n")
        
    def GAND(self,section):
        print("Instruction not implmented!\n")

    def GOR(self,section):
        print("Instruction not implmented!\n")
        
    def GPSH(self,section):
        print("Instruction not implmented!\n")
        
    def GPOP(self,section):
        print("Instruction not implmented!\n")
        
    def GMV(self,section):
        print("Instruction not implmented!\n")

    def GBRGI(self,section):
        print("Instruction not implmented!\n")
        
    def GBRL(self,section):
        print("Instruction not implmented!\n")
        
    def GBRE(self,section):
        print("Instruction not implmented!\n")
        
    def GBRP(self,section): 
        print("Instruction not implmented!\n")
        
    def GBRN(self,section):
        print("Instruction not implmented!\n")
        
    def GJMP(self,section):
        print("Instruction not implmented!\n")
        
    def GSUB(self,section):
        print("Instruction not implmented!\n")
        
    def GSRET(self,section):
        print("Instruction not implmented!\n")
        
    def GINTE(self,section):
        print("Instruction not implmented!\n")
        
    def GINTD(self,section):
        print("Instruction not implmented!\n")
        
    def GINTD(self,section):
        print("Instruction not implmented!\n")
        
    def GIRET(self,section):
        print("Instruction not implmented!\n")
