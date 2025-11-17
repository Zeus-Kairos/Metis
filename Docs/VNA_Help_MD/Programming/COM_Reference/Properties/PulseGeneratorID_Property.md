##### Read-only

|

##### [About External Pulse
Generators](../../../System/Configure_an_External_Pulse_Generator.htm)  
  
---|---  
  
## PulseGeneratorID Property

* * *

#### Description

|  Returns the ID of the specified External Pulse Generator name. Use this ID
number when setting properties on the [PulseGenerator
Object](../Objects/PulseGenerator_Object.htm). Use
[PulseGeneratorNames](PulseGeneratorNames_Property.md) to read the names of
the internal and configured external pulse generators.  
---|---  
  
####  VB Syntax

|  value = chan.PulseGeneratorID (name)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long Integer) \- Variable to store the returned ID.  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
name |  Name of the pulse generator. Use [PulseGeneratorNames](PulseGeneratorNames_Property.md) to read the names of configured pulse generators.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Example

|  id = chan.PulseGeneratorID "My81110"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PulseGeneratorID(long* count, BSTR name)  
  
#### Interface

|  IChannel23  
  
* * *

* * *

