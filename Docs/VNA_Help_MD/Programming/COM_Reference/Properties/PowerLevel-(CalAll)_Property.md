##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## PowerLevel (Cal All) Property

* * *

#### Description

| Sets and returns the power level at which a Cal All calibration is to be
performed.  
---|---  
  
####  VB Syntax

| calAll.PowerLevel (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll | A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
port | (Long) Source port number.  
value | (Double) Power level at which the calibration is to be performed.  
  
#### Return Type

| Double  
  
#### Default

|  
  
#### Examples

| calAll.PowerLevel = 0 'Power Level of cal value = calAll.PowerLevel 'returns
the power level of the cal  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PowerLevel (long port, double val); HRESULT put_PowerLevel long
port, double* newVal);  
  
#### Interface

| ICalibrateAllChannels  
  
* * *

* * *

