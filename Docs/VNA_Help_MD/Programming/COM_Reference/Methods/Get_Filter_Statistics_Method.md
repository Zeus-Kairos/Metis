##### Read-only

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## GetFilterStatistics Method

* * *

#### Description

|  Returns all four Filter Statistics resulting from a
[SearchFilterBandwidth](Search_Filter_Bandwidth_Method.md). These statistics
are useful for determining the bandwidth, center frequency, loss, and Q factor
(Center Frequency / Bandwidth) of resonators.  
To retrieve individual filter statistics, use
[meas.FilterCF](../Properties/Filter_CF_Property.md),
[meas.FilterBW](../Properties/Filter_BW_Property.md),
[meas.FilterLoss](../Properties/Filter_Loss_Property.md),
[meas.FilterQ](../Properties/Filter_Q_Property.md) properties.  
---|---  
  
####  VB Syntax

|  meas.GetFilterStatistics cf,bw,loss,q  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
cf,bw,loss,q |  Dimensioned variables to store the returned values  
  
#### Return Type

|  (double) cf  
(single) bw,loss,q  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Dimension variables  
Dim cf as Double  
Dim bw as Single  
Dim loss as Single  
Dim q as Single  
  
meas.GetFilterStatistics cf,bw,loss,q  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetFilterStatistics(double* centerFreq, float* bw, float* loss,
float* quality)  
  
#### Interface

|  IMeasurement

