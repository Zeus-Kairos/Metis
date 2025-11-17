##### Write/Read

|

##### [About Electrical Delay](../../../S2_Opt/Phase_Accy.md#ed)  
  
---|---  
  
## ElectricalDelay Property

* * *

#### Description

|  Sets the Electrical Delay for the active channel.  
---|---  
  
####  VB Syntax

|  meas.ElectricalDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (double) - Electrical Delay in seconds. Choose any number between -9.99 and 9.99  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  meas.ElectricalDelay = 1e-3 'Write  
edelay = meas.ElectricalDelay 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ElectricalDelay(double *pVal)  
HRESULT put_ElectricalDelay(double newVal)  
  
#### Interface

|  IMeasurement

