##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## C0 Property

* * *

#### Description

|  Sets and Returns the C0 (C-zero) value (the first capacitance value) for
the calibration standard. To set the other capacitance values, use
[C1](C1_Property.md), [C2](C2_Property.md), [C3](C3_Property.md)  
---|---  
  
####  VB Syntax

|  calstd.C0 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) \- Value for C0 in femtofarads (1E-15)  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.C0 = 15 'Write the value of C0 to 15femtofarads  
cap0 = calstd.C0 'Read the value of C0  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_C0(float *pVal)  
HRESULT put_C0(float newVal)  
  
#### Interface

|  ICalStandard

