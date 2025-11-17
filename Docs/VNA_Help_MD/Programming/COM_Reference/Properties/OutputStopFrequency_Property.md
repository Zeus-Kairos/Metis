##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## OutputStopFrequency Property

* * *

#### Description

|  Sets or returns the mixer Output Stop frequency. If you are changing
several mixer configuration settings, you can make all the changes first and
then issue the [Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.OutputStopFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- Output stop frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print mixer.OutputStopFrequency 'prints the value of the
OutputStopFrequency  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OutputStopFrequency(double *pVal) HRESULT
put_OutputStopFrequency(double newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

