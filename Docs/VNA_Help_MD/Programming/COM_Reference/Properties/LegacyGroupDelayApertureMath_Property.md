##### Write/Read

|

##### [About Group
Delay](../../../Tutorials/Group_Delay6_5.htm#apertureDialog)  
  
---|---  
  
# LegacyGroupDelayApertureMath Property

* * *

#### Description

| Sets the group delay aperture to use the legacy computation method.  
---|---  
  
####  VB Syntax

| pref.LegacyGroupDelayApertureMath = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref | A [Preferences](../Objects/Preferences_Object.md) (object)  
value | (Boolean) \- Choose from: True - Use legacy computation method. False - Do not use legacy computation method.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| pref.LegacyGroupDelayApertureMath = True 'Write  
gda = pref.LegacyGroupDelayApertureMath 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_LegacyGroupDelayApertureMath(VARIANT_BOOL* pVal);  
HRESULT put_LegacyGroupDelayApertureMath(VARIANT_BOOL pVal);  
  
#### Interface

| IPreferences19  
  
* * *

