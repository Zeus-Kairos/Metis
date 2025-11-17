##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTerm Method Superseded

* * *

#### Description

|  This command has been replaced with [Get
ErrorTermByString](Get_ErrorTermByString_Method.htm) Returns error term data
from the Cal Set. The returned data is complex pairs. Learn more about
[Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  data = calSet.getErrorTerm (setNumber, term, rcv, src)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (Variant) Two-dimensional safe array to store the returned data. Memory for the returned Variant is allocated by the VNA and must be released by client. Note: See also [getErrorTermComplex](Get_ErrorTermComplex2_Method.md) on the ICalData2 interface to avoid using the variant data type.  
calSet |  A [Cal Set](../Objects/CalSet_Object.md) (object)  
setNumber |  (Long) There can be more than one set of error terms in a Cal Set.

  * SetNumber 0 contains the original set of error terms for a Cal Set.
  * SetNumbers > 0 contain Interpolated error terms. Interpolated error terms are generated when interpolation is required and destroyed when no longer used. [Learn about Interpolation](../../../S3_Cals/Quest_Cal.md).
  * To determine the SetNumber in use by a channel, see [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md)

  
term |  (enum As NaErrorTerm2). Choose from: 0 - naET_Directivity (rcv = src) 1 - naET_SourceMatch ( rcv = src) 2 - naET_ReflectionTracking ( rcv = src ) 3 - naET_TransmissionTracking (rcv ¹ src) 4 - naET_LoadMatch ( rcv ¹ src) 5 - naET_Isolation (rcv ¹ src)  
rcv |  (Long) \- Receiver Port  
src |  (Long) \- Source Port  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varError As Variant  
varError = CalSet.getErrorTerm(0,naET_TransmissionTracking,2,1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getErrorTerm(long setID, tagNAErrorTerm2 ETerm, long ReceivePort,
long SourcePort, VARIANT* pData)  
  
#### Interface

|  ICalSet

