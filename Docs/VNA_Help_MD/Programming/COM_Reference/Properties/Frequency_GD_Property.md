##### Write/Read

|

##### [About Group Delay](../../../Tutorials/Group_Delay6_5.md)  
  
---|---  
  
## Frequency Property

* * *

#### Description

|  Sets group delay aperture using a fixed frequency range.  
---|---  
  
####  VB Syntax

|  gdAperture.Frequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gdAperture |  A [GroupDelayAperture](../Objects/GroupDelayAperture_Object.md) (object)  
value |  (Double) Frequency range (in Hz) to use for the aperture setting.  
  
#### Return Type

|  Double  
  
#### Default

|  Frequency range that equates to 11 points. This can be changed to two
points with a [preference
setting](../../../System/Preferences.htm#GroupDelay).  
  
#### Examples

|  gdAperture.Frequency = 1e6 'Write  
aperture = gdAperture.Frequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Frequency(double Frequency *pVal) HRESULT put_Frequency(double
Frequency newVal)  
  
#### Interface

|  IGroupDelayAperture  
  
* * *

