##### Read-only

|

##### [About Trace
Statistics](../../../S4_Collect/Math_Operations.htm#statistics)  
  
---|---  
  
## GetTraceStatistics Method

* * *

#### Description

|  Returns all four Trace Statistics. To retreive individual Trace statistics,
use [Mean](../Properties/Mean_Property.md),
[PeakToPeak](../Properties/PeakToPeak_Property.md),
[StandardDeviation](../Properties/Standard_Deviation_Property.md) properties.
Use [ShowStatistics](../Properties/Show_Statistics_Property.md) to display
the statistics of the screen.  
---|---  
  
####  VB Syntax

|  meas.GetTraceStatistics pp,mean,stdev  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
pp,mean,stdev |  (double) - Dimensioned variables to store the returned values  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Dimension variables  
Dim pp As Double  
Dim mean As Double  
Dim stdv As Double  
meas.GetTraceStatistics pp, mean, stdv  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetTraceStatistics(double* pp, double* mean, double* stdDeviation)  
  
#### Interface

|  IMeasurement

