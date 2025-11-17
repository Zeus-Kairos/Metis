##### Write-only

## Activate Method

* * *

#### Description

|  Makes an object the Active Object. When making a measurement active, the
channel and window the measurement is contained in becomes the active channel
and active window. In order to change properties on any of the active objects,
you must first have a "handle" to the active object using the Set command. For
more information, See [Getting a Handle to an
Object.](../../Learning_about_COM/Getting_a_Handle_to_an_Object.htm) You do
not have to make an object "Active" to set or read its properties remotely.
But an object must be "Active" to change its values from the front panel.  
---|---  
  
####  VB Syntax

|  object.Activate  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [Measurement](../Objects/Measurement_Object.md) (object)  
or[  
Marker](../Objects/Marker_Object.htm) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meas.Activate  
mark.Activate  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Activate()  
  
#### Interface

|  IMeasurement  
IMarker

