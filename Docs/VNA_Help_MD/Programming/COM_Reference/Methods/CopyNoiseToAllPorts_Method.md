##### Write-only

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# CopyNoiseToAllPorts Method

* * *

#### Description

|  Copies the characterized noise data associated with the specified port, to
all the other ports.  
---|---  
  
#### VB Syntax

|  oPorts.CopyNoiseToAllPorts (value)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
oPorts |  A [Ports](../Objects/Ports_Collection.md) Collection  
value |  (Long) Port number from which noise data is to be copied.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  oPorts.CopyNoiseToAllPorts(2) [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CopyNoiseToAllPorts([in] long fromPortNumber);  
  
#### Interface

|  IUncertaintyPorts  
  
* * *

