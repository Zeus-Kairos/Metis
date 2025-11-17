#####  Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## StringToNACalClass Method

* * *

#### Description

|  Converts the returned strings from
[GetStandardsList](Get_StandardsList_Method.md) into the enumeration
(NACalClass) and the port numbers required for
[PutStandard](Put_Standard_Method.md) and
[GetStandard](Get_Standard2_Method.md) methods that transmit data in and out
of the Cal Set. Learn more about [reading and writing Cal data using
COM](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
#### VB Syntax

|  CalSet.StringToNACalClass (list, std, rcv, src)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A Cal Set object  
list |  (string) \- a string containing the textual description of the standard.  
std |  (enum NACalClass) Choose from: |  1 - naClassA  
---  
2 - naClassB  
3 - naClassC  
4 - naClassD  
5 - naClassE  
6 - naReferenceRatioLine  
7 - naReferenceRatioThru  
SOLT Standards  
1 - naSOLT_Open  
2 - naSOLT_Short  
3 - naSOLT_Load  
4 - naSOLT_Thru  
5 - naSOLT_Isolation  
TRL Standards  
1 - naTRL_Reflection  
2 - naTRL_Line_Reflection  
3 - naTRL_Line_Tracking  
4 - naTRL_Thru  
5 - naTRL_Isolation  
rcv |  (long) \- port number of the receiver  
src |  (long) \- port number of the source  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  guid = CalSet.StringToNACalClass(list, std, rcv, src)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT StringtoNACalClass ( BSTR* str, NACalClass* item, long *rcv, long
*src);  
  
#### Interface

|  ICalSet

