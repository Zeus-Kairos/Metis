##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## StandardForClass Property - Superseded

* * *

#### Description

|  Superseded This command sets a single standard to a calibration class. Does
NOT set or dictate the order for measuring the standards. Use
[GetStandardForClass](../Methods/Get_StandardForClass_Method.md) and
[SetStandardForClass](../Methods/Set_StandardForClass_Method.md). These
commands allow up to seven standards to be assigned to a cal class.  
---|---  
  
####  VB Syntax

|  calKit.StandardForClass(class, portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calKit |  A CalKit (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
class |  (enum NACalClass) Standard. Choose from: |  1 - naClassA  
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
portNum |  (long) - The port number the standard will be connected to. For example, you may have a 3.5mm connector designated for port 1, and Type N designated for port 2.  
value |  (long) - Calibration class number. Choose a number between 1 and 8. The <value> numbers are associated with the following calibration classes:  
  
|  <value> |  Class |  Description  
---|---|---|---  
|  1 |  S11A |  Reflection standard  
|  2 |  S11B |  Reflection standard  
|  3 |  S11C |  Reflection standard  
|  4 |  S21T |  Thru standard  
|  5 |  S22A |  Reflection standard  
|  6 |  S22B |  Reflection standard  
|  7 |  S22C |  Reflection standard  
|  8 |  S21T |  Thru standard  
  
####

#### Return Type

|  Long Integer  
---|---  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calKit.StandardForClass(naSOLT_Short, 1) = 1  
Kclass = calKit.StandardForClass(naSOLT_Short, 1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_StandardForClass (NACalClass item, long pNum); HRESULT
get_StandardForClass (NACalClass* item, long *pNum);  
  
#### Interface

|  ICalKit

