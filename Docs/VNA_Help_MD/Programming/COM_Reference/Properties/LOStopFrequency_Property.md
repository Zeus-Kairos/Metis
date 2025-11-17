##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## LOStopFrequency Property

* * *

#### Description

|  Sets or returns the LO stop frequency value. This command can only be used
with SMC (not VMC) measurements. If you are changing several mixer
configuration settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.LOStopFrequency (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- LO Stop Frequency in Hertz.  
n |  (Long) \- LO stage number Choose from 1 or 2  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print mixer.LOStopFrequency(1) 'prints the value of the first LO stop
frequency  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LOStopFrequency(long id, double *pVal) HRESULT
put_LOStopFrequency(long id,double newVal)  
  
#### Interface

|  IMixer3 IConverter  
  
* * *

