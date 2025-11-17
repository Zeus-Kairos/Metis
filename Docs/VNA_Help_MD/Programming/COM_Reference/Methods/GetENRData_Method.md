##### Read-only

|

##### [About ENR tables](../../../Applications/Noise_Cal.md#ENRFiles)  
  
---|---  
  
## GetENRData Method

* * *

#### Description

|  Read the ENR calibration data from VNA memory.  
---|---  
  
####  VB Syntax

|  vData = enr.GetENRData( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
vData |  Variable to store the returned ENR data. Frequency value in Hz, followed by corresponding ENR value in dB.  
enr |  An [ENRFile](../Objects/ENRFile_Object.md) (object)  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See example
program](../../COM_Example_Programs/ENR_File_Management_Example.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetENRData (VARIANT vdata);  
  
#### Interface

|  IENRFile  
  
* * *

