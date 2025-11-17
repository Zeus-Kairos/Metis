##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
# ReadDCAtCompression Property

* * *

#### Description

|  Set and read the DC readings at the compression point in the last iteration
of a smart sweep. Taking only these DC readings improves measurement speed.  
---|---  
  
####  VB Syntax

|  gca.ReadDCAtCompression = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Boolean)  Choose from: True Enable reading DC value at compression point in the last iteration of a smart sweep. False Disable reading DC value at compression point in the last iteration of a smart sweep.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gca.ReadDCAtCompression = True 'Write  
enable = gca.ReadDCAtCompression 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReadDCAtCompression(VARIANT_BOOL* enable) HRESULT
put_ReadDCAtCompression(VARIANT_BOOL enable)  
  
#### Interface

|  IGainCompression5  
  
* * *

