##### Write only  
  
---  
  
## LoadFile Method

* * *

#### Description

| Loads a previously-configured mixer attributes file (.mxr)  
---|---  
  
####  VB Syntax

| obj.LoadFile (filename)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj | A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
filename | (String) Full path, file name, and .mxr extension of the mixer attributes file. Files are typically stored in "C:\Program Files(x86)\Keysight\Network Analyzer\Documents".  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| mixer.LoadFile ("D:\myMixer.mxr")  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT LoadFile(BSTR newVal)  
  
#### Interface

| IMixer IConverter  
  
* * *

