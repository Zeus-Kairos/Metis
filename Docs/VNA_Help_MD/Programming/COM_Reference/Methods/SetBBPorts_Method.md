##### Write-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## SetBBPorts Method

* * *

#### Description

|  For a Balanced - Balanced device type, maps the VNA ports to the DUT ports.
Set the Balanced device type using the [DUTTopology
Property](../Properties/DUTTopology_Property.htm)  
---|---  
  
####  VB Syntax

|  balTopology.SetBBPorts p1Pos, p1Neg, p2Pos, p2Neg  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
p1Pos, p1Neg, p2Pos, p2Neg |  (Long Integer) VNA port number that connects to each of the following DUT ports: ![](../../../assets/images/Programming/BBalTopMap.gif)  
  
#### Return Type

|  Not applicable - To read port mappings, use the
[BalancedTopology](../Objects/BalancedTopology_Object.md) properties.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  balTop.SetBBPorts 1,2,3,4  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetBBPorts (long p1Pos, long p1Neg, long p2Pos, long p2Neg)  
  
#### Interface

|  IBalancedTopology

