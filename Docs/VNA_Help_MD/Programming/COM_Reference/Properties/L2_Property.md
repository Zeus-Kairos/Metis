##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## L2 Property

* * *

#### Description

|  Sets and Returns the L2 value (the third inductance value) for the
calibration standard. To set the other inductance values, use
[L0](L0_Property.md), [L1](L1_Property.md), [L3](L3_Property.md).  
---|---  
  
####  VB Syntax

|  calstd.L2 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Value for L2.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.L2 = 15 'Write the value of L2.  
Induct2 = calstd.L2 'Read the value of L2  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_L2(float *pVal)  
HRESULT put_L2(float newVal)  
  
#### Interface

|  ICalStandard

