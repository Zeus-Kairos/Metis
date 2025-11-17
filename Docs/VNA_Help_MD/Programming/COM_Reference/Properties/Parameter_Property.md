##### Read-only

|

#####  
  
---|---  
  
## Parameter Property

* * *

#### Description

|  Returns the measurement Parameter. To change the parameter, use
meas.[ChangeParameter](../Methods/Change_Parameter_Method.md)  
---|---  
  
####  VB Syntax

|  measPar = meas.Parameter  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measPar |  (string) - Variable to store Parameter string  
meas |  A Measurement (object)  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable  
  
#### Examples

|  measPar = meas.Parameter 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Parameter(BSTR *pVal)  
  
#### Interface

|  IMeasurement

