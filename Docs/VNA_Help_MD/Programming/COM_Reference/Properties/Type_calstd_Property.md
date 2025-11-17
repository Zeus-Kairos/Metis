##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Type (calstd) Property

* * *

#### Description

|  Sets and Returns the type of calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.Type = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (enum NACalStandardType) -Choose from:  
0 - naOpen  
1 - naShort  
2 - naLoad  
3 - naThru  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.Type = naOpen 'Write  
standardtype = calstd.Type 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Type(tagNACalStandardType *pVal)  
HRESULT put_Type(tagNACalStandardType newVal)  
  
#### Interface

|  ICalStandard

