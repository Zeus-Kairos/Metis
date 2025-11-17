##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## L0 Property

* * *

#### Description

|  Sets and Returns the L0 (L-zero) value (the first inductance value) for the
calibration standard. To set the other inductance values, use
[L1](L1_Property.md), [L2](L2_Property.md), [L3](L3_Property.md).  
---|---  
  
####  VB Syntax

|  calstd.L0 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Value for L0 in femtohenries(1E-15)  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.L0 = 15 'Write the value of L0 = 15 femtohenries  
Induct0 = calstd.L0 'Read the value of L0  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_L0(float *pVal)  
HRESULT put_L0(float newVal)  
  
#### Interface

|  ICalStandard

