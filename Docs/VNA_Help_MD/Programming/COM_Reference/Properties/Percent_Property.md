##### Write/Read

|

##### [About Group Delay](../../../Tutorials/Group_Delay6_5.md)  
  
---|---  
  
## Percent Property

* * *

#### Description

|  Sets group delay aperture using a percent of the channel frequency span.  
---|---  
  
####  VB Syntax

|  gdAperture.Percent = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gdAperture |  A [GroupDelayAperture](../Objects/GroupDelayAperture_Object.md) (object)  
value |  (Double) Percent of frequency span to use for the aperture setting. Choose between the equivalent of 2 points and 100 percent of the channel frequency span.  
  
#### Return Type

|  Double  
  
#### Default

|  Percent range that equates to 11 points. This can be changed to two points
with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
#### Examples

|  gdAperture.Percent = 25 'Write  
aperture = gdAperture.Percent 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Percent(double Percent *pVal) HRESULT put_Percent(double
Percent newVal)  
  
#### Interface

|  IGroupDelayAperture  
  
* * *

