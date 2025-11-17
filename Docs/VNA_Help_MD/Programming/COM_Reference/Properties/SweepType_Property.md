##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# SweepType Property

* * *

#### Description

| Set and read the sweep type.  
---|---  
  
####  VB Syntax

| HotS22.SweepType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 | A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
value | (Enum as NAHOTSweepType) - Choose from:

  * 0 - naHOTS22LinearFrencySweep Frequency linear sweep.
  * 1 - naHOTS22LogFrencySweep  Frequency log sweep.
  * 2 - naHOTS22PowerSweep  Power sweep.
  * 3 - naHOTS22MultiSweep  Multiple sweep. Sweeps frequency with fixed power and has several sweeps with different power values. This is called a 3D sweep: frequency, power, and phase.

  
  
#### Return Type

| Enum  
  
#### Default

| 0  
  
#### Examples

| HotS22.SweepType = naHOTS22LinearFrencySweep 'Write  
value = HotS22.SweepType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SweepType(tagNAHOTSweepType* value)  
HRESULT put_SweepType(tagNAHOTSweepType value)  
  
#### Interface

| IActiveChannelSettings  
  
* * *

