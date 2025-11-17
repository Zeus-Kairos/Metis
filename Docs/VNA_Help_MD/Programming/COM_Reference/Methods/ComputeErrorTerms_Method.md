##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## ComputeErrorTerms Method

* * *

#### Description

|  Computes error terms for the caltype specified by a preceding OpenCal Set
call. The Cal Set must first be opened using
[OpenCalSet](Open_CalSet_Method.md). If this call has not been made, the
following error is issued: E_NA_Cal Set_ACCESS_DENIED The standards data
required for the CalType must be available in the Cal Set or this error will
be returned: E_NA_STANDARD_NOT_FOUND. Note: Error term computation requires
data for the actual calibration kit standards from the current kit definition.
ComputeErrorTerms assumes that the standards were acquired using only one
standard per class.  
---|---  
  
#### VB Syntax

|  CalSet.ComputeErrorTerms  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A [Cal Set](../Objects/CalSet_Object.md) object  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  CalSet.ComputeErrorTerms  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ComputeErrorTerms( )  
  
#### Interface

|  ICalSet

