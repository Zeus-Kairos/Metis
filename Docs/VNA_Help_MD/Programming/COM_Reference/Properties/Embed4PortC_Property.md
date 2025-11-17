##### Read-only

|

##### About Fixturing  
  
---|---  
  
## Embed4PortC Property

* * *

#### Description

|  Returns the VNA port number associated with 'c' based on the device
topology. To see 'c' for all topologies, and to specify the port connections,
use [Embed4PortList Property](Embed4PortList_Property.md). Specify topology
using [Embed4PortTopology Property](Embed4PortTopology_Property.md)  
---|---  
  
####  VB Syntax

|  value = fixture.Embed4PortC  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Short Integer) Variable to store the returned VNA port number.  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
  
#### Return Type

|  Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = fixture.Embed4PortC 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Embed4PortC(short *portC );  
  
#### Interface

|  IFixturing2

