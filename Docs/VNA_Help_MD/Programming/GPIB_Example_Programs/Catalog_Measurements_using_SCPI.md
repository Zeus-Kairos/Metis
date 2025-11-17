# Catalog Measurements using SCPI

* * *

This Python Program does the following:

  * Catalogs the currently defined measurements, windows, and traces

  * Selects a measurement for further definition

  * Adds a Title to the window

#### See Also:

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

[SCPI Example Programs](SCPI_Example_Programs.md)

**import** **pyvisa** **as** **visa**  
  
**_# Change this variable to the address of your instrument_**  
**VISA_ADDRESS =** **' TCPIP0::localhost::inst0::INSTR'**  
  
**_# Create a connection (session) to the instrument_**  
**resourceManager = visa.ResourceManager()**  
**session = resourceManager.open_resource(VISA_ADDRESS)**  
  
**def** **convertStrings****(****oldString****):**  
**********_# Remove the quotation marks and new line char_**  
**newString = oldString.replace(****' "'****,****' '****)**  
**newString = newString.replace(****'****\n****'****,****' '****)**  
**newString = newString.split(****' ,'****)**  
**********return** **newString**  
  
**_# Read the current measurements in Channel 1_**  
**currMeas = session.query(****" CALC:PAR:CAT:EXT?"****)**  
**currMeas = convertStrings(currMeas)**  
**print****(****f****" Ch1 Measurements:**
**{****currMeas****}****\n****"****)**  
  
**_# Read the current windows_**  
**currWindow = session.query(****" DISP:CAT?"****)**  
**currWindow = convertStrings(currWindow)**  
**print****(****f****" Windows:** **{****currWindow****}****\n****"****)**  
  
**_# Read trace numbers in window 1, returns string "EMPTY" if no traces_**  
**if** **(currWindow == [****' EMPTY'****]):**  
**currTrace = [****' EMPTY'****]**  
**else****:**  
**currTrace = session.query(****" DISP:WIND1:CAT?"****)**  
**currTrace = convertStrings(currTrace)**  
**print (f"Traces in Window1: {currTrace}\n") **  
---

