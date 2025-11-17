##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Loss Property

* * *

#### Description

|  Sets and Returns the insertion loss for the calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.loss = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (single) - Insertion loss in Gohms / sec. (Giga Ohms per second of electrical delay)  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.loss = 3.5 'Write 3.5 Gohms of loss  
stdLoss = calstd.loss 'Read the value of Loss  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Loss(float *pVal)  
HRESULT put_Loss(float newVal)  
  
#### Interface

|  ICalStandard

