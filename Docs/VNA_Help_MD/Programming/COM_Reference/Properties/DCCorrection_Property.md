##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## DCCorrection Property

* * *

#### Description

|  Sets and returns the correction ON/OFF state for a DC Meter and a DC
Source.  
---|---  
  
####  VB Syntax

|  extDC.DCCorrection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Boolean) Correction ON/OFF state. Choose from: True \- Turn Correction ON False \- Turn Correction OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  extDC.DCCorrection = True 'Write  
bool = extDC.DCCorrection 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DCCorrection (BOOL *pValue) HRESULT put_DCCorrection (BOOL
newVal)  
  
#### Interface

|  IExternalDCDevice  
  
* * *

* * *

