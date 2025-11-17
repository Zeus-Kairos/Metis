##### Read-only

|

##### [About Measurement Class](../../../S1_Settings/Measurement_Classes.md)  
  
---|---  
  
## MeasurementClass Property

* * *

#### Description

|  Returns the measurement class name from the channel. Use
[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)
to create a measurement from a class other than standard S-Parameters.  
---|---  
  
####  VB Syntax

|  class = chan.MeasurementClass  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
class |  (string) - Variable to store the returned measurement class name.  
chan |  [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  class = chan.MeasurementClass 'Read  
For a standard S-Parameter channel, returns...  
"Standard"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MeasurementClass();  
  
#### Interface

|  IChannel15  
  
* * *

