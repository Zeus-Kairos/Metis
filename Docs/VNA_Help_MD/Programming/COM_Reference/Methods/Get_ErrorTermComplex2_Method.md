##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTermComplex Method Superseded

* * *

#### Description

|  This command is [replaced](../../Replacement_Commands.md) with [Get
ErrorTermComplexByString](Get_ErrorTermComplexByString_Method.htm) Returns
error term data from the Cal Set. The data is in complex pairs. Learn more
about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data Note: This method exists on a non-default interface. If you cannot
access this method, use the [GetErrorTerm](Get_ErrorTerm2_Method.md) Method
on ICal Set.  
---|---  
  
####  VB Syntax

|  iCalData2.GetErrorTermComplex setNumber, term, rcv, src, numPts, real(),
imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
iCalData2 |  An [ICalData2](../Objects/CalSet_Object.md#ICalData2) pointer to the Cal Set object  
setNumber |  (Long) There can be more than one set of error terms in a Cal Set.

  * setNumber 0 contains the original set of error terms for a Cal Set.
  * setNumbers > 0 contain Interpolated error terms. Interpolated error terms are generated when interpolation is required and destroyed when no longer used. [Learn about Interpolation](../../../S3_Cals/Quest_Cal.md).
  * To determine the setNumber in use by a channel, see [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md)

  
term |  (enum NAErrorTerm2) \- The error term to be retrieved. Choose from: 0 - naET_Directivity 1 - naET_SourceMatch 2 - naET_ReflectionTracking 3 - naET_TransmissionTracking 4 - naET_LoadMatch 5 - naET_Isolation  
rcv |  (Long) \- Receiver Port  
src |  (Long) \- Source Port  
numPts |  (Long) An In/Out parameter. On the way in, you specify the max number of values being requested. On the way out, the VNA returns number of values actually returned.  
real() |  (single) \- array to accept the real part of the error-term. One-dimensional for the number of data points.  
imag() |  (single) \- array to accept the imaginary part of the error-term. One-dimensional for the number of data points.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  dim numpts as long  
numpts = ActiveChannel.NumberOfPoints  
ReDim r(numpts) ' real part  
ReDim i(numpts) ' imaginary part  
Dim CalSet as CalSet  
set CalSet = pna.GetCalManager.GetCal SetByGUID( txtGUID )  
Dim eData As ICalData2  
Set eData = CalSet  
eData.getErrorTermComplex 0, naET_LoadMatch, 1, 2, numpts, r(0),i (0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT getErrorTermComplex(long setID, tagNAErrorTerm2 ETerm, long
ReceivePort, long SourcePort, long* pNumValues, float* pReal, float* pImag)  
  
#### Interface

|  ICalData2

