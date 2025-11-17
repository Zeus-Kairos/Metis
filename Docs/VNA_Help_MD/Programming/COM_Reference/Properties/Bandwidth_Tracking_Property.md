##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## BandwidthTracking Property

* * *

#### Description

|  Searches continually (every sweep) for the current
[BandwidthTarget](Bandwidth_Target_Property.md) (default is -3). To search
the filter bandwidth for ONE SWEEP only (not continually), use
meas.[SearchFilterBandwidth.](../Methods/Search_Filter_Bandwidth_Method.md)
This feature uses [markers 1-4](../../../S4_Collect/Markers.md#Bandwidth). To
turn off these markers, either turn them off individually or
[DeleteAllMarkers.](../Methods/DeleteAllMarkers_Method.md) The bandwidth
statistics are displayed on the analyzer screen. To get the bandwidth
statistics, use either
[GetFilterStatistics](../Methods/Get_Filter_Statistics_Method.md) or
[FilterBW](Filter_BW_Property.md), [FilterCF](Filter_CF_Property.md) ,
[FilterLoss](Filter_Loss_Property.md) ,or [FilterQ.](Filter_Q_Property.md)
The analyzer screen will show either Bandwidth statistics OR Trace statistics;
not both. To restrict the search to a [UserRange](User_Range_Property.md)
with the bandwidth search, first activate marker 1 and set the desired
UserRange. Then send the SearchFilterBandwidth command. The user range used
with bandwidth search only applies to marker 1 searching for the max value.
The other markers may fall outside the user range.  
---|---  
  
####  VB Syntax

|  meas.BandwidthTracking = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (boolean)  
True \- Turns bandwidth tracking ON  
False \- Turns bandwidth tracking OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.BandwidthTracking = False 'Write  
bwtrack = meas.BandwidthTracking 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthTracking(VARIANT_BOOL state)  
HRESULT get_BandwidthTracking(VARIANT_BOOL* state)  
  
#### Interface

|  IMeasurement

