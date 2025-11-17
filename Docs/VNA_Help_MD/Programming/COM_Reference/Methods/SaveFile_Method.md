##### Write only  
  
---  
  
## SaveFile Method

* * *

#### Description

|  Saves the mixer/converter test setup to a mixer attributes (.mxr) file.  
---|---  
  
####  VB Syntax

|  obj.SaveFile (filename)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
filename |  (String) Full path, file name, and .mxr extension of the file. Files are typically stored in "D:\".  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mixer.SaveFile ("D:\myMixer.mxr")  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SaveFile(BSTR newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

