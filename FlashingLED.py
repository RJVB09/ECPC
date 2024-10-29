import pyvisa
import time as t
import numpy as np

# Prep stuff
# Retrive the resource manager
rm = pyvisa.ResourceManager("@py")
# Retrive all ports
ports = rm.list_resources()
print(ports)
# Get the device
device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")

# Flashing settings
period = 0
duration = 0.01

while True:
    t.sleep(period)
    device.query("OUT:CH0 1023")
    t.sleep(duration)
    device.query("OUT:CH0 0")

