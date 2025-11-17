##### Write-only

|

##### [About Saving to File](../../../S5_Output/SaveRecall.md)  
  
---|---  
  
## PrintToFile Method

* * *

#### Description

|  Saves the screen image to a bitmap file.  
---|---  
  
####  VB Syntax

|  app.PrintToFile filename  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
filename |  (string) Full path, file name, and extension of the screen image file. Files are typically stored in "D:\". Use one of the following extensions:

  * .bmp - not recommended due to large file size
  * .jpg - not recommended due to poor quality
  * .png - recommended

  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.PrintToFile "D:\myfile.png"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT PrintToFile(BSTR bstrFile)  
  
#### Interface

|  IApplication

