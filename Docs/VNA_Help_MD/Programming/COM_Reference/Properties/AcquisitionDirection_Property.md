##### Read / Write

|

##### [About Performing a Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## AcquisitionDirection Property

* * *

#### Description

|  Specifies the direction of each part of a 2-port calibration.  
---|---  
  
####  VB Syntax

|  cal.AcquisitionDirection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
value |  (enum NADirection) - Choose from: 0 - naForward \- measures the forward direction  
1 - naReverse \- measures the reverse direction  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naForward  
  
#### Examples

|  cal.AcquisitionDirection = naForward  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AcquisitionDirection(tagNADirection dir);  
  
#### Interface

|  ICalibrator

