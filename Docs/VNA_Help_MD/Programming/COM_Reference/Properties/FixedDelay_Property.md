##### Write/Read

|

##### [About SMC Phase](../../../FreqOffset/SMC_plus_Phase.md)  
  
---|---  
  
## FixedDelay Property

* * *

#### Description

|  Set and return the known delay through the calibration mixer.  
---|---  
  
####  VB Syntax

|  smc.FixedDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
smc |  An [SMCType](../Objects/SMC_Type_Object.md) (object)  
value |  (Double) Known delay through the calibration mixer in seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  0 seconds  
  
#### Example

|  SMC.FixedDelay = 12e-9 'Write value =SMC.FixedDelay 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_FixedDelay(Double Value); HRESULT get_FixedDelay(Double*
Value);  
  
#### Interface

|  SMCType5  
  
* * *

