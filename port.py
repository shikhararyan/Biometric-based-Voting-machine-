import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for port in ports:
    print("Port:", port.device)
    print("Description:", port.description)
    print("Manufacturer:", port.manufacturer)
    print("Product:", port.product)
    print(" ")