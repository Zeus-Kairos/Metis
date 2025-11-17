##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## AutoCWSweepTime Property

* * *

#### Description

|  This command replaces [AutoIFBandWidth
Property](AutoIFBandWidth_Property.htm). Sets and returns the state of
automatic CW sweep time (used in Pulse Profile mode).  
---|---  
  
####  VB Syntax

|  pulseMeas.AutoCWSweepTime = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  True \- In Pulse Profile mode, adjusts the default X-axis start time to zero and the stop time to double the Pulse Width. This allows you to see one complete pulse. False \- The Sweep Time is not changed.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.AutoCWSweepTime = True 'Write  
value = pulse.AutoCWSweepTime 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoCWSweepTime(VARIANT_BOOL *pVal); HRESULT
put_AutoCWSweepTime(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl2  
  
* * *

* * *

