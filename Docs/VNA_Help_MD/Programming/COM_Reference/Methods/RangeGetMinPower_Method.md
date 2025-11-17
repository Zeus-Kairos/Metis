##### Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# RangeGetMinPower Method

* * *

#### Description

|  Returns the maximum of all minimum power values from
[RangeStartFrequency](../Properties/RangeStartFrequency_\(PowerRange\)_Property.md)
to
[RangeStopFrequency](../Properties/RangeStopFrequency_\(PowerRange\)_Property.md)
(inclusive).  
---|---  
  
####  VB Syntax

|  minPower = powerRange.RangeGetMinPower  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### minPower

|  (Double) Variable to store the power level in dBm.  
  
#### Return Type

|  (Double)  
  
#### Default

|  Not Applicable  
|  minPower = powerRange.RangeGetMinPower  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_RangeGetMinPower(double* pMin);  
  
#### Interface

|  IPowreRange  
  
* * *

