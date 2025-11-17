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
interface. Note: There is also a [InputRangeMode
Property](InputRangeMode_cv_Property.htm) on the Converter Object.  
---|---  
  
####  VB Syntax

|  obj.InputRangeMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (Enum as MixerRangeMode) \- Input sweep mode. Choose from: 0 - mixSwept 1 - mixFixed  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - mixSwept  
  
#### Examples

|  mixer.InputRangeMode = mixSwept  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputRangeMode(long *pVal) HRESULT put_InputRangeMode(long
newVal)  
  
#### Interface

|  IMixer6  
  
* * *

