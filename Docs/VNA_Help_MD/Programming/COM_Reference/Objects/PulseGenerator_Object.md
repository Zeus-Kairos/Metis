# PulseGenerator Object

* * *

### Description

Contains the properties for configuring the five internal pulse generators in
the PNA-X.

[Learn more about the PNA-X Pulse
Generators.](../../../IFAccess/IF_Path_Configuration.htm#PulseGens)

### Accessing the PulseGenerator object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim pulse as PulseGenerator  
Set pulse = chan.PulseGenerator

Each pulse generator is specified in the Pulse Generator properties.

External Pulse Generators Beginning with A.09.50, [External Pulse
Generators](ExternalPulseGenerator_Object.htm) can be used with the Integrated
Pulse Application. Use
chan.[PulseGeneratorNames](../Properties/PulseGeneratorNames_Property.md) and
chan.[PulseGeneratorID](../Properties/PulseGeneratorID_Property.md) to refer
to the external pulse generator when setting properties on this
(PulseGenerator) Object.  
---  
  
### Pulse Definitions

![](../../../assets/images/Programming/PulseDiag.gif)

  * D = Delay; the time before each pulse begins
  * W = Width; the time the pulse is ON
  * P = Period; one complete pulse cycle
  * W/P = Duty Cycle; the ratio of pulse ON/OFF

Important: If D + W is greater than P, then undefined VNA behavior results.
There is NO error message or warning.  
---  
  
### See Also:

  * [IF Path Block Diagram.](../../../IFAccess/IF_Path_Configuration.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * About PNA-X Pulse Measurements

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

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
  
[Delay](../Properties/Delay_pulse_Property.md) | IPulsedGenerator | Sets the pulse delay.  
[DelayIncrement](../Properties/DelayIncrement_Property.md) | IPulsedGenerator | Sets the pulse delay increment.  
[EnableOffsetDelays](../Properties/EnableOffsetDelays_Property.md) | IPulsedGenerator5 | Enables / Disables offset delays.  
[ADCDelay](../Properties/FixedADCDelay_Property.md) | IPulsedGenerator5 | Returns the ADC delay.  
[Invert](../Properties/Invert_Property.md) | IPulsedGenerator4 | Sets whether to invert the polarity of the pulse.  
[ModulatorDelay](../Properties/ModulatorDelay_Property.md) | IPulsedGenerator5 | Sets the time lag between the pulse drive signal and the actual RF output.  
[Period](../Properties/Period_Property.md) | IPulsedGenerator | Sets the pulse-period (1/PRF) for ALL PNA-X internal pulse generators.  
[Pulse4OutAsADCActivity](../Properties/Pulse4OutAsADCActivity_Property.md) | IPulsedGenerator5 | Enables / Disables pulse4 to use an oscilloscope connected to pin 13 of the [PULSE I/O connector](../../../Rear_Panel/XPulseIO.md) on the rear panel of the VNA to display when the ADC is making measurements.  
[PulseTimingDevice](../Properties/PulseTimingDevice_Property.md) | IPulsedGenerator6 | Sets the device being controlled by the pulse generator output.  
[State](../Properties/State_pulse_Property.md) | IPulsedGenerator | Turns the specified pulse generator ON and OFF.  
[SubPointTrigger](../Properties/SubPointTrigger_Property.md) | IPulsedGenerator2 | Enables / Disables subpoint triggering.  
[TriggerInPolarity](../Properties/TriggerInPolarity_Property.md) | IPulsedGenerator3 | Sets the polarity of trigger to which the internal pulse generators will respond when being externally triggered.  
[TriggerInType](../Properties/TriggerInType_Property.md) | IPulsedGenerator3 | Sets the type of trigger to which the internal pulse generators will respond when being externally triggered.  
[Width](../Properties/Width_Property.md) | IPulsedGenerator | Sets the pulse width for the specified pulse generator.  
  
###  IPulseGenerator History

Interface | Introduced with VNA Rev:  
---|---  
IPulseGenerator | 7.2  
IPulseGenerator2 | 8.55.09  
IPulseGenerator3 | 9.10  
IPulseGenerator4 | 9.33  
IPulseGenerator5 | 13.50  
IPulseGenerator6 | 13.60  
  
* * *

  

