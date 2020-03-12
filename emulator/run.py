import memory
import cpu


mainmem = memory.Memory(0xFFFFFF)

mainmem.mem[0] = 33
mainmem.mem[1] = 15
mainmem.mem[7] = 30
mainmem.mem[8] = 1
mainmem.mem[9] = 11
mainmem.mem[15] = 31
mainmem.writeByte(30,-10)
mainmem.mem[31] = 12
mainmem.mem[16] = 6
mainmem.mem[17] = 15
mainmem.mem[18] = 11
mainmem.mem[19] = 1

test = cpu.CPU(mainmem)

