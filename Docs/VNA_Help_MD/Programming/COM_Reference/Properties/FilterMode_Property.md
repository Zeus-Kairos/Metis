##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## FilterMode Property

* * *

#### Description

|  Sets and returns whether the VNA configures the 3-stage digital filter
settings or they will be configured manually. When making manual settings,
also send [ADCCaptureMode Property](ADCCaptureMode_Property.md) which routes
the IF through the 3-stage filter.  
---|---  
  
####  VB Syntax

|  spm4.FilterMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
value |  (enum as NAModes) Filter mode. Choose from: naAUTO VNA controls digital filter settings. naMANUAL You control digital filter settings using other [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) commands.  
  
#### Return Type

|  Enum  
  
#### Default

|  naAUTO  
  
#### Examples

|  spm4.FilterMode = naAUTO 'Write  
mode = spm4.FilterMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FilterMode(tagNAModes* dspMode); HRESULT
put_FilterMode(tagNAModes dspMode);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

* * *

