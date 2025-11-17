##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## MaximumIterationsPerPoint Property

* * *

#### Description

|  This command, along with [IterationsTolerance
Property](IterationsTolerance_Property.htm) deal with ADUSTMENTS made to the
source power. Sets the maximum number of readings to take at each data point
for iterating the source power. Power readings will continue to made, and
source power adjusted, until a reading is within the
[IterationsTolerance](IterationsTolerance_Property.md) value or this max
number of readings has been met. The last value to be read is the valid
reading for that data point. The following two commands allow for settling of
power READINGS. [ReadingsPerPoint Property](ReadingsPerPoint_Property.md)
[ReadingsTolerance Property](ReadingsTolerance_Property.md)  
---|---  
  
#### VB Syntax

|  pwrCal.MaximumIterationsPerPoint = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  (object) - A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (object)  
value |  (Long)  Maximum number of readings. Choose any number between 1 and 100.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  5  
  
#### Examples

|  Set powerCalibrator = pna.SourcePowerCalibrator  
powerCalibrator.MaximumIterationsPerPoint = 5 'Write  
MaxReads = powerCalibrator.MaximumIterationsPerPoint 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumIterationsPerPoint( long *pVal); HRESULT
put_MaximumIterationsPerPoint( long newVal);  
  
#### Interface

|  ISourcePowerCalibrator3  
  
* * *

