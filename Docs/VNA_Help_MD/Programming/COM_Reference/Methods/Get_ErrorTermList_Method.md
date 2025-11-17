##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTermList Method Superseded

* * *

#### Description

| Note: This command is replaced by
[CalSet.getErrorTermList2](Get_ErrorTermList2_Method.md) Returns the list of
Error Terms contained in this Cal Set for the CalType specified in the
[OpenCal Set](Open_CalSet_Method.md) method. Learn more about [reading and
writing Cal Data using
COM.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
The list is a comma separated, textual representation of the error terms with
the term name followed by the port path in parentheses: Term (n, n), Term
(m,n)  Before calling this method you must open the Cal Set with [OpenCal
Set.](Open_CalSet_Method.htm). If the Cal set is not open, this method returns
E_NA_Cal Set_ACCESS_DENIED.  Use
[StringToNAErrorTerm2](StringtoNAErrorTerm2_Method.md) to convert the list
entrees to values that can be used with
[GetErrorTerm](Get_ErrorTerm2_Method.md) and
[PutErrorTerm](Put_ErrorTerm2_Method.md). Note: The port path designation (m
n) indicates the ports that contribute to the error being compensated.
Directivity, source match and reflection tracking are single port
characteristics, designated in this list by (n n) where n equals the port
being characterized.  
Other terms characterize the interaction between ports. For example, the load
match term is describing the match at port (m) while looking into port (n).
Thus the notation (m n) indicates the two ports that contribute to the
loadmatch error.  
---|---  
  
#### VB Syntax

| CalSet.GetErrorTermList (SetID, count, strList)  
---|---  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet | (object) - A Cal Set object  
SetID | (long) - specifies the error term set to query. Use 0 for the primary set.  
count | (long) - the number of error terms in the returned list  
strList | (string) - comma separated list of error terms found in Cal Set  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| **_dim count as Integer_**** _  
dim list as string_**** _  
OpenCalSet_** (**naCalType_TwoPortSOLT 1, 2)****  
GetErrorTermList( 0, count, list)****  
CloseCalSet( )** Assuming the cal set contained the full set of error terms
for this two-port Cal, the returned list would be: "Directivity(1
1),SourceMatch(1 1),ReflectionTracking(1 1),TransmissionTracking(2
1),LoadMatch(2 1),Isolation(2 1),Directivity(2 2),SourceMatch(2
2),ReflectionTracking(2 2),TransmissionTracking(1 2),LoadMatch(1
2),Isolation(1 2)"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT GetErrorTermList (long etermSetID, long* count, BSTR* strList);  
  
#### Interface

| ICalSet

