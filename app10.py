from mettler_toledo_device import MettlerToledoDevice

dev = MettlerToledoDevice(port='COM5') # Windows specific port


a = dev.get_weight_stable()
print(a)
