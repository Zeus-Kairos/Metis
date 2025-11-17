# PhaseReferenceCalibration Object

* * *

### Description

Use this interface to perform a Phase Reference Calibration. This calibration
is performed as a 'Tier 1' cal. After it is performed and saved, it can then
be recalled into an SMC+Phase Calibration.

  * It is NOT necessary to create an SMC measurement before performing a remote Phase Reference Cal. It is necessary when performed from the user interface.

  * Port selection is made remotely by selecting connectors and Cal Kits for the ports to be included in the SOLT calibration.

### Accessing the PhaseReferenceCalibration Object

Dim app as AgilentPNA835x.Application Dim CalMgr Set CalMgr =
app.GetCalManager Dim phaseRefCal Set phaseRefCal =
CalMgr.PhaseReferenceCalibration 'Then get a handle to the GuidedCal object
Dim guidedCal Set guidedCal = phaseRefCal.GuidedCalibration  
---  
  
### See Also:

  * [Example program](../../COM_Example_Programs/Perform_a_CalAllChannels_Calibration.md)

  * Learn about [Calibrate All Channels](../../../S3_Cals/Calibrate_All_Channels.md).

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

In the following table IPhaseReferenceCalibration is abbreviated to
IPhaseRefCal

### Methods

|

### Interface

[See History](CalManager_Object.md#Interface1) | 

### Description  
  
---|---|---  
[GetConnectedPhaseReferences](../Methods/GetConnectedPhaseReferences_Method.md) |  IPhaseRefCal |  Reads the ID strings of the phase references that are currently connected to the VNA USB  
[Reset](../Methods/Reset_\(CalAll\)_Method.md) |  IPhaseRefCal |  Resets all properties associated with the Cal All session to their default values.  
  
### Properties

|

###

|

###  
  
[CalKitType](../Properties/CalKitType_PhaseRef_Property.md) |  IPhaseRefCal2 |  Sets and returns the Cal Kit to be used during the S-parameter portion of a Phase Reference calibration.  
[CalSet](../Properties/CalSet_Property.md) |  IPhaseRefCal |  Sets and reads the Cal Set name into which the calibration will be saved.  
[GuidedCalibration](GuidedCalibration_Object.md) |  IPhaseRefCal |  Provides access to the GuidedCal object. Use this to perform the Calibration.  
[IncludePort](../Properties/IncludePort_Property.md) |  IPhaseRefCal2 |  Sets and returns the enable state for the specified port.  
[IncludeUnknownMixer](../Properties/IncludeUnknownMixer_Property.md) |  IPhaseRefCal2 |  Sets and returns the state of Unknown Mixer calibration.  
[PhaseReference](../Properties/PhaseReference_Property.md) |  IPhaseRefCal |  Sets and returns the Phase Reference ID to be used for the Phase Reference calibration.  
[SourceAttenuator](../Properties/SourceAttenuator_PR_Property.md) |  IPhaseRefCal |  Sets and returns the Source Attenuator setting.  
[StartFrequency](../Properties/StartFrequency_PR_Property.md) |  IPhaseRefCal |  Sets and returns the phase reference cal start frequency.  
[StopFrequency](../Properties/Stop_Frequency_Property.md) |  IPhaseRefCal |  Sets and returns the phase reference cal stop frequency.  
[UnknownMixerInputPower](../Properties/UnknownMixerInputPower_Property.md) |  IPhaseRefCal2 |  Sets and returns the input power level to the unknown mixer.  
[UnknownMixerLOFrequency](../Properties/UnknownMixerLOFrequency_Property.md) |  IPhaseRefCal2 |  Sets and returns the LO Frequency of the unknown mixer.  
[UnknownMixerLOPower](../Properties/UnknownMixerLOPower_Property.md) |  IPhaseRefCal2 |  Sets and returns the LO power level to the unknown mixer.  
  
###  IPhaseReferenceCalibration History

Interface |  Introduced with VNA Rev:  
---|---  
IPhaseReferenceCalibration |  9.70  
  
* * *

