##### Write / Read

|

##### [About Path Elements](../../RF_PathConfig.md)  
  
---|---  
  
# PathElement Property

* * *

#### Description

|  Returns the name of the setting for the given path element name or sets the
value of a path element.  
---|---  
  
####  VB Syntax

|  powerRange.PathElement (element).value = setting  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
element |  (String) Path configuration element to be set. [See a list of configurable RF Path elements](../../RF_PathConfig.md).  
setting |  (String) Path configuration element setting.  
  
#### Return Type

|  String  
  
#### Default

|  Default settings vary with each element.  
  
#### Examples

|  powerRange.PathElement("Src2Out1LowBand").value = "HiPwr"  
'returns the PathElement setting  
value = powerRange.PathElement(Src2Out1LowBand).value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_PathElement(BSTR name, IPathElement** pElement);  
  
#### Interface

|  IPowreRange  
  
* * *

