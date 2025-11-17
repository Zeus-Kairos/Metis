##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# MaxOutputState Property

* * *

#### Description

|  Sets and returns the "Define Max As" ON/OFF state for an external DC
Source.  
---|---  
  
####  VB Syntax

|  extDC.MaxOutputState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Boolean) "Define Max As" ON/OFF state. Choose from: True \- Turn "Define Max As" ON False \- Turn "Define Max As" OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  extDC.MaxOutputState = True 'Write  
value = extDC.MaxOutputState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaxOutputState(VARIANT_BOOL *value) HRESULT
put_MaxOutputState(VARIANT_BOOL value)  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

