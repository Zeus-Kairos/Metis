##### Write/Read

|

##### [About Compression Markers](../../../S4_Collect/Markers.md#Compression)  
  
---|---  
  
## CompressionLevel (Marker) Property

* * *

#### Description

|  Set and read the marker compression level. First use
[SearchCompressionPoint](../Methods/SearchCompressionPoint_Method.md) to
create the compression marker.  
---|---  
  
####  VB Syntax

|  mkr.CompressionLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (Double) - Compression level in dB. Choose any number between: -500 dB to 500 dB Standard gain compression values are positive.  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  [See example
program](../../COM_Example_Programs/Setup_Compression_Marker.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionLevel(double* pVal) HRESULT
put_CompressionLevel(double newVal)  
  
#### Interface

|  IMarker4  
  
* * *

