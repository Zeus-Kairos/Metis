##### Read-only

|

##### [About Compression Markers](../../../S4_Collect/Markers.md#Compression)  
  
---|---  
  
## CompressionPin Property

* * *

#### Description

|  Reads the input power at the marker compression level. First issue
[SearchCompressionPoint Method](../Methods/SearchCompressionPoint_Method.md)
or [Tracking Property](Tracking_Property.md).  
---|---  
  
####  VB Syntax

|  value = mkr.CompressionPin  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (Double) - Variable to store the returned input power value.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  compLevel=mkr.CompressionPin 'Read [See example
program](../../COM_Example_Programs/Setup_Compression_Marker.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionPin(double* pVal)  
  
#### Interface

|  IMarker4  
  
* * *

