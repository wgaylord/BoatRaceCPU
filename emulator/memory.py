import numpy
import struct

class Memory:
    def __init__(self,size,memMap={"rom":{"start":-1,"stop":-1},"io":{}}):
        self.memMap = memMap
        self.mem = numpy.zeros(size,dtype=numpy.uint8)
        
        
    def canWrite(self,addr):
        roms = self.memMap["rom"]
        for x in roms:
            if addr > x["start"] and addr < x["stop"]:
                return False
        return True
        
    def isIO(self,addr,read=False):
        IOs = self.memMap["io"]
        for y in IOs.keys():
            if addr > IOs[y]["start"] and addr < IOs[y]["stop"]:
                if read:
                    return IOs[y]["read"]
                else:
                    return IOs[y]["write"]
        return False
        
        
    def doWriteOperation(self,addr,val):
        if self.canWrite(addr):
            io =  self.isIO(addr)
            if not io:
                return val
            else:
                io(addr,val)
                return val
        else:
            return None
            
    def doReadOPeration(self,addr,val):
        io =  self.isIO(addr,True)
        if not io:
            return val
        else:
            val = io(addr,val)
            return val
        
    def readUByte(self,adr):
        return self.doReadOPeration(adr,self.mem[adr])

    def readByte(self,adr):
        return struct.unpack('b',struct.pack("B",self.doReadOPeration(adr,self.mem[adr])))[0]

    def readUShort(self,adr):
        return struct.unpack("<H",struct.pack("B",self.doReadOPeration(adr,self.mem[adr]))+struct.pack("B",self.doReadOPeration(adr+1,self.mem[adr+1])))[0]

    def readShort(self,adr):
        return struct.unpack("<h",struct.pack("B",self.doReadOPeration(adr,self.mem[adr]))+struct.pack("B",self.doReadOPeration(adr+1,self.mem[adr+1])))[0]

    def readULong(self,adr):
        return struct.unpack("<L",struct.pack("B",self.doReadOPeration(adr,self.mem[adr]))+struct.pack("B",self.doReadOPeration(adr+1,self.mem[adr+1]))+struct.pack("B",self.doReadOPeration(adr+2,self.mem[adr+2]))+struct.pack("B",self.doReadOPeration(adr+3,self.mem[adr+3])))[0]

    def readLong(self,adr):
        return struct.unpack("<l",struct.pack("B",self.doReadOPeration(adr,self.mem[adr]))+struct.pack("B",self.doReadOPeration(adr+1,self.mem[adr+1]))+struct.pack("B",self.doReadOPeration(adr+2,self.mem[adr+2]))+struct.pack("B",self.doReadOPeration(adr+3,self.mem[adr+3])))[0]

    def writeUByte(self,adr,val):
        val = self.doWriteOperation(adr,val)
        if not val == None:
            self.mem[adr] = val

    def writeByte(self,adr,val):
        val = struct.unpack("B",struct.pack("b",val))[0]
        val = self.doWriteOperation(adr,val)
        if not val == None:
            self.mem[adr] = val

    def writeUShort(self,adr,val):
        a,b = struct.unpack("BB",struct.pack("<H",val))
        val1 = self.doWriteOperation(adr,a)
        val2 = self.doWriteOperation(adr+1,b)
        if (not val == None) and (not val2 == None):
            self.mem[adr] ,self.mem[adr+1] = a,b

    def writeShort(self,adr,val):
        a,b = struct.unpack("BB",struct.pack("<h",val))
        val1 = self.doWriteOperation(adr,a)
        val2 = self.doWriteOperation(adr+1,b)
        if (not val == None) and (not val2 == None):
            self.mem[adr] ,self.mem[adr+1] = a,b

    def writeULong(self,adr,val):
        a,b,c,d = struct.unpack("BBBB",struct.pack("<L",val))
        a = self.doWriteOperation(adr,a)
        b = self.doWriteOperation(adr+1,b)
        c = self.doWriteOperation(adr+2,c)
        d = self.doWriteOperation(adr+3,d)
        if (not a == None) and (not b == None) and (not c == None) and (not d == None):
            self.mem[adr],self.mem[adr+1],self.mem[adr+2],self.mem[adr+3] = a,b,c,d

    def writeLong(self,adr,val):
        a,b,c,d = struct.unpack("BBBB",struct.pack("<l",val))
        a = self.doWriteOperation(adr,a)
        b = self.doWriteOperation(adr+1,b)
        c = self.doWriteOperation(adr+2,c)
        d = self.doWriteOperation(adr+3,d)
        if (not a == None) and (not b == None) and (not c == None) and (not d == None):
            self.mem[adr],self.mem[adr+1],self.mem[adr+2],self.mem[adr+3] = a,b,c,d

class Registers:
    def __init__(self,size):
        self.mem = numpy.zeros(size,dtype=numpy.uint8)

        
    def readUByte(self,adr):
        return self.mem[adr]

    def readByte(self,adr):
        return struct.unpack('b',struct.pack("B",self.mem[adr]))[0]

    def readUShort(self,adr):
        return struct.unpack("<H",struct.pack("B",self.mem[adr])+struct.pack("B",self.mem[adr+1]))[0]

    def readShort(self,adr):
        return struct.unpack("<h",struct.pack("B",adr,self.mem[adr])+struct.pack("B",adr+1,self.mem[adr+1]))[0]

    def readULong(self,adr):
        return struct.unpack("<L",struct.pack("B",adr,self.mem[adr])+struct.pack("B",adr+1,self.mem[adr+1])+struct.pack("B",adr+2,self.mem[adr+2])+struct.pack("B",adr+3,self.mem[adr+3]))[0]

    def readLong(self,adr):
        return struct.unpack("<l",struct.pack("B",adr,self.mem[adr])+struct.pack("B",adr+1,self.mem[adr+1])+struct.pack("B",adr+2,self.mem[adr+2])+struct.pack("B",adr+3,self.mem[adr+3]))[0]

    def writeUByte(self,adr,val):
        self.mem[adr] = val

    def writeByte(self,adr,val):
        val = struct.unpack("B",struct.pack("b",val))[0]
        self.mem[adr] = val

    def writeUShort(self,adr,val):
        a,b = struct.unpack("BB",struct.pack("<H",val))
        self.mem[adr] ,self.mem[adr+1] = a,b

    def writeShort(self,adr,val):
        a,b = struct.unpack("BB",struct.pack("<h",val))
        self.mem[adr] ,self.mem[adr+1] = a,b

    def writeULong(self,adr,val):
        a,b,c,d = struct.unpack("BBBB",struct.pack("<L",val))
        self.mem[adr],self.mem[adr+1],self.mem[adr+2],self.mem[adr+3] = a,b,c,d

    def writeLong(self,adr,val):
        a,b,c,d = struct.unpack("BBBB",struct.pack("<l",val))
        self.mem[adr],self.mem[adr+1],self.mem[adr+2],self.mem[adr+3] = a,b,c,d

    
    
    
       