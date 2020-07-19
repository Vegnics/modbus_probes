#!/usr/bin/python3.6
"""
EJEMPLO DE COMUNICACIÓN MODBUSTCP BIDIRECCIONAL
Pymodbus server on port 5020
Pydmodbus client on port 5021

BLOQUES:
di: Discrete Inputs
co: Coil Outputs
hr: Holding Registers
ir: Input Registers
"""

import tkinter as tk
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.server.sync import ModbusTcpServer,StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock as dataServer
from pymodbus.datastore import ModbusSlaveContext as contextSlave
from pymodbus.datastore import ModbusServerContext as contextServer
from time import sleep
from threading import Timer

class readHoldRegisters():
    def __init__(self,client,address,numReg):
        self.t=t
        self.client=client
        self.address=address
        self.numReg=numReg
        self.thread = Timer(self.t,self.printregisters)
    def printregisters(self):
        response=self.client.read_holding_registers(self.address,self.numReg,unit=0x1)
        print(response.registers)
    def start(self):
        self.thread.start()
    def cancel(self):
        self.thread.cancel()

#Asignamos valores para conexión TCP/IP
serverIp="192.168.1.107" #La IP de esta PC
serverPort=5020          #El puerto para la escucha
clientIp="192.168.1.100" #La IP de la otra PC
clientPort=5021          #El puerto para la lectura/escritura

#CONFIGURAMOS EL CLIENTE MODBUS TCP
client=ModbusTcpClient(clientIp,clientPort)
print(client.connect())
readReg=readHoldRegisters(client,4014,2)

#CONFIGURAMOS EL SERVIDOR MODBUS TCP
myBlock=dataServer(4015,[1000,8000])                  #Creamos el bloque de datos del servidor Modbus TCP
store=contextSlave(di=None,co=None,hr=myBlock,ir=None)#Asignamos los bloques de datos al servidor Modbus TCP
context=contextServer(slaves=store,single=True)
StartTcpServer(context,address=(serverIp,serverPort)) #Encendemos el servidor ModbusTCP
while True:
    print("SERVER ACTIVE")
    sleep(5)
