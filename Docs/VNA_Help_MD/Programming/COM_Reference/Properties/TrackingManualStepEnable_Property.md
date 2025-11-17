##### Write/Read

|

##### [About IM Spectrum
Tracking](../../../Applications/IMSpectrum.htm#Tracking)  
  
---|---  
  
## TrackingManualStepEnable Property

* * *

#### Description

|  Sets and returns the step sweep mode for the IM Spectrum channel.  
---|---  
  
####  VB Syntax

|  ims.TrackingManualStepEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Boolean) Choose from: False - Automatic Step True \- Manual Step  
  
#### Return Type

|  Boolean  
  
#### Default

|  False - Automatic Step  
  
#### Examples

|  ims.TrackingManualStepEnable = True 'Write  
value = ims.TrackingManualStepEnable 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TrackingManualStepEnable(VARIANT BOOL *bVal)  
HRESULT put_TrackingManualStepEnable(VARIANT BOOL newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

