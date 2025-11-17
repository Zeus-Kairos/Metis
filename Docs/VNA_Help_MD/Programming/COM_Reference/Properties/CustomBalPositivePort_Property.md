##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# CustomBalPositivePort Property

* * *

#### Description

|  Returns the VNA physical port number that is connected to the Positive side
of the specified logical balanced port of the DUT.  
---|---  
  
####  VB Syntax

|  var = balTopology.CustomBalPositivePort(logicalBalancedPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
var |  (Long Integer) Variable to store the returned value.  
logicalBalancedPort |  (Long Integer) Logical balanced port number.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'In the following example, 6 logical ports are mapped to 8 physical VNA
ports.  
'Logical ports 3 and 6 are balanced.  
'Logical port 3 is queried returning physical port 3.  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
variable = balTopology.CustomBalPositivePort(3) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CustomBalPositivePort(long *logicalBalancedPort)  
  
#### Interface

|  IBalancedTopology3

