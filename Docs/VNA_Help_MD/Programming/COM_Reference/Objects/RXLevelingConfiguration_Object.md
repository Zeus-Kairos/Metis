# RxLevelingConfiguration Object

* * *

### Description

Contains the properties for configuring Receiver Leveling in the VNA.

### Accessing the RxLevelingConfiguration object

Dim app as AgilentPNA835x.Application Dim chan as Channel Set chan =
app.ActiveChannel Dim RxLevel as RxLevelingConfiguration Set RxLevel =
chan.RxLevelingConfiguration  
---  
  
### See Also:

  * [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Program](../../COM_Example_Programs/Setup_Receiver_Leveling.md)

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
  
[FastMode](../Properties/FastMode_Property.md) |  IRxLevelingConfiguration |  Select separate IFBW for leveling sweeps  
[FrequencyType](../Properties/FrequencyType_Property.md) |  IRxLevelingConfiguration3 |  Frequency range to use for receiver leveling.  
[IterationNumber](../Properties/IterationNumber_Property.md) |  IRxLevelingConfiguration |  Max number of leveling sweeps  
[LastLevelingAsSPC](../Properties/LastLevelingAsSPC_Property.md) |  IRxLevelingConfiguration2 |  Turn ON Source Power Cal using latest correction data  
[LevelingIFBW](../Properties/LevelingIFBW_Property.md) |  IRxLevelingConfiguration |  IFBW for leveling sweeps  
[PowerMax](../Properties/PowerMax_Property.md) |  IRxLevelingConfiguration |  Max power for safe mode  
[PowerMin](../Properties/PowerMin_Property.md) |  IRxLevelingConfiguration |  Min power for safe mode  
[PowerOffset](../Properties/PowerOffset_Property.md) |  IRxLevelingConfiguration |  Offset power for external components  
[PowerStep](../Properties/PowerStep_Property.md) |  IRxLevelingConfiguration |  Power step for safe mode  
[ReferenceReceiver](../Properties/ReferenceReceiver_Property.md) |  IRxLevelingConfiguration |  Select a receiver  
[SafeMode](../Properties/SafeMode_Property.md) |  IRxLevelingConfiguration |  Enable safe mode  
[State](../Properties/State_rx_Property.md) |  IRxLevelingConfiguration |  Enable receiver leveling  
[Tolerance](../Properties/Tolerance_Property.md) |  IRxLevelingConfiguration |  Tolerance value for leveling sweeps  
  
###  ReceiverLevelingConfiguration History

Interface |  Introduced with VNA Rev:  
---|---  
IRxLevelingConfiguration |  8.5  
IRxLevelingConfiguration2 |  9.30  
IRxLevelingConfiguration3 |  9.50  
  
* * *

  

