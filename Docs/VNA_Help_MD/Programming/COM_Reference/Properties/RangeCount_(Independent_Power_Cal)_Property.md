##### Read-only

|

##### [About Independent Power
Calibration](../../../S3_Cals/Calibrate_All_Channels.htm#Setting_Up_an_Independent_Power_Calibration)  
  
---|---  
  
# RangeCount (Independent Power Cal Port) Property

* * *

#### Description

| Queries how many ranges are included in the calibration for source port <n>.  
---|---  
  
####  VB Syntax

| value = IndependentPwrrCalPort.RangeCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value | (Long) \- Variable to store the returned range count.  
IndependentPwrrCalPort | A [IndependentPowerCalibrationPort](../Objects/IndependentPowerCalibrationPort_Object.md) (object)  
  
#### Return Type

| Long  
  
#### Default

| Not Applicable  
  
#### Example

| value = CalibrateAllChannels.IndependentPowerCalibrationPort.RangeCount
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT RangeCount(Int* ranges);  
  
#### Interface

| IIndependentPowerCalibrationPort

