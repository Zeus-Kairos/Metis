##### Write/Read

|

##### [About iTMSA](../../../Applications/iTMSA.md)  
  
---|---  
  
## BalPort2PowerOffset Property

* * *

#### Description

| Sets and returns the power offset between the two ports that comprise
Balanced port 2. [balStim.Mode](Mode-iTMSA_Property.md) must be set to a True
Stimulus mode. Applicable only with [Opt S93460A/B -
iTMSA](../../../Applications/iTMSA.htm).  
---|---  
  
####  VB Syntax

| balStim.BalPort2PowerOffset = value  
  
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

| balStim.BalPort2PowerOffset = 2 'Write variable =
balStim.BalPort2PowerOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BalPort2PowerOffset (double *pVal) HRESULT
put_BalPort2PowerOffset (double newVal)  
  
#### Interface

| IBalancedStimulus  
  
* * *

