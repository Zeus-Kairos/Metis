##### Write-only

|

##### [About Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
---|---  
  
## ErrorCorrection (Channel) Property

* * *

#### Description

|  Attempts to set error correction ON or OFF for all of the measurements on
the channel. This setting may not be successful for some measurements because
the Cal Set currently in place may not contain the appropriate calibration
data. To read the error correction state for a measurement, use [Error
Correction Property](Error_Correction_Property.htm).  
---|---  
  
####  VB Syntax

|  chan.ErrorCorrection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
value |  (boolean) False \- Turns error correction OFF True \- Turns error correction ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  [About Error
Correction](../../../S3_Cals/Error_Correction_and_Interpolation.htm)  
  
#### Examples

|  chan.ErrorCorrection = True  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ErrorCorrection (VARIANT_BOOL bState)  
  
#### Interface

|  IChannel7

