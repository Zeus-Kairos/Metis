##### Read-only

|

#####  
  
---|---  
  
# DimensionCatalog Property

* * *

#### Description

|  Read the names of source domains in the multi-dimensional sweep whose state
is ON and whose dimension order is the specified dimension order.  
---|---  
  
####  VB Syntax

|  names = md.DimensionCatalog(dim)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_names_ |  (Variant) Variable to store the returned source domain names.  
_md_ |  A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
dim |  (long) Dimension order. Choose an integer value of 1 or higher.  
  
#### Return Type

|  String. Names are separated by commas.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  names = md.DimensionCatalog(3) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DimensionCatalog (long dim, VARIANT * pValue);  
  
#### Interface

|  IMultiDimensionalSweep  
  
* * *

