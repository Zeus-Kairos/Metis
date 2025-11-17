# ENRFile Object

* * *

### Description

Provide commands for creating or editing an ENR file. This is rarely necessary
as ENR files, which contain factory calibrated data, are typically provided by
the manufacturer of the noise source.

[Learn more about Noise Figure
Application](../../../Applications/Noise_Figure.htm)

### Accessing the ENRFile object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim enr As ENRFile  
Set enr = app.ENRFile

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Program](../../COM_Example_Programs/ENR_File_Management_Example.md)

### Methods

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
---|---|---  
[GetENRData](../Methods/GetENRData_Method.md) | IENRFile | Read the ENR calibration data from VNA memory.  
[PutENRData](../Methods/PutENRData_Method.md) | IENRFile | Write the ENR calibration data to VNA memory.  
[LoadENRFile](../Methods/LoadENRFile_Method.md) | IENRFile | Recalls an ENR file from disk into VNA Memory.  
[SaveENRFile](../Methods/SaveENRFile_Method.md) | IENRFile | Saves an ENR file from VNA memory to disk.  
  
### Properties

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
[ENRID](../Properties/ENRID_Property.md) | IENRFile | Sets and returns ID of ENR table.  
[ENRSN](../Properties/ENRSN_Property.md) | IENRFile | Sets and returns the serial number of the noise source.  
[NoiseCalTemperature](../Properties/NoiseCalTemperature_Property.md) | IENRFile | Read the cal temperature of the noise source.   
  
###  IENRFile History

Interface | Introduced with VNA Rev:  
---|---  
IENRFile | 8.0  
|  
  
* * *

