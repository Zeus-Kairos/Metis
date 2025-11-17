##### Write/Read

|

#####  
  
---|---  
  
# SourcePortPhaseOrder Property

* * *

#### Description

|  Set and read the source phase domains order in the multi-dimensional
sweep.  
---|---  
  
####  VB Syntax

|  md.SourcePortPhaseOrder(_port_) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_md_ |  A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
_port_ |  (long) **Source port number for which to set the source phase order value.**  
_value_ |  (long) Dimension order. Choose an integer value of 1 or higher.  
  
#### Return Type

|  long  
  
#### Default

|  1  
  
#### Examples

|  md.SourcePortPhaseOrder(0) = 2  'Write  
value = md.SourcePortPhaseOrder(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePortPhaseOrder(long port, long value); HRESULT
get_SourcePortPhaseOrder(long port, long* value);  
  
#### Interface

|  IMultiDimensionalSweep  
  
* * *

