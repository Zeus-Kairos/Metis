##### Write/Read

|

##### [About Phase Sweep](../../../Applications/iTMSA.md)  
  
---|---  
  
## PhaseSwpState Property

* * *

#### Description

|  Sets and reads the state of phase sweep. [Sweep
type](Sweep_Type_Property.htm) must be set to CWTime.  
---|---  
  
####  VB Syntax

|  balStim.PhaseSwpState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim |  A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value |  (Boolean) State of phase sweep. False Phase sweep disabled. True Phase sweep enabled.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  balStim.PhaseSwpState = False 'Write var = balStim.PhaseSwpState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseSwpState (VARIANT_BOOL *bVal) HRESULT put_PhaseSwpState
(VARIANT_BOOL bVal)  
  
#### Interface

|  IBalancedStimulus2  
  
* * *

