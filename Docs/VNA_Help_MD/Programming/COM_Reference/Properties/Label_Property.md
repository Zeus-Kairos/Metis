##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Label Property

* * *

#### Description

|  Sets and Returns the label for the calibration standard. The label is used
to prompt the user to connect the specified standard.  
---|---  
  
####  VB Syntax

|  calstd.Label = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (string) - between 1 and 12 characters long. Cannot begin with a numeric.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.Label = "Short" 'Write  
stdLabel = calstd.Label 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Label(BSTR *pVal)  
HRESULT put_Label(BSTR newVal)  
  
#### Interface

|  ICalStandard

