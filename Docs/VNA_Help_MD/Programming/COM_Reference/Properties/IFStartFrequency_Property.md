##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## IFStartFrequency Property

* * *

#### Description

|  Sets or returns the start frequency value of the mixer IF frequency. Only
applies to 2 stage mixers. If you are changing several mixer configuration
settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
#### VB Syntax

|  mixer.IFStartFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A [Converter](../Objects/Converter_Object.md) (object)  
value |  (double) \- Frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print mixer.IFStartFrequency 'prints the value of the IFStartFrequency  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFStartFrequency(double *pVal) HRESULT
put_IFStartFrequency(double newVal)  
  
#### Interface

|  IMixer  
  
* * *

