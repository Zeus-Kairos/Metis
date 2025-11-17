##### Write/Read

|  
---|---  
  
# DCState Property

* * *

#### Description

|  Set and read the specified DC sources ON/OFF state in the multi-
dimensional sweep.  
---|---  
  
####  VB Syntax

|  md.DCState (_name,port_) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_md_ |  A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
_name,port_ |  (string) Name of the "DC source, port"  
_value_ |  (Boolean) Choose from: **0 - OFF** -Disable the specified DC source in multi-dimensional sweep. **1 - ON** \- Enable the specified DC source in multi-dimensional sweep.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  md.DCState ("AO1") = OFF  'Write  
value = md.DCState("MyDCSource,Port 1") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_DCState (BSTR name, VARIANT_BOOL value); HRESULT get_DCState
(BSTR name, VARIANT_BOOL* value);  
  
#### Interface

|  IMultiDimensionalSweep  
  
* * *

