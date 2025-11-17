##### Write-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# Close Method

* * *

#### Description

|  Closes the specified remote VISA session. VISA sessions should always be
closed when you are finished communicating with the remote device. Use this
command to close (end) each VISA session that was opened successfully using
the [Open](Open_VISAPassthrough_Method.md) method. If you have more than one
open session, and need to close them all at the same time, it may be faster
and easier to use the [Reset](Reset_VISAPassthrough_Method.md) method.  
---|---  
  
#### VB Syntax

|  Vpassthru.Close visaID  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Vpassthru.Close 2  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Close(long session_num)  
  
#### Interface

|  IVISAPassthrough

