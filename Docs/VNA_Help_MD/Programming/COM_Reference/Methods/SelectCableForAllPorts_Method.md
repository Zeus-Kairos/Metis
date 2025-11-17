##### Write-only

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# SelectCableForAllPorts Method

* * *

#### Description

|  Selects the name of the cable to be associated with all the ports currently
enabled on the VNA  
---|---  
  
#### VB Syntax

|  oPorts.SelectCableForAllPorts (value)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
oPorts |  A [Ports](../Objects/Ports_Collection.md) Collection  
value |  (String) Name of the cable.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  oPorts.SelectCableForAllPorts("myCable") [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SelectCableForAllPorts([in] BSTR cableName);  
  
#### Interface

|  IUncertaintyPorts  
  
* * *

