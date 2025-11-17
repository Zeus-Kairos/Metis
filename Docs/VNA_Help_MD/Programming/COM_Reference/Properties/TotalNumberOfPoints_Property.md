##### Read-only

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## TotalNumberOfPoints Property

* * *

#### Description

|  Read the total number of points a complete GCA measurement will generate.

  * For 2D modes, this is Frequency * Power points
  * For SMART Sweep, this is Frequency points.

The total can NOT exceed the [VNA
maximum.](../../../S1_Settings/DPoints.htm#PointsDiag) See
[Frequency](NumberOfFrequencyPoints_Property.md) and
[Power](NumberOfPowerPoints_Property.md) points.  
---|---  
  
####  VB Syntax

|  value = gca.TotalNumberOfPoints  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (integer) Variable to store the returned total number of points  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
  
#### Return Type

|  Integer  
  
#### Default

|  5226 (201 * 26)  
  
#### Example

|  totPoints = gca.TotalNumberOfPoints 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TotalNumberOfPoints(int* pVal)  
  
#### Interface

|  IGainCompression  
  
* * *

