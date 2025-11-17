##### Write-only

|

##### [About Performing a Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## SetCalInfo Method

* * *

#### Description

|  Specifies the type of Unguided calibration. This method should be the first
method called on the calibrator object. It prepares the internal state for the
rest of the calibration. Note: You can NOT perform a 3 or 4-port cal using
SetCalInfo even though there is enumCalTypes. You must use the
[GuidedCalibration](../Objects/GuidedCalibration_Object.md) object. Learn
more about [reading and writing Cal data using
COM](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
The analyzer can measure both ports simultaneously, assuming you have two of
each standard type. For a 2-port cal, See
[cal.Simultaneous2PortAcquisition](../Properties/Simultaneous2PortAcquisition_Property.md)  
---|---  
  
####  VB Syntax

|  cal.SetCalInfo (type,rcvPort,srcPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
type |  (enum NACalType) \- Calibration type. Choose from: |  0 \- naCalType_Response_Open  
---  
1 \- naCalType_Response_Short  
2 \- naCalType_Response_Thru  
3 \- naCalType_Response_Thru_And_Isol  
4 \- naCalType_OnePort  
5 \- naCalType_TwoPort_SOLT  
6 \- naCalType_TwoPort_TRL  
7 \- naCalType_None  
8 \- naCalType_ThreePort_SOLT  
9 \- Custom  
10 \- naCalType_FourPort_SOLT  
  
Note: For 1-port cals, the source port = receiver port. For 2, 3,4-port SOLT
and TRL, it doesn't matter which port is specified as source and receiver  
  
rcvPort |  (long integer) - Receiver Port  
srcPort |  (long integer) - Source Port  
  
#### Return Type

|  NACalType  
  
#### Default

|  7- naCalType_None  
  
#### Examples

|  cal.setCalInfo(naCalType_Response_Open,1,1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetCalInfo(tagNACalType calType,long portA, long portB)  
  
#### Interface

|  ICalibrator

