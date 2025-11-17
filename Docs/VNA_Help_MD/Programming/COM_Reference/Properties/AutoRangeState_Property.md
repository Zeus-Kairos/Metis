##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## AutoRangeState Property

* * *

#### Description

|  Sets and reads the ON/ OFF state of auto range source attenuation. On the
[Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Auto range source attenuator setting.  
---|---  
  
####  VB Syntax

|  DIQ.AutoRangeState (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Boolean)  Choose from:

  * ON or 1 - Auto range the source attenuation.
  * OFF or 0 - Do not Auto range the source attenuation.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  ON  
  
#### Examples

|  diq.AutoRangeState = True 'Write  
value = diq.AutoRangeState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoRangeState(BSTR port, BOOL* AutoRangeState); HRESULT
put_AutoRangeState(BSTR port, BOOL AutoRangeState);  
  
#### Interface

|  IDifferentialIQ  
  
* * *

