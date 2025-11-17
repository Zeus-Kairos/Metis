##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# IsBalanced Property

* * *

#### Description

|  Returns whether or not the specified logical port number is balanced.  
---|---  
  
####  VB Syntax

|  value = chan.IsBalanced(logicalPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
value |  (boolean) - Returned value is either: False \- Logical port number is NOT balanced. True \- Logical port number IS balanced.  
logicalPort |  (Long Integer) Logical port number.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'In the following example, 6 logical ports are mapped to 8 physical VNA
ports.  
'Logical port 3 is queried and "True" is returned.  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
variable = balTopology.IsBalanced(3) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsBalanced(long logicalPort, VARIANT_BOOL *bBalanced);  
  
#### Interface

|  IBalancedTopology3

