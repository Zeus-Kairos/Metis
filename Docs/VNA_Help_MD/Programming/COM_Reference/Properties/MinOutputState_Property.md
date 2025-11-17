##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# MinOutputState Property

* * *

#### Description

|  Sets and returns the "Define Min As" ON/OFF state for an external DC
Source.  
---|---  
  
####  VB Syntax

|  extDC.MinOutputState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Boolean) "Define Min As" ON/OFF state. Choose from: True \- Turn "Define Min As" ON False \- Turn "Define Min As" OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  extDC.MinOutputState = True 'Write  
value = extDC.MinOutputState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MinOutputState(VARIANT_BOOL *value) HRESULT
put_MinOutputState(VARIANT_BOOL value)  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

