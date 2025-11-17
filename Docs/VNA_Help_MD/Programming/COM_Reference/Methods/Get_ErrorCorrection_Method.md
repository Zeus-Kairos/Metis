##### Read-only

|

##### [About Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
---|---  
  
## GetErrorCorrection Method

* * *

#### Description

|  Reads the error correction state for the channel. Use [ErrorCorrection
Property](../Properties/ErrorCorrection_Channel_Property.htm) to set this
value. When this command returns true, some measurements on the channel MAY
not have error correction ON. This is because the Cal Set currently in place
may not contain the appropriate calibration data. To read the error correction
state for a measurement, use [Error Correction
Property](../Properties/Error_Correction_Property.htm).  
---|---  
  
####  VB Syntax

|  bool = chan.GetErrorCorrection  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
boolean |  (boolean) Variable to store the returned value. False \- Error correction has been set OFF True \- Error correction has been set ON  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  [About Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
#### Examples

|  value = chan.GetErrorCorrection  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetErrorCorrection (VARIANT_BOOL *bState)  
  
#### Interface

|  IChannel8  
  
* * *

