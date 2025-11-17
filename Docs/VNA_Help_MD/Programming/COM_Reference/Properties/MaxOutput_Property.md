##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# MaxOutput Property

* * *

#### Description

|  Sets and returns the "Define Max As" value for an external DC Source.  
---|---  
  
####  VB Syntax

|  extDC.MaxOutput = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Double) Maximum value for the external DC Source.  
  
#### Return Type

|  Double  
  
#### Default

|  10 V  
  
#### Examples

|  extDC.MaxOutput = 10 'Write value = extDC.MaxOutput 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaxOutput( double* value); HRESULT put_MaxOutput( double
value);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

