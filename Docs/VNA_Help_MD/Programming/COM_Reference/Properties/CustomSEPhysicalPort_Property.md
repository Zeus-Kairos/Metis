##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# CustomSEPhysicalPort Property

* * *

#### Description

|  Returns the VNA physical port number that is mapped to the specified
single-ended logical port.  
---|---  
  
####  VB Syntax

|  var = balTopology.CustomSEPhysicalPort(logicalSingleEndedPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
var |  (Long Integer) Variable to store the returned value.  
logicalSingleEndedPort |  (Long Integer) Logical single ended port number.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'In the following example, 6 logical ports are mapped to 8 physical VNA
ports.  
'Logical ports 1, 2, 4 and 5 are single-ended.  
'Logical port 5 is queried returning physical port 6.  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
variable = balTopology.CustomSEPhysicalPort(5) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CustomSEPhysicalPort(long *physicalPort)  
  
#### Interface

|  IBalancedTopology3

