##### Write-only

|

##### About 4-Port Fixturing  
  
---|---  
  
## NetworkPortMap Method

* * *

#### Description

|  Set the port mapping for a 4-port SNP file to be embedded. To read port
mapping, use [NetworkPortMapA](../Properties/NetworkPortMapA_Property.md),
[NetworkPortMapB](../Properties/NetworkPortMapB_Property.md),
[NetworkPortMapC](../Properties/NetworkPortMapC_Property.md),
[NetworkPortMapD](../Properties/NetworkPortMapD_Property.md).  
---|---  
  
####  VB Syntax

|  fixture.NetworkPortMap network, inA, inB, outA, outB  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
network |  Network position. Choose from 1 or 2.  
inA, inB, outA, outB |  Port Mapping. Use four port numbers in any order.  
  
#### Return Type

|  Not Applicable.  
  
#### Default

|  1,2,3,4  
  
#### Examples

|  fixture.NetworkPortMap 1,1,3,2,4  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT NetworkPortMap(short Net, *Long inA, *Long inB,* Long outA,* Long
outB,)  
  
#### Interface

|  IFixturing6  
  
* * *

