##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## CreateCalSet Method

* * *

#### Description

|  Creates a new Cal Set. The new cal set is initialized with the stimulus
settings from the channel whose number is passed as the argument to this
method. Stimulus settings include frequency, bandwidth, number of points, and
so forth. Use this method when you want to manually upload data to the Cal Set
using the returned ICal Set interface handle..  The channel number does not
restrict the usage of this Cal Set on any other channel. It simply provides a
link to the originating channel so that the stimulus values can be stored in
the Cal Set. Note: Be sure to SAVE the CalSet you are creating. Use
[ICalSet::Save](Save_CalSet_Method.md).  
---|---  
  
####  VB Syntax

|  calMgr.CreateCalSet (chan)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
chan |  (long) \- channel number of the new Cal Set.  
  
#### Return Type

|  ICal Set Interface  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.CreateCalSet 1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT CreateCalSet( long ChannelNumber, ICal Set** pCal Set);  
  
#### Interface

|  ICalManager

