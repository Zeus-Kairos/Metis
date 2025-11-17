##### Write/Read

|

##### [About Power Limit](../../../System/Power_Limit_and_Power_Offset.md)  
  
---|---  
  
## State (GPL) Property

* * *

#### Description

|  Enables and disables Global Power Limiting for the specified port.  
---|---  
  
####  VB Syntax

|  gpl.State(port) = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gpl |  A [GlobalPowerLimit](../Objects/GlobalPowerLimit_Object.md) (object)  
port |  (Long) Port number for which power limit state is to be set.  
bool |  (Boolean) Choose from: True \- Power Limiting is enabled. False \- Power Limiting is disabled.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gpl.State(1) = True 'Write  
Limit = gpl.State(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_State(long port, VARIANT_BOOL *pVal)  
HRESULT put_Limit(long port, VARIANT_BOOL newVal)  
  
#### Interface

|  IGlobalPowerLimit  
  
* * *

