##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# CustomPortTypeSequence Property

* * *

#### Description

|  Returns a string containing the characters "S" (single-ended) or "B"
(balanced) corresponding to the logical port types. To view the physical
ports, use the
[CustomPhysicalPortsSequence](CustomPhysicalPortsSequence_Property.md)
command.  
---|---  
  
####  VB Syntax

|  var = balTopology.CustomPortTypeSequence  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
var |  (String) Variable to store the returned value.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'In the following example, 6 logical ports are mapped to 8 physical VNA
ports.  
'This query returns SSBSSB, which is the sequence of the 6 logical ports.  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
variable = balTopology.CustomPortTypeSequence 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CustomPortTypeSequence(BSTR *portType)  
  
#### Interface

|  IBalancedTopology3

