##### Read-only

|

##### About 4-Port Fixturing  
  
---|---  
  
## NetworkPortMapD Property

* * *

#### Description

|  Read the port mapping of out B port for a 4-port SNP file to be embedded.
Use [NetworkPortMap Method](../Methods/NetworkPortMap_Method.md) to set the
port map for all four ports.  
---|---  
  
####  VB Syntax

|  value = fixture.NetworkPortMapD (network)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) Variable to store the returned value.  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
network |  (Integer) Network position. Choose from 1 or 2.  
  
#### Default

|  4  
  
#### Examples

|  value = fixture.NetworkPortMapD(1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NetworkPortMapD(short* Net);  
  
#### Interface

|  IFixturing6  
  
* * *

