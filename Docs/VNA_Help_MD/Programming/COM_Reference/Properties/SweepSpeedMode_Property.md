##### Write/Read

|

##### [About Fast Sweep](../../../S1_Settings/Sweep.md#SweepSetupDiag)  
  
---|---  
  
## SweepSpeedMode Property

* * *

#### Description

|  Sets and returns the sweep speed mode: FastSweep or Normal.  
---|---  
  
####  VB Syntax

|  chan.SweepSpeedMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
value |  (enum as NASweepSpeedMode) \- Choose from: 0 - naSweepSpeedModeNormal \- Standard VNA sweep mode 1 - naSweepSpeedModeFast \- Fast sweep mode  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naSweepSpeedModeNormal  
  
#### Examples

|  chan.SweepSpeedMode = naSweepSpeedModeNormal 'Write  
swpSpeed = chan.SweepSpeedMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SweepSpeedMode(tagNASweepSpeedModes* pVal)  
HRESULT put_SweepSpeedMode(tagNASweepSpeedModes newVal)  
  
#### Interface

|  IChannel14  
  
* * *

