##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## MaximumFrequency Property

* * *

#### Description

|  Sets and Returns the maximum frequency for the calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.MaximumFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (double) - Maximum frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.MaximumFrequency = 9e9 'Write  
maxFrequency = calstd.MaximumFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumFrequency(double *pVal)  
HRESULT put_MaximumFrequency(double newVal)  
  
#### Interface

|  ICalStandard

