##### Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# RangeGetMaxPower Method

* * *

#### Description

|  Returns the minimum of all max leveled power values from
[RangeStartFrequency](../Properties/RangeStartFrequency_\(PowerRange\)_Property.md)
to
[RangeStopFrequency](../Properties/RangeStopFrequency_\(PowerRange\)_Property.md)
(inclusive).  
---|---  
  
####  VB Syntax

|  maxPower = powerRange.RangeGetMaxPower  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### maxPower

|  (Double) Variable to store the power level in dBm.  
  
#### Return Type

|  (Double)  
  
#### Default

|  Not Applicable  
|  maxPower = powerRange.RangeGetMaxPower  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_RangeGetMaxPower(double* pMax);  
  
#### Interface

|  IPowreRange  
  
* * *

