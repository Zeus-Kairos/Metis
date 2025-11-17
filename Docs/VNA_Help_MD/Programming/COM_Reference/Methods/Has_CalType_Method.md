##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## HasCalType Method

* * *

#### Description

|  Verifies that the Cal Set object contains the error terms required to
perform the specified correction (CalType) to an appropriate measurement. The
argument list includes specifiers for up to 3 ports. The number of arguments
required depends on the CalType specified. The value for each port is set to 0
if not specified.  
---|---  
  
#### VB Syntax

|  check = CalSet.HasCalType (calType, p1, p2, p3)  
---|---  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
check |  (boolean) - variable to store the returned value TRUE (1) - Cal Set has all of the error terms necessary to apply the specified correction CalType. FALSE(0) - Cal Set DOES NOT have all of the error terms necessary to apply the specified CalType.  
CalSet |  (object) - A Cal Set object  
calType |  (enum as naCalType) - type of correction to be applied. Choose from: |  Caltype |  p arguments required  
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
  
p1 |  (long) \- required. This argument must be specified. This specifies either: \- the one significant port for an open/short response cal or a 1 port cal. \- or one of the ports involved in a 2, 3, or 4 port cal \- or the **_receive_** port for a thru response / thru-isolation cal.  
p2 |  (long) - required for any CalType involving more than one port This specifies either: \- one of the ports involved in a 2, 3, or 4 port cal (order independent) \- or the _**source **_ port for a thru response / thru-isolation cal  
p3 |  (long) - required for 3 and 4-port cal This specifies one of the ports involved in a 3 or 4 port cal (order independent)  
  
#### Return Type

|  VARIANT_BOOL  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = CalSet.HasCalType(naCalType_TwoPort_TRL, 1, 2)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT HasCalType( tagNACalType, long port1, long port2, long port3, BOOL
*pVal);  
  
#### Interface

|  ICalSet

