##### Write/Read

|

##### [About External DC Devices](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
# VoltageLimit Property

* * *

#### Description

|  Sets and returns the maximum output voltage value of the external DC
Source. This command supports Keysight B2900A and N6700 series devices only.  
---|---  
  
####  VB Syntax

|  extDC.VoltageLimit (devicename) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
devicename |  (String) Name of the device.  
value |  (Double) Voltage limit value.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  extDC.VoltageLimit("myDCDevice") = 4 'Write  
limit = extDC.VoltageLimit("myDCDevice") 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_VoltageLimit(BSTR devicename, double *vLimit)  
HRESULT put_VoltageLimit(BSTR devicename, double newLimit)  
  
#### Interface

|  IExternalDCDevice2

