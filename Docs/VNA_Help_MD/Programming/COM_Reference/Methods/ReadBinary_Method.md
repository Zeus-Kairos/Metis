##### Read-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# ReadBinary Method

* * *

#### Description

|  Returns data from the VISA pass-through device as a Safe Array of variants.
Note that binary data transfers over sockets are not supported.  
---|---  
  
#### VB Syntax

|  value = Vpassthru.ReadBinary (visaID)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (variant) \- Variable to store the returned data.  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### Return Type

|  Safe Array of variants  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value=Vpassthru.ReadBinary(1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ReadBinary(long session_num)  
  
#### Interface

|  IVISAPassthrough

