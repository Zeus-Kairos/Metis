##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
## SafeSweepFineThreshold Property

* * *

#### Description

|  Set and read the compression level at which Safe Sweep changes from the
COARSE power adjustment to the FINE power adjustment.  
---|---  
  
####  VB Syntax

|  gca.SafeSweepFineThreshold = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double)  Threshold setting in dBm. Choose a value from +30 to (-30).  
  
#### Return Type

|  Double  
  
#### Default

|  0.5 dBm  
  
#### Examples

|  gca.SafeSweepFineThreshold = 0.1 'Write  
SSThresh = gca.SafeSweepFineThreshold 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SafeSweepFineThreshold(double* value) HRESULT
put_SafeSweepFineThreshold(double value)  
  
#### Interface

|  IGainCompression  
  
* * *

