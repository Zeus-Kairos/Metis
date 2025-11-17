##### Write/Read

|

##### [About SMC Phase](../../../FreqOffset/SMC_plus_Phase.md)  
  
---|---  
  
## DelayCalculationMethod Property

* * *

#### Description

|  Set and return the method of setting the delay through the calibration
mixer. To select Phase Reference Cal method for correcting an SMC+Phase
measurement, use [ImportDataSet Method](../Methods/ImportDataSet_Method.md).  
---|---  
  
####  VB Syntax

|  smc.DelayCalculationMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
smc |  An [SMCType](../Objects/SMC_Type_Object.md) (object)  
value |  (Enum as NADelayCalculationMethod) 0 - naDelayCalculationMethod_FixedDelay \- use a known delay value set with [FixedDelay Property](FixedDelay_Property.md) 1 - naDelayCalculationMethod_MixerCharacterizationFile \- use the S2P file set with [MixerCharacterizationFile Property](MixerCharacterizationFile_Property.md)  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naDelayCalculationMethod_FixedDelay  
  
#### Example

|  SMC.DelayCalculationMethod = naDelayCalculationMethod_FixedDelay  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_DelayCalculationMethod(tagNADelayCalculationMethod Value);
HRESULT get_DelayCalculationMethod(tagNADelayCalculationMethod* Value);  
  
#### Interface

|  SMCType5  
  
* * *

