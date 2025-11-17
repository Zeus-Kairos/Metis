##### Write-only

|

##### [About Display Formatting](../../../S1_Settings/Data_Format.md)  
  
---|---  
  
## Autoscale Method

* * *

#### Description

|  Trace Object \- Autoscales only the ONE trace on which Autoscale is being
called. NAWindow Object \- Scales ALL of the traces to fit in the same window.
This is equivalent to "Autoscale All" from the front panel. Autoscale (both
trace and window) behaves differently when [scale
coupling](../Properties/ScaleCouplingMethod_Property.htm) is enabled. How it
behaves depends on the scale coupling method. [Learn
more.](../../../S1_Settings/Scale.htm#ScaleCoupling)  
---|---  
  
####  VB Syntax

|  object.Autoscale  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [Trace](../Objects/Trace_Object.md) (object)  
or[  
NAWindow](../Objects/NAWindow_Object.htm) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Trac.Autoscale 'Autoscales the trace  
Win.Autoscale 'Autoscales all the traces in the window -Write  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AutoScale()  
  
#### Interface

|  INAWindow  
ITrace  
  
* * *

