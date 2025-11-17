##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Delay Property

* * *

#### Description

|  Sets and Returns the electrical delay value for the calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.Delay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Electrical delay in picoseconds  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Exaamples

|  calstd.Delay = 12 'Write 12ps Delay  
stdDelay = calstd.Delay 'Read the value of Delay  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Delay(float *pVal)  
HRESULT put_Delay(float newVal)  
  
#### Interface

|  ICalStandard  
  
* * *

