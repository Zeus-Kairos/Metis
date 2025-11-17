##### Write-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# SetBSSPorts Method

* * *

#### Description

| For a Balanced-Single-ended \- Single-ended device type, maps the VNA ports
to the DUT ports. Set the Balanced-Single-ended \- Single-ended device type
using the [DUTTopology Property](../Properties/DUTTopology_Property.md)  
---|---  
  
####  VB Syntax

| balTopology.SetBSSPorts balanced_Pos, balanced_Neg, singleEnded1,
singleEnded2  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology | A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
balanced_Pos, balanced_Neg, singleEnded1, singleEnded2 | VNA port number that connects to each of the DUT ports:  
  
#### Return Type

| Not applicable - To read port mappings, use the
[BalancedTopology](../Objects/BalancedTopology_Object.md) properties.  
  
#### Default

| Not Applicable  
  
#### Examples

| balTop.SetBSSPorts 1,2,3,4  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT SetBSPorts (long balanced_Pos, long balanced_Neg, long singleEnded1,
long singleEnded2)  
  
#### Interface

| IBalancedTopology4  
  
* * *

