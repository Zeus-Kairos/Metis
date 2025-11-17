##### Read only

|

##### [About Measurement
Classes](../../../S1_Settings/Measurement_Classes.htm)  
  
---|---  
  
## AvailableMeasurementClasses Property

* * *

#### Description

|  Returns a list of available measurement classes on the VNA.  
---|---  
  
####  VB Syntax

|  value = cap.AvailableMeasurementClasses  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned list of measurement classes.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Read all measurement classes Set app =
CreateObject("AgilentPNA835x.Application") Set cap = app.Capabilities
meas=cap.AvailableMeasurementClasses dim i For i = 0 To UBound(meas) msg = msg
& meas(i) & vbCrLf Next MsgBox msg  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AvailableMeasurementClasses(Variant *value);  
  
#### Interface

|  ICapabilities7  
  
* * *

