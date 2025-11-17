##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## LOPower Property

* * *

#### Description

|  Sets or returns the value of LO Power.  
---|---  
  
####  VB Syntax

|  obj.LOPower (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
n |  (Long) \- LO stage number Choose from 1 or 2  
value |  (double) \- LO Power in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  -10dBm  
  
#### Examples

|  Print mixer.LOPower(1) 'prints the value of the LO Power  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LOPower(double *pVal) HRESULT put_LOPower(double newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

