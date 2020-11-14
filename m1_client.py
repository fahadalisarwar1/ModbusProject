from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient("localhost", 5020)
client.open()
while True:
    reg_address = 1
    reg_value = client.read_holding_registers(reg_address)
    print("Register: ", reg_address, "\t value: ", reg_value)
    sleep(2)