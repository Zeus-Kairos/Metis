##### Read-only

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## PropertyValues Property

* * *

#### Description

|  Returns the valid property values for a specific property name. [See a list
of valid properties and values for each measurement
class](../../../S3_Cals/Calibrate_All_Channels.htm#propertiesDiag).  
---|---  
  
####  VB Syntax

|  props = calAll.PropertyValues (propName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
props |  (Variant Array) Variable to store the returned property values that can be set.  
calAll |  A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
propName |  (String) Property name for which valid values are to be returned.  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  props = calAll.PropertyValues ("Noise Cal Method")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PropertyValues (BSTR propName, VARIANT* propValues);  
  
#### Interface

|  CalibrateAllChannels  
  
* * *

* * *

