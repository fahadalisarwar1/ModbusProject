from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
server = ModbusServer("localhost", 5020, no_block=True)

try:
    print("starting the server")
    server.start()
    print("server started")
    data = [0]

    while True:
        reg_address = 1
        value = int(uniform(0, 200))
        DataBank.set_words(reg_address, [value])
        print("The value in register ", reg_address, " is ", DataBank.get_words(reg_address))
        sleep(2)
except:
    print("Error")
    print("Closing the server")

