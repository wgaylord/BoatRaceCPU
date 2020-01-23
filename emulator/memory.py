import numpy
import struct

class Memory:
    def __init__(self,size,memMap):
        self.memMap = memMap
        self.mem = numpy.zeros(size,dtype=numpy.uint8)

    def readUByte(self,adr):
        return self.mem[adr]

    def readByte(self,adr):
        return struct.unpack('b',struct.pack("B",self.mem[adr]))[0]

    def readUShort(self,adr):
        return struct.unpack("<H",struct.pack("B",self.mem[adr])+struct.pack("B",self.mem[adr+1]))[0]

    def readShort(self,adr):
        return struct.unpack("<h",struct.pack("B",self.mem[adr])+struct.pack("B",self.mem[adr+1]))[0]

    def readULong(self,adr):
        return struct.unpack("<L",struct.pack("B",self.mem[adr])+struct.pack("B",self.mem[adr+1])+struct.pack("B",self.mem[adr+2])+struct.pack("B",self.mem[adr+3]))[0]

    def readLong(self,adr):
        return struct.unpack("<l",struct.pack("B",self.mem[adr])+struct.pack("B",self.mem[adr+1])+struct.pacl("B",self.mem[adr+2])+struct.pack("B"+self.mem[adr+3]))[0]

    def writeUByte(self,adr,val):
        self.mem[adr] = val

    def writeByte(self,adr,val):
        self.mem[adr] = struct.unpack("B",struct.pack("b",val))[0]

    def writeUShort(self,adr,val):
        self.mem[adr] ,self.mem[adr+1] = struct.unpack("BB",struct.pack("<H",val))

    def writeShort(self,adr,val):
        self.mem[adr],self.mem[adr+1[ = struct.unpack("BB",struct.pack("<h",val))

    def writeULong(self,adr,val):
        self.mem[adr],self.mem[adr+1],self.mem[adr+2],self.mem[adr+3] = struct.unpack("BBBB",struct.pack("<L"))

    def writeLong(self,adr,val):
        self.mem[adr],self.mem[adr+1],self.mem[adr+2],self.mem[adr+3] = struct.unpack("BBBB",struct.pack("<l"))
