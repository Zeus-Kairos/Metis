##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## L1 Property

* * *

#### Description

|  Sets and Returns the L1 value (the second inductance value) for the
calibration standard. To set the other inductance values, use
[L0](L0_Property.md), [L2](L2_Property.md), [L3](L3_Property.md).  
---|---  
  
####  VB Syntax

|  calstd.L1 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Value for L1.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.L1 = 15 'Write the value of L1  
Induct1 = calstd.L1 'Read the value of L1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_L1(float *pVal)  
HRESULT put_L1(float newVal)  
  
#### Interface

|  ICalStandard

