##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## C1 Property

* * *

#### Description

|  Sets and Returns the C1 value (the second capacitance value) for the
calibration standard. To set the other capacitance values, use
[C0](C0_Property.md), [C2](C2_Property.md), [C3](C3_Property.md).  
---|---  
  
####  VB Syntax

|  calstd.C1 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Value for C1.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.C1 = 15 'Write the value of C1.  
cap1 = calstd.C1 'Read the value of C1.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_C1(float *pVal)  
HRESULT put_C1(float newVal)  
  
#### Interface

|  ICalStandard

