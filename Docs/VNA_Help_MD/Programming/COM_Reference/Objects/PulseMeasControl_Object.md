# PulseMeasControl Object

* * *

### Description

Contains the properties for configuring pulse measurements in the PNA-X.

Some of these settings require Opt H08 / S93026A/B.

Learn about Integrated Pulse Application.

### Accessing the PulseMeasControl object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim pulse as PulseMeasControl  
Set pulse = chan.PulseMeasControl

The following shows how to make two new settings introduced with A.09.50:

  * Primary Pulse Trigger \- to select an external pulse generator as the primary trigger, use IPathElement.Value and using PulseTrigInput = Internal or External. However, there is no way to tell which external pulse generator is selected.
  * To select an external pulse generator for a receiver, use [IPathElement.Value](../Properties/Value_element_Property.md) commands. For example, to select an external pulse generator for RCVR A, send "IFGateA,RearPanel.

  
---  
  
### See Also:

  * [IF Path Block Diagram.](../../../IFAccess/IF_Path_Configuration.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

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
  
[AutoCWSweepTime](../Properties/AutoCWSweepTime_Property.md) | IPulseMeasControl2 | Sets the state of automatic CW sweep time in Pulse Profile mode.  
[AutoDetection](../Properties/AutoDetection_Property.md) | IPulseMeasControl | Automatically or manually set pulse mode (Narrowband or Wideband)  
[AutoIFBandWidth](../Properties/AutoIFBandWidth_Property.md) | IPulseMeasControl | Autoselect the IFBW  
AutoIFGain | IPulseMeasControl | For future use.  
[AutoOptimizePRF](../Properties/AutoOptimizePRF_Property.md) | IPulseMeasControl | Auto-optimize pulse clock period  
[AutoPulseTiming](../Properties/AutoPulseTiming_Property.md) | IPulseMeasControl | Autoselect Width and Delay  
[AutoSelectPulseGen](../Properties/AutoSelectPulseGen_Property.md) | IPulseMeasControl | Autoselect Pulse Generators  
[PrimaryFrequency](../Properties/MasterFrequency_Property.md) | IPulseMeasControl2 | Sets the pulse repetition frequency (PRF) for ALL internal pulse generators.  
[PrimaryPeriod](../Properties/MasterPeriod_Property.md) | IPulseMeasControl2 | Sets the period for ALL internal pulse generators.  
[PrimaryWidth](../Properties/MasterWidth_Property.md) | IPulseMeasControl2 | Sets the pulse width for ALL internal pulse generators.  
[Parent](../Properties/Parent_Property.md) | IPulseMeasControl | Returns the channel object  
[PulseMeasMode](../Properties/PulseMeasMode_Property.md) | IPulseMeasControl | Select Pulse Measurement selection  
[PulseProfileStart](../Properties/PulseProfileStart_Property.md) | IPulseMeasControl3 | Sets and returns the start time of the profile pulse.  
[PulseProfileStop](../Properties/PulseProfileStop_Property.md) | IPulseMeasControl3 | Sets and returns the stop time of the profile pulse.  
[SoftwareGateState](../Properties/SoftwareGateState_Property.md) | IPulseMeasControl2 | This setting is used for troubleshooting purposes.  
[WideBandDectionState](../Properties/WideBandDectionState_Property.md) | IPulseMeasControl | Select Narrowband or Wideband pulse detection.  
  
###  IPulseMeasControl History

Interface | Introduced with VNA Rev:  
---|---  
IPulseMeasControl | 9.2  
IPulseMeasControl2 | 9.40  
IPulseMeasControl3 | 10.45  
  
* * *

  

