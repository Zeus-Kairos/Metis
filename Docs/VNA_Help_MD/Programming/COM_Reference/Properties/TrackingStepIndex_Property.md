##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## TrackingStepIndex Property

* * *

#### Description

|  When [TrackingManualStepEnable](TrackingManualStepEnable_Property.md) =
True (Manual step), sets and returns the data point number at which the IM
spectrum measurement occurs.  
---|---  
  
####  VB Syntax

|  ims.TrackingStepIndex = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Integer) Existing IMD channel number to which frequency and power settings are coupled.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1  
  
#### Examples

|  ims.TrackingStepIndex = 50 'Write  
value = ims.TrackingStepIndex 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TrackingStepIndex(long *pVal)  
HRESULT put_TrackingStepIndex(long newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

