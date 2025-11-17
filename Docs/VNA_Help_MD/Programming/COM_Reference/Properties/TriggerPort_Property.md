##### Write/Read

|

##### [About
ExternalDevices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## TriggerPort Property

* * *

#### Description

|  Sets and returns the VNA port through which an external source is to be
triggered.  
---|---  
  
####  VB Syntax

|  extSource.TriggerPort = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extSource |  An [ExternalSource Object](../Objects/ExternalSource_Object.md) (object)  
value |  (enum NAExtDevTriggerPort) \- Choose from: 0 - naExtDevTriggerPortBNC1 (VNA 'C' models) 1 - naExtDevTriggerPortAux1 (PNA-X models) 2 - naExtDevTriggerPortAux2 (PNA-X models)  
  
#### Return Type

|  Enum  
  
#### Default

|  For VNA 'C' models - BNC1 For PNA-X models - Aux1  
  
#### Examples

|  extSource.TriggerPort = 1 'Write  
trigpt = extSource.TriggerPort 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerPort (tagNAExtDevTriggerPort *pValue)  
HRESULT put_TriggerPort (tagNAExtDevTriggerPort newVal)  
  
#### Interface

|  IExternalSource  
  
* * *

