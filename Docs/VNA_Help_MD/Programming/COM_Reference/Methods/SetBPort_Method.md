##### Write-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# SetBPort Method

* * *

#### Description

|  For a single port balanced device type, maps the VNA ports to the DUT
ports. Set the Balanced device type using the [DUTTopology
Property](../Properties/DUTTopology_Property.htm)  
---|---  
  
####  VB Syntax

|  balTopology.SetBPort balanced_pos, balanced_neg  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
balanced_pos, balanced_neg |  (Long Integer) VNA port number that connects to each of the following DUT ports: ![](../../../assets/images/Balanced_SetBPort.GIF)  
  
#### Return Type

|  Not applicable - To read port mappings, use the
[BalancedTopology](../Objects/BalancedTopology_Object.md) properties.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  balTopology.SetBPort 1,2  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetBPort(long Pos, long Neg)  
  
#### Interface

|  IBalancedTopology3

