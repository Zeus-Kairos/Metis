##### Write/Read

|

##### [About SMC
CalTypes](../../../FreqOffset/SMC_Measurements.htm#SMCCalType)  
  
---|---  
  
## IncludeReverseSweep Property

* * *

#### Description

|  Sets whether to include SC12 sweeps during measurements.  
---|---  
  
####  VB Syntax

|  obj.IncludeReverseSweep = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter](../Objects/Converter_Object.md) (object)  
bool |  (Boolean) - True \- Include the SC12 (reverse) sweep. False \- Do NOT Include the SC12 (reverse) sweep.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  obj.IncludeReverseSweep = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IncludeReverseSweep(VARIANT_BOOL * val); HRESULT
put_IncludeReverseSweep(VARIANT_BOOL val);  
  
#### Interface

|  IMixer12  
  
* * *

