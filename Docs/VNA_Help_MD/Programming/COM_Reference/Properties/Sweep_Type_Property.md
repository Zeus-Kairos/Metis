##### Write/Read

|

##### [About Sweep Types](../../../S1_Settings/Sweep.md)  
  
---|---  
  
## SweepType Property

* * *

#### Description

|  Sets and returns the type of sweep. First set SweepType, then set sweep
parameters such as frequency or power settings.  
---|---  
  
####  VB Syntax

|  object.SweepType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  One of the following:

  * [Channel](../Objects/Channel_Object.md) (object)
  * [FOMRange](../Objects/FOMRange_Object.md) (object) Must be an [UNCOUPLED](Coupled_Property.md) range.
  * [CalSet](../Objects/CalSet_Object.md) (object) - Read-only property

  
value |  (enum NASweepTypes) \- Choose from: 0 - naLinearSweep 1 - naLogSweep 2 - naPowerSweep 3 - naCWTimeSweep 4 - naSegmentSweep 5 - naPhaseSweep Note: Sweep type cannot be set to Segment sweep if there are no segments turned ON. A segment is automatically turned ON when a application is created.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naLinearSweep  
  
#### Examples

|  chan.SweepType = naPowerSweep 'Write  
swptyp = chan.SweepType 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SweepType(tagNASweepTypes* pVal) HRESULT
put_SweepType(tagNASweepTypes newVal)  
  
#### Interface

|  IChannel |CalSet3 IFOMRange  
  
* * *

