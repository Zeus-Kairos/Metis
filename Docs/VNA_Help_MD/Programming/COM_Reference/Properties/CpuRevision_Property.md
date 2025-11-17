##### Read only

|

##### [About Help, About VNA](../../../S0_Start/HelpAbout.md)  
  
---|---  
  
## CpuRevision Property

* * *

#### Description

| Returns a number that corresponds to the CPU speed of the VNA.  
---|---  
  
####  VB Syntax

| value = cap.CpuRevision  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value | (String) - Variable to store the returned number. Use the following table to learn the CPU speed. Reported CPU version - Clock speed 1.0 \- 266 MHz 2.0 \- 500 MHz 3.0 \- 1100 MHz 4.0 \- 1600 MHz 5.0 \- 2000 MHz 6.0 \- 2000 MHz dual core 7.0 \- 2200 MHz dual core  
cap | A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| value = cap.CpuRevision 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_CpuRevision(BSTR *value);  
  
#### Interface

| ICapabilities6  
  
* * *

  

