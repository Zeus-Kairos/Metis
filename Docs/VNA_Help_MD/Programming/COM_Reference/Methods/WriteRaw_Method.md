##### Write-only

|

##### [About the ExtTestSetIO connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## WriteRaw Method

* * *

#### Description

|  Writes a 16-bit value to the external test set connector lines AD0 - AD12,
RLW, LAS and LDS. The analyzer does NOT generate the appropriate timing
signals. The user has control of all 16 lines using this write method. Note:
When RLW (pin25) is set to 1 (high) it causes lines AD0 - AD12 to float. It
disables their output latches and sets the hardware for reading. LDS and LAS
are not affected by this behavior. Below is the format of data that is written
with WriteRaw: * This Output will float if RLW (bit-13) is set high  
---|---  
  
  
|  Pin |  Bit |  Signal name  
---|---|---|---  
|  22 |  0 |  AD0*  
|  23 |  1 |  AD1*  
|  11 |  2 |  AD2*  
|  10 |  3 |  AD3*  
|  9 |  4 |  AD4*  
|  21 |  5 |  AD5*  
|  20 |  6 |  AD6*  
|  19 |  7 |  AD7*  
|  6 |  8 |  AD8*  
|  5 |  9 |  AD9*  
|  4 |  10 |  AD10*  
|  17 |  11 |  AD11*  
|  3 |  12 |  AD12*  
|  25 |  13 |  RLW  
|  24 |  14 |  LDS  
|  8 |  15 |  LAS  
  

####  VB Syntax

|  ExtIO.WriteRaw value  
---|---  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ExtIO |  (object) - An External IO object  
value |  (variant) \- Data to be written  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ExtIO.WriteRaw 12  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT WriteRaw( VARIANT Output );  
  
#### Interface

|  IHWExternalTestSetIO

