##### Read-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# ReadBinaryCompact Method

* * *

#### Description

|  Reads binary data the same as the [ReadBinary](ReadBinary_Method.md)
method, but returns the data in a more compact form of Safe Array. This is
significantly faster but is not supported in all client environments. Note
that binary data transfers over sockets are not supported.  
---|---  
  
#### VB Syntax

|  value = Vpassthru.ReadBinaryCompact (visaID)  
  
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

|  value=Vpassthru.ReadBinaryCompact(1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ReadBinaryCompact(long session_num)  
  
#### Interface

|  IVISAPassthrough

