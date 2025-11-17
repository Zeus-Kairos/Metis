##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# DisplayInputPower Property

* * *

#### Description

| Set and read a fixed trace input power level.  
---|---  
  
####  VB Syntax

| HotS22.DisplayInputPower = level  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 | A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
level | (Double) \- Input power level. Choose a value from start power to stop power.  
  
#### Return Type

| Double  
  
#### Default

| Start power in a power sweep  
  
#### Examples

| HotS22.DisplayInputPower = 0 'Write  
level = HotS22.DisplayInputPower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DisplayInputPower(double* level) HRESULT
put_DisplayInputPower(double level)  
  
#### Interface

| IActiveChannelSettings  
  
* * *

