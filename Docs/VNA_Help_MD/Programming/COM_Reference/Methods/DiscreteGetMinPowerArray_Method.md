##### Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# DiscreteGetMinPowerArray Method

* * *

#### Description

|  Returns an array of minimum power values (in dBm), where each element
corresponds to the minimum power possible for CW stimulus at the corresponding
frequency set by the
[DiscreteFrequencies](../Properties/DiscreteFrequencies_Property.md)
property.  
---|---  
  
####  VB Syntax

|  minPower = powerRange.DiscreteGetMinPowerArray  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### minPower

|  (Variant array) Variable to store the list of minimum power values in dBm.  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
|  minPower = powerRange.DiscreteGetMinPowerArray  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiscreteGetMinPowerArray(VARIANT* pMin);  
  
#### Interface

|  IPowreRange  
  
* * *

