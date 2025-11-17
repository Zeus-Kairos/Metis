##### Read-only

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# BSS_SEPort2 Property

* * *

#### Description

| With a Balanced \- Single-ended - Single-ended topology, returns the VNA
port number that is connected to the Single-ended port 2. Use [SetBSSPorts
Method](../Methods/SetBSSPorts_Method.htm) to set the port mapping for a
Balanced - Single-ended \- Single-ended topology.  
---|---  
  
####  VB Syntax

| var = balTopology.BSS_SEPort2  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
var | (Long Integer) Variable to store the returned value.  
balTopology | A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
  
#### Return Type

| Long Integer  
  
#### Default

| Not Applicable  
  
#### Examples

| variable = balTop.BSS_SEPort2 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BSS_SEPort2(long *pSEPort2)  
  
#### Interface

| IBalancedTopology4  
  
* * *

