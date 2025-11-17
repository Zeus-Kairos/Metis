##### Write/Read

|

##### [About iTMSA](../../../Applications/iTMSA.md)  
  
---|---  
  
## Mode Property

* * *

#### Description

| Sets and returns the stimulus mode for balanced measurements.  
---|---  
  
####  VB Syntax

| balStim.Mode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim | A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value | (Enum NABALSTIMulus) \- Stimulus Mode. True modes are applicable only with [Opt S93460A/B \- iTMSA](../../../Applications/iTMSA.md). When a True-Mode is selected, the Balanced port powers are automatically uncoupled. Choose from: 0 - naSEStim: Single-Ended stimulus 1 - naTMStim: True-Mode stimulus 2 - naFTMStim: Forward only True-Mode stimulus 3 - naRTMStim: Reversed only True-Mode stimulus  
  
#### Return Type

| Enum  
  
#### Default

| 0 \- naSEStim: Single-Ended stimulus  
  
#### Examples

| balStim.Mode = naTMStim 'Write variable = balStim.Mode 'Read [See an example
iTMSA program](../../COM_Example_Programs/Create_an_iTMSA_Measurement.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Mode(tagNABALSTIMulus *eVal ); HRESULT put_Mode(tagNABALSTIMulus
eVal );  
  
#### Interface

| IBalancedStimulus  
  
* * *

