##### Write/Read

|

#####  
  
---|---  
  
# DimensionRepeatCount Property

* * *

#### Description

|  Set and read the repeat count for the specified dimension order in the
multi-dimensional sweep.  
---|---  
  
####  VB Syntax

|  md.DimensionRepeatCount (dim) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_md_ |  A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
dim |  (long) Dimension order. Choose an integer value of 1 or higher.  
_value_ |  (long) Repeat count. Choose an integer value of 1 or higher.  
  
#### Return Type

|  long  
  
#### Default

|  1  
  
#### Examples

|  md.DimensionRepeatCount (2) = 1  'Write  
value = md.DimensionRepeatCount(4) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ DimensionRepeatCount (long dim, long value); HRESULT get_
DimensionRepeatCount (long dim, long* value);  
  
#### Interface

|  IMultiDimensionalSweep  
  
* * *

