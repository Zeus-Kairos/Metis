##### Write-only

|

##### [About Trace
Statistics](../../../S4_Collect/Math_Operations.htm#statistics)  
  
---|---  
  
## ShowStatistics Property

* * *

#### Description

|  Displays and hides the measurement (Trace) statistics (peak-to-peak, mean,
standard deviation) on the screen. To display measurement statistics for a
narrower band of the X-axis, use
[StatisticsRange.](Statistics_Range_Property.md) The analyzer will display
either measurement statistics or Filter Bandwidth statistics; not both.  
---|---  
  
####  VB Syntax

|  meas.ShowStatistics = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (boolean) - Boolean value: True \- Show statistics False \- Hide statistics  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.ShowStatistics = True  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ShowStatistics(VARIANT_BOOL bState)  
  
#### Interface

|  IMeasurement  
  
* * *

