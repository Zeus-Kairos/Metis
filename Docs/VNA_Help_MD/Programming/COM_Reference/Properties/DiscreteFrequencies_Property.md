##### Write / Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# DiscreteFrequencies Property

* * *

#### Description

|  Sets or returns the list of discrete frequencies corresponding to the
powers returned by
[DiscreteGetMaxPowerArray](../Methods/DiscreteGetMaxPowerArray_Method.md) or
[DiscreteGetMinPowerArray](../Methods/DiscreteGetMinPowerArray_Method.md).  
---|---  
  
####  VB Syntax

|  powerRange.DiscreteFrequencies = discreteFreqs  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### discreteFreqs

|  (Variant array) Variable to store the list of discrete frequencies.  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
|  discreteFreqs = Array(1e9,2e9,3e9,4e9) 'Write  
powerRange.DiscreteFrequencies = discreteFreqs 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DiscreteFrequencies(VARIANT* Freq); HRESULT
put_DiscreteFrequencies(VARIANT Freq);  
  
#### Interface

|  IPowreRange  
  
* * *

