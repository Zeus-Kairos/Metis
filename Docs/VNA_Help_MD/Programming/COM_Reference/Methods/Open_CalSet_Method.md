##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## OpenCalSet Method Superseded

* * *

#### Description

|  This command is no longer necessary. The CalSet.get... and put... commands
that required this command have been replaced, Open the Cal Set to read/write
a particular **_CalType._** Learn more about [reading and writing Cal Data
using
COM.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
This method is a prerequisite to several other Cal Set methods. A Cal Set can
contain more than one C _**alType. **_This method opens the Cal Set and allows
access to a particular set of terms. Subsequent commands like
[getErrorTerm](Get_ErrorTerm2_Method.md) use this information to access the
correct error terms in the Cal Set. For example: cset.OpenCalSet
(**_naCalType_TwoPortSOLT_** ,3,2)  
cset.PutErrorTerm(naDirectivity, 1, 1, Buffer) The directivity error term for
port 1 could belong to any number of caltypes: Full1Port (S11), Full2Port
(12), Full2Port (13) or Full3Port (123). The **_CalType_** _**and port**_
specifiers in OpenCalSet directs the uploaded directivity term to the correct
set of error terms.  To close the Cal Set, see
[CloseCalSet](Close_CalSet_Method.md).  
---|---  
  
#### VB Syntax

|  CalSet.OpenCalSet (CalType, p1, p2, p3)  
---|---  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A Cal Set object  
CalType |  (enum as naCalType) - type of correction to be applied. Choose from: |  Caltype |  p arguments required  
---|---  
0 \- naCalType_Response_Open |  p1  
1 \- naCalType_Response_Short |  p1  
2 \- *naCalType_Response_Thru |  p1 (rcv), p2 (src)  
3 \- *naCalType_Response_Thru_And_Isol |  p1 (rcv), p2 (src)  
4 \- naCalType_OnePort |  p1  
5 \- naCalType_TwoPort_SOLT |  p1, p2  
6 \- naCalType_TwoPort_TRL |  p1, p2  
7 \- naCalType_None |  N/A  
8 \- naCalType_ThreePort_SOLT |  p1, p2, p3  
9 \- Custom |  N/A  
10 \- naCalType_FourPort_SOLT |  p1, p2, p3 (port 4 is assumed)  
  
* order of port arguments is significant for these CalTypes  
  
p1 |  (long) \- required. This argument must be specified. This specifies either: \- the one significant port for an open/short response cal or a 1 port cal. \- or one of the ports involved in a 2 or 3 port cal \- or the **_receive_** port for a thru response / thru-isolation cal.  
p2 |  (long) - required for any caltype involving more than one port This specifies either: \- one of the ports involved in a 2 or 3 port cal (order independent) \- or the _**source**_ port for a thru response / thru-isolation cal  
p3 |  (long) - required only for 3 port cal This specifies either: \- one of the ports involved in a 3 port cal (order independent)  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  CalSet.OpenCalSet naCalType_ThreePort_SOLT, 3,2,1  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT OpenCalSet ( naCalType, port1, [optional] port2, [optional] port3);  
  
#### Interface

|  ICalSet

