##### Write-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## SetSSBPorts Method

* * *

#### Description

|  For a Single-ended - Single-ended - Balanced device type, maps the VNA
ports to the DUT ports. Set the Single-ended - Single-ended - Balanced device
type using the [DUTTopology Property](../Properties/DUTTopology_Property.md)  
---|---  
  
####  VB Syntax

|  balTopology.SetSSBPorts se, se2, bPos, bNeg  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology |  A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
se, se2, bPos, bNeg |  VNA port number that connects to each of the following DUT ports: ![](../../../assets/images/Programming/SSBalTopMap.gif)  
  
#### Return Type

|  Not applicable - To read port mappings, use the
[BalancedTopology](../Objects/BalancedTopology_Object.md) properties.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  balTop.SetSSBPorts 1,2,3,4  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetSSBPorts (long se, long se2, long bPos, long bNeg)  
  
#### Interface

|  IBalancedTopology

