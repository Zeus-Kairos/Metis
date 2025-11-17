##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## IterationsTolerance Property

* * *

#### Description

|  This command, along with [MaximumIterationsPerPoint
Property](MaximumIterationsPerPoint_Property.htm) deal with ADUSTMENTS made to
the source power. Sets the maximum desired deviation from the sum of the [test
port power](Test_Port_Power_Property.htm) and the
[offset](SourcePowerCalPowerOffset_Property.md) value. Power readings will
continue to be made, and source power adjusted, until a reading is within this
tolerance value or the [max number of
readings](MaximumIterationsPerPoint_Property.htm) has been met. The last value
to be read is the valid reading for that data point. The following two
commands allow for settling of power READINGS. [ReadingsPerPoint
Property](ReadingsPerPoint_Property.htm) [ReadingsTolerance
Property](ReadingsTolerance_Property.htm)  
---|---  
  
#### VB Syntax

|  pwrCal.IterationsTolerance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  (object) - A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (object)  
value |  (Double)  Tolerance value in dBm. Choose any number between 0 and 5  
  
#### Return Type

|  Double  
  
#### Default

|  .05 dB  
  
#### Examples

|  Set powerCalibrator = pna.SourcePowerCalibrator  
powerCalibrator.IterationsTolerance = .1 'Write  
ReadTol = powerCalibrator.IterationsTolerance 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IterationsTolerance( double *pVal); HRESULT
put_IterationsTolerance( double newVal);  
  
#### Interface

|  ISourcePowerCalibrator3  
  
* * *

