##### Write-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# SetCustomDUTTopology Method

* * *

#### Description

|  Maps the physical VNA ports to a device of balanced and single-ended
logical ports for multi-port systems with greater than 4 ports. The device
type is set using the following commands:

  * [SetBPort](SetBPort_Method.md) \- single balanced port DUT topology.
  * [SetBBPorts](SetBBPorts_Method.md) \- balanced - balanced DUT topology.
  * [SetBSPorts](SetBSPorts_Method.md) \- balanced - single-ended DUT topology.
  * [SetSBPorts](SetSBPorts_Method.md) \- single-ended - balanced DUT topology.
  * [SetSSBPorts](SetSSBPorts_Method.md) \- single-ended - single-ended - balanced DUT topology.

The [Parameter](../Properties/Parameter_Property.md) command returns the list
of parameters available for the currently selected topology.  
---|---  
  
####  VB Syntax

|  balTopology.SetCustomDUTTopology (portTypeSequence, physicalPortsSequence)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
portTypeSequence |  (String) Device type for the balanced measurement. B means the Balanced port; S means the Single-ended port. Choose from: B  1 port balanced device (2 ports) BB  Balanced - Balanced device (4 ports) BS  Balanced - Single-ended device (3 ports) SB  Single-ended - Balanced device (3 ports) SSB  Single-ended - Single-ended - Balanced device (4 ports)  
  
#### physicalPortsSequence

|  (Variant) Physical port numbers mapped to the logical ports, separated by
,. B (Balanced) requires 2 physical port numbers: <nPos>, <nNeg>. S
(Single-ended) requires 1 physical port number.  
  
#### Return Type

|  Not applicable - To read port mappings, use the
[BalancedTopology](../Objects/BalancedTopology_Object.md) properties.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'The following example sets up 8 physical ports into 6 logical ports:  
'Logical port 1 is a single ended port mapped to physical port 1  
'Logical port 2 is a single ended port mapped to physical port 2  
'Logical port 3 is a balanced port mapped to physical ports 3 and 4  
'Logical port 4 is a single ended port mapped to physical port 5  
'Logical port 5 is a single ended port mapped to physical port 6  
'Logical port 6 is a balanced port mapped to physical ports 7 and 8  
  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetCustomDUTTopology(BSTR portTypeSequence, VARIANT
physicalPortsSequence)  
  
#### Interface

|  IBalancedTopology3

