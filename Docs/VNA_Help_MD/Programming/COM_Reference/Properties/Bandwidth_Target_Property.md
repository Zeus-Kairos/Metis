##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## BandwidthTarget Property

* * *

#### Description

|  Sets the insertion loss value at which the bandwidth of a filter is
measured (using [BandwidthTracking](Bandwidth_Tracking_Property.md) or
[SearchFilterBandwidth](../Methods/Search_Filter_Bandwidth_Method.md)). For
example, if you want to determine the filter bandwidth 3 db below the bandpass
peak value, set BandwidthTarget to -3.  
---|---  
  
####  VB Syntax

|  meas.BandwidthTarget = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (single) - Target value. Choose any number between -500 and 500  
  
#### Return Type

|  Single  
  
#### Default

|  -3  
  
#### Examples

|  meas.BandwidthTarget = -3 'Write  
fbw = meas.BandwidthTarget 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthTarget(float target)  
HRESULT get_BandwidthTarget(float* target)  
  
#### Interface

|  IMeasurement

