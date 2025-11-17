# PSaturation Object

* * *

### Description

Contains the methods and properties that initiate a Power Saturation marker
search and returns PSAT data.

### Accessing the PSaturation Object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application")  
  
Dim PSat As PSaturation  
Set PSat = app.ActiveMeasurement.PSaturation

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [PSaturation Markers](../../../S4_Collect/Markers.md#PSat)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[SearchPowerSaturation](../Methods/SearchPowerSaturation_Method.md) |  IPSaturation |  Initiates a Power Saturation marker search.  
  
### Properties

|

###

|

### Description  
  
[CompressionMax](../Properties/CompressionMax_Property.md) |  IPSaturation |  Returns the Compression Max result of a PSat marker search.  
[CompressionSaturation](../Properties/CompressionSaturation_Property.md) |  IPSaturation |  Returns the Compression Saturation result of a PSat marker search.  
[GainLinear](../Properties/GainLinear_Property.md) |  IPSaturation |  Returns the Linear Gain result of a PSat marker search.  
[GainMax](../Properties/GainMax_Property.md) |  IPSaturation |  Returns the GainMax result of a PSAT marker search.  
[GainSaturation](../Properties/GainSaturation_Property.md) |  IPSaturation |  Returns the GainSaturation result of a PSAT marker search.  
[Pin](../Properties/Pin_Property.md) |  IPSaturation |  Returns the Pin result of a PSAT marker search.  
[PMaxBackOff](../Properties/PMaxBackOff_Property.md) |  IPSaturation |  Sets and returns the backoff value used to calculate various PSAT parameters.  
[PMaxIn](../Properties/PMaxIn_Property.md) |  IPSaturation |  Returns the PMaxIn result of a PSAT marker search.  
[PMaxOut](../Properties/PMaxOut_Property.md) |  IPSaturation |  Returns the PMaxOut result of a PSAT marker search.  
[POut Property](../Properties/POut_Property.md) |  IPSaturation |  Returns the POut result of a PSAT marker search.  
  
###  IPSaturation History

Interface |  Introduced with VNA Rev:  
---|---  
IPSaturation |  A.09.20  
  
* * *

