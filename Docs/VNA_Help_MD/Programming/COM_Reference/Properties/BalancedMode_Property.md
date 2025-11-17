##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## BalancedMode Property

* * *

#### Description

|  Sets and returns whether the balanced transform is ON or OFF  
---|---  
  
####  VB Syntax

|  balMeas.BalancedMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balMeas |  A [BalancedMeasurement](../Objects/BalancedMeasurement_Object.md) (object)  
value |  (Boolean) \- State of balanced transform. Choose from False Balanced Transform OFF True Balanced Transform ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  balMeas.BalancedMode = True 'Write variable = balMeas.BalancedMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BalancedMode(VARIANT_BOOL *bVal) HRESULT
put_BalancedMode(VARIANT_BOOL newVal)  
  
#### Interface

|  IBalancedMeasurement

