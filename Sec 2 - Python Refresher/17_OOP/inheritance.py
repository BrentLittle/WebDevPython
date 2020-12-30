# allows one class to take methods androperties from another class

class Device:
    def __init__(self,name,connection):
        self.name = name
        self.connection = connection
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connection})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connection, capacity):
        super().__init__(name, connection)
        self.capacity = capacity
        self.remainingPages = capacity
    def __str__(self):
        return f"{super().__str__()} ({self.remainingPages} pages remaining)"
    def print(self,pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"printing {pages}")
        self.remainingPages -= pages


device = Device("Printer", "USB")
print(device)
device.disconnect()

printer = Printer("Printer","USB",500)
printer.print(20)
print(printer)

printer.disconnect()
printer.print(20)