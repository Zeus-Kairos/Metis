##### Write/Read

|

##### [About Path
Configurator](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## DescriptiveText Property

* * *

#### Description

|  Write and read descriptive text associated with the configuration. This
text is displayed in the path configuration dialog. Text is generally used to
describe external connections that must be made manually to complete the
configuration setup.  
---|---  
  
####  VB Syntax

|  pathConfig.DescriptiveText = text  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
name |  (String) Variable to store the returned configuration name.  
pathConfig |  A [PathConfiguration](../Objects/PathConfiguration_Object.md) (object)  
text |  (String) Descriptive text enclosed in quotes.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  pathConf.DescriptiveText "here are the instructions for connecting the
device for this configuration"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DescriptionText(BSTR* pConnectionText ); HRESULT
put_DescriptionText(BSTR connectionText );  
  
#### Interface

|  IPathConfiguration  
  
* * *

