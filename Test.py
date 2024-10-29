import pyvisa


# Retrive the resource manager
rm = pyvisa.ResourceManager("@py")

# Retrive all ports
ports = rm.list_resources()

print(ports)

# Get the device
device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")

# Papers please
identification = device.query("*IDN?")
print(identification)