##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## SSB_SEPort1 Property

* * *

#### Description

|  With a Single-ended - Single-ended - Balanced topology, returns the VNA
port number that is connected to the DUT's Logical Port 1. Use [SetSSBPorts
Method](../Methods/SetSSBPorts_Method.htm) to set the port mapping for a
Single-Ended - Single-Ended - Balanced topology.  
---|---  
  
####  VB Syntax

|  var = balTopology.SSB_SEPort1  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
var |  (Long Integer) Variable to store the returned value.  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  variable = balTopology.SSB_SEPort1 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SSB_SEPort1(long *bVal)  
  
#### Interface

|  IBalancedTopology

