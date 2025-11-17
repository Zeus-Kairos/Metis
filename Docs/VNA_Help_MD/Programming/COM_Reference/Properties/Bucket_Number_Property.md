##### Write/Read

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## BucketNumber Property

* * *

#### Description

|  Sets or returns the bucket number (data point) for the active marker. When
the markers are [interpolated (non-
discrete](../../../S4_Collect/Markers.htm#discrete)), the returned value is
the nearest marker bucket position.  
---|---  
  
####  VB Syntax

|  mark.BucketNumber = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (long integer) - Data point. Choose any number between 0 and the measurement's number of data points - 1. For example, with Number of points = 201, choose between 0 and 200  
  
#### Return Type

|  Long Integer  
  
#### Default

|  The first marker is set to the middle of the span. Subsequent markers are
set to the bucket number of the previously active marker.  
  
#### Examples

|  mark.BucketNumber = 100 'moves the active marker to data point 100 -Write  
pointNumber = mark.BucketNumber 'returns the data point number of the marker
object. When the markers are interpolated (non-discrete), the returned value
is the nearest marker bucket position.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_BucketNumber(long *pVal)  
HRESULT put_BucketNumber(long newVal)  
  
#### Interface

|  IMarker

