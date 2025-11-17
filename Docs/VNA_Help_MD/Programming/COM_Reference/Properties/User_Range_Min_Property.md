##### Write/Read

|

##### [About User Ranges](../../../S4_Collect/Markers.md#domain)  
  
---|---  
  
## UserRangeMin Property

* * *

#### Description

|  Sets the stimulus start value for the specified User Range. This property
uses different arguments for the channel and marker objects.  
---|---  
  
####  VB Syntax

|  chan.UserRangeMin(domainType,range) = value or mark.UserRangeMin(range) =
value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
mark |  A [Marker](../Objects/Marker_Object.md) (object) To assign a marker to a User Range, use the [UserRange Property](User_Range_Property.md).  
domainType |  Note: The Marker object does not require the domainType argument. (enum NADomainType) Type of sweep currently implemented on the channel - Choose from: 0 - naDomainFrequency 1 - naDomainTime 2 - naDomainPower 3 - naDomainPhase  
range |  (long) \- User Range number. Choose any number between 1 and 16 (0=Full Span)  
value |  (double) - Start value. Choose any number within the full span of the analyzer  
  
#### Return Type

|  Double  
  
#### Default

|  The current stimulus setting for the channel  
  
#### Examples

|  mark.UserRangeMin(1) = 3e9 'Write  
chan.UserRangeMin(naDomainFrequency,1) = 3e9 'Write  
UseRngeMin = mark.UserRangeMin 'Read  
UseRngeMin = chan.UserRangeMin 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_UserRangeMin(tagNADomainType domain, long rangeNumber, double
minValue)  
HRESULT get_UserRangeMin(tagNADomainType domain, long rangeNumber, double
*minValue)  
  
#### Interface

|  IChannel  
  
* * *

