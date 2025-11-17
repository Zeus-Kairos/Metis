# Create New Cal Kit using SCPI

When creating new cal kits programmatically, the order in which cal kit
commands are sent can be important.

For example to create a kit with opens, shorts, loads, and thrus. Be sure to
use the following sequence for each newly defined standard.

  1. Programmatically select the standard number

  2. Programmatically select the standard type. 

  3. Program the cal standard's values.

  4. Repeat steps 1, 2, 3 for additional new standards being defined.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

import pyvisa as visa  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_ resourceManager =
visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
session.timeout = 25000  _# Changed timeout to 25 seconds_  
  
_# Helper functions_ def Get_label():  
label = session.query("SENS:CORR:COLL:CKIT:STAN:LAB?")  
print(label)  
  
def Get_std():  
type = session.query("SENS:CORR:COLL:CKIT:STAN:TYPE?")  
print(type)  
  
def Print_connector():  
name = session.query("SENS:CORR:COLL:CKIT:CONN:SNAME?")  
print(name)  
  
def Verify_std():  
label = session.query("SENS:CORR:COLL:CKIT:STAN:LAB?")  
print(label)  
  
_# Select the standard number_  
_# Select the standard type_  
_# Program the cal standard 's values_  
_# Repeat above steps for additional new standards being defined_  
  
calkitNum = int(session.query("SENS:CORR:CKIT:COUN?")) \+ 1  
session.write(f"SENS:CORR:COLL:CKIT {calkitNum}")  
  
_# Name the kit with your name_  
session.write("SENS:CORR:COLL:CKIT:NAME 'Special 2.4 mm Model 85056'")  
  
_# Set up standard #1_  
print("Defining kit standard 1...")  
session.write("SENS:CORR:COLL:CKIT:STAN 1")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE SHORT")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'My Short'")  
Get_label()  
  
_# Set up standard #2_  
print("Defining kit standard 2...")  
session.write("SENS:CORR:COLL:CKIT:STAN 2")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE OPEN")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'My Open'")  
Get_label()  
  
_# Set up standard #3_  
print("Defining kit standard 3...")  
session.write("SENS:CORR:COLL:CKIT:STAN 3")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE LOAD")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'My Fixed Load'")  
Get_label()  
  
_# Set up standard #4_  
print("Defining kit standard 4...")  
session.write("SENS:CORR:COLL:CKIT:STAN 4")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE THRU")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'My Thru'")  
Get_label()  
  
_# Set up standard #5_  
print("Defining kit standard 5...")  
session.write("SENS:CORR:COLL:CKIT:STAN 5")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE SLOAD")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'Sliding Load'")  
Get_label()  
_# Set up standard #6_  
print("Defining kit standard 6...")  
session.write("SENS:CORR:COLL:CKIT:STAN 6")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE SHORT")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'Short'")  
Get_label()  
  
_# Set up standard #7_  
print("Defining kit standard 7...")  
session.write("SENS:CORR:COLL:CKIT:STAN 7")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE SHORT")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'Short'")  
Get_label()  
  
_# Set up standard #8_  
print("Defining kit standard 8...")  
session.write("SENS:CORR:COLL:CKIT:STAN 8")  
session.write("SENS:CORR:COLL:CKIT:STAN:TYPE ARBI")  
Get_std()  
session.write("SENS:CORR:COLL:CKIT:STAN:CHAR COAX")  
session.write("SENS:CORR:COLL:CKIT:STAN:TZR 15")  
session.write("SENS:CORR:COLL:CKIT:STAN:TZI -9")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'Z Load'")  
Get_label()  
  
_# Remove old connector names_  
session.write("SENS:CORR:COLL:CKIT:CONN:DEL")  
  
_# Verify no connectors are currently installed '_  
emptyConn = session.query("SENS:CORR:COLL:CKIT:CONN:CAT?")  
print(f"Verify empty list: {emptyConn}")  
  
_# Define new connectors_ session.write("SENS:CORR:COLL:CKIT:CONN:ADD 'PSC
2.4', 0HZ, 999GHZ, 50.0, MALE, COAX, 0.0")  
session.write("SENS:CORR:COLL:CKIT:CONN:ADD 'PSC 2.4', 0HZ, 999GHZ, 50.0,
FEMALE, COAX, 0.0")  
  
_# Verify no connectors are currently installed '_  
newConn = session.query("SENS:CORR:COLL:CKIT:CONN:CAT?")  
print(f"Verify new connectors: {newConn}")  
  
_# Set up Standard #1_  
print("Defining conn std 1...")  
session.write("SENS:CORR:COLL:CKIT:STAN 1")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',FEMALE,1")  
Print_connector()  
  
_# Set up Standard #2_  
print("Defining conn std 2...")  
session.write("SENS:CORR:COLL:CKIT:STAN 2")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',FEMALE,1")  
Print_connector()  
  
_# Set up Standard #3_  
print("Defining conn std 3...")  
session.write("SENS:CORR:COLL:CKIT:STAN 3")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',FEMALE,1")  
Print_connector()  
  
_# Set up Standard #4_  
print("Defining conn std 4...")  
session.write("SENS:CORR:COLL:CKIT:STAN 4")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',FEMALE,1")  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',MALE,2")  
Print_connector()  
  
_# Set up Standard #5_  
print("Defining conn std 5...")  
session.write("SENS:CORR:COLL:CKIT:STAN 5")  
session.write("SENS:CORR:COLL:CKIT:STAN:LAB 'Sliding Load'")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',MALE,1")  
Print_connector()  
  
_# Set up Standard #6_  
print("Defining conn std 6...")  
session.write("SENS:CORR:COLL:CKIT:STAN 6")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',MALE,1")  
Print_connector()  
  
_# Set up Standard #7_  
print("Defining conn std 7...")  
session.write("SENS:CORR:COLL:CKIT:STAN 7")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',MALE,1")  
Print_connector()  
  
_# Set up Standard #8_  
print("Defining conn std 8...")  
session.write("SENS:CORR:COLL:CKIT:STAN 8")  
Verify_std()  
session.write("SENS:CORR:COLL:CKIT:CONN:SNAM 'PSC 2.4',MALE,1")  
Print_connector()  
  
print("Class Assignments...")  _# Designate the order associated with
measuring the standards_  
_# Set Port 1, 1st standard measured to be standard #2_  
session.write("SENS:CORR:COLL:CKIT:ORD1 2")  
_# Set Port 1, 2nd standard measured to be standard #1_  
session.write("SENS:CORR:COLL:CKIT:ORD2 1,6,7")  
_# Set Port 1, 3rd standard measured to be standard #3 and #5_  
session.write("SENS:CORR:COLL:CKIT:ORD3 3,5")  
_# Set Port 1, 4th standard measured to be standard #4_  
session.write("SENS:CORR:COLL:CKIT:ORD4 4")  
  
_# Set Port 2, 1st standard measured to be standard #2_  
session.write("SENS:CORR:COLL:CKIT:ORD5 2")  
_# Set Port 2, 2nd standard measured to be standard #1_  
session.write("SENS:CORR:COLL:CKIT:ORD6 1,6,7")  
_# Set Port 2, 3rd standard measured to be standard #3 and #6_  
session.write("SENS:CORR:COLL:CKIT:ORD7 3,5")  
_# Set Port 2, 4th standard measured to be standard #4_  
session.write("SENS:CORR:COLL:CKIT:ORD8 4")  
  
_# Set Port 1, 1st standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB1 'MyOpen1'")  
_# Set Port 1, 2nd standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB2 'MyShorts1'")  
_# Set Port 1, 3rd standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB3 'MyLoads1'")  
_# Set Port 1, 4th standard measured to be standard #4_  
session.write("SENS:CORR:COLL:CKIT:OLAB4 'MyThrus1'")  
  
_# Set Port 2, 1st standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB5 'MyOpen2'")  
_# Set Port 2, 2nd standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB6 'MyShorts2'")  
_# Set Port 2, 3rd standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB7 'MyLoads2'")  
_# Set Port 2, 4th standard_  
session.write("SENS:CORR:COLL:CKIT:OLAB8 'MyThrus2'")  
  
print("Done")  
  
---

