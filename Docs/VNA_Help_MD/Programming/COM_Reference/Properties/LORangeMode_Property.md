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
interface. Note: There is also a [LORangeMode](LORangeMode_cv_Property.md) on
the Converter Object.  
---|---  
  
####  VB Syntax

|  obj.LORangeMode (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object)  
n |  (Long) \- LO stage number. Choose from 1 or 2  
value |  (Enum as MixerRangeMode) \- LO sweep mode. Choose from: 0 - mixSwept 1 - mixFixed  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - mixSwept  
  
#### Examples

|  mixer.LORangeMode(1)=mixSwept  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LORangeMode(long LO, enum *pVal) HRESULT put_LORangeMode(long
LO, enum newVal)  
  
#### Interface

|  IMixer3  
  
* * *

