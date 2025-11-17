##### Write/Read

|

##### [About
ExternalDevices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## TriggerMode (ExtendedProperties) Property

* * *

#### Description

|  Sets and returns the trigger mode for an external source.  
---|---  
  
####  VB Syntax

|  extSource.TriggerMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extSource |  An [ExternalSource Object](../Objects/ExternalSource_Object.md) (object)  
value |  (enum NAExtDevTriggerMode) - Choose from: 0 - naExtDevTriggerModeCW 1 - naExtDevTriggerModeHW  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naExtDevTriggerModeCW  
  
#### Examples

|  extSource.TriggerMode = naExtDevTriggerModeCW 'Write  
tm = extSource.TriggerMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerMode (tagNAExtDevTriggerMode *pMode)  
HRESULT put_TriggerMode (tagNAExtDevTriggerMode newMode)  
  
#### Interface

|  IExternalSource  
  
* * *

