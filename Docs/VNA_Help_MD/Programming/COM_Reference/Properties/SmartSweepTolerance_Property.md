##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## SmartSweepTolerance Property

* * *

#### Description

|  Set and read the acceptable range SMART Sweep will allow for the measured
compression level.  
---|---  
  
####  VB Syntax

|  gca.SmartSweepTolerance = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (double) - Tolerance level in dB. Choose a value between .01 and 10  
  
#### Return Type

|  Double  
  
#### Default

|  .05  
  
#### Examples

|  gca.SmartSweepTolerance = .01 'Write  
tol = gca.SmartSweepTolerance 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SmartSweepTolerance(double* pVal) HRESULT
put_SmartSweepTolerance(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

