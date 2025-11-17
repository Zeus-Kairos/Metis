##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Z0 Property

* * *

#### Description

|  Sets and Returns the characteristic impedance for the calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.Z0 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) -Impedance in Ohms  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.Z0 = 50 'Write  
impedance = calstd.Z0 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Z0(float *pVal)  
HRESULT put_Z0(float newVal)  
  
#### Interface

|  ICalStandard

