##### Read-only

|

##### [About LXI](../../../S0_Start/LXI_Compliance.md)  
  
---|---  
  
# LANConfiguration Property

* * *

#### Description

|  Returns information about the current status of the VNAs computer
networking configuration. This is the same set of information that is returned
in an NA_IPConfiguration data structure by the GetIPConfigurationStruct
method.  
---|---  
  
####  VB Syntax

|  value = app.LANConfiguration  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (String) Variable to contain the VNAs LAN configuration string  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  Comma-delimited string  
  
#### Default

|  Not Applicable  
  
#### Examples

|  networkConfigInfo = app.LANConfiguration  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LANConfiguration (BSTR * pStrConfig);  
  
#### Interface

|  IApplication13  
  
* * *

