##### Read only

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## ResBWList Property

* * *

#### Description

|  Returns a list of Res BW values that are supported by the IM Spectrum apps.  
---|---  
  
####  VB Syntax

|  value = cap.ResBWList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned array of Res BW values  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (Object)  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Read the supported IFBW values Set app =
CreateObject("AgilentPNA835x.Application") Set cap = app.Capabilities
list=cap.ResBWList For i = 0 To UBound(list) msg = msg & list(i) & vbCrLf Next
MsgBox msg  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ResBWList(Variant *value);  
  
#### Interface

|  ICapabilities8  
  
* * *

