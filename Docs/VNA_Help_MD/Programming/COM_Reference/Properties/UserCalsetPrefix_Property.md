##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## UserCalsetPrefix Property

* * *

#### Description

|  Sets and returns the prefix to be used when saving User Cal Sets that
result from the Cal All session. The Meas Class and channel number are
appended to this prefix for each calibrated channel. Use
[GeneratedCalsets](GeneratedCalsets_Property.md) to read the saved cal set
names. If a Cal Set prefix is NOT set, the cal data for each channel will be
saved only to cal registers.  
---|---  
  
####  VB Syntax

|  calAll.UserCalsetPrefix = prefix  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll |  A [CalibrateAlChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
prefix |  (String) User CalSet prefix.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calAll.UserCalsetPrefix = "MyCalSet" 'Set csPrefix =
calAll.UserCalsetPrefix 'Returns the CalSet prefix  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UserCalsetPrefix (BSTR calsetPrefix); HRESULT
put_UserCalsetPrefix (BSTR* calsetPrefix);  
  
#### Interface

|  ICalibrateAllChannels  
  
* * *

* * *

