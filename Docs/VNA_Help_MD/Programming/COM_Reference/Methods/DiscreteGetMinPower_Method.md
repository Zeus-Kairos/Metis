##### Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# DiscreteGetMinPower Method

* * *

#### Description

|  Returns a single minimum power value (in dBm) indicating the most
restrictive minimum for all discrete minimum powers (the maximum of all
minimum powers).  
---|---  
  
####  VB Syntax

|  minPower = powerRange.DiscreteGetMinPower  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### minPower

|  (Double) Variable to store the most restrictive minimum power level in dBm.  
  
#### Return Type

|  (Double)  
  
#### Default

|  Not Applicable  
|  minPower = powerRange.DiscreteGetMinPower  
  
#### [C++](../../Learning_about_COM/COM_Data_Types.md) Syntax

|  HRESULT get_DiscreteGetMinPower(double* pMin);  
  
#### Interface

|  IPowreRange  
  
* * *

