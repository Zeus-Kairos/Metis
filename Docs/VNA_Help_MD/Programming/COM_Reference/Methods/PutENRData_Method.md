##### Write-only

|

##### [About ENR tables](../../../Applications/Noise_Cal.md#ENRFiles)  
  
---|---  
  
## PutENRData Method

* * *

#### Description

|  Write ENR calibration data to VNA memory. All of the frequency and ENR data
must be sent at the same time.  
---|---  
  
####  VB Syntax

|  enr.PutENRData (vData)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
enr |  An [ENRFile](../Objects/ENRFile_Object.md) (object)  
vData |  (Variant array) -ENR data. Frequency value in Hz, followed by corresponding ENR value in dB. Enter as many data pairs as necessary.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See example
program](../../COM_Example_Programs/ENR_File_Management_Example.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT PutENRData(VARIANT vdata);  
  
#### Interface

|  IENRFile  
  
* * *

