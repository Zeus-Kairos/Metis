##### Write/Read

|

##### [About iTMSA](../../../Applications/iTMSA.md)  
  
---|---  
  
# BalPort1PowerOffset Property

* * *

#### Description

| Sets and returns the power offset for Balanced port 1. [balStim.Mode](Mode-
iTMSA_Property.htm) must be set to a True Stimulus mode. Applicable only with
[Opt S93460A/B - iTMSA](../../../Applications/iTMSA.md).  
---|---  
  
####  VB Syntax

| balStim.BalPort1PowerOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balStim | A [BalancedStimulus](../Objects/BalancedStimulus_Object.md) (object)  
value | (Double) \- Power Offset in dB.  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| balStim.BalPort1PowerOffset = 2 'Write variable =
balStim.BalPort1PowerOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BalPort1PowerOffset (double *pVal) HRESULT
put_BalPort1PowerOffset (double newVal)  
  
#### Interface

| IBalancedStimulus  
  
* * *

