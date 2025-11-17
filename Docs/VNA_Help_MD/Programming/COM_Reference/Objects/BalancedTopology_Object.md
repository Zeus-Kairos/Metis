# BalancedTopology Object

* * *

### Description

The [DUTTopology](../Properties/DUTTopology_Property.md) property sets and
returns the topology of a balanced DUT.

The following methods set the port mappings for the DUT.

The remaining properties return the port mappings for the DUT.

Use the [BalancedMeasurement object](BalancedMeasurement_Object.md) to set
the measurement type.

### Accessing the BalancedTopology object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
  
Dim balTopology as BalancedTopology  
Set balTopology = chan.BalancedTopology

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [About Balanced Measurements](../../../S1_Settings/Balanced_Measurements.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
[SetBPort](../Methods/SetBPort_Method.md) | IBalancedTopology3 | Sets the physical port mappings for the single Balanced port DUT topology.  
[SetCustomDUTTopology](../Methods/SetCustomDUTTopology_Method.md) | IBalancedTopology3 | Sets a custom topology for instruments with greater than 4 physical ports.  
[SetBBPorts](../Methods/SetBBPorts_Method.md) | IBalancedTopology | Sets the physical port mappings for the Balanced - Balanced DUT topology.  
[SetBSPorts](../Methods/SetBSPorts_Method.md) | IBalancedTopology2 | Sets the physical port mappings for the Balanced - Single-Ended DUT topology.  
[SetBSSPorts](../Methods/SetBSSPorts_Method.md) | IBalancedTopology4 | Sets the physical port mappings for the Balanced - Single-Ended - Single-Ended DUT topology.  
[SetSBPorts](../Methods/SetSBPorts_Method.md) | IBalancedTopology | Sets the physical port mappings for the Single-Ended - Balanced DUT topology.  
[SetSSBPorts](../Methods/SetSSBPorts_Method.md) | IBalancedTopology | Sets the physical port mappings for the Single-Ended - Single-Ended \- Balanced DUT topology.  
  
### Property

|

### Interface

|

### Description  
  
[B_BalPortNegative](../Properties/B_BalPortNegative_Property.md) | IBalancedTopology3 | Returns the negative balanced port number in the Balanced DUT topology.  
[B_BalPortPositive](../Properties/B_BalPortPositive_Method.md) | IBalancedTopology3 | Returns the positive balanced port number in the Balanced DUT topology.  
[BB_BalPort1Negative](../Properties/BB_BalPort1Negative_Property.md) | IBalancedTopology | Returns the VNA port number that is connected to the Negative side of the DUT's logical Port 1 .  
[BB_BalPort1Positive](../Properties/BB_BalPort1Positive_Property.md) | IBalancedTopology | Returns the first positive balanced port number in the Balanced - Balanced topology  
[BB_BalPort2Negative](../Properties/BB_BalPort2Negative_Property.md) | IBalancedTopology | Returns the second negative balanced port number in the Balanced - Balanced topology.  
[BB_BalPort2Positive](../Properties/BB_BalPort2Positive_Property.md) | IBalancedTopology | Returns the second positive balanced port number in the Balanced - Balanced topology.  
[BS_BalPortNegative](../Properties/BS_BalPortNegative_Property.md) | IBalancedTopology2 | Returns the negative balanced port number in the Balanced - Single-ended topology.  
[BS_BalPortPositive](../Properties/BS_BalPortPositive_Property.md) | IBalancedTopology2 | Returns the positive balanced port number in the Balanced - Single-ended topology.  
[BS_SEPort](../Properties/BS_SEPort_Property.md) | IBalancedTopology2 | Returns the single-ended port number in the Balanced - Single-ended topology.  
[BSS_BalPortNegative](../Properties/BSS_BalPortNegative_Property.md) | IBalancedTopology4 | Returns the negative balanced port number in the Balanced - Single-ended \- Single-ended topology.  
[BSS_BalPortPositive](../Properties/BSS_BalPortPositive_Property.md) | IBalancedTopology4 | Returns the positive balanced port number in the Balanced - Single-ended \- Single-ended topology.  
[BSS_SEPort1](../Properties/BSS_SEPort1_Property.md) | IBalancedTopology4 | Returns the Single-ended1 port number in the Balanced - Single-ended - Single-ended topology.  
[BSS_SEPort2](../Properties/BSS_SEPort2_Property.md) | IBalancedTopology4 | Returns the Single-ended2 port number in the Balanced - Single-ended - Single-ended topology.  
[CustomBalNegativePort](../Properties/CustomBalNegativePort_Property.md) | IBalancedTopology3 | Returns the negative physical port for the specified balanced port.  
[CustomBalPositivePort](../Properties/CustomBalPositivePort_Property.md) | IBalancedTopology3 | Returns the positive physical port for the specified balanced port.  
[CustomPhysicalPortsSequence](../Properties/CustomPhysicalPortsSequence_Property.md) | IBalancedTopology3 | Returns an array of physical port numbers corresponding to the CustomPortTypeSequence.  
[CustomPortTypeSequence](../Properties/CustomPortTypeSequence_Property.md) | IBalancedTopology3 | Returns a string containing characters "S" or "B" conveying the type of each logical port.  
[CustomSEPhysicalPort](../Properties/CustomSEPhysicalPort_Property.md) | IBalancedTopology3 | Returns the physical port for the specified single-ended port.  
[CustomTopologyPortCount](../Properties/CustomTopologyPortCount_Property.md) | IBalancedTopology3 | Returns the number of configured logical ports.  
[DUTTopology](../Properties/DUTTopology_Property.md) | IBalancedTopology | Sets and returns the device topology setting.  
[IsBalanced](../Properties/IsBalanced_Property.md) | IBalancedTopology3 | Returns true if the port is balanced.  
[IsSingleEnded](../Properties/IsSingleEnded_Property.md) | IBalancedTopology3 | Returns true if the port is single ended.  
[SB_BalPortNegative](../Properties/SB_BalPortNegative_Property.md) | IBalancedTopology | Returns the negative balanced port number in the Single-Ended - Balanced topology.  
[SB_BalPortPositive](../Properties/SB_BalPortPositive_Property.md) | IBalancedTopology | Returns the positive balanced port number in the Single-Ended - Balanced topology.  
[SB_SEPort](../Properties/SB_SEPort_Property.md) | IBalancedTopology | Returns the single ended port number in the Single-Ended - Balanced topology.  
[SSB_BalPortNegative](../Properties/SSB_BalPortNegative_Property.md) | IBalancedTopology | Returns the negative balanced port number in the Single-Ended - Single-Ended \- Balanced topology.  
[SSB_BalPortPositive](../Properties/SSB_BalPortPositive_Property.md) | IBalancedTopology | Returns the positive balanced port number in the Single-Ended - Single-Ended \- Balanced topology  
[SSB_SEPort1](../Properties/SSB_SEPort1_Property.md) | IBalancedTopology | Returns the first single ended port in the Single-Ended - Single-Ended \- Balanced topology.  
[SSB_SEPort2](../Properties/SSB_SEPort2_Property.md) | IBalancedTopology | Returns the second single ended port in the Single-Ended - Single-Ended \- Balanced topology.  
  
###  BalancedTopology History

Interface | Introduced with VNA Rev:  
---|---  
IBalancedTopology | 5.0  
IBalancedTopology2 | 9.70  
IBalancedTopology3 | 12.70  
IBalancedTopology4 | 14.20

