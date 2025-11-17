##### Read-only

|

##### [About Compression Markers](../../../S4_Collect/Markers.md#Compression)  
  
---|---  
  
## CompressionPout Property

* * *

#### Description

|  Reads the output power at the marker compression level. First issue
[SearchCompressionPoint Method](../Methods/SearchCompressionPoint_Method.md)
or [Tracking Property](Tracking_Property.md).  
---|---  
  
####  VB Syntax

|  value = mkr.CompressionPout  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (Double) - Variable to store the returned output power value.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  compLevel=mkr.CompressionPout 'Read [See example
program](../../COM_Example_Programs/Setup_Compression_Marker.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionPout(double* pVal)  
  
#### Interface

|  IMarker4  
  
* * *

