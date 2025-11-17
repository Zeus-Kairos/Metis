Write-only | 

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## PutErrorTerm Method - Superseded

* * *

#### Description

| Note: This command is replaced by
[PutErrorTermByString](Put_ErrorTermByString_Method.md) Puts variant error
term data into the error-correction buffer. If this command is being used to
modify a calset that is currently in use by the channel, you must send the
following commands to see the effects of the change: Calset::Save
Channel::ErrorCorrection = false Channel::ErrorCorrection = true [Learn about
reading and writing Calibration
data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
####  VB Syntax

| cal.putErrorTerm(term,rcv, src, data)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal | A Calibrator (object)  
term | (enum As NaErrorTerm) naErrorTerm_Directivity_Isolation  
naErrorTerm_Match  
naErrorTerm_Tracking  
rcv | (long integer) - Receiver Port  
src | (long integer) - Source Port  
data | (variant) Error term data in a two-dimensional array (0:1, 0:numpts-1).  
  
* * *

To get this | Specify these parameters:  
---|---  
Error Term | term | rcv | src  
Fwd Directivity | naET_Directivity Isolation | 1 | 1  
Rev Directivity | naET_Directivity Isolation | 2 | 2  
Fwd Isolation | naET_Directivity Isolation | 2 | 1  
Rev Isolation | naET_Directivity Isolation | 1 | 2  
Fwd Source Match | naErrorTerm_Match | 1 | 1  
Rev Source Match | naErrorTerm_Match | 2 | 2  
Fwd Load Match | naErrorTerm_Match | 2 | 1  
Rev Load Match | naErrorTerm_Match | 1 | 2  
Fwd Reflection Tracking | naErrorTerm_Tracking | 1 | 1  
Rev Reflection Tracking | naErrorTerm_Tracking | 2 | 2  
Fwd Trans Tracking | naErrorTerm_Tracking | 2 | 1  
Rev Trans Tracking | naErrorTerm_Tracking | 1 | 2  
Fwd Trans Tracking | naErrorTerm_Tracking | 2 | 1  
  
#### Return Type

| Not Applicable  
---|---  
  
#### Default

| Not Applicable  
  
#### Examples

| Dim varError As Variant  
varError = cal.putErrorTerm (naErrorTerm_Tracking,2,1,VarData)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT putErrorTerm(tagNAErrorTerm ETerm, long ReceivePort, long
SourcePort, VARIANT varData)  
  
#### Interface

| ICalibrator

