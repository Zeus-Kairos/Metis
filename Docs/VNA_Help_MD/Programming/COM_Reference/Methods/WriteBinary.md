##### Write-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# WriteBinary Method

* * *

#### Description

|  Sends binary data to the VISA pass-through device. Note that binary data
transfers over sockets are not supported.  
---|---  
  
#### VB Syntax

|  Vpassthru.WriteBinary visaID, bin_data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### bin_data

|  (variant) Data to be sent to the VISA pass-through device.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Vpassthru.WriteBinary 2,"*IDN?"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT WriteBinary(long session_num, variant bin_data)  
  
#### Interface

|  IVISAPassthrough

