##### Write-only

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## SearchFilterBandwidth Method

* * *

#### Description

|  Searches the measurement data with the current
[BandwidthTarget](../Properties/Bandwidth_Target_Property.md) (default is
-3). To continually track the filter bandwidth, use
[BandwidthTracking.](../Properties/Bandwidth_Tracking_Property.md) This
feature uses [bandwidth markers
1-4](../../../S4_Collect/Markers.htm#Bandwidth) to determine the bandwidth,
center frequency, loss, and Q factor (Center Freq / Bandwidth). If not
already, they are activated. To turn off these markers, either turn them off
individually or [DeleteAllMarkers.](Delete_Marker_Method.md) The bandwidth
statistics are displayed on the analyzer screen. To get the bandwidth
statistics, use either [GetFilterStatistics](Get_Filter_Statistics_Method.md)
or [FilterBW](../Properties/Filter_BW_Property.md),
[FilterCF](../Properties/Filter_CF_Property.md) ,
[FilterLoss](../Properties/Filter_Loss_Property.md) ,or
[FilterQ.](../Properties/Filter_Q_Property.md) The analyzer screen will show
either Bandwidth statistics OR Trace statistics; not both. To search a
[UserRange](../Properties/User_Range_Property.md) with the bandwidth search,
first activate marker 1 and set the desired UserRange. Then send the
SearchFilterBandwidth command. The user range used with bandwidth search only
applies to marker 1 searching for the max value. The other markers may fall
outside the user range.  
---|---  
  
####  VB Syntax

|  meas.SearchFilterBandwidth  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meas.SearchFilterBandwidth  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SearchFilterBandwidth()  
  
#### Interface

|  IMeasurement

