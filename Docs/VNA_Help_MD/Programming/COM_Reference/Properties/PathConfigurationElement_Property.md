##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## PathConfigurationElement Property

* * *

#### Description

|  Allows you to set and return the Path Configuration settings for a Cal All
calibration.  
---|---  
  
####  VB Syntax

|  calAll.PathConfigurationElement (element).value = setting  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll |  A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
element |  (String) Path configuration element to be set. [See a list of configurable RF Path elements](../../RF_PathConfig.md). Is this also for IF Path configuration elements?  
setting |  (String) Path configuration element setting.  
  
#### Return Type

|  String  
  
#### Default

|  Default settings vary with each element.  
  
#### Examples

|  CalAll.PathConfigurationElement(Port1NoiseTuner).value = Internal
'returns the PathConfigurationElement setting  
value = CalAll.PathConfigurationElement(Port1NoiseTuner).value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_PathConfigurationElement(BSTR name, IPathElement** pElement);  
  
#### Interface

|  ICalibrateAllChannels  
  
* * *

* * *

