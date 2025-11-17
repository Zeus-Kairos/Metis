# PhaseControl Object

* * *

### Description

Contains the properties for configuring Phase Sweep (Opt S93088A/B) in the
VNA.

### Accessing the PhaseControl object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim phase as PhaseControl  
Set phase = chan.PhaseControl

### See Also:

  * [About Phase Control](../../../S1_Settings/Phase_Control.md)

  * Set Phase Sweep using [SweepType Property](../Properties/Sweep_Type_Property.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Program](../../COM_Example_Programs/Setup_Phase_Control.md)

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
  
[CouplePhasePortSettings](../Properties/CouplePhasePortSettings_Property.md) | IPhaseControl | Set and return whether to couple phase control settings.  
[FixedPhase](../Properties/FixedPhase_Property.md) | IPhaseControl | Set and return the fixed phase value.  
[FixedRatioedPower](../Properties/FixedRatioedPower_Property.md) | IPhaseControl | Set and return the fixed ratioed power value.  
[PhaseControlMode](../Properties/PhaseControlMode_Property.md) | IPhaseControl | Set and return the ON/Off state of phase control.  
[PhaseCorrectionData](../Properties/PhaseCorrectionData_Property.md) | IPhaseControl | Set and return an array of phase offsets.  
[PhaseCorrectionEnabled](../Properties/PhaseCorrectionEnabled_Property.md) | IPhaseControl | Set and return whether to use the phase correction offset array.  
[PhaseIterationNumber](../Properties/PhaseIterationNumber_Property.md) | IPhaseControl | Set and return max number of leveling sweeps  
[PhaseParameter](../Properties/PhaseParameter_Property.md) | IPhaseControl | Set and return the ratioed receivers (parameter) to use for phase control.  
[PhaseParameterModes](../Properties/PhaseParameterModes_Property.md) | IPhaseControl | Returns the available phase control modes for the specified port.  
[PhaseReferencePort](../Properties/PhaseReferencePort_Property.md) | IPhaseControl | Sets and returns the reference port for the Phase Control measurement.  
[PhaseTolerance](../Properties/PhaseTolerance_Property.md) | IPhaseControl | Set and return tolerance value for leveling sweeps  
[RatioedPowerCorrectionData](../Properties/RatioedPowerCorrectionData_Property.md) | IPhaseControl | Set and return ratioed power offset data  
[RatioedPowerCorrectionEnabled](../Properties/RatioedPowerCorrectionEnabled_Property.md) | IPhaseControl | Set and return whether to use the ratioed power offset array  
[StartPhase](../Properties/StartPhase_Property.md) | IPhaseControl | Set and return the start value of phase sweep.  
[StartRatioedPower](../Properties/StartRatioedPower_Property.md) | IPhaseControl | Set and return the start ratioed power value.  
[StopPhase](../Properties/StopPhase_Property.md) | IPhaseControl | Set and return the stop value of phase sweep.  
[StopRatioedPower](../Properties/StopRatioedPower_Property.md) | IPhaseControl | Set and return the stop ratioed power value.  
  
###  IPhaseControl History

Interface | Introduced with VNA Rev:  
---|---  
IPhaseControl | 9.33  
  
* * *

