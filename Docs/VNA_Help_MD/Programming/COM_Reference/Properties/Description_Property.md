##### Write / Read

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Description Property

* * *

#### Description

|  Sets or returns the descriptive string assigned to the Cal Set. Change this
string so that you can easily identify each Cal Set constructed.  
---|---  
  
#### VB Syntax

|  CalSet.Description = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A [Cal Set object](../Objects/CalSet_Object.md)  
value |  (string)  Description of the Cal Set  
  
#### Return Type

|  String  
  
#### Default

|  CalSet_n where n is an integer number.  
  
#### Examples

|  CalSet.Description = "My Cal Set" 'Write  
desc = CalSet.Description 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Description(BSTR *pVal) HRESULT put_Description(BSTR newVal);  
  
#### Interface

|  ICalSet  
  
* * *

