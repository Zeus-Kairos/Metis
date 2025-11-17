##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetCalSetUsageInfo Method

* * *

#### Description

|  Returns a string identifying the Cal Set currently in use by the specified
channel. This method identifies the Cal Set being used by returning its GUID.
This method also identifies the "Error Term set" within the Cal Set. Error
term sets are identified by integers, with set 0 belonging to the original
(non-interpolated) terms. As stimulus values for a channel are changed causing
interpolation to be required, a new Error Term set is constructed within the
Cal Set to hold the interpolated Error Terms. The sets are sequentially
numbered 1, 2, 3, and so forth. These Error Term sets are destroyed when they
are no longer being used. If there is no Cal Set in use for the given channel,
the <GUID> argument is set to the empty string.  
---|---  
  
####  VB Syntax

|  calMgr.GetCalSetUsageInfo chan, GUID, setNumber  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A CalManager object  
chan |  (long) - channel of the Cal Set being requested   
GUID |  (string) \- variable to store the GUID of the Cal Set being requested. If there is no Cal Set in use for the given channel, the <GUID> argument is set to the empty string.  
setNumber |  (long) - variable to store the error term ID being requested. If the returned argument is greater than 0, the set is being interpolated.   
  
#### Return Type

|  String, Long Integer  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.GetCalSetUsageInfo 1,GUID,EtermID  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetCalSetUsageInfo (long lChannel, BSTR* CalSetGUID, long*
etermSetID);  
  
#### Interface

|  ICalManager  
  
* * *

