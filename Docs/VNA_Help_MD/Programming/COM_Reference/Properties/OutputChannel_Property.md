##### Write/Read

|

##### [About Ext Pulse
Gens](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## OutputChannel Property

* * *

#### Description

|  Sets and returns the output channel of the pulse generator.  
---|---  
  
####  VB Syntax

|  extPulseGen.OutputChannel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extPulseGen |  An [ExternalPulseGenerator](../Objects/ExternalPulseGenerator_Object.md) (object)  
value |  (Long) Pulse Generator output port. Choose from 1 or 2.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1  
  
#### Examples

|  extPulseGen.OutputChannel = 2 'Write  
port = extPulseGen.OutputChannel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_OutputChannel (long *pValue) HRESULT put_OutputChannel (long
newVal)  
  
#### Interface

|  IExternalPulseGenerator  
  
* * *

