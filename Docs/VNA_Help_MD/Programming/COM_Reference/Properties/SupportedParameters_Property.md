##### Read only

|

##### [About Measurement
Classes](../../../S1_Settings/Measurement_Classes.htm)  
  
---|---  
  
## SupportedParameters Property

* * *

#### Description

|  Returns a list of supported parameters for the specified measurement class.  
---|---  
  
####  VB Syntax

|  value = measClassProps.SupportedParameters  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned array of parameters.  
measClassProps |  A [MeasurementClassProperties](../Objects/MeasurementClassProperties_Object.md) (Object)  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Access the MeasurmentClassProperties Object Set app =
CreateObject("AgilentPNA835x.Application") Set cap = app.Capabilities Set
measProps = cap.MeasurmentClassProperties ("Swept IMD") 'Read the supported
parameters list=measProps.SupportedParameters dim i For i = 0 To UBound(list)
msg = msg & list(i) & vbCrLf Next MsgBox msg  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SupportedParameters(Variant *value);  
  
#### Interface

|  ICapabilities8  
  
* * *

