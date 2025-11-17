##### Write/Read

|

##### [About Phase Offset](../../../S2_Opt/Phase_Accy.md#po)  
  
---|---  
  
## PhaseOffset Property

* * *

#### Description

|  Sets the Phase Offset for the active channel.  
---|---  
  
####  VB Syntax

|  meas.PhaseOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (double) - PhaseOffset in degrees. Choose any number between:  
-360 and +360  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  meas.PhaseOffset = 25 'Write  
poffset = meas.PhaseOffset 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseOffset(double *pVal)  
HRESULT put_PhaseOffset(double newVal)  
  
#### Interface

|  IMeasurement

