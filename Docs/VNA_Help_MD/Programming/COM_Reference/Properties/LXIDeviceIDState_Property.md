##### Write/Read

|

##### [About LXI](../../../S0_Start/LXI_Compliance.md)  
  
---|---  
  
## LXIDeviceIDState Property

* * *

#### Description

|  Opens and closes the [LAN Status
dialog](../../../S0_Start/LXI_Compliance.htm#LAN) with the LAN Status
Indicator showing IDENTIFY. The VNA supports this capability to satisfy a
requirement of the LAN eXtensions for Instrumentation (LXI) standard. Changing
the value of this property is the same operation that occurs when clicking the
Toggle LXI Identification button on the Welcome web page presented by the VNA
web server.  
---|---  
  
####  VB Syntax

|  app.LXIDeviceIDState = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### bool

|  (boolean) Choose from: True \- Displays the [LAN Status
dialog](../../../S0_Start/LXI_Compliance.htm#LAN) with the Status Indicator
showing IDENTIFY.  False -

  * If the dialog had been opened by this property, then the LAN Status dialog is closed.
  * If the dialog was opened manually, then it will stay open.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  app.LXIDeviceIDState = True 'Write value = app.LXIDeviceIDState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LXIDeviceIDState( VARIANT_BOOL* pState); HRESULT
put_LXIDeviceIDState( VARIANT_BOOL state);  
  
#### Interface

|  IApplication14  
  
* * *

