##### Write/Read

|

##### [About User Ranges](../../../S4_Collect/Markers.md#domain)  
  
---|---  
  
## UserRange Property

* * *

#### Description

|  Assigns the marker to the specified User Range. This restricts the marker's
x-axis travel to the User Range span, specified with
[Start](User_Range_Min_Property.md) and [Stop](User_Range_Max_Property.md)
values.

  * Each channel has 16 user ranges.
  * Markers and trace statistics can be restricted to any user range.
  * More than one marker can occupy a user range.
  * User ranges can overlap. For example:
  *     * User range 1: 3 GHz to 5 GHz
    * User range 2: 4 GHz to 6 GHz

Note: User ranges are especially useful in restricting marker searches to
specific areas of the measurement.  
---|---  
  
####  VB Syntax

|  mark.UserRange = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (long integer) \- User Range. Choose any number between 0 and 16 (0=Full Span)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 - Full Span  
  
#### Examples

|  mark.UserRange = 1 'Write  
UseRnge = mark.UserRange 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_UserRange(long *pRangeNumber)  
HRESULT put_UserRange(long lRangeNumber)  
  
#### Interface

|  IMarker

