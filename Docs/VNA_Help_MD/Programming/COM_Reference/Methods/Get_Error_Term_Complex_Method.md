##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## GetErrorTermComplex Method Superseded

* * *

#### Description

|  This command has been replaced by [Get
ErrorTermComplexByString](Get_ErrorTermComplexByString_Method.htm) Retrieves
error term data from the error correction buffer. The data is in complex
pairs. Note: When performing an ECal, send [SetCalInfoEx
Method](SetCalInfoEx_Method.htm) BEFORE calling GetErrorTermComplex method.
Learn more about [reading and writing Cal Data using
COM.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
This method exists on a non-default interface. If you cannot access this
method, use the [GetErrorTerm](Get_Error_Term_Method.md) Method on
ICalibrator.  
---|---  
  
####  VB Syntax

|  eData.GetErrorTermComplex term, rcv, src, numPts, real(), imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
eData |  An ICalData pointer to the Calibrator object  
term |  (enum NAErrorTerm) - The error term to be retrieved. Choose from:

  * naErrorTerm_Directivity_Isolation
  * naErrorTerm_Match
  * naErrorTerm_Tracking

  
rcv |  (long integer) - Receiver Port  
src |  (long integer) - Source Port  
numPts |  (long integer) \- on input, max number of data points to return;  
on output: indicates the actual number of data points returned.  
real() |  (single) \- array to accept the real part of the error-term. One-dimensional for the number of data points.  
imag() |  (single) \- array to accept the imaginary part of the error-term. One-dimensional for the number of data points.  
  
* * *

|  To get this |  Specify these parameters:  
---|---|---  
|  Error Term |  term |  rcv |  src  
|  Fwd Directivity |  naET_Directivity Isolation |  1 |  1  
|  Rev Directivity |  naET_Directivity Isolation |  2 |  2  
|  Fwd Isolation |  naET_Directivity Isolation |  2 |  1  
|  Rev Isolation |  naET_Directivity Isolation |  1 |  2  
|  Fwd Source Match |  naErrorTerm_Match |  1 |  1  
|  Rev Source Match |  naErrorTerm_Match |  2 |  2  
|  Fwd Load Match |  naErrorTerm_Match |  2 |  1  
|  Rev Load Match |  naErrorTerm_Match |  1 |  2  
|  Fwd Reflection Tracking |  naErrorTerm_Tracking |  1 |  1  
|  Rev Reflection Tracking |  naErrorTerm_Tracking |  2 |  2  
|  Fwd Trans Tracking |  naErrorTerm_Tracking |  2 |  1  
|  Rev Trans Tracking |  naErrorTerm_Tracking |  1 |  2  
  
#### Return Type

|  Single  
---|---  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ReDim rel(numpts)  
ReDim img(numpts)  
Dim eData As ICalData  
Set eData = chan.Calibrator  
eData.getErrorTermComplex naErrorTerm_Directivity_Isolation, 1, 1, 201,
rel(0), img(0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT raw_getErrorTermComplex(tagNAErrorTerm ETerm, long ReceivePort,
long SourcePort, long* pNumValues, float* pReal, float* pImag)  
  
#### Interface

|  ICalData

