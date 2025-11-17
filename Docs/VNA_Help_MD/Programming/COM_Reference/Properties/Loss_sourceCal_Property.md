##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## Loss (Power Segment) Property

* * *

#### Description

| Sets or returns the loss value associated with a PowerLossSegment.  
---|---  
  
#### VB Syntax

| lossSeg.Loss = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
lossSeg | A [PowerLossSegment](../Objects/PowerLossSegment_Object.md) (object) A [PowerLossSegmentPMAR](../Objects/PowerLossSegmentPMAR_Object.md) (object)  
value | (double)  Loss value in dB. Loss is entered as a POSITIVE number.  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| lossSeg.Loss = 0.5 'Write  
lossVal = lossSeg.Loss 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_Loss(Double newVal); HRESULT get_Loss(Double *pVal);  
  
#### Interface

| IPowerLossSegment  
  
* * *

