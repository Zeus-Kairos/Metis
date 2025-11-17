##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## C3 Property

* * *

#### Description

|  Sets and Returns the C3 value (the fourth capacitance value) for the
calibration standard. To set the other capacitance values, use
[C0](C0_Property.md), [C1](C1_Property.md), [C2](C2_Property.md)  
---|---  
  
####  VB Syntax

|  calstd.C3 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Value for C3.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.C3 = 15 'Write the value of C3.  
cap3 = calstd.C3 'Read the value of C3  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_C3(float *pVal)  
HRESULT put_C3(float newVal)  
  
#### Interface

|  ICalStandard

