#####  Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## LastModified Property

* * *

#### Description

|  Returns the time stamp of the last modification to this Cal Set. The time
is returned in the local time zone setting of the VNA.  
---|---  
  
#### VB Syntax

|  value = Object.LastModified  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (Variant)  Variable to store the time stamp.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  date = CalSet.LastModified 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LastModified(VARIANT* datetime)  
  
#### Interface

|  ICalSet3  
  
* * *

