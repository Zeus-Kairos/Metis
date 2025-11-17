##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Name (CalKit) Property

* * *

#### Description

|  Sets and Returns a name for the selected calibration kit.  
---|---  
  
####  VB Syntax

|  calKit.Name = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calKit |  A CalKit (object).  
value |  (string) -Calibration Kit name. Any string name, can include numerics, period, and spaces; any length (although the dialog box display is limited to about 30 characters).  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calKit.Name = "MyCalKit" 'Write  
KitName = calKit.Name 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Name(BSTR *pVal)  
HRESULT put_Name(BSTR newVal)  
  
#### Interface

|  ICalKit

