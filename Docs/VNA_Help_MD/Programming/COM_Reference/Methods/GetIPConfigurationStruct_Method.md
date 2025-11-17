##### Read-only

|

##### [About LXI](../../../S0_Start/LXI_Compliance.md)  
  
---|---  
  
## GetIPConfigurationStruct Method

* * *

#### Description

|  Returns an NA_IPConfiguration data structure which contains information
about the current status of the VNAs computer networking configuration. This
is the same set of information that is returned in a single string by the
[LANConfiguration](../Properties/LANConfiguration_Property.md) property.  
---|---  
  
####  VB Syntax

|  value = app.GetIPConfigurationStruct  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (NA_IPConfiguration) Variable to receive the VNA IP (LAN) configuration information.  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  NA_IPConfiguration  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim networkConfigInfo As NA_IPConfiguration  
networkConfigInfo = app.GetIPConfigurationStruct()  
  
MsgBox Host name =  & networkConfigInfo.HostName  
  
MsgBox Domain name =  & networkConfigInfo.DomainName  
  
MsgBox IP address =  & networkConfigInfo.IPAddress  
  
If Not networkConfigInfo.DHCPEnabled Then  
MsgBox IP address is static  
Else  
MsgBox IP address is dynamic  
End If  
  
MsgBox Subnet mask =  & networkConfigInfo.SubNet  
  
MsgBox Gateway =  & networkConfigInfo.DefaultGateway  
  
MsgBox Primary DNS server =  & networkConfigInfo.DNSServer1  
  
MsgBox Secondary DNS server =  & networkConfigInfo.DNSServer2  
  
MsgBox First suffix in DNS suffix search order =  &
networkConfigInfo.DNSSuffix1  
  
MsgBox Second suffix in DNS suffix search order =  &
networkConfigInfo.DNSSuffix2  
  
MsgBox Primary WINS server =  & networkConfigInfo.PrimaryWINSServer  
  
MsgBox Secondary WINS server =  & networkConfigInfo.SecondaryWINSServer  
  
MsgBox Network adapter device ID =  & networkConfigInfo.DeviceID  
  
MsgBox Description of network adapter =  & networkConfigInfo.Description  
  
MsgBox MAC address =  & networkConfigInfo.MacAddress  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetIPConfigurationStruct (tagNA_IPConfiguration * pIPConfig);  
  
#### Interface

|  IApplication14  
  
* * *

