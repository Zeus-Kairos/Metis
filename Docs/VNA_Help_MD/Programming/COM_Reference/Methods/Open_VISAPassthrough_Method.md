##### Write/Read

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# Open Method

* * *

#### Description

|  Initiates a VISA pass-through session for a device, and returns a unique
session ID to be used whenever communicating with that device. Pass-through
sessions can be closed by using the [Close](Close_VISAPassthrough_Method.md)
method, the [Reset](Reset_VISAPassthrough_Method.md) method, or by properly
shutting down the instrument or the analyzer application. Presetting the
instrument will not close existing pass-through sessions. Note: **When opening
a socket session (addresses of type: TCPIP[board]::host
address::port::SOCKET) , you must use the appropriate VISA Address for the
identifier argument. Using an alias to open a socket session is not currently
supported. Aliases are allowed for all other types of supported sessions.**  
---|---  
  
#### VB Syntax

|  value = Vpassthru.Open (identifier, timeoutVal)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (long) \- Variable to store the returned session ID.  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### identifier

|  (string) VISA address, or VISA alias of the device to be controlled.  
  
#### timeoutVal

|  (long) The amount of time (in milliseconds) to wait for a response from the
remote device after sending a command. A "timeout" error is displayed after
this time has passed without a response.  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
Examples |  value=Vpassthru.Open("TCPIP0::A-N5242A-10096::hislip1::INSTR",1000) value=Vpassthru.Open("MyAlias",5000)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Open(BSTR visaIdentifier, long timeOut, long* sessionID)  
  
#### Interface

|  IVISAPassthrough

