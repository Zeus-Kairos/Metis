##### Write/Read

|

##### [About Power Slope](../../../S1_Settings/Power_Level.md#slope)  
  
---|---  
  
## PowerSlopeState Property

* * *

#### Description

|  Turns point slope ON or OFF for all measurements on the channel. Use
[PowerSlope](Power_Slope_Property.md) to set the slope value.  
---|---  
  
####  VB Syntax

|  chan.PowerSlopeState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
state |  (boolean) False \- Turns power slope OFF True \- Turns point slope ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  chan.PowerSlopeState = True 'Write  
state = chan.PowerSlopeState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSlopeState(VARIANT_BOOL *pVal) HRESULT
put_PowerSlopeState(VARIANT_BOOL newVal)  
  
#### Interface

|  IChannel18  
  
* * *

* * *

