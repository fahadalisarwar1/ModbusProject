from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient("192.168.2.205", 502)
client.open()
print("started")
while True:

    voltage_reg_address = 107
    voltage_reg_value = client.read_holding_registers(voltage_reg_address,3)
    v = client.read_input_registers(voltage_reg_address, 1)
    Curr_reg_address = 102
    Curr_reg_value = client.read_holding_registers(Curr_reg_address)
    # voltage_actual_value = 0.018 * voltage_reg_value[]
    print("Voltage:\t", voltage_reg_value)
    print("Voltage:\t", v)
    sleep(3)
