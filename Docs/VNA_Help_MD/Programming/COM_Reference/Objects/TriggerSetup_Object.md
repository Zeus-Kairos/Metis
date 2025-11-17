# TriggerSetup Object

* * *

### Description

These properties setup Global triggering that effects the entire VNA
application.

### Accessing the TriggerSetup object

Dim app as AgilentPNA835x.Application  
Dim trigSetup as ITriggerSetup  
Set trigSetup = app.TriggerSetup

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
  
[AcceptTriggerBeforeArmed](../Properties/AcceptTriggerBeforeArmed_Property.md) |  ITriggerSetup2 |  Allows a trigger signal to be remembered and then used when the VNA becomes armed (ready to be triggered).  
[ExternalTriggerConnectionBehavior](../Properties/ExternalTriggerConnectionBehavior_Property.md) |  ITriggerSetup |  Configures the external triggering signal for the VNA  
[ReadyForTriggerPolarity](../Properties/ReadyForTriggerPolarity_Property.md) |  ITriggerSetup3 |  Specifies the polarity of Ready for Trigger output.  
[ReadyForTriggerStatus](../Properties/ReadyForTriggerStatus_Property.md) |  ITriggerSetup4 |  Checks if the PNA is ready for a specific or any hardware trigger  
[Scope](../Properties/Scope_Property.md) |  ITriggerSetup |  Determines whether a trigger signal affects a single channel or all channels in the VNA.  
[Source](../Properties/Source_Property.md) |  ITriggerSetup |  Sets or returns the source of triggering in the VNA.  
[TriggerOutputEnabled](../Properties/TriggerOutputEnabled_Property.md) |  ITriggerSetup2 |  Superseded Enables the VNA to send trigger signals out the rear-panel TRIGGER OUT connector.  
  
###  ITriggerSetup History

Interface |  Introduced with VNA Rev:  
---|---  
ITriggerSetup |  4.0  
ITriggerSetup2 |  4.2  
ITriggerSetup3 |  7.50.2 and 8.2  
ITriggerSetup4 |  12.80

