##### Write/Read

|

##### [About External DC Devices](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
# CurrentLimit Property

* * *

#### Description

|  Sets and returns the maximum output current value of the external DC
Source. This command supports Keysight B2900A and N6700 series devices only.  
---|---  
  
####  VB Syntax

|  extDC.CurrentLimit (devicename) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
devicename |  (String) Name of the device.  
value |  (Double) Current limit value.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  extDC.CurrentLimit("myDCDevice") = 4 'Write  
Limit = extDC.CurrentLimit("myDCDevice") 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CurrentLimit(BSTR devicename, double *cLimit)  
HRESULT put_CurrentLimit(BSTR devicename, double newLimit)  
  
#### Interface

|  IExternalDCDevice2

