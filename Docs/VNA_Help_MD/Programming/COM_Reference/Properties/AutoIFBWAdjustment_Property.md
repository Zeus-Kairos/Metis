##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## AutoIFBWAdjustment Property

* * *

#### Description

|  Set and read auto IFBW adjustment ON | OFF state for Gain Compression measurements.  
---|---  
  
####  VB Syntax

|  gca.AutoIFBWAdjustment = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Boolean) - Auto IFBW adjustment state. Choose from: False \- Sets auto IFBW adjustment OFF True - Sets auto IFBW adjustment ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  ON  
  
#### Examples

|  gca.AutoIFBWAdjustment = True 'Write  
aifbw = gca.AutoIFBWAdjustment 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoIFBWAdjustment(VARIANT_BOOL* bState) HRESULT
put_AutoIFBWAdjustment(VARIANT_BOOL bState)  
  
#### Interface

|  IGainCompression  
  
* * *

