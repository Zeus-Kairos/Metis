##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## SmartSweepShowIterations Property

* * *

#### Description

|  Set and read whether to show intermediate results for each iteration in
SMART sweep.  
---|---  
  
####  VB Syntax

|  gca.SmartSweepShowIterations = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Boolean)  Choose from: True Compression traces are updated after each iteration. False Compression traces are updated after ALL iterations are complete.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gca.SmartSweepShowIterations = True 'Write  
SShow = gca.SmartSweepShowIterations 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SmartSweepShowIterations(VARIANT_BOOL *pVal) HRESULT
put_SmartSweepShowIterations(VARIANT_BOOL newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

