##### Write/Read

|

##### [About Phase Sweep](../../../Applications/iTMSA.md)  
  
---|---  
  
## PhaseSwpAsFixture Property

* * *

#### Description

|  Sets and reads the state of phase offset as a fixture with True Mode
balanced measurements.  
---|---  
  
####  VB Syntax

|  balStim.PhaseAsFixture = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim |  A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value |  (Boolean) State of phase offset as a fixture. False Offset is applied but is NOT included as a fixture in the output calculations. True Offset is applied and included as a fixture in the output calculations.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  balStim.PhaseAsFixture = False 'Write var = balStim.PhaseAsFixture 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseAsFixture (VARIANT_BOOL *bVal) HRESULT put_PhaseAsFixture
(VARIANT_BOOL bVal)  
  
#### Interface

|  IBalancedStimulus2  
  
* * *

