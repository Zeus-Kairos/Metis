##### Read-only

|

##### [About Calibration Kits](../../../S3_Cals/Calibration_Standards.md)  
  
---|---  
  
## ActiveCalKit Property

* * *

#### Description

|  Returns a handle to the Active CalKit object. The active cal kit is the kit
selected for use in Unguided calibrations. You can either (1) use the handle
directly to access CalKit properties and methods, or (2) set a variable to the
CalKit object. The variable retains a handle to the original object if another
CalKit becomes active.  
---|---  
  
####  VB Syntax

|  1) app.ActiveCalKit.<setting>  
or  
2) Set cKit = app.ActiveCalKit  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
<setting> |  A CalKit property (or method) and arguments  
cKit |  (object) - A CalKit object  
  
#### Return Type

|  CalKit object  
  
#### Default

|  None  
  
#### Examples

|  Public cKit as calKit  
Set cKit = app.ActiveCalKit 'read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveCalKit (ICalkit * kit)  
  
#### Interface

|  IApplication  
  
* * *

