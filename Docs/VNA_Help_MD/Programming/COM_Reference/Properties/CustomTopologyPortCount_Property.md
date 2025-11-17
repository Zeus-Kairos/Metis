##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# CustomTopologyPortCount Property

* * *

#### Description

|  Returns the number of configured logical ports.  
---|---  
  
####  VB Syntax

|  var = balTopology.CustomTopologyPortCount  
  
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

|  'In the following example, 6 logical ports are mapped to 8 physical VNA
ports.  
'This query returns 6 (SSBSSB).  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
variable = balTopology.CustomTopologyPortCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CustomTopologyPortCount(long *logicalPortCount)  
  
#### Interface

|  IBalancedTopology3

