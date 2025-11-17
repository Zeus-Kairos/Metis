##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## Medium Property

* * *

#### Description

|  Sets and Returns the media type of the calibration standard.  
---|---  
  
####  VB Syntax

|  calstd.Medium = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calstd |  A CalStandard (object). Use calKit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) to get a handle to the standard.  
value |  (enum NACalStandardMedium) - Medium of the transmission line of the standard. Choose from:  
0 - naCoax \- Coaxial Cable  
1 - naWaveGuide  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calstd.Medium = naCoax 'Write  
stdMedium = calstd.Medium 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Medium(tagNACalStandardMedium *pVal)  
HRESULT put_Medium(tagNACalStandardMedium newVal)  
  
#### Interface

|  ICalStandard

