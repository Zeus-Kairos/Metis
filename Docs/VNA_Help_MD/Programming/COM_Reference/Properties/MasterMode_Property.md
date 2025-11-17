##### Write/Read

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## PrimaryMode Property

* * *

#### Description

| Sets and returns the primary (On/Off) setting of the external pulse
generator. this setting allows the external pulse generator to set the primary
clock frequency for the other pulse generators.  
---|---  
  
####  VB Syntax

| extPulseGen.PrimaryMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extPulseGen | An [ExternalPulseGenerator](../Objects/ExternalPulseGenerator_Object.md) (object)  
value | (Boolean) Primary setting. Choose from: True \- Use the external pulse generator becomes the primary clock frequency. False \- Use the internal pulse generator as the primary clock frequency.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| extPulseGen.PrimaryMode = True 'Write  
primary = extPulseGen.PrimaryMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PrimaryMode (VARIANT BOOL *pValue) HRESULT put_PrimaryMode
(VARIANT BOOL newVal)  
  
#### Interface

| IExternalPulseGenerator2  
  
* * *

