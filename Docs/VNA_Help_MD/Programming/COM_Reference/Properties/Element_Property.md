##### Read only

|

##### [About Path
Configurator](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## Element Property

* * *

#### Description

|  Returns a handle to the specified
[PathElement](../Objects/PathElement_Object.md) object. Each element object
contains a unique set of values. The [Value
Property](Value_element_Property.htm) is used to set the value for each
element. This command is used to set both RF and IF Path Configuration.

  * See [RF Path Configuration (elements, value)](../../RF_PathConfig.md)
  * See [IF Path Configuration (elements,value)](../../../IFAccess/IF_Path_Configuration.md#elements)
  * See [Spectrum Analyzer IF Gain path settings](../../../Applications/Spectrum_Analyzer.md#IF_Gain).

  
---|---  
  
####  VB Syntax

|  Set elem = pathConfig.Element (element)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
elem |  (Object) [IPathElement](../Objects/PathElement_Object.md)  
pathConfig |  A [PathConfiguration](../Objects/PathConfiguration_Object.md) (object)  
element |  (String) Configurable element. Use [pathConfig.Elements](Elements_Property.md) to return a list of configurable elements or [see a list of configurable elements](../../RF_PathConfig.md) for various VNA models.  
  
#### Return Type

|  Object  
  
#### Default

|  Not Applicable  
  
#### Examples

|  See examples: [IF Path
Config](../../COM_Example_Programs/IFPathConfiguration_Setup.htm) [RF Path
Config](../../COM_Example_Programs/PathConfiguration_Example.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Element( BSTR elemName, IPathElement** ppElement);  
  
#### Interface

|  IPathConfiguration  
  
* * *

