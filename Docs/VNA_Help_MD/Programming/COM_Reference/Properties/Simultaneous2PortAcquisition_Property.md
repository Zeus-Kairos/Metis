##### Read / Write

|

##### [About Performing a Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## Simultaneous2PortAcquisition Property

* * *

#### Description

|  Specifies whether a 2-port calibration will be done with a single set of
standards (one port at a time) or with two sets of standards (simultaneously).
The [AcquireCalStandard2](../Methods/AcquireCalStandard2_Method.md) command
uses the same standard index for each calibration class. To specify the
calibration standard gender for each port, you must first ensure that the
order of calibration class accurately reflects the configuration of your DUT.
For example, for a DUT with a male connector on port 1 and a female connector
on port 2, order the devices within the S11 classes (A, B, and C) such that
the MALE standards are first in the list. Then order the S22 classes
specifying the FEMALE standards as the first in the list.  
---|---  
  
####  VB Syntax

|  cal.Simultaneous2PortAcquisition = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
state |  (boolean) - Choose from: True \- measures 2 ports simultaneously False \- measures 1 port at a time  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  cal.Simultaneous2PortAcquisition = True  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Simultaneous2PortAcquisition( VARIANT_BOOL bTwoSetsOfStandards)
HRESULT Simultaneous2PortAcquisition( VARIANT_BOOL *bTwoSetsOfStandards)  
  
#### Interface

|  ICalibrator  
  
* * *

