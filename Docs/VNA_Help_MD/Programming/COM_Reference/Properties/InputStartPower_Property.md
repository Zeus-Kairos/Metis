##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputStartPower Property

* * *

#### Description

|  Sets and returns the Start Power value of the mixer Input Power. If you are
changing several mixer configuration settings, you can make all the changes
first and then issue the [Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.InputStartPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- Input start Power in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  Start Power of the VNA  
  
#### Examples

|  mixer.InputStartPower = 0  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputStartPower(double *pVal) HRESULT
put_InputStartPower(double newVal)  
  
#### Interface

|  IConverter  
  
* * *

