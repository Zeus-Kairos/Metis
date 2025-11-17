##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutErrorTermComplex Method Superseded

* * *

#### Description

|  This command is [replaced](../../Replacement_Commands.md) with
[PutErrorTermComplexByString](Put_ErrorTermComplexByString_Method.md) Puts
error term data into the Cal Set. Learn more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  data.putErrorTermComplex term, rcv, src, numPts, real(), imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  An [ICalData2](../Objects/CalSet_Object.md#ICalData2) pointer to a Cal Set object  
term |  (enum NAErrorTerm2) - The error term to be written. Choose from: 0 - naET_Directivity 1 - naET_SourceMatch 2 - naET_ReflectionTracking 3 - naET_TransmissionTracking 4 - naET_LoadMatch 5 - naET_Isolation  
rcv |  (long) - Receiver Port  
src |  (long) - Source Port  
numPts |  (long) - number of data points in the real and imaginary arrays.  
real() |  (single) \- array containing the real part of the calibration data. One-dimensional: the number of data points.  
imag() |  (single) \- array containing the imaginary part of the calibration data. One-dimensional: the number of data points.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim eData As ICalData2  
Set eData = app.GetCalManager.Cal Sets.Item(1)  
eData.putErrorTermComplex naET_LoadMatch, 1, 2, numpts, rel(0), img(0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT putErrorTermComplex(tagNAErrorTerm2 ETerm, long ReceivePort, long
SourcePort, long* pNumValues, float* pReal, float* pImag)  
  
#### Interface

|  ICalData2

