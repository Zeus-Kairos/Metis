##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortPhaseState Property

* * *

#### Description

|  Sets and reads the ON/ OFF state of phase control. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Phase State setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortPhaseState (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (Enum as NAPhaseControlMode)  Choose from:

  * naPhaseControlOff or 0 \- Phase is NOT set or controlled.
  * naPhaseControlParameter or 1 \- Phase is measured and iterated to within the specified tolerance. Specify the receivers and iteration properties using the [Source:Phase](../../GP-IB_Command_Finder/SourcePhase.md) commands.
  * naPhaseControlOpenLoop or 3\- Phase is set, but receivers are NOT used to measure and iterate the phase of the source. Therefore, the setting of phase is not as accurate or stable. Open Loop mode can be used with phase sweep (for example, from 0 to 360 degrees). However, each sweep may not start at 0 degrees. NO settings on the Phase Control Setup dialog are used in Open Loop. After selecting Open Loop, set each source to ON (not Auto).

  
  
#### Return Type

|  Enum  
  
#### Default

|  naPhaseControlOff or 0  
  
#### Examples

|  diq.PortPhaseState = naPhaseControlOff 'Write  
value = diq.PortPhaseState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortPhaseStateBSTR port, (tagNAPhaseControlMode*
PortPhaseState); HRESULT put_PortPhaseState(BSTR port, tagNAPhaseControlMode
PortPhaseState);  
  
#### Interface

|  IDifferentialIQ  
  
* * *

