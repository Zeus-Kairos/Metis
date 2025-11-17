##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## IFBW Property

* * *

#### Description

|  Sets and returns the IFBW for a Cal All calibration. [Learn more about this
setting](../../../S3_Cals/Calibrate_All_Channels.htm#ifbw).  
---|---  
  
####  VB Syntax

|  calAll.IFBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll |  A [CalibrateAllIFBW](../Objects/CalibrateAllChannels_Object.md) (object)  
value |  (Double) IFBW in Hz.  
  
#### Return Type

|  Variant  
  
#### Default

|  1 kHz  
  
#### Examples

|  calAll.IFBW = 10e3 'sets IFBW to 10 kHz ifbw = calAll.IFBW 'returns the
ifbw setting  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IFBW (Double *Val) HRESULT put_IFBW (Double newVal)  
  
#### Interface

|  ICalibrateAllChannels  
  
* * *

* * *

