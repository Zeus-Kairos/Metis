##### Write/Read

|

##### [About Phase Sweep](../../../Applications/iTMSA.md#BalancedTopDiag)  
  
---|---  
  
## BalPort2StartPhase Property

* * *

#### Description

|  Sets and returns the start phase of a phase sweep.  
---|---  
  
####  VB Syntax

|  balStim.BalPort2StartPhase = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim |  A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value |  (Double) \- Start phase in degrees. Choose a value between -360 and 360.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  balStim.BalPort2StartPhase = 10 'Write variable =
balStim.BalPort2StartPhase 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BalPort2StartPhase (double *pVal) HRESULT
put_BalPort2StartPhase (double newVal)  
  
#### Interface

|  IBalancedStimulus2  
  
* * *

