##### Read only

|

##### [About Measurement
Classes](../../../S1_Settings/Measurement_Classes.htm)  
  
---|---  
  
## MeasurementClassProperties Property

* * *

#### Description

|  Provides access to the
[MeasurementClassProperties](../Objects/MeasurementClassProperties_Object.md)
Object.  
---|---  
  
####  VB Syntax

|  handle = cap.MeasurementClassProperties (measClass)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
handle |  (Variant) - Variable to store the returned object.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
measClass |  (String) Name of the measurement class to be accessed. Use [AvailableMeasurementClasses Property](AvailableMeasurementClasses_Property.md) to return a list of measurement classes installed on the VNA.  
  
#### Return Type

|  Object  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Access the MeasurmentClassProperties Object Set app =
CreateObject("AgilentPNA835x.Application") Set cap = app.Capabilities Set
measProps = cap.MeasurmentClassProperties("SweptIMD")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_MeasurementClassProperties(IMeasurementClassProperties
*handle);  
  
#### Interface

|  ICapabilities8  
  
* * *

