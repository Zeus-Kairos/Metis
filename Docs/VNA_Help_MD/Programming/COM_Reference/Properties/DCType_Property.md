##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## DCType Property

* * *

#### Description

|  Sets and returns the DC Type for an external DC Device which can be
configured as either a DC Meter or a DC Source. This setting is used as the
units for display on the VNA X-axis.  
---|---  
  
####  VB Syntax

|  extDC.DCType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (String) DC type. Choose from: "dBm", "A", "V", "W", "K", "F", "C"  
  
#### Return Type

|  String  
  
#### Default

|  "V"  
  
#### Examples

|  extDC.DCType = "A" 'Write  
units = extDC.DCType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DCType (BSTR *pValue) HRESULT put_DCType (BSTR newVal)  
  
#### Interface

|  IExternalDCDevice  
  
* * *

* * *

