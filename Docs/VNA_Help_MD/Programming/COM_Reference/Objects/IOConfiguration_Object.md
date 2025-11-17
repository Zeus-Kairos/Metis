# IOConfiguration Object

* * *

Description

Contains the methods and properties that support IO Configuration.

### Accessing the IOConfiguration object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim IOConfig As IOConfiguration  
Set IOConfig = app.IOConfiguration

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [IO Configuration topic](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.md#configure)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[HiSLIPAddress](../Properties/HiSLIPAddress_Property.md) |  IOConfiguration |  Set and returns HiSLIP instrument number.  
[HiSLIPPort](../Properties/HiSLIPPort_Property.md) |  IOConfiguration |  Set and returns the TCPIP port for HiSLIP communication.  
[InterfaceTypes](../Properties/InterfaceTypes_Property.md) |  IOConfiguration |  Returns the valid interface types for the VNA.  
[VisaResourceString](../Properties/VisaResourceString_Property.md) |  IOConfiguration |  Returns the valid resource string for the specified interface type.  
  
###  IOConfiguration History

Interface |  Introduced with VNA Rev:  
---|---  
IIOConfiguration |  10.0  
|

