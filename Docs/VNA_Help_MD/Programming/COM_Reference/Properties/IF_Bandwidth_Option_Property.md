##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## IFBandwidthOption Property

* * *

#### Description

|  Enables the IFBandwidth to be set on individual sweep segments. This
property must be set True before seg.[IFBandwidth](IF_Bandwidth_Property.md)
= value is sent. Otherwise, this command will be ignored.  
---|---  
  
####  VB Syntax

|  segs.IFBandwidthOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A Segments collection (object)  
value |  (boolean)  
True \- Enables variable IFBandwidth setting for segment sweep False \-
Disables variable IFBandwidth setting for segment sweep  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  segs.IFBandwidthOption = True 'Write  
IFOption = IFBandwidthOption 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFBandwidthOption(VARIANT_BOOL *pVal)  
HRESULT put_IFBandwidthOption(VARIANT_BOOL newVal)  
  
#### Interface

|  ISegments

