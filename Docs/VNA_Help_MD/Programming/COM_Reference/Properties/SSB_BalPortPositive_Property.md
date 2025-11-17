##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## SSB_BalPortPositive Property

* * *

#### Description

|  With a Single-ended - Single-ended - Balanced topology, returns the VNA
port number that is connected to the Positive side of the DUT's Balanced Port.
Use [SetSSBPorts Method](../Methods/SetSSBPorts_Method.md) to set the port
mapping for a Single-Ended - Single-Ended - Balanced topology.  
---|---  
  
####  VB Syntax

|  var = balTopology.SSB_BalPortPositive  
  
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

|  variable = balTopology.SSB_BalPortPositive 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SSB_BalPortPositive(long *bVal)  
  
#### Interface

|  IBalancedTopology

