##### Write-only

|

##### [About Differential IQ](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## Load Method

* * *

#### Description

|  Recalls the parameters and/or frequency ranges that you previously defined
and saved.  
---|---  
  
####  VB Syntax

|  DIQ.Load (name, type)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [DIQ Object](../Objects/DIQ_Object.md)  
name |  (String) Full path (optional) and filename with or without the *.xml extension. If the full path is not provided, the file is loaded from D:\\.  
type |  (Enum NADIQSaveLoadType) Choose the type of settings to be recalled: naParameterList \- just the parameters. naFrequencyRange \- just the frequency settings. naALL \- both parameters and frequency settings.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  naParameterList  
  
#### Examples

|  Diq.Load "myParams",naParameterList Diq.Load "D:\myParams.xml",naALL  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Load(BSTR name,tag NADIQSaveLoadType type);  
  
#### Interface

|  IDIQ2  
  
* * *

