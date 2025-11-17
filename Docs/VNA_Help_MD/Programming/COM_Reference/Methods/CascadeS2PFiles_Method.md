#### Write-only

|

##### [About Cal Plane Manager](../../../S3_Cals/Cal_Plane_Manager.md)  
  
---|---  
  
## CascadeS2PFiles Method

* * *

#### Description

| Combines the losses and phase shift of two S2P files into a single S2P file.
[Learn more](../../../S3_Cals/Cal_Plane_Manager.md#Cascade).  
---|---  
  
#### VB Syntax

| calmgr.CascadeS2PFiles (s2p1, s2p2, s2pResult, format)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr | [Cal Manager](../Objects/CalManager_Object.md) (Object)  
s2p1 | (String)  Path and filename of one of the S2P files to be combined.  
s2p2 | (String) Path and filename of the other S2P file to be combined.  
s2pResult | (String) Path and filename of the combined S2P file.  
format | (Enum as NAPairedDataFormat) Format in which the data is to be saved to the combined S2P file. Choose from: 0 - naLogMagPhase 1 - naLinMagPhase 2 \- naRealImaginary  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| CalManager.CascadeS2PFiles C:\Users\PNA-ADMIN\AppData\Local\Keysight\Network
Analyzer\CPM\a.s2p","C:\Users\PNA-ADMIN\AppData\Local\Keysight\Network
Analyzer\CPM\b.s2p","C:\Users\PNA-ADMIN\AppData\Local\Keysight\Network
Analyzer\CPM\c.s2p",1  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT CascadeS2PFiles(BSTR s2p1, BSTR s2p2, BSTR s2pCombo,
tagNAPairedDataFormat format);  
  
#### Interface

| ICalManager10  
  
* * *

