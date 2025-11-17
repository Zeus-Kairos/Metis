##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## TrackingEnable Property

* * *

#### Description

|  When an IMD channel exists, allows the IM Spectrum frequency and power
setting to track (couple with) the IMD channel settings. Use
[TrackingChannel](TrackingChannel_Property.md) to set the channel number to
track.  
---|---  
  
####  VB Syntax

|  ims.TrackingEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Boolean) Tracking state. Choose from: True \- IM Spectrum frequency and power settings track the IMD channel settings. False \- IM Spectrum frequency and power settings are specified in the IMS channel.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  ims.TrackingEnable = True 'Write  
value = ims.TrackingEnable 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TrackingEnable(VARIANT_BOOL* bValue)  
HRESULT put_TrackingEnable(VARIANT_BOOL newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

