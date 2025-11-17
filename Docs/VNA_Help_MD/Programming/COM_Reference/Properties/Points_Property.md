##### Write/Read

|

##### [About Group Delay](../../../Tutorials/Group_Delay6_5.md)  
  
---|---  
  
## Points Property

* * *

#### Description

|  Sets group delay aperture using a fixed number of data points.  
---|---  
  
####  VB Syntax

|  gdAperture.Points = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gdAperture |  A [GroupDelayAperture](../Objects/GroupDelayAperture_Object.md) (object)  
value |  (Double) Number of data points to use for the aperture setting. Choose between two points and the number of points in the channel.  
  
#### Return Type

|  Double  
  
#### Default

|  Points range that equates to 11 points. This can be changed to two points
with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
#### Examples

|  gdAperture.Points = 25 'Write  
aperture = gdAperture.Points 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Points(double Points *pVal) HRESULT put_Points(double Points
newVal)  
  
#### Interface

|  IGroupDelayAperture  
  
* * *

