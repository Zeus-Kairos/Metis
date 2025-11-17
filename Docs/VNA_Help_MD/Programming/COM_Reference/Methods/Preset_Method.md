##### Write-only

|

##### [Factory Preset Settings](../../../S1_Settings/Preset_the_Analyzer.md)  
  
---|---  
  
## Preset Method

* * *

#### Description

|  Application Object: Deletes all traces and windows. In addition, resets the
analyzer to factory defined default settings and creates an S11 measurement
named "CH1_S11_1" in window 1. Channel Object: Resets the channel (object) to
factory defined default settings. Does NOT delete the current measurements or
add a new measurement.  
---|---  
  
####  VB Syntax

|  app.Preset  
chan.Preset  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
chan |  A Channel (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.Preset  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Preset()  
  
#### Interface

|  IApplication  
IChannel

