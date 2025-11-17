##### Read-only

|

#####  
  
---|---  
  
## ActiveMeasurement Property

* * *

#### Description

|  Returns a handle to the Active Measurement object. You can either (1) use
the handle directly to access measurement properties and methods, or (2) set a
variable to the measurement object. The variable retains a handle to the
original measurement.  
---|---  
  
####  VB Syntax

|  1) app.ActiveMeasurement.<setting>  
or  
2) Set meas = app.ActiveMeasurement  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
app |  An [Application](../Objects/Application_Object.md) (object)  
<setting> |  A measurement property (or method) and arguments  
  
#### Return Type

|  Measurement object  
  
#### Default

|  None  
  
#### Examples

|  1) app.ActiveMeasurement.Averaging = 1  
2) Public meas as Measurement  
Set meas = app.ActiveMeasurement  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveMeasurement(IMeasurement **ppMeas)  
  
#### Interface

|  IApplication

