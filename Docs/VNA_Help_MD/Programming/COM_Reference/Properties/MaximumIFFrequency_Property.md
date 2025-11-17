##### Read-only

|

##### [About Pulsed
Application](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## MaximumIFFrequency Property

* * *

#### Description

|  Returns the Maximum allowed value for the [IFFrequency
Property](IFFrequency_Property.htm)  
---|---  
  
####  VB Syntax

|  value = IfConfig.MaximumIFFrequency  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (double) Variable to store the returned maximum allowed frequency that can be applied to the [IFFrequency Property](IFFrequency_Property.md).  
IfConfig |  [IFConfiguration](../Objects/IIFConfiguration_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  val = App.ActiveChannel.IFConfiguration.MaximumIFFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumIFFrequency( double * pMaxFreq);  
  
#### Interface

|  IIFConfiguration3  
  
* * *

