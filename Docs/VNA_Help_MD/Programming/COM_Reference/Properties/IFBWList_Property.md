##### Read only

|

##### [About IFBW](../../../S2_Opt/Trce_Noise.md#Variable_IF_Bandwidth)  
  
---|---  
  
## IFBWList Property

* * *

#### Description

|  Returns a list of supported IFBW values.  
---|---  
  
####  VB Syntax

|  value = cap.IFBWList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned array of IFBW values  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (Object)  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Read the supported IFBW values Set app =
CreateObject("AgilentPNA835x.Application") Set cap = app.Capabilities
list=cap.IFBWList For i = 0 To UBound(list) msg = msg & list(i) & vbCrLf Next
MsgBox msg  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IFBWList(Variant *value);  
  
#### Interface

|  ICapabilities8  
  
* * *

