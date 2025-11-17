##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## CompressionInterpolation Property

* * *

#### Description

|  Sets whether or not interpolation should be performed on 2D measured
compression data. Applies ONLY to [2D acquisition
modes](AcquisitionMode_Property.htm).  
---|---  
  
####  VB Syntax

|  gca.CompressionInterpolation = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (boolean) - Choose from: True Interpolate the results False Do NOT interpolate the results but return the value closest to compression.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gca.CompressionInterpolation = True 'Write  
compInt = gca.CompressionInterpolation 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionInterpolation(VARIANT_BOOL* pVal) HRESULT
put_CompressionInterpolation(VARIANT_BOOL newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

