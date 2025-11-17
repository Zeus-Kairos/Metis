# Transfer Files using SCPI

* * *

The following Python examples transfer files to and from a remote PC using the
[MMEM:TRANsfer](../GP-IB_Command_Finder/Memory.md#Transfer) command.

import pyvisa as visa  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
_# Make sure to enable remote drive access in Remote Interface dialog, else
MMEM:TRAN will return an error_  
  
_# ======================= Transferring from the VNA to the remote PC
=======================_  
  
_# Open file to be stored on local computer. Creates file if not already
existing_  
fp = open("./myTestData.s2p", 'w+')  
  
_# Analyzer has file 'testdata.s2p' in default directory._  
_# The default directory is where the VNA saves files to on default_  
data = session.query("MMEM:TRAN? './testdata.s2p'")  
  
_# Now save the file locally to myTestData.s2p_  
fp.write(data)  
fp.close()  
  
_# ======================= Transferring from the remote PC to the VNA
=======================_  
  
_# Local file to be transferred_  
fp = open("./myTestData.s2p", 'r')  
  
_# Store file content into variable_  
_# Data to be transferred to analyzer file 'testupld.s2p' in default
directory._  
data = fp.read()  
session.write(f"MMEM:TRAN 'testupld.s2p', {data}")  
  
fp.close()  
  
---  
  
* * *

