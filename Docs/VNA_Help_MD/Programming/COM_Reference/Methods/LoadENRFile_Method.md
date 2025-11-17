##### Write-only

|

##### [About ENR tables](../../../Applications/Noise_Cal.md#ENRFiles)  
  
---|---  
  
## LoadENRFile Method

* * *

#### Description

|  Loads an ENR file from disk into VNA memory. This file is typically
provided by the manufacturer of the noise source.  
---|---  
  
####  VB Syntax

|  enr.LoadENRFile (filename)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
enr |  An [ENRFile](../Objects/ENRFile_Object.md) (object)  
filename |  (String) - Absolute path and filename of the ENR file.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See example
program](../../COM_Example_Programs/ENR_File_Management_Example.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT LoadENRFile(BSTR filename);  
  
#### Interface

|  IENRFile  
  
* * *

