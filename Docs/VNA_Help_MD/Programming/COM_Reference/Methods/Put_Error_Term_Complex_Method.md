##### Write-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## PutErrorTermComplex Method Superseded

* * *

#### Description

| Note: This command is replaced by
[PutErrorTermComplexByString](Put_ErrorTermComplexByString_Method.md) Puts
error term data into the error-correction data buffer. If this command is
being used to modify a calset that is currently in use by the channel, you
must send the following commands to see the effects of the change:
Calset::Save Channel::ErrorCorrection = false Channel::ErrorCorrection = true
Learn more about [reading and writing Cal data using
COM](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
####  VB Syntax

| data.putErrorTermComplex term, rcv, src, numPts, real(), imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data | An ICalData pointer to the Calibrator object  
term | (enum NAErrorTerm) - The error term to be retrieved. Choose from:

  * naErrorTerm_Directivity_Isolation
  * naErrorTerm_Match
  * naErrorTerm_Tracking

  
rcv | (long integer) - Receiver Port  
src | (long integer) - Source Port  
numPts | (long integer) - number of data points in the array  
real() | (single) \- array containing the real part of the calibration data. One-dimensional: the number of data points.  
imag() | (single) \- array containing the imaginary part of the calibration data. One-dimensional: the number of data points.  
  
| To get this | Specify these parameters:  
---|---|---  
| Error Term | term | rcv | src  
| Fwd Directivity | naET_Directivity Isolation | 1 | 1  
| Rev Directivity | naET_Directivity Isolation | 2 | 2  
| Fwd Isolation | naET_Directivity Isolation | 2 | 1  
| Rev Isolation | naET_Directivity Isolation | 1 | 2  
| Fwd Source Match | naErrorTerm_Match | 1 | 1  
| Rev Source Match | naErrorTerm_Match | 2 | 2  
| Fwd Load Match | naErrorTerm_Match | 2 | 1  
| Rev Load Match | naErrorTerm_Match | 1 | 2  
| Fwd Reflection Tracking | naErrorTerm_Tracking | 1 | 1  
| Rev Reflection Tracking | naErrorTerm_Tracking | 2 | 2  
| Fwd Trans Tracking | naErrorTerm_Tracking | 2 | 1  
| Rev Trans Tracking | naErrorTerm_Tracking | 1 | 2  
| Fwd Trans Tracking | naErrorTerm_Tracking | 2 | 1  
  
#### Return Type

| Not Applicable  
---|---  
  
#### Default

| Not Applicable  
  
#### Examples

| Dim eData As ICalData  
Set eData = chan.Calibrator  
eData.putErrorTermComplex naErrorTerm_Directivity_Isolation, 1, 1, 201,
rel(0), img(0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT putErrorTermComplex(tagNAErrorTerm ETerm, long ReceivePort, long
SourcePort, long* pNumValues, float* pReal, float* pImag)  
  
#### Interface

| ICalData

