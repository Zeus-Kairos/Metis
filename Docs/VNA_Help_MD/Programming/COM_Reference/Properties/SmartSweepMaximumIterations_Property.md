##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## SmartSweepMaximumIterations Property

* * *

#### Description

|  Set and read the maximum permitted number of iterations which SMART Sweep
may utilize to find the desired compression level, to within the specified
tolerance.  
---|---  
  
####  VB Syntax

|  gca.SmartSweepMaximumIterations = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (integer) - Maximum number of iterations. Choose a value between 1 and 50.  
  
#### Return Type

|  Integer  
  
#### Default

|  20  
  
#### Examples

|  gca.SmartSweepMaximumIterations = 10 'Write  
iters = gca.SmartSweepMaximumIterations 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SmartSweepMaximumIterations(int* pVal) HRESULT
put_SmartSweepMaximumIterations(int newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

