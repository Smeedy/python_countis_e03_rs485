#!/usr/bin/python

import minimalmodbus

rs485 = minimalmodbus.Instrument('/dev/cu.usbserial-FTYXZ40E', 1)
rs485.serial.baudrate = 9600
rs485.serial.bytesize = 8
rs485.serial.parity = minimalmodbus.serial.PARITY_NONE
rs485.serial.stopbits = 1
rs485.serial.timeout = 1
rs485.debug = False
rs485.mode = minimalmodbus.MODE_RTU
#print(rs485)

Simple_Voltage = rs485.read_long(50520, functioncode=3, signed=False) / 100.0 # U32 V/100
Frequency = rs485.read_long(50526, functioncode=3, signed=False) / 100.0 # U32 Hz/100
Current = rs485.read_long(50528, functioncode=3, signed=False) / 1000.0 # U32 A/1000
Sum_Active_Power = rs485.read_long(50536, functioncode=3, signed=True) / 0.1 # S32 W/0.1
Sum_Reactive_Power = rs485.read_long(50538, functioncode=3, signed=True) / 0.1 # S32 VAr/0.1
Sum_Apparent_Power = rs485.read_long(50540, functioncode=3, signed=False) / 0.1 # U32 VA/0.1
Sum_Power_Factor = rs485.read_long(50542, functioncode=3, signed=True) / 1000 # S32 -/1000
Active_Power_Phase1 = rs485.read_long(50544, functioncode=3, signed=True) / 0.1 # S32 W/0.1
Reactive_Power_Phase1 = rs485.read_long(50550, functioncode=3, signed=True) / 0.1 # S32 var/0.1
Apparent_Power_Phase1 = rs485.read_long(50556, functioncode=3, signed=False) / 0.1 # U32 VA/0.1
Power_Factor_Phase1 = rs485.read_long(50562, functioncode=3, signed=True) / 1000 # U32 -/1000

Active_Energy = rs485.read_long(36868, functioncode=3, signed=False)  # U32 Wh

print('Simple Voltage: {0:.2f} Volts'.format(Simple_Voltage))
print('Frequency: {0:.2f} Hz'.format(Frequency))
print('Current: {0:.3f} Amps'.format(Current))
print('Sum Active Power: {0:.1f} Watts'.format(Sum_Active_Power))
print('Sum Reactive Power: {0:.1f} VAr'.format(Sum_Reactive_Power))
print('Sum Apparent Power: {0:.1f} VoltAmps'.format(Sum_Apparent_Power))
print('Sum Power Factor: {0:.3f}'.format(Sum_Power_Factor))
print('Active Power Phase 1: {0:.1f} Watt'.format(Active_Power_Phase1))
print('Reactive Power Phase 1: {0:.1f} Watt'.format(Reactive_Power_Phase1))
print('Apparent Power Phase 1: {0:.1f} Watt'.format(Apparent_Power_Phase1))
print('Power Factor Phase 1: {0:.1f}'.format(Power_Factor_Phase1))
print('Active Energy: {0:.3f} kWh'.format(Active_Energy / 1000.0))
