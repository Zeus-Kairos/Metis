##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTermComplexByString Method

* * *

#### Description

|  Returns error term data from the Cal Set by specifying the string name.
Learn more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data Note: This method exists on a non-default interface. If you cannot
access this method, use
[GetErrorTermByString](Get_ErrorTermByString_Method.md)  
---|---  
  
####  VB Syntax

|  ICalData3.GetErrorTermComplexByString setNumber, errorTerm, numPoints,
real(0), imag(0)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ICalData3 |  An ICalData3 pointer to a [CalSet](../Objects/CalSet_Object.md) (Object)  
setNumber |  (Long) There can be more than one set of error terms in a Cal Set.

  * setNumber 0 contains the original set of error terms for a Cal Set.
  * setNumbers > 0 contain Interpolated error terms. Interpolated error terms are generated when interpolation is required and destroyed when no longer used. [Learn about Interpolation](../../../S3_Cals/Quest_Cal.md).
  * To determine the setNumber in use by a channel, see [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md)

  
errorTerm |  (String) The string name of error term in the Cal Set. An example string for port 3 directivity in a full 2 port cal might be "Directivity(3,3)". For a list error term string names, use [Get ErrorTermList2](Get_ErrorTermList2_Method.md)  
numPoints |  (Long) An In/Out parameter. On the way in, you specify the max number of values being requested. On the way out, the VNA returns number of values actually returned.  
real |  (Single) The real component of the complex data.  
imag |  (Single) The imaginary component of the complex data.   
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetErrorTermComplexByString(long etermSetID, BSTR bufferName, long*
lnumPoints, single* real, single* imag);  
  
#### Interface

|  ICalData3

