##### Write-only

|

##### [About LXI](../../../S0_Start/LXI_Compliance.md)  
  
---|---  
  
## SetIPConfiguration Method

* * *

#### Description

|  Modifies settings of the VNA computer networking configuration.  
---|---  
  
####  VB Syntax

|  app.SetIPConfiguration AutoIPAddress, DNSServer1, DNSServer2, HostName,
DomainName, IPAddress, SubNet, Gateway, DNSSuffix1, DNSSuffix2 or retStr =
app.SetIPConfiguration (AutoIPAddress, DNSServer1, DNSServer2, HostName,
DomainName, IPAddress, SubNet, Gateway, DNSSuffix1, DNSSuffix2)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
AutoIPAddress |  (boolean) -Choose either: True \- VNA is assigned an IP address by a DHCP server, or will use AutoIP (Dynamic Link-Local Addressing) if DHCP server not found. False  VNA will use the static IP address value specified by IPAddress.  
DNSServer1 |  (string) IP address of primary DNS server. When AutoIPAddress = True and an empty string is specified for DNSServer1, the VNA will attempt to obtain the addresses of primary and secondary DNS servers automatically.  When AutoIPAddress = False, an IP address must be specified for DNSServer1 and/or DNSServer2 or else the VNAs host name will not be resolvable on the computer network.  
DNSServer2 |  (string) IP address of secondary DNS server. When specifying an empty string for DNSServer1, then specify an empty string here also.  
HostName |  (string) DNS host name (computer name) to be assigned to this VNA. Note: If specifying a name different than the VNAs current host name, the change will not take effect until after you reboot the VNA.  
DomainName |  (string) DNS domain name associated with this VNA.  
IPAddress |  (string) Static IP address to assign to this VNA when AutoIPAddress = False. When AutoIPAddress = True, the value of IPAddress is ignored.  
SubNet |  (string) Subnet mask value to assign to the VNA network configuration.  
Gateway |  (string) Gateway address to assign to the VNA network configuration.  
DNSSuffix1 |  (string) Primary suffix to set in the VNA DNS suffix search order. An empty string is allowed.  
DNSSuffix2 |  (string) Secondary suffix to set in the VNA DNS suffix search order. An empty string is allowed.  
retStr |  (string) String returned by this method should be ignored. It is intended for Keysight diagnostic use.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.SetIPConfiguration True, , , MyHostName,
MyRegion.MyCompany.com, , 255.255.255.0, 123.45.67.890, , 
app.SetIPConfiguration False, 123.456.78.90, 234.56.78.901, MyHostName,
MyRegion.MyCompany.com, 123.456.789.0, 255.255.255.0, 123.45.67.890,
MyCompany.com,   
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetIPConfiguration(VARIANT_BOOL AutoIPAddress, BSTR DNSServer1,
BSTR DNSServer2, BSTR HostName, BSTR DomainName, BSTR IPAddress, BSTR SubNet,
BSTR Gateway, BSTR DNSSuffix1, BSTR DNSSuffix2, BSTR *pRetStr);  
  
#### Interface

|  IApplication14  
  
* * *

