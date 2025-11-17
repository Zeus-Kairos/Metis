##### Write-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# SetVISATimeout Method

* * *

#### Description

|  Sets the timeout value (in milliseconds) for subsequent pass-through
commands for the specified VISA session.  
---|---  
  
#### VB Syntax

|  Vpassthru.SetVISATimeout visaID, timeoutVal  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### timeoutVal

|  (long) Timeout value for the specified session identification number that
is used when communicating with this device.  
  
#### Default

|  2000  
Examples |  Vpassthru.SetVISATimeout 2,6000  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetVISATimeout(long session_num, long timeout)  
  
#### Interface

|  IVISAPassthrough

