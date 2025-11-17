##### Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# DiscreteGetMaxPower Method

* * *

#### Description

|  Returns a single max leveled power value (in dBm) indicating the most
restrictive maximum for all discrete maximum powers (the minimum of all
maximum leveled powers).  
---|---  
  
####  VB Syntax

|  maxPower = powerRange.DiscreteGetMaxPower  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### maxPower

|  (Double) Variable to store the most restrictive maximum power level in dBm.  
  
#### Return Type

|  (Double)  
  
#### Default

|  Not Applicable  
|  maxPower = powerRange.DiscreteGetMaxPower  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiscreteGetMaxPower(double* pMax);  
  
#### Interface

|  IPowreRange  
  
* * *

