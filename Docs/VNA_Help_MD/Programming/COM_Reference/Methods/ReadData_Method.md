##### Read-only

|

##### [About the ExtTestSetIO connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## ReadData Method

* * *

#### Description

|  Reads a 13-bit data word from the specified address. Data is read using the
AD0 through AD12 lines of the external test set connector. The instrument
generates the appropriate timing signals. It automatically controls timing
signals LDS, LAS and RLW to strobe the address, and then read the data, from
the external test set. See the [timing
diagram](../../TestSetIO_Connector.htm#AD0-AD12) for Address and Data I/O
read.  
---|---  
  
####  VB Syntax

|  value = ExtIO.ReadData (address)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (variant) \- Variable to store the returned data  
ExtIO |  (object) - An ExternalTestSetIO object  
address |  (variant) \- address to read data from.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = ExtIO.ReadData (15)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ReadData (VARIANT Address, VARIANT* Data);  
  
#### Interface

|  IHWExternaTestSetIO

