##### Write/Read

|

#####  
  
---|---  
  
# SourcePortPhaseState Property

* * *

#### Description

|  Set and read the source phase domains ON/OFF state in the multi-
dimensional sweep.  
---|---  
  
####  VB Syntax

|  md.SourcePortPhaseState(_port_) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_md_ |  A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
_port_ |  (long) **Source port number for which to set the source phase state.**  
_value_ |  Boolean) Choose from: **0 - OFF** -Disable the specified source phase domain in multi-dimensional sweep. **1 - ON** \- Enable the specified source phase domain in multi-dimensional sweep.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  md.SourcePortPhaseState(0) = OFF  'Write  
value = md.SourcePortPhaseState(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePortPhaseState(long port, VARIANT_BOOL value); HRESULT
get_SourcePortPhaseState(long port, VARIANT_BOOL* value);  
  
#### Interface

|  IMultiDimensionalSweep  
  
* * *

