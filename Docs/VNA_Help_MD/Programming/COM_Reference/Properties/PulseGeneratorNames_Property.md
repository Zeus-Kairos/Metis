##### Read-only

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## PulseGeneratorNames Property

* * *

#### Description

| Returns the string names of internal and configured external pulse
generators.  
---|---  
  
####  VB Syntax

| names = chan.PulseGeneratorNames  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
names | Variant array to store the returned string names.  
chan | A [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

| Variant Array of string names  
  
#### Default

| Not applicable  
  
#### Example

| names = extPulseGen.PulseGeneratorNames 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PulseGeneratorNames (VARIANT *pNames)  
  
#### Interface

| IChannel  
  
* * *

