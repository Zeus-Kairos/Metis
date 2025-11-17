##### Read-Write

|

##### [About FCA
embed/deembed](../../../FreqOffset/VMC_Measurements.htm#Waveguide)  
  
---|---  
  
## NetworkFilename Property

* * *

#### Description

|  Specifies the S2P filename to embed or de-embed on the input or output of
your mixer measurement.  
---|---  
  
#### VB Syntax

|  object.NetworkFilename(n) = filename  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [SMCType](../Objects/SMC_Type_Object.md) (object) or [VMCType](../Objects/VMC_Type_Object.md) (object)  
n |  (Integer) Apply network to input or output of mixer. Choose from: 1 \- Input of mixer 2 \- Output of mixer  
filename |  (String) Filename of the S2P used for embedding or de-embedding. Use the full path name, file name, and .S2P suffix, enclosed in quotes.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  VMC.Filename(2) = "D:\WaveguideAdapt.S2P"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_NetworkFilename(short networkNum, BSTR filename); HRESULT
get_NetworkFilename(short networkNum, BSTR *filename);  
  
#### Interface

|  SMCType2 VMCType2  
  
* * *

