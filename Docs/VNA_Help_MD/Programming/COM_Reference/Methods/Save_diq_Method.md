##### Write-only

|

##### [About Differential IQ](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## Save Method

* * *

#### Description

|  Stores the list of parameters and frequency range settings to an*.xml file
for recall at a later time. Use [Load Method](Load_Method.md) to recall
files. Note: The Frequency Range settings and the [DIQ
Parameters](../../../Applications/Differential_IQ.htm#DefineParameter) are
saved and recalled from a single *.xml file.  
---|---  
  
####  VB Syntax

|  DIQ.Save (filename)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [DIQ Object](../Objects/DIQ_Object.md)  
filename |  (String) Full path (optional) and filename with or without the *.xml extension. If the full path is not provided, the file is saved to the D:\ drive.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Diq.Save "myDIQfile" or Diq.Save ""D:\myDIQfile.xml"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Save(BSTR filename);  
  
#### Interface

|  IDIQ2  
  
* * *

