##### Write-only

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## GetCalStandard Method

* * *

#### Description

|  Returns a handle to a calibration standard for modifying its definitions.
To select a standard for performing a calibration (use
Calibrator.[AquireCalStandard](AcquireCalStandard2_Method.md)).  
---|---  
  
####  VB Syntax

|  calkit.GetCalStandard(index)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calkit |  A calKit (object)  
index |  (long) \- Number of calibration standard. Choose 1 to 30; (there are 30 cal standards in every kit).  
  
#### Return Type

|  calStandard  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim short As CalStandard  
Set short = calKit.getCalStandard(1)  
short.label = "myShort"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetCalStandard(long standardNumber, ICalStandard **pCalStd)  
  
#### Interface

|  ICalKit

