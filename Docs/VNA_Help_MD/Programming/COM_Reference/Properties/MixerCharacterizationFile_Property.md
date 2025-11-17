##### Write-only

|

##### [About SMC Phase](../../../FreqOffset/SMC_plus_Phase.md)  
  
---|---  
  
## MixerCharacterizationFile Property

* * *

#### Description

| Set the filename of the S2P file used to characterize the calibration mixer  
---|---  
  
####  VB Syntax

| smc.MixerCharacterizationFile = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
smc | An [SMCType](../Objects/SMC_Type_Object.md) (object)  
value | (String) Full path, file name, and extension of the mixer characterization file.  
  
#### Return Type

| String  
  
#### Default

| Not applicable  
  
#### Example

| SMC.MixerCharacterizationFile = "C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\default.S2P"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_MixerCharacterizationFile(BSTR Value);  
  
#### Interface

| SMCType5  
  
* * *

