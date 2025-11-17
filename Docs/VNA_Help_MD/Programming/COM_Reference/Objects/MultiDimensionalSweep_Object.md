# MultiDimensionalSweep Object

* * *

### Description

Controls a multi-dimensional sweep in a spectrum analyzer channel. This is
also called a 3D sweep (power, phase, and frequency). Each sweep can be set to
a different power level. Within each sweep is a 2D sweep of phase and
frequency.

### Accessing the MultiDimensionalSweep object

set pna = CreateObject("AgilentPNA835x.Application","A-N5242A-10096")  
CreateSAMeasurement  
SetupMultiSweep Sub CreateSAMeasurement  
pna.Channels.RemoveChannelNumber(1)  
call
pna.[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)(1,
"SpectrumAnalyzer", "B")  
set chan = pna.ActiveChannel  
chan.Hold  
End Sub  
---  
  
### Method

|

### Interface

### See History

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[DCOrder](../Properties/DCOrder_Property.md) | IMultiDimensionalSweep | Set and read the order for the specified DC source in the multi-dimensional sweep.  
[DCState](../Properties/DCState_Property.md) | IMultiDimensionalSweep | Set and read the specified DC sources ON/OFF state in the multi-dimensional sweep.  
[DimensionCatalog](../Properties/DimensionCatalog_Property.md) | IMultiDimensionalSweep | Read the names of source domains in the multi-dimensional sweep whose state is ON and whose dimension order is the specified dimension order.  
[DimensionCount](../Properties/DimensionCount_Property.md) | IMultiDimensionalSweep | Read the highest dimension order in the multi-dimensional sweep.  
[DimensionPointCount](../Properties/DimensionPointCount_Property.md) | IMultiDimensionalSweep | Set and read the point count for the specified dimension order in the multi-dimensional sweep.  
[DimensionRepeatCount](../Properties/DimensionRepeatCount_Property.md) | IMultiDimensionalSweep | Set and read the repeat count for the specified dimension order in the multi-dimensional sweep.  
[SourcePortFrequencyOrder](../Properties/SourcePortFrequencyOrder_Property.md) | IMultiDimensionalSweep | Set and read the source frequency domains order in the multi-dimensional sweep.  
[SourcePortFrequencyState](../Properties/SourcePortFrequencyState_Property.md) | IMultiDimensionalSweep | Set and read the source frequency domains ON/OFF state in the multi-dimensional sweep.  
[SourcePortPhaseOrder](../Properties/SourcePortPhaseOrder_Property.md) | IMultiDimensionalSweep | Set and read the source phase domains order in the multi-dimensional sweep.  
[SourcePortPhaseState](../Properties/SourcePortPhaseState_Property.md) | IMultiDimensionalSweep | Set and read the source phase domains ON/OFF state in the multi-dimensional sweep.  
[SourcePortPowerOrder](../Properties/SourcePortPowerOrder_Property.md) | IMultiDimensionalSweep | Set and read the source power domains order in the multi-dimensional sweep.  
[SourcePortPowerState](../Properties/SourcePortPowerState_Property.md) | IMultiDimensionalSweep | Set and read the source power domains ON/OFF state in the multi-dimensional sweep.  
  
###  MultiDimensionalSweep History

Interface | Introduced with VNA Rev:  
---|---  
IMultiDimensionalSweep | 12.90

