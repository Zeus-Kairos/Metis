##### Write/Read

|

##### [About Power Limit](../../../System/Power_Limit_and_Power_Offset.md)  
  
---|---  
  
## Lock Property

* * *

#### Description

|  Enables or disables the ability to change the power limit values through
the user interface.  
---|---  
  
####  VB Syntax

|  gpl.Lock = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gpl |  A [GlobalPowerLimit](../Objects/GlobalPowerLimit_Object.md) (object)  
state |  (boolean) False \- Disables the ability to change the power limit values from the user interface. True - Enables the ability to change the power limit values from the user interface.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gpl.Lock = True 'Write  
UILock = gpl.Lock 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Lock(BOOL *pVal)  
HRESULT put_Lock(BOOL newVal)  
  
#### Interface

|  IGlobalPowerLimit  
  
* * *

