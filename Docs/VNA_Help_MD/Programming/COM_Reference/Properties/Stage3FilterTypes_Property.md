##### Read-only

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3FilterTypes Property

* * *

#### Description

|  Returns a list of strings for the currently supported filter types that can
be used for the stage 3 filter. This command is only used when
[FilterMode](FilterMode_Property.md) is set to False (Manual). See
[Stage3FilterType](Stage3FilterType_Property.md) for a list of currently
supported filter types.  
---|---  
  
####  VB Syntax

|  values= spm4.Stage3FilterTypes  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the returned filter types.  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
Examples |  mode = spm4.Stage3FilterTypes 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3FilterTypes(VARIANT* pTypes);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

