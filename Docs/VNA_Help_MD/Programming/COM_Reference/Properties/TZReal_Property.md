##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
# TZReal Property

* * *

#### Description

|  Sets and Returns the TZReal value (the real Terminal Impedance value) for
the calibration standard. Only applicable when
"[Type](../Objects/CalStandard_Object.md)" is set to naArbitraryImpedance. To
set the other resistance values, use [TZImag](TZImag_Property.md)  
---|---  
  
####  VB Syntax

|  calstd.TZReal = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) \- Value for TZReal in Ohms  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.TZReal = 15 'Write the value of TZReal to 15 Ohms  
imp0 = calstd.TZReal 'Read the value of TZReal  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TZReal(float *pVal);  
HRESULT put_TZReal(float newVal);  
  
#### Interface

|  ICalStandard2

