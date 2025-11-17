##### Write/Read

|  
---|---  
  
## FootswitchMode Property Obsolete

* * *

#### Description

|  Determines what occurs when the footswitch is pressed. For more information
see the FootSwitch In pin description in the Auxiliary IO connector.  
---|---  
  
####  VB Syntax

|  AuxIo.FootSwitchMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (enum NAFootSwitchMode ) 0 - naIgnoreFootswitch \- Footswitch presses are ignored. 1 - naSweepTrigger \- Footswitch presses trigger a sweep. The VNA must be in Manual Trigger Mode. 2 - naRecallNextState \- Footswitch presses recall an instrument state. When more than one state is available, then each footswitch press recalls the next state, then starts over from the beginning. It is possible for a recalled state to override the current mode. If the recalled state is IGNore, then mode changes and additional footswitch presses are ignored. 3 - naRunMacro \- Footswitch presses load and run a macro. When more than one macro is available, then each footswitch press loads and runs the next macro, then starts over from the beginning. It is possible for a Macro to override the current mode. If the macro contains a Preset, then the mode changes to the default setting IGNore and additional footswitch presses are ignored.  
AuxIO |  (object) - A Hardware Aux I/O object  
  
#### Return Type

|  NAFootSwitchMode  
  
#### Default

|  0 - naIgnoreFootswitch  
  
#### Examples

|  auxIo.FootSwitchMode = naIgnoreFootSwitch 'Write  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FootSwitchMode(NAFootSwitchMode *pFootSwitchMode ) HRESULT
put_FootSwitchMode(NAFootSwitchMode newFootSwitchMode)  
  
#### Interface

|  IHWAuxIO3

