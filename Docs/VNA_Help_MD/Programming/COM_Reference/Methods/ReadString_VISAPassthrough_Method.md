##### Read-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# ReadString Method

* * *

#### Description

|  Returns data from the VISA pass-through device.  
---|---  
  
#### VB Syntax

|  value = Vpassthru.ReadString (visaID)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (string) \- Variable to store the returned string data.  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### visaID

|  (long) VISA session number (see [Open](Open_VISAPassthrough_Method.md)
method).  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value=Vpassthru.ReadString(1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ReadString(long session_num)  
  
#### Interface

|  IVISAPassthrough

