##### Write/Read

|

##### [About Power
Coupling](../../../S1_Settings/Power_Level.htm#Power_Coupling)  
  
---|---  
  
## CouplePorts Property

* * *

#### Description

|  Turns ON and OFF port power coupling. ON means the power level is the same
for both ports. OFF means the power level may be set independently for each
port.  
---|---  
  
####  VB Syntax

|  object.CouplePorts = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (enum NAStates) Choose from: 0 - NaOff \- Turns coupling OFF 1 - NaOn - Turns coupling ON  
  
#### Return Type

|  Long Integer  
1 \- ON  
0 \- OFF  
  
#### Default

|  NaON (1)  
  
#### Examples

|  chan.CouplePorts = NaOff 'Write  
couplport = chan.CouplePorts 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CouplePorts(tagNAStates *pState)  
HRESULT put_CouplePorts(tagNAStates newState)  
  
#### Interface

|  IChannel |CalSet3

