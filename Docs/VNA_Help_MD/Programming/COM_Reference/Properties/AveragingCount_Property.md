##### Read-only

|

##### [About Averaging](../../../S2_Opt/Trce_Noise.md#averaging)  
  
---|---  
  
## AveragingCount Property

* * *

#### Description

|  Returns the number of sweeps that have been acquired and averaged into the
measurements on this channel. [AveragingFactor](Averaging_Factor_Property.md)
specifies the number of sweeps to average. AveragingCount indicates the
progress toward that goal.  
---|---  
  
####  VB Syntax

|  value = chan.AveragingCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
value |  (Long Integer) \- Variable to store the returned count  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Example

|  avgcount = chan.AveragingCount  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AveragingCount(long* count)  
  
#### Interface

|  IChannel

