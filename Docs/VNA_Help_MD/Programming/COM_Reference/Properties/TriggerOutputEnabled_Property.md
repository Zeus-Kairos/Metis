##### Write/Read.

|

##### [About Trigger](../../../S1_Settings/Trigger.md#scope)  
  
---|---  
  
## TriggerOutputEnabled Property - Superseded

* * *

#### Description

|  Use [AUX.Enable](Enable_Property.md) to enable AUXI/O triggering. Use
Trigger Source= External to enable Meas Trig Ready output. Enables the VNA to
send trigger signals out the rear-panel TRIGGER OUT connector.  
---|---  
  
####  VB Syntax

|  trigsetup.TriggerOutputEnabled = boolean  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trigsetup |  A [TriggerSetup2](../Objects/TriggerSetup_Object.md) (object)  
boolean |  Choose from: False - VNA does NOT send output trigger signals. True - VNA sends output trigger signals.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  trigsetup.TriggerOutputEnabled = True 'Write  
atba = trigsetup.TriggerOutputEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerOutputEnabled( BOOL *pVal); HRESULT
put_TriggerOutputEnabled( BOOL newVal);  
  
#### Interface

|  ITriggerSetup2  
  
* * *

