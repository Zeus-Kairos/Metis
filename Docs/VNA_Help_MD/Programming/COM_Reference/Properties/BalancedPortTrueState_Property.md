##### Write/Read

|

##### [About iTMSA](../../../Applications/iTMSA.md)  
  
---|---  
  
# BalancedPortTrueState(bpnum) Property

* * *

#### Description

| Sets and reads the True Mode state for a specified balanced port.  
---|---  
  
####  VB Syntax

| balStim.BalancedPortTrueState(bpnum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim | A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
bpnum | Balanced port number. This corresponds to the [Balanced Port](../../../Applications/iTMSA.md#Topology) number in the GUI.  
value | (Boolean) Choose from: ON or 1 Turns True Mode ON. OFF or 0  Turns True Mode OFF.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| balStim.BalancedPortTrueState(2) = ON 'Write var =
balStim.BalancedPortTrueState(2) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BalancedPortTrueState (int bpnum, VARIANT_BOOL *pState) HRESULT
put_BalancedPortTrueState (int bpnum, VARIANT_BOOL pState)  
  
#### Interface

| IBalancedStimulus3  
  
* * *

