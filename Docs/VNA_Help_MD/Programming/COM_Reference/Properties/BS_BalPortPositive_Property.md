##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## BS_BalPortPositive Property

* * *

#### Description

|  With a Balanced - Single-ended topology, returns the VNA port number that
is connected to the Positive side of the DUT's balanced port. Use [SetSBPorts
Method](../Methods/SetSBPorts_Method.htm) to set the port mapping for a
Balanced - Single-ended topology.  
---|---  
  
####  VB Syntax

|  var = balTopology.BS_BalPortPositive  
  
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

|  variable = balTop.BS_BalPortPositive 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BS_BalPortPositive(long *bVal)  
  
#### Interface

|  IBalancedTopology2  
  
* * *

