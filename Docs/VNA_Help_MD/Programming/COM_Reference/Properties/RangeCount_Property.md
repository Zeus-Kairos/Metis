##### Read-only

|

##### [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## RangeCount Property

* * *

#### Description

|  Returns the number of ranges that are available in the VNA. To see the
range names, query the [Name](Name_FOMRange_Property.md) property of each
range in the FOM collection.  
---|---  
  
####  VB Syntax

|  value = FOM.RangeCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [FOM](../Objects/FOM_Collection.md) (collection object)  
value |  (long) \- Variable to store the returned number of ranges.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  NumRanges = fom.RangeCount 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_RangeCount(long *count)  
  
#### Interface

|  IFOM  
  
* * *

