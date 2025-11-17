##### Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# DiscreteGetMaxPowerArray Method

* * *

#### Description

|  Returns an array of max leveled power values (in dBm), where each element
corresponds to the maximum leveled power possible for CW stimulus at the
corresponding frequency set by the
[DiscreteFrequencies](../Properties/DiscreteFrequencies_Property.md)
property.  
---|---  
  
####  VB Syntax

|  maxPower = powerRange.DiscreteGetMaxPowerArray  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### maxPower

|  (Variant array) Variable to store the list of maximum leveled power values
in dBm.  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
|  maxPower = powerRange.DiscreteGetMaxPowerArray  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiscreteGetMaxPowerArray(VARIANT* pMax);  
  
#### Interface

|  IPowreRange  
  
* * *

