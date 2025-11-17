##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# B_BalPortNegative Property

* * *

#### Description

|  Returns the negative balanced port number in the balanced DUT topology. Use
[SetBPort Method](../Methods/SetBPort_Method.md) to set the single balanced
port DUT topology. ![](../../../assets/images/Balanced_SetBPort.GIF)  
---|---  
  
####  VB Syntax

|  var = balTopology.B_BalPortNegative  
  
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

|  variable = balTopology.B_BalPortNegative 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_B_BalPortNegative(long *NegPort)  
  
#### Interface

|  IBalancedTopology3

