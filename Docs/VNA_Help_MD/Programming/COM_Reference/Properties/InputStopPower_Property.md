##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputStopPower Property

* * *

#### Description

|  Sets and returns the Stop Power value of the mixer Input Power. If you are
changing several mixer configuration settings, you can make all the changes
first and then issue the [Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.InputStopPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- Input Stop Power in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  Stop Power of the VNA  
  
#### Examples

|  mixer.InputStopPower = 0  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputStopPower(double *pVal) HRESULT put_InputStopPower(double
newVal)  
  
#### Interface

|  IConverter  
  
* * *

