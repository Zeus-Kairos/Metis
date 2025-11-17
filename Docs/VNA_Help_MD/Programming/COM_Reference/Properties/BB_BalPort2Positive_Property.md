##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## BB_BalPort2Positive Property

* * *

#### Description

|  With a Balanced - Balanced topology, returns the VNA port number that is
connected to the Positive side of the DUT's logical Port 2. Use [SetBBPorts
Method](../Methods/SetBBPorts_Method.htm) to set the port mapping for a
Balanced - Balanced topology.  
---|---  
  
####  VB Syntax

|  var = balTopology.BB_BalPort2Positive  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
var |  (Long Integer) Variable to store the returned value.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  variable = balTop.BB_BalPort2Positive 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BB_BalPort2Positive(long *bVal)  
  
#### Interface

|  IBalancedTopology

