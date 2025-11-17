##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## DUTTopology Property

* * *

#### Description

| Sets and returns the device type for the balanced measurement. To map the
device type logical ports to the VNA physical ports, use the
[SetCustomDUTTopology](../Methods/SetCustomDUTTopology_Method.md) command.  
---|---  
  
####  VB Syntax

| balTopology.DUTTopology = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balTopology | A [BalancedTopology](../Objects/BalancedTopology_Object.md) (object)  
value | (enum NADUTTopology) \- Choose either: 0 naSEBal: Single-Ended - Balanced topology 1 naSESEBal: Single-Ended - Single-Ended - Balanced topology 2 naBalBal: Balanced - Balanced topology 3 naBalSE: Balanced - Single-ended topology 4 naBal: Singe ended balanced 5 naCustom: Custom 6 naBalSESE: Balanced - Single-ended - Single-ended topology  
  
#### Return Type

| Enum as NADUTTopology  
  
#### Default

| naSEBal  
  
#### Examples

| balTop.DUTTopology = naSESEBal 'Write  
DutTop = balTop.DUTTopology 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DUTTopology(tagNADUTTopology* pVal)  
HRESULT put_DUTTopology(tagNADUTTopology newVal)  
  
#### Interface

| IBalancedTopology  
  
* * *

