##### Write-only

|

##### [About the ExtTestSetIO connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## WriteData Method

* * *

#### Description

|  Writes a 13-bit value to the specified address using the AD0 through AD12
lines of the external test set connector. The VNA generates the appropriate
timing signals. It automatically controls timing signals LDS, LAS and RLW to
strobe the address, then the data, to the external test set. See the [timing
diagram](../../TestSetIO_Connector.htm#AD0-AD12) for Address and Data I/O
read.  
---|---  
  
####  VB Syntax

|  ExtIO.WriteData address, value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ExtIO |  (object) - An [External IO object](../Objects/HWExternalTestSetIO_Object.md)  
address |  (variant) \- Address to be written to.  
value |  (variant) \- 13-bit word to write  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ExtIO.WriteData 15,12  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT WriteData(VARIANT Address, VARIANT Data);  
  
#### Interface

|  IHWExternaTestSetIO  
  
* * *

