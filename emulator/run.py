import memory
import cpu


mainmem = memory.Memory(0xFFFFFF)

mainmem.mem[0] = 1
mainmem.mem[1] = 15
mainmem.mem[7] = 30
mainmem.mem[30] = 10

test = cpu.CPU(mainmem)

