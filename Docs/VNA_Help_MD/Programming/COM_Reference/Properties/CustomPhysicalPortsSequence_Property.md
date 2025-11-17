##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# CustomPhysicalPortsSequence Property

* * *

#### Description

|  Returns an array of physical port numbers corresponding to the logical
ports. To view the type of each logical port, use the
[CustomPortTypeSequence](CustomPortTypeSequence_Property.md) command.  
---|---  
  
####  VB Syntax

|  var = balTopology.CustomPhysicalPortsSequence  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
var |  (Variant) Variable to store the returned value.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'In the following example, 6 logical ports are mapped to 8 physical VNA
ports.  
'This query returns the portlist, which is the sequence of the 8 physical VNA
ports.  
Int portlist[] = {1,2,3,4,5,6,7,8}  
balTopology.SetCustomDuTTopology ("SSBSSB", portlist)  
variable = balTopology.CustomPhysicalPortsSequence 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CustomPhysicalPortsSequence(VARIANT *physicalPorts)  
  
#### Interface

|  IBalancedTopology3

