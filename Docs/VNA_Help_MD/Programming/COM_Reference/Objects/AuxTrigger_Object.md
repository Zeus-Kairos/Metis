# AuxiliaryTrigger Object

* * *

### Description

These properties setup Auxiliary triggering on a channel.

### Accessing the object

Use chan.AuxTrigger (n) to access the object.

where n= the connector pair to be used for Auxiliary Triggering.

  * VNA models: Use 1 or 2

Use
[app.AuxiliaryTriggerCount](../Properties/AuxiliaryTriggerCount_Property.md)
to determine the number of auxiliary trigger pairs on the rear panel of a VNA.

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim AuxTrig as AuxTrigger  
AuxTrig = chan.AuxTrigger(2)

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Triggering in the VNA](../../../S1_Settings/Trigger.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History (below)](TriggerSetup_Object.md#history) | 

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[Delay](../Properties/Delay_trigger_Property.md) (Input) |  IAuxTrigger |  Specifies the delay that should be applied by the VNA after the Aux trigger input is received and before the acquisition is made  
[Enable](../Properties/Enable_Property.md) |  IAuxTrigger |  Turns ON / OFF the trigger output.  
[HandshakeEnable](../Properties/HandshakeEnable_Property.md) (Input) |  IAuxTrigger |  Turns handshake ON / OFF.  
[Number](../Properties/Number_Property.md) |  IAuxTrigger |  Reads the number of the Aux I/O pair being used.  
[TriggerInPolarity](../Properties/TriggerInPolarity_Property.md) (Input) |  IAuxTrigger |  Specifies the polarity of the trigger IN signal to which the VNA will respond.  
[TriggerInType](../Properties/TriggerInType_Property.md) (Input) |  IAuxTrigger |  Specifies the type of Aux trigger input being supplied to the VNA  
[TriggerOutDuration](../Properties/TriggerOutDuration_Property.md) |  IAuxTrigger |  Specifies the width of the pulse or the time that the Aux trigger output will be asserted  
[TriggerOutInterval](../Properties/TriggerOutInterval_Property.md) |  IAuxTrigger |  Specifies how often a trigger output signal is sent.  
[TriggerOutPolarity](../Properties/TriggerOutPolarity_Property.md) |  IAuxTrigger |  Specifies the polarity of the trigger output signal being supplied by the VNA.  
[TriggerOutPosition](../Properties/TriggerOutPosition_Property.md) |  IAuxTrigger |  Specifies whether the Aux trigger out signal is sent Before or After the acquisition.  
  
### IAuxTrigger History

Interface |  Introduced with VNA Rev:  
---|---  
IAuxTrigger |  7.2  
|  
  
* * *

