##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## Embed4PortTopology Property

* * *

#### Description

|  Specifies the VNA / DUT topology. Learn more about these and other VNA/DUT
configurations.  
---|---  
  
####  VB Syntax

|  fixture.Embed4PortTopology = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
value |  (Enum as NA4PortEmbedTopology) VNA / DUT topology. Choose from: 0 or naTOPOLOGY_A \- 2 VNA/DUT Ports 1 or naTOPOLOGY_B \- 3 VNA/DUT Ports 2 or naTOPOLOGY_C \- 4 VNA/DUT Ports 3 or naTOPOLOGY_D \- >4 VNA/DUT Ports  
  
#### Return Type

|  Enum  
  
#### Default

|  naTOPOLOGY_A (2 VNA/DUT Ports)  
  
#### Examples

|  fixture.Embed4PortTopology = naTOPOLOGY_A 'Write  
value = fixture.Embed4PortTopology 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Embed4PortTopology( tagNA4PortEmbedTopology *eVal );  
HRESULT put_Embed4PortTopology( tagNA4PortEmbedTopology eVal );  
  
#### Interface

|  IFixturing2

