##### Read-only

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
# SegmentCount Property

* * *

#### Description

|  Returns the number of segments used in a limit test. All segments are
counted, whether they are on or not.  
---|---  
  
####  VB Syntax

|  value = limitst.SegmentCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long integer) Variable in which to store the returned segment count.  
limitst |  A LimitTest (object)  
  
#### Return Type

|  Long integer  
  
#### Default

|  1 Segment is created on new limit test objects.  
  
#### Examples

|  count=limitst.SegmentCount  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SegmentCount(long *value);  
  
#### Interface

|  ILimitTest  
  
* * *

