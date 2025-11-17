# IFConfiguration Object

* * *

### Description

These properties control the IF gain and source path settings for the PNA-X
([IFConfiguration3](IIFConfiguration_Object.md#history) commands ONLY).

### Accessing the IFConfiguration object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim cfg as IIFConfiguration  
Set cfg = chan.IFConfiguration

### See Also

  * [IF Path Configuration](../../../IFAccess/IF_Path_Configuration.md)

  * [SignalProcessingModuleFour Object](SignalProcessingModuleFour_Object.md) (PNA-X ONLY)

  * [PulseGenerator Object](PulseGenerator_Object.md) (PNA-X ONLY)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * Pulsed Application

### Methods

|

###

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[IFFrequency](../Properties/IFFrequency_Property.md) |  IFConfiguration3 |  Sets IF frequency in manual mode.  
[IFFrequencyMode](../Properties/IFFrequencyMode_Property.md) |  IFConfiguration3 |  Sets IF frequency mode to automatic or manual.  
[MaximumIFFrequency](../Properties/MaximumIFFrequency_Property.md) |  IFConfiguration3 |  Returns the maximum IF frequency setting  
[MinimumIFFrequency](../Properties/MinimumIFFrequency_Property.md) |  IFConfiguration3 |  Returns the minimum IF frequency setting  
  
###  IFConfiguration History

Interface |  Introduced with VNA Rev:  
---|---  
IIFConfiguration |  4.0  
IIFConfiguration2 |  4.0  
IIFConfiguration3 |  7.2  
  
* * *

