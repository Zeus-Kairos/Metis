##### Write/Read

|

##### [About Path
Configurator](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## Value Property

* * *

#### Description

|  Write or read a value (setting) for the current element. This command is
used to set both RF and IF Path Configuration.

  * See [RF Path Configuration (elements, value)](../../RF_PathConfig.md)
  * See [IF Path Configuration (elements,value)](../../../IFAccess/IF_Path_Configuration.md#elements)

  
---|---  
  
####  VB Syntax

|  pathElement.Value = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pathElement |  A [PathElement](../Objects/PathElement_Object.md) (object)  
value |  (String) Value for the element. Use pathElement.Values to return a list of valid settings for this element.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  See Examples:

  * [IFPathConfiguration Setup](../../COM_Example_Programs/IFPathConfiguration_Setup.md)
  * [RF PathConfiguration Example](../../COM_Example_Programs/PathConfiguration_Example.md)

  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Value( BSTR* pValue ); HRESULT put_Value( BSTR value );  
  
#### Interface

|  IPathElement  
  
* * *

