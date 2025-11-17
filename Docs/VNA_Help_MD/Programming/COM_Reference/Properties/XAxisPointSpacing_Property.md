##### Write/Read

|

##### [About X-Axis Spacing](../../../S1_Settings/Sweep.md#X-AxisPoint)  
  
---|---  
  
## XAxisPointSpacing Property

* * *

#### Description

|  Sets X-axis Point Spacing for the displaytraces measured with segment
sweeps on the active channel.  
---|---  
  
####  VB Syntax

|  chan.XAxisPointSpacing = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
value |  (Enum as naStates) \- Choose from: 0 - naOFF \- Turns X-axis Point Spacing OFF 1 - naON \- Turns X-axis Point Spacing ON  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naOFF  
  
#### Examples

|  chan.XAxisPointSpacing = naOFF 'Write  
xspac = chan.XAxisPointSpacing 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_XAxisPointSpacing (tagNAStates *pState);  
HRESULT put_XAxisPointSpacing (tagNAStates newState);  
  
#### Interface

|  IChannel2

