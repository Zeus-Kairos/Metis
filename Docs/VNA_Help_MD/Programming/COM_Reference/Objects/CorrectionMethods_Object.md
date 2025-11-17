# CorrectionMethods Object

* * *

### Description

These methods and properties control various error-correction settings for a
channel.

### Accessing the object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim corrMethods as CorrectionMethods  
corrMethods = chan.CorrectionMehods

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History (below)](TriggerSetup_Object.md#history) | 

### Description  
  
---|---|---  
[ResetPortValues](../Methods/ResetPortValues_Method.md) |  ICorrectionMethods2 |  Resets the full and response list to their default values.  
  
### Properties

|

###

|

### Description  
  
[CorrectionSubsettingState](../Properties/CorrectionSubsettingState_Property.md) |  ICorrectionMethods2 |  Set and return the ON/OFF subset correction state.  
[FullyCorrectedPorts](../Properties/FullyCorrectedPorts_Property.md) |  ICorrectionMethods2 |  Sets and returns the selected ports to include in a full NPort correction.  
[MatchCorrectPower](../Properties/MatchCorrectPower_Property.md) |  ICorrectionMethods |  Turns match-correction ON or OFF after performing an Enhanced Power Cal.  
[ResponseCorrectedPorts](../Properties/ResponseCorrectedPorts_Property.md) |  ICorrectionMethods2 |  Sets and returns the selected ports to be corrected with enhanced response calibration.  
  
### IAuxTrigger History

Interface |  Introduced with VNA Rev:  
---|---  
ICorrectioMethods |  9.30  
ICorrectionMethods2 |  12.70  
  
* * *

