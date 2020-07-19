import tkinter as tk
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.server.sync import ModbusTcpServer,StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock as dataServer
from pymodbus.datastore import ModbusSlaveContext as contextSlave
from pymodbus.datastore import ModbusServerContext as contextServer
from time import sleep
myData=dataServer.create() #Creamos el bloque de datos del servidor Modbus TCP
myData.setValues(0x15,[15000,62000])# Seteamos dos bloques: el bloque 0x15 a 15000 y 0x16 62000
store=contextSlave(myData)
context=contextServer(slaves=store)
StartTcpServer(context,address=("192.168.1.107",5020))
while True:
    print("SERVER ACTIVE")
    sleep(5)
#client = ModbusClient('localhost', port=5020)
#client.connect()
#client.read...
