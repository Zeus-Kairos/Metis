##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetStandardsList Method Superseded

* * *

#### Description

|  Note: This command is replaced by
[CalSet.getStandardList2](Get_StandardList2_Method.md). Returns the list of
Standards contained in this Cal Set for the CalType specified in the [OpenCal
Set](Open_CalSet_Method.htm) method. Learn more about [reading and writing Cal
Data using
COM.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
The list is a comma separated, textual representation of the error terms with
the term name followed by the port path in parentheses. Standard (n, n),
Standard (m, n)  Before calling this method you must open the Cal Set with
[OpenCal Set.](Open_CalSet_Method.md) If the Cal Set is not open, this method
returns E_NA_Cal Set_ACCESS_DENIED.  Use
[StringToNACalClass](StringToNACalClass_Method.md) to convert the list
entrees to values that can be used with
[GetStandard](Get_Standard2_Method.md) and
[PutStandard](Put_Standard_Method.md). Note: The port path designation (m n)
indicates the receive and source ports for the measurement. Shorts, opens and
loads are single port devices, designated in this list by (n n) where n equals
the port to which the device is connected. These devices are all characterized
by reflection measurements.  
The dual port thru device is characterized by both transmission and reflection
measurements in order to compensate for load match and tracking terms.  
The notation (n n) indicates the reflection measurement for this device.  
The notation (m n) indicates the transmission measurement, where the source
and receive ports are different.  
---|---  
  
#### VB Syntax

|  CalSet.GetStandardsList (count, list)  
---|---  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A Cal Set object  
count |  (long [out]) \- indicates the number of items returned in the list  
list |  (string) \- Variable to store the returned Comma separated list of items.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  **_dim count as Integer_**** _  
d_**** _im list as string_**** _  
OpenCalSet_** (**_naCalType_TwoPortSOLT, 1, 2)_****_  
GetStandardsList( count, list)_****_  
CloseCalSet( )_** Assuming the Cal Set contained the full set of standards for
this two port cal, the returned list would be: "Open(1 1), Short(1 1), Load(1
1), Thru(1 1), Isolation(2 1), Open(2 2), Short(2 2), Load(2 2), Thru(2 2),
Isolation(1 2) Thru(2 1), Thru(1 2)"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetStandardsList( long* count, BSTR* list);  
  
#### Interface

|  ICalSet

