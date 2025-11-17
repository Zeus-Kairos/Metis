##### Write/Read

|

##### [About iTMSA](../../../Applications/iTMSA.md)  
  
---|---  
  
## PowerAsFixture Property

* * *

#### Description

|  Sets and reads the state of power offset as a fixture with True Mode
balanced measurements. [Learn more about iTMSA power and power
offset.](../../../Applications/iTMSA.htm#Offset)  
---|---  
  
####  VB Syntax

|  balStim.PowerAsFixture = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim |  A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value |  (Boolean) State of power offset as a fixture. False Offset is applied but is NOT included as a fixture in the output calculations. True Offset is applied and included as a fixture in the output calculations.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  balStim.PowerAsFixture = False 'Write var = balStim.PowerAsFixture 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerAsFixture (VARIANT_BOOL *bVal) HRESULT put_PowerAsFixture
(VARIANT_BOOL bVal)  
  
#### Interface

|  IBalancedStimulus  
  
* * *

