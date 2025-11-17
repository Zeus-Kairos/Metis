##### Read-only

|

##### [About Trigger](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## GetNumberOfGroups Method

* * *

#### Description

|  Returns the number of groups a channel has yet to acquire. To set the
number of groups for a channel, use [Number Of Groups
Method](Number_Of_Groups_Method.htm)  
---|---  
  
####  VB Syntax

|  value = chan.GetNumberOfGroups  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long Integer) \- Number of groups  
chan |  Channel (object)  
  
#### Return Type

|  (Long Integer)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  groups = chan.GetNumberOfGroups 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetNumberOfGroups(long* numberOfGroups);  
  
#### Interface

|  IChannel3

