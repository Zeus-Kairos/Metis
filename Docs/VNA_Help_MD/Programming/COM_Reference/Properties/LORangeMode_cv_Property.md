##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## LORangeMode Property

* * *

#### Description

|  Sets or returns the LO sweep mode. If you are changing several mixer
configuration settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface. Note: There is also a [LORangeMode](LORangeMode_Property.md) on
the Mixer Interface  
---|---  
  
####  VB Syntax

|  obj.LORangeMode (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
n |  (Long) \- LO stage number. Choose from 1 or 2  
value |  (Enum as NARangeMode) \- LO sweep mode. Choose from: 0 - naSwept 1 - naFixed  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naSwept  
  
#### Examples

|  mixer.LORangeMode(1)=naSwept  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LORangeMode(long LO, enum *pVal ) HRESULT put_LORangeMode(long
LO, enum newVal)  
  
#### Interface

|  IConverter  
  
* * *

