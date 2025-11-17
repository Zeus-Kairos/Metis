##### Write/Read

|

##### [About External DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# MinOutput Property

* * *

#### Description

|  Sets and returns the "Define Min As" value for an external DC Source.  
---|---  
  
####  VB Syntax

|  extDC.MinOutput = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  A [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Double) Minimum value for the external DC Source.  
  
#### Return Type

|  Double  
  
#### Default

|  -10 V  
  
#### Examples

|  extDC.MinOutput = -10 'Write value = extDC.MinOutput 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MinOutput( double* value); HRESULT put_MinOutput( double
value);  
  
#### Interface

|  IExternalDCDevice3  
  
* * *

