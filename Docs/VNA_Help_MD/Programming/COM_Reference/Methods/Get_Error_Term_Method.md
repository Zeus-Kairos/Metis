##### Read-only

|

##### [About Measurement
Calibration](../../../S3_Cals/Measurement_Calibration.htm)  
  
---|---  
  
## GetErrorTerm Method - Superseded

* * *

#### Description

|  Note: This command is replaced by [Get
ErrorTermByString_Method](Get_ErrorTermByString_Method.htm) Retrieves error
term data that is used for error correction. The data is complex pairs. Memory
for the returned Variant is allocated by the server. The server returns a
variant containing a two-dimensional safe Array. This method returns a variant
which is less efficient than
[getErrorTermComplex](Get_Error_Term_Complex_Method.md) on the ICalData
interface. Note: When performing an ECal, send [SetCalInfoEx
Method](SetCalInfoEx_Method.htm) BEFORE calling GetErrorTerm method. [Learn
about reading and writing Calibration
data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
####  VB Syntax

|  data = cal.getErrorTerm term, rcv. src  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array to store the data.  
cal |  A Calibrator (object)  
term |  (enum As NaErrorTerm). Choose from: naErrorTerm_Directivity_Isolation  
naErrorTerm_Match  
naErrorTerm_Tracking  
rcv |  (long integer) - Receiver Port  
src |  (long integer) - Source Port  
  
* * *

To get this |  Specify these parameters:  
---|---  
Error Term |  term |  rcv |  src  
Fwd Directivity |  naET_Directivity Isolation |  1 |  1  
Rev Directivity |  naET_Directivity Isolation |  2 |  2  
Fwd Isolation |  naET_Directivity Isolation |  2 |  1  
Rev Isolation |  naET_Directivity Isolation |  1 |  2  
Fwd Source Match |  naErrorTerm_Match |  1 |  1  
Rev Source Match |  naErrorTerm_Match |  2 |  2  
Fwd Load Match |  naErrorTerm_Match |  2 |  1  
Rev Load Match |  naErrorTerm_Match |  1 |  2  
Fwd Reflection Tracking |  naErrorTerm_Tracking |  1 |  1  
Rev Reflection Tracking |  naErrorTerm_Tracking |  2 |  2  
Fwd Trans Tracking |  naErrorTerm_Tracking |  2 |  1  
Rev Trans Tracking |  naErrorTerm_Tracking |  1 |  2  
  
* * *  
  
---  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varError As Variant  
varError = cal.getErrorTerm(naErrorTerm_Tracking,2,1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT getErrorTerm(tagNAErrorTerm ETerm, long ReceivePort, long
SourcePort, VARIANT* pData)  
  
#### Interface

|  ICalibrator

