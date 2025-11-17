##### Write/Read

|

##### [About Source Power](../../../S1_Settings/Power_Level.md)  
  
---|---  
  
## SweepTimeOption Property

* * *

#### Description

|  Enables the Sweep time or Dwell time to be set on individual sweep
segments. This property must be set True before the sweep or dwell time
commands are sent. Otherwise, those commands will be ignored.  
---|---  
  
####  VB Syntax

|  segs.SweepTimeOption = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A [Segments](../Objects/Segments_Collection.md) collection (object)  
state |  (boolean) True \- Enables Sweep or Dwell time to be set independently. False \- Disables Sweep or Dwell time from being set independently.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  segs.SweepTimeOption = True 'Write  
timeOption = SweepTimeOption 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SweepTimeOption(VARIANT_BOOL *pVal)  
HRESULT put_SweepTimeOption(VARIANT_BOOL newVal)  
  
#### Interface

|  ISegments3  
  
* * *

