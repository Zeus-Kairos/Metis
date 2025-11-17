##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## MinimumFrequency Property

* * *

#### Description

|  Sets and Returns the minimum frequency for the calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.MinimumFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (double) -Minimum frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.MinimumFrequency = 300e3 'Write  
minFrequency = calstd.MinimumFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MinimumFrequency(double *pVal)  
HRESULT put_MinimumFrequency(double newVal)  
  
#### Interface

|  ICalStandard

