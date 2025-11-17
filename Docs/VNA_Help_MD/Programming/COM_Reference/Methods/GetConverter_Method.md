##### Read-only

|

##### [About Swept IMD for Converters](../../../Applications/Swept_IMDx.md)  
  
---|---  
  
## GetConverter Method

* * *

#### Description

|  This method returns a handle to a
[Converter](../Objects/Converter_Object.md) object.  
---|---  
  
####  VB Syntax

|  chan.GetConverter( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

|  IConverter  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim app as AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application") Dim chan As IChannel Set chan =
app.ActiveChannel Dim convert Set convert = chan.GetConverter()  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetConverter( IConverter **obj);  
  
#### Interface

|  IChannel17  
  
* * *

