##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutErrorTerm Method Superseded

* * *

#### Description

|  This command is [replaced](../../Replacement_Commands.md) with
[PutErrorTermByString](Put_ErrorTermByString_Method.md) Puts error term data
into the Cal Set. Learn more about [Reading and Writing Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  CalSet.putErrorTerm (term, rcv, src, data)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (Object) A [CalSet](../Objects/CalSet_Object.md) Object  
term |  (enum As NaErrorTerm2) Error Term. Choose from: 0 - naET_Directivity (src = rcv) 1 - naET_SourceMatch ( src = rcv) 2 - naET_ReflectionTracking (src = rcv) 3 - naET_TransmissionTracking (src ¹ rcv) 4 - naET_LoadMatch (src ¹ rcv) 5 - naET_Isolation (src ¹ rcv)  
rcv |  (long integer) - Receiver Port  
src |  (long integer) - Source Port  
data |  (variant) Error term data in a two-dimensional array (0:1, 0:numpts-1). The data must be complex pairs. Note: See also [PutErrorTermComplex](Put_ErrorTermComplex2_Method.md) on the ICalData2 interface to avoid using the variant data type.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See an
Example](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT putErrorTerm(tagNAErrorTerm2 ETerm, long ReceivePort, long
SourcePort, VARIANT varData)  
  
#### Interface

|  ICalSet

