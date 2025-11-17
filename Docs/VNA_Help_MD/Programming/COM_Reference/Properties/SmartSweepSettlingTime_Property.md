##### Write/Read

|

##### [About SMART
Sweep](../../../Applications/Gain_Compression_Application.htm#SMART)  
  
---|---  
  
## SmartSweepSettlingTime Property

* * *

#### Description

|  Set and read the amount of time SMART Sweep will dwell at the first point
where the input power changes by the Backoff or X level. [Learn
more.](../../../Applications/Gain_Compression_Application.htm#SmartBO)  
---|---  
  
####  VB Syntax

|  gca.SmartSweepSettlingTime = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (double) - Settling time in seconds. Choose any positive value.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  gca.SmartSweepSettlingTime = .01 'Write  
sTime = gca.SmartSweepSettlingTime 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SmartSweepSettlingTime(double* pVal) HRESULT
put_SmartSweepSettlingTime(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

