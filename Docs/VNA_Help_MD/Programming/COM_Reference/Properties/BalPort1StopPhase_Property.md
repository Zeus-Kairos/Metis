##### Write/Read

|

##### [About Phase Sweep](../../../Applications/iTMSA.md#BalancedTopDiag)  
  
---|---  
  
## BalPort1StopPhase Property

* * *

#### Description

|  Sets and returns the stop phase of a phase sweep.  
---|---  
  
####  VB Syntax

|  balStim.BalPort1StopPhase = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim |  A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value |  (Double) \- Stop phase in degrees. Choose a value between -360 and 360.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  balStim.BalPort1StopPhase = 10 'Write variable = balStim.BalPort1StopPhase
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BalPort1StopPhase (double *pVal) HRESULT put_BalPort1StopPhase
(double newVal)  
  
#### Interface

|  IBalancedStimulus2  
  
* * *

