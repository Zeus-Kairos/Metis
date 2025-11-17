##### Read-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# GetVISATimeout Method

* * *

#### Description

|  Returns the timeout value (in milliseconds) for pass-through commands for
the specified VISA session.  
---|---  
  
#### VB Syntax

|  value = Vpassthru.GetVISATimeout (visaID)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (long) \- Variable to store the returned value of the timeout.  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) \- VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
Examples |  value=Vpassthru.GetVISATimeout(2)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetVISATimeout(long session_num)  
  
#### Interface

|  IVISAPassthrough

