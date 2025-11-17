##### Write-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# WriteString Method

* * *

#### Description

|  Sends ASCII string data to the VISA pass-through device.  
---|---  
  
#### VB Syntax

|  Vpassthru.WriteString visaID, text  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### text

|  (string) Text to be sent to the VISA pass-through device (usually a
command).  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Vpassthru.WriteString 2,"*IDN?"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT WriteString(long session_num, string text)  
  
#### Interface

|  IVISAPassthrough

