##### Write/Read

|

#####  
  
---|---  
  
# SourcePortFrequencyState Property

* * *

#### Description

|  Set and read the source frequency domains ON/OFF state in the multi-
dimensional sweep.  
---|---  
  
####  VB Syntax

|  md.SourcePortFrequencyState(_port_) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_md_ |  A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
_port_ |  (long) **Source port number for which to set the source frequency state.**  
_value_ |  Boolean) Choose from: **0 - OFF** -Disable the specified source frequency domain in multi-dimensional sweep. **1 - ON** \- Enable the specified source frequency domain in multi-dimensional sweep.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  md.SourcePortFrequencyStateOrder(0) = OFF  'Write  
value = md.SourcePortFrequencyStateOrder(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePortFrequencyState(long port, VARIANT_BOOL value);
HRESULT get_SourcePortFrequencyState(long port, VARIANT_BOOL* value);  
  
#### Interface

|  IMultiDimensionalSweep  
  
* * *

