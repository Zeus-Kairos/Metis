# ActiveParametersApp Object

* * *

### Description

Controls the Active (Hot) Parameter Application settings.

### Accessing the ActiveParametersApp object

Dim app Set app = CreateObject("AgilentPNA835x.Application") app.Preset
app.[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)
2, "Active Parameters", "IPwr" Set ActParam =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)  
---  
  
### See Also:

  * [About Active Match Application](../../../Applications/Active_Match.md)

  * [PNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The PNA Object Model](The_Analyzer_Object_Model.md)

  * [Programming Example](../../COM_Example_Programs/Active_\(Hot\)_Parameters.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[AbsoluteExtractionToneLevel](../Properties/AbsoluteExtractionToneLevel_Property.md) | IActiveChannelSettings | Set and read the absolute tone power level.  
[DisplayDomain](../Properties/DisplayDomain_Property.md) | IActiveChannelSettings | Set and read the X-axis domain type.  
[DisplayInputPower](../Properties/DisplayInputPower_Property.md) | IActiveChannelSettings | Set and read a fixed input power.  
[DisplayInterpolationState](../Properties/DisplayInterpolationState_Property.md) | IActiveChannelSettings | Set and read whether or not interpolation is on for display.  
[ExtractionToneMode](../Properties/ExtractionToneMode_Property.md) | IActiveChannelSettings | Set and read the tuning tone mode.  
[PhaseSweepPoints](../Properties/PhaseSweepPoints_Property.md) | IActiveChannelSettings | Set and read the number of phase points.  
[PowerStepsIn3DSweep](../Properties/PowerStepsIn3DSweep_Property.md) | IActiveChannelSettings | Set and read the number of power steps for a 3D sweep.  
[RelativeExtractionToneLevel](../Properties/RelativeExtractionToneLevel_Property.md) | IActiveChannelSettings | Set and read the relative tone power level.  
[StartPowerIn3DSweep](../Properties/StartPowerIn3DSweep_Property.md) | IActiveChannelSettings | Set and read the start power level for a 3D sweep.  
[StopPowerIn3DSweep](../Properties/StopPowerIn3DSweep_Property.md) | IActiveChannelSettings | Set and read the stop power level for a 3D sweep.  
[SweepType](../Properties/SweepType_Property.md) | IActiveChannelSettings | Set and read the sweep type.  
  
### IActiveChannelSettings History

Interface | Introduced with PNA Rev:  
---|---  
IActiveChannelSettings | 12.90

