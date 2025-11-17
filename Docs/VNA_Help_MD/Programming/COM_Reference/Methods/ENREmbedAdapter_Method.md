##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## ENREmbedAdapter Method

* * *

#### Description

|  Generate a new ENR file by embedding an adapter to an existing ENR file.  
---|---  
  
####  VB Syntax

|  calMgr.ENREmbedAdapter (inENR, s2p, outEnr)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
inENR |  (String) Path and filename of an existing ENR file  
s2p |  (String) Path and filename of an s2p file of adapter.  
outENR |  (String) Path and filename of an ENR file to output  
  
#### Return Type

|  ICal Set Interface  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.ENREmbedApater (D:\Original.enr","D:\adapter.s2p","D:\new.enr")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ENREmbedAdapter (BSTR inEnr, BSTR s2p, BSTR outEnr);  
  
#### Interface

|  ICalManager11

