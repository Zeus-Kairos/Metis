##### Write/Read

|

##### [About Stepped Sweep](../../../S1_Settings/Sweep.md#Stepped)  
  
---|---  
  
## SweepGenerationMode Property

* * *

#### Description

|  Sets the method used to generate a sweep: continuous ramp (analog) or
discrete steps (stepped).  
---|---  
  
####  VB Syntax

|  object.SweepGenerationMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (enum NASweepGenerationModes) - Choose either: 0 - naSteppedSweep \- source frequency is CONSTANT during measurement of eah displayed point. More accurate than Analog. Dwell time can be set in this mode. 1 - naAnalogSweep \- source frequency is continuously RAMPING during measurement of each displayed point. Faster than Stepped. Sweep time (not dwell time) can be set in this mode.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Analog  
  
#### Examples

|  Chan.SweepGenerationMode = naAnalogSweep 'Write  
swpgen = Chan.SweepGenerationMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SweepGenerationMode(tagNASweepGenerationModes* pVal)  
HRESULT put_SweepGenerationMode(tagNASweepGenerationModes newVal)  
  
#### Interface

|  IChannel |CalSet3

