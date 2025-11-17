####  Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## StringtoNAErrorTerm2 Method

* * *

#### Description

|  Converts the returned strings from
[GetErrorTermList](Get_ErrorTermList_Method.md) into the enumeration
(NAErrorTerm2) and the port numbers required for
[PutErrorTerm](Put_ErrorTerm2_Method.md) and
[GetErrorTerm](Get_ErrorTerm2_Method.md) methods that transmit data in and
out of the Cal Set. Learn more about [reading and writing Cal data using
COM](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
#### VB Syntax

|  Cal Set.StringToNAErrorTerm2 (list, eterm, rcv, src)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Cal Set |  (object) - A Cal Set object  
list |  (string) \- a string containing the textual description of the error term.  
eterm |  (enum As NaErrorTerm2). Choose from: 0 - naET_Directivity (rcv = src)  
1 - naET_SourceMatch ( rcv = src)  
2 - naET_ReflectionTracking ( rcv = src )  
3 - naET_TransmissionTracking (rcv != src)  
4 - naET_LoadMatch ( rcv != src)  
5 - naET_Isolation (rcv != src)  
rcv |  (long) \- port number of the receiver  
src |  (long) \- port number of the source  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  CalSet.StringToNAErrorTerm2 str, term, rcv, src  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT StringToNAErrorTerm2 (BSTR* str, NAErrorTerm2* item, long *rcv,
long *src);  
  
#### Interface

|  ICalSet

