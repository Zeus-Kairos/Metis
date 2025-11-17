##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## C2 Property

* * *

#### Description

|  Sets and Returns the C2 value (the third capacitance value) for the
calibration standard. To set the other capacitance values, use
[C0](C0_Property.md), [C1](C1_Property.md), [C3](C3_Property.md).  
---|---  
  
####  VB Syntax

|  calstd.C2 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Value for C2.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.C2 = 15 'Write the value of C2.  
cap2 = calstd.C2 'Read the value of C2  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_C2(float *pVal)  
HRESULT put_C2(float newVal)  
  
#### Interface

|  ICalStandard

