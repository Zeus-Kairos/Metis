##### Write/Read

|

##### [About Dwell Time](../../../S1_Settings/Sweep.md#SweepSetupDiag)  
  
---|---  
  
## DwellTime Property

* * *

#### Description

|  Sets or returns the dwell time at the start of each sweep point for all
measurements in a channel. Dwell time is only available with
Chan.[SweepGenerationMode](Sweep_Generation_Mode_Property.md) =
naSteppedSweep (not naAnalogSweep). Sets or returns the dwell time of a
specified sweep segment.  
---|---  
  
####  VB Syntax

|  object.DwellTime = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A Channel (object) or CalSet (object) - Read-only property or Segment (object)  
value |  (double) \- Dwell Time in seconds. Choose any number between  0 and 86400. Note that 0 is equivalent to no dwell time.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  chan.DwellTime = 3e-3 'sets the dwell time for the channel -Write
segs(3).DwellTime = 5e-3 'sets the dwell time of segment 3 -Write  
dwell = chan.DwellTime 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DwellTime(double *pVal)  
HRESULT put_DwellTime(double newVal)  
  
#### Interface

|  IChannel  
ISegment |CalSet3

