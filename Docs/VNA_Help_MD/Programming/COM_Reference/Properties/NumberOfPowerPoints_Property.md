##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## NumberOfPowerPoints Property

* * *

#### Description

|  Set and read the number of data points in each power sweep. Applies ONLY to
2D [acquisition modes](AcquisitionMode_Property.md).  
---|---  
  
####  VB Syntax

|  gca.NumberOfPowerPoints = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (integer) - Power points. Do not exceed the max number of points. For 2D sweeps, total = frequency x power. Max = 20,001 For Smart sweep, total = frequency. Max = 10,000.  
  
#### Return Type

|  Integer  
  
#### Default

|  26  
  
#### Examples

|  gca.NumberOfPowerPoints = 31 'Write  
pwrPts = gca.NumberOfPowerPoints 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NumberOfPowerPoints(int* pVal) HRESULT
put_NumberOfPowerPoints(int newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

