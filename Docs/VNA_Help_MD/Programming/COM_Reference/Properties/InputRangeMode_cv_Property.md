##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputRangeMode Property

* * *

#### Description

|  Sets or returns the Input sweep mode. If you are changing several mixer
configuration settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface. Note: There is also a [InputRangeMode](InputRangeMode_Property.md)
on the Mixer Interface.  
---|---  
  
####  VB Syntax

|  obj.InputRangeMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
value |  (Enum as NARangeMode) \- Input sweep mode. Choose from: 0 - naSwept 1 - naFixed  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naSwept  
  
#### Examples

|  conv.InputRangeMode = naSwept  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputRangeMode(long LO, enum *pVal) HRESULT
put_InputRangeMode(long LO, enum newVal)  
  
#### Interface

|  IConverter  
  
* * *

