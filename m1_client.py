from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient("192.168.2.205", 502)
client.open()
print("started")
while True:

    voltage_reg_address = 107
    voltage_reg_value = client.read_holding_registers(voltage_reg_address,3)
    print("Voltage:\t", voltage_reg_value)
    sleep(3)
