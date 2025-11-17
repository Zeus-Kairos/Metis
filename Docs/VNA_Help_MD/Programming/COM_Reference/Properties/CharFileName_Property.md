##### Write/Read

|

#####  
  
---|---  
  
## CharFileName Property

* * *

#### Description

|  Specifies the mixer characterization (.S2P) file and immediately loads the
file. Also specify the use of a characterization file with [LoadCharFromFile
Property](LoadCharFromFile_Property.htm)  
---|---  
  
####  VB Syntax

|  VMC.CharFileName = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
  
#### value

|  (String) Full path, file name, and extension of the mixer characterization
file.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  VMC.CharFileName = "c:\users\public\network analyzer\documents/default.S2P"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CharFileName(BSTR filename); HRESULT get_CharFileName(BSTR
*filename);  
  
#### Interface

|  VMCType

