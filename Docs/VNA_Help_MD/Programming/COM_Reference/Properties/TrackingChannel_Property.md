##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## TrackingChannel Property

* * *

#### Description

|  Sets and returns the IMD channel number to which the IM Spectrum channel is
coupled. Use [TrackingEnable](TrackingEnable_Property.md) to enable tracking.  
---|---  
  
####  VB Syntax

|  ims.TrackingChannel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Integer) Existing IMD channel number to which frequency and power settings are coupled.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  First existing IMD channel  
  
#### Examples

|  ims.TrackingChannel = 1 'Write  
value = ims.TrackingChannel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TrackingChannel(long *pVal)  
HRESULT put_TrackingChannel(long newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

