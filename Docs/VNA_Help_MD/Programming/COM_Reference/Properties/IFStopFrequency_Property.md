##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## IFStopFrequency Property

* * *

#### Description

|  Sets or returns the stop frequency value of the mixer IF frequency. Only
applies to 2 stage mixers. If you are changing several mixer configuration
settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  mixer.IFStopFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A [Converter](../Objects/Converter_Object.md) (object)  
value |  (double) \- IF stop frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print mixer.IFStopFrequency 'prints the value of the IFStopFrequency  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFStopFrequency(double *pVal) HRESULT
put_IFStopFrequency(double newVal)  
  
#### Interface

|  IMixer  
  
* * *

