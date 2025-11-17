##### Write/Read

|

##### [About Power Slope](../../../S1_Settings/Power_Level.md#Power_Slope)  
  
---|---  
  
## PowerSlope Property

* * *

#### Description

|  Sets or returns the Power Slope value. Power Slope function increases or
decreases the output power over frequency. Units are db/GHz. For example:
PowerSlope = 2 will increase the power 2db/1GHZ.  
---|---  
  
####  VB Syntax

|  object.PowerSlope = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [Channel](../Objects/Channel_Object.md) (object) or [CalSet](../Objects/CalSet_Object.md) (object) - Read-only property  
value |  (double) - Power Slope. Choose any number between -2 and 2.  
No slope = 0  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  chan.PowerSlope = 2 'Write  
pwrslp = chan.PowerSlope 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSlope(double *pVal)  
HRESULT put_PowerSlope(double newVal)  
  
#### Interface

|  IChannel |CalSet3

