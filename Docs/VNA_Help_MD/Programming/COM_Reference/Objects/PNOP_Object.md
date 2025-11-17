# PNOP Object

* * *

### Description

Contains the methods and properties that initiate and return Power Normal
Operating Point markers.

### Accessing the PNOP Object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application")  
  
Dim pnop As PNOP  
Set pnop = app.ActiveMeasurement.PNOP

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [PNOP Markers](../../../S4_Collect/Markers.md#PNOP)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[SearchPowerNormalOperatingPoint](../Methods/SearchPowerNormalOperatingPoint_Method.md) |  IPNOP |  Initiates a PNOP search  
  
### Properties

|

###

|

### Description  
  
[BackOff](../Properties/BackOff_Property.md) |  IPNOP |  Sets and returns the backoff value.  
[BackOffGain](../Properties/BackOffGain_Property.md) |  IPNOP |  Returns the BackOffGain result.  
[BackOffPIn](../Properties/BackOffPIn_Property.md) |  IPNOP |  Returns the BackOffPIn result  
[BackOffPout](../Properties/BackOffPout_Property.md) |  IPNOP |  Returns the BackOffPout result  
[Compression](../Properties/Compression_Property.md) |  IPNOP |  Returns the Compression result  
[CompressionMax](../Properties/CompressionMax_Property.md) |  IPNOP |  Returns the Compression Max result  
[Gain](../Properties/Gain_Property.md) |  IPNOP |  Returns the Gain result  
[GainMax](../Properties/GainMax_Property.md) |  IPNOP |  Returns the Gain Max result  
[Pin](../Properties/Pin_Property.md) |  IPNOP |  Returns the Pin result  
[PinOffset](../Properties/PinOffset_Property.md) |  IPNOP |  Sets and returns the PinOffset value  
[PMaxIn](../Properties/PMaxIn_Property.md) |  IPNOP |  Returns the PMaxIn result  
[PMaxOut](../Properties/PMaxOut_Property.md) |  IPNOP |  Returns the PMaxOut result  
[POut](../Properties/POut_Property.md) |  IPNOP |  Returns the P Out result  
  
###  IPNOP History

Interface |  Introduced with VNA Rev:  
---|---  
IPNOP |  A.09.20  
  
* * *

