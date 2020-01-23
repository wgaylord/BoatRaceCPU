
class mem_map:
    def __init__(self):
        self.map = []

    def __getitem__(self,adr):
        for x in self.map:
            if adr > x["start"] and adr < x["end"]:
                return x["memory"]
    def __setitem__(self,adr,val):
        pass

    def register_memory(self,mem):
        self.map.append(mem)

class memory:
    def __init__(self,size,start=0):
        self.mem = array.array('B',(0,)*size)
        self.write_listeners = []
        self.read_listeners = []
        self.starting_addr = start

    def __getitem__(self,adr):
        return None

    def __setitem__(self,adr,val):
        pass

    def notify_read_listeners(self,adr):
        for x in self.read_listeners:
            x(adr)

    def notify_write_listeners(self,adr,val):
        for x in self.write_listeners:
            x(adr,val)

class rom(memory):
    def __getitem__(self,adr):
        self.notify_read_listeners(adr-self.starting_addr)
        return self.mem[adr-self.starting_addr]

class ram(memory):
    def __getitem__(self,adr):
        self.notify_read_listeners(adr-self.starting_addr)
        return self.mem[adr-self.starting_addr]

    def __setitem__(self,adr,val):
        self.notify_write_listeners(self,adr-self.start_addr,val)
        self.mem[adr-self.starting_addr] = val

class io(memory):
    def __init__(self,size):
        self.io_devices = []
        super()

    def __getitem__(self,adr):
        self.notify_read_listeners(adr)
        value = 0
        for x in self.io_devices:
            if adr in x.adrs:
                value = x[adr]
        return value

    def __setitem__(self,adr,val):
        self.notify_write_listeners(adr,val)
        for x in self.io_devices:
            if adr in x.adrs:
                x[adr] = val

