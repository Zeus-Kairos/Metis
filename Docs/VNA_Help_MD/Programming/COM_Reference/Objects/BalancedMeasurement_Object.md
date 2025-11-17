# BalancedMeasurement Object

* * *

### Description

These properties set the measurement type that is used with balanced
topologies.

Use the [BalancedTopology Object](BalancedTopology_Object.md) to set the
topology and port mappings for the DUT,

### Accessing the BalancedMeasurement object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim balMeas As BalancedMeasurement  
Set balMeas = app.ActiveMeasurement.BalancedMeasurement

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [About Balanced Measurements](../../../S1_Settings/Balanced_Measurements.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

(Bold Methods or Properties provide access to a child object)

### Method

|

###

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[BalancedMode](../Properties/BalancedMode_Property.md) | IBalancedMeasurement | Sets and returns whether the balanced transform is ON or OFF.  
[BalancedStimulus](BalancedStimulus_Object.md) | IBalancedMeasurement2 | Sets and returns the stimulus properties of a balanced DUT.  
[BalancedTopology](BalancedTopology_Object.md) | IBalancedMeasurement | Sets and returns the topology of a balanced DUT.  
[BalSMeasurement](../Properties/BalSMeasurement_Property.md) | IBalancedMeasurement3 | Sets and returns the measurement for the Balanced - Single-ended topology.  
[BBalMeasurement](../Properties/BBalMeasurement_Property.md) | IBalancedMeasurement | Sets and returns the measurement for the Balanced - Balanced topology.  
[BSSMeasurement](../Properties/BSSMeasurement_Property.md) | IBalancedMeasurement4 | Sets and returns the measurement for the Balanced - Single-Ended - Single-Ended topology.  
[SBalMeasurement](../Properties/SBalMeasurement_Property.md) | IBalancedMeasurement | Sets and returns the measurement for the Single-Ended - Balanced topology.  
[SSBMeasurement](../Properties/SSBMeasurement_Property.md) | IBalancedMeasurement | Sets and returns the measurement for the Single-Ended - Single-Ended \- Balanced topology  
  
###  IBalancedMeasurement History

Interface | Introduced with VNA Rev:  
---|---  
IBalancedMeasurement | 5.0  
IBalancedMeasurement2 | 8.2  
IBalancedMeasurement3 | 9.70  
IBalancedMeasurement4 | 14.20

