##### Write/Read

|

##### [About Group
Delay](../../../Tutorials/Group_Delay6_5.htm#apertureDialog)  
  
---|---  
  
## TwoPointGroupDelayAperture Property

* * *

#### Description

|  Sets the default group delay aperture setting.  
---|---  
  
####  VB Syntax

|  pref.TwoPointGroupDelayAperture = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - Set the default group delay aperture setting to two points. False - Set the default group delay aperture setting to 11 points.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.TwoPointGroupDelayAperture = True 'Write  
gda = pref.TwoPointGroupDelayAperture 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TwoPointGroupDelayAperture(VARIANT_BOOL* pVal);  
HRESULT put_TwoPointGroupDelayAperture(VARIANT_BOOL pVal);  
  
#### Interface

|  IPreferences11  
  
* * *

