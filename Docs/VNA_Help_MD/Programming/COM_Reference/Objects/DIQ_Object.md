# DifferentialIQ Object

* * *

### Description

Controls the Differential I/Q application settings.

### Accessing the Diff IQ and Diff IQMeas objects

Dim app as AgilentPNA835x.Application app.CreateCustomMeasurementEx 2,
"Differential I/Q", "IPwrF1" Dim DIQ Set DIQ =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)
Dim DiqMeas Set DiqMeas = app.ActiveMeasurement.CustomMeasurementConfiguration  
---  
  
### See Also:

  * [Differential I/Q application](../../../Applications/Differential_IQ.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

Diff IQ Setup Dialog |   
---|---  
![](../../../assets/images/IQSetupDiag.gif) |  [AddRange Method](../Methods/AddRange_Method.md)  
[DeleteRange Method](../Methods/DeleteRange_Method.md)  
[RangeCount Method](../Methods/RangeCount_Method.md)  
Range Settings Dialog |  |   
---|---|---  
![](../../../assets/images/IQRangeSettingsDiag.gif) |  Frequency |  [RangeStartFrequency](../Properties/RangeStartFrequency_Property.md)  
[RangeStopFrequency](../Properties/RangeStopFrequency_Property.md)  
[RangeIFBW Property](../Properties/RangeIFBW_Property.md)  
Coupling |  [RangeCoupleState Property](../Properties/RangeCoupleState_Property.md)  
[RangeCoupleId Property](../Properties/RangeCoupleId_Property.md)  
[RangeOffset Property](../Properties/RangeOffset_Property.md)  
[RangeOffsetUp Property](../Properties/RangeOffsetUp_Property.md)  
[RangeMultiplier Property](../Properties/RangeMultiplier_Property.md)  
[RangeDivisor Property](../Properties/RangeDivisor_Property.md)  
Source Configuration Dialog |   
---|---  
![](../../../assets/images/IQSourceConfigDiag.gif) |  |  [SourceState Property](../Properties/SourceState_Property.md)  
[SourceRange Property](../Properties/SourceRange_Property.md)  
Power |  [PowerSweepState Property](../Properties/PowerSweepState_Property.md)  
[PortStartPower Property](../Properties/PortStartPower_Property.md)  
[PortStopPower Property](../Properties/PortStopPower_Property.md)  
[PortLevelingMode Property](../Properties/PortLevelingMode_Property.md)  
[PortAttenuator Property](../Properties/PortAttenuator_Property.md)  
[AutoRangeState Property](../Properties/AutoRangeState_Property.md)  
Phase |  [PortPhaseState Property](../Properties/PortPhaseState_Property.md)  
[PhaseSweepState Property](../Properties/PhaseSweepState_Property.md)  
[PortPhaseStart Property](../Properties/PortPhaseStart_Property.md)  
[PortPhaseStop Property](../Properties/PortPhaseStop_Property.md)  
[PortReference Property](../Properties/PortReference_Property.md)  
[PortPhaseParameter Property](../Properties/PortPhaseParameter_Property.md)  
Match Correction |  [MatchState Property](../Properties/MatchState_Property.md)  
[MatchTestReceiver Property](../Properties/MatchTestReceiver_Property.md)  
[MatchRefReceiver Property](../Properties/MatchRefReceiver_Property.md)  
[MatchFrequencyRange Property](../Properties/MatchFrequencyRange_Property.md)  
Edit Parameters Dialog |   
---|---  
![](../../../assets/images/IQEditParamsDiag.gif) |  [DefineParameter Method](../Methods/DefineParameter_Method.md)  
[DeleteParameter Method](../Methods/DeleteParameter_Method.md)  
[ParameterList Property](../Properties/ParameterList_Property.md)  
[Save Method](../Methods/Save_diq_Method.md) (DIQ2)  
[Load Method](../Methods/Load_Method.md) (DIQ2)  
  
###  DIQ History

Interface |  Introduced with VNA Rev:  
---|---  
IDIQ |  10.25  
IDIQ2 |  10.40  
  
* * *

