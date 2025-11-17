##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## OutputRangeMode Property

* * *

#### Description

|  Sets or returns the Output sweep mode. If you are changing several mixer
configuration settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface. Note: There is also a
[OutputRangeMode](OutputRangeMode_Property.md) Property on the Mixer
Interface.  
---|---  
  
####  VB Syntax

|  obj.OutputRangeMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
value |  (Enum as NARangeMode) \- Output sweep mode. Choose from: 0 - naSwept 1 - naFixed  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naSwept  
  
#### Examples

|  conv.OutputRangeMode = naSwept  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_OutputRangeMode(long *pVal) HRESULT put_OutputRangeMode(long
newVal)  
  
#### Interface

|  IConverter  
  
* * *

