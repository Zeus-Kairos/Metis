##### Write/Read

|

##### [About Power Limit](../../../System/Power_Limit_and_Power_Offset.md)  
  
---|---  
  
## Limit Property

* * *

#### Description

|  Sets and returns the power limit for the specified port.  
---|---  
  
####  VB Syntax

|  gpl.Limit (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gpl |  A [GlobalPowerLimit](../Objects/GlobalPowerLimit_Object.md) (object)  
port |  (Long) Port number for which power limit value is to be set.  
value |  (Double) Power limit value. Choose a value between -27 dBm (approximately) and the max settable power for the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  100 dBm for all ports  
  
#### Examples

|  gpl.Limit(1) = 0 'Write  
Limit = gpl.Limit(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Limit(long port, double *pVal)  
HRESULT put_Limit(long port, double newVal)  
  
#### Interface

|  IGlobalPowerLimit  
  
* * *

