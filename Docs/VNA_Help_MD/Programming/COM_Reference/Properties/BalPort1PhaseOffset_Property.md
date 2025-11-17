##### Write/Read

|

##### [About iTMSA](../../../Applications/iTMSA.md)  
  
---|---  
  
## BalPort1PhaseOffset Property

* * *

#### Description

| Sets and returns the phase offset between the two ports that comprise
Balanced port 1. [balStim.Mode](Mode-iTMSA_Property.md) must be set to a True
Stimulus mode. Applicable only with [Opt S93460A/B -
iTMSA](../../../Applications/iTMSA.htm).  
---|---  
  
####  VB Syntax

| balStim.BalPort1PhaseOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim | A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value | (Double) \- Phase Offset in degrees. Choose a value between -360 and 360.  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| balStim.BalPort1PhaseOffset = 10 'Write variable =
balStim.BalPort1PhaseOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BalPort1PhaseOffset (double *pVal) HRESULT
put_BalPort1PhaseOffset (double newVal)  
  
#### Interface

| IBalancedStimulus  
  
* * *

