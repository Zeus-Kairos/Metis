##### Write/Read

|

##### [About PointSweep](../../../S1_Settings/Sweep.md#pointSweep)  
  
---|---  
  
## PointSweepState Property

* * *

#### Description

|  Turns point sweep ON or OFF for all measurements on the channel. Point
sweep measures both the forward and reverse parameters at each frequency point
before stepping to the next frequency. The display trace is updated after the
forward and reverse parameters are measured at that frequency point.  
---|---  
  
####  VB Syntax

|  chan.PointSweepState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
state |  (boolean) False \- Turns point sweep OFF True \- Turns point sweep ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  chan.PointSweepState = True 'Write  
averg = chan.PointSweepState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PointSweepState(VARIANT_BOOL *pVal)  
HRESULT put_PointSweepState(VARIANT_BOOL newVal)  
  
#### Interface

|  IChannel16  
  
* * *

