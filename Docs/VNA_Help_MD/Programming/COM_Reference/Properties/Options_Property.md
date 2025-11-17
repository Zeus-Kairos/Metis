##### Read-only

|

##### [About Options](../../../Support/Configurations.md)  
  
---|---  
  
## Options Property

* * *

#### Description

|  Returns a string identifying the analyzer option configuration. Refer to
the [option number
differences](../../../Support/Configurations.htm#OPT_and_Options_COM_Behavior)
between the common option numbers and those returned using this command.  
---|---  
  
####  VB Syntax

|  value = app.Options  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (string) - variable to contain the returned string  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  availOptions = app.Options  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Options(BSTR* OptionString)  
  
#### Interface

|  IApplication

