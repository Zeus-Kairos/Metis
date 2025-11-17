##### Read/Write

|

#####  
  
---|---  
  
## LoadCharFromFile Property

* * *

#### Description

|  Sets and returns whether a Mixer characterization file is to be loaded.
Specify and load the filename with [CharFileName
Property](CharFileName_Property.htm)  
---|---  
  
#### VB Syntax

|  VMC.LoadCharFromFile = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) - Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
bool |  (Boolean) True \- Load from file False \- Perform mixer characterization  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  value = VMC.LoadCharFromFile  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_LoadCharFromFile(VARIANT_BOOL bLoadCharFromFile); HRESULT
get_LoadCharFromFile(VARIANT_BOOL *bLoadCharFromFile);  
  
#### Interface

|  VMCType

