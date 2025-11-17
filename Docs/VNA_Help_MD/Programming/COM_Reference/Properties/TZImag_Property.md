##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## TZImag Property

* * *

#### Description

|  Sets and Returns the TZImag value (the Imaginary Terminal Impedance value)
for the calibration standard. Only applicable when
"[Type](../Objects/CalStandard_Object.md)" is set to naArbitraryImpedance. To
set the other resistance values, use [TZReal](TZReal_Property.md)  
---|---  
  
####  VB Syntax

|  calstd.TZImag = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) \- Value for TZImag in Ohms  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.TZImag = 15 'Write the value of TZImag to 15 Ohms  
imp0 = calstd.TZImag 'Read the value of TZImag  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TZImag(float *pVal);  
HRESULT put_TZImag(float newVal);  
  
#### Interface

|  ICalStandard2

