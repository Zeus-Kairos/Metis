##### Write/Read

|

##### [About Electrical Delay](../../../S2_Opt/Phase_Accy.md#ed)  
  
---|---  
  
## ElecDistanceDelayUnit Property

* * *

#### Description

|  Sets and returns the units for specifying electrical delay in physical
length (distance).  
---|---  
  
####  VB Syntax

|  meas.ElecDistanceDelayUnit = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (enum naDistanceUnit) Choose from: 0  naDistanceUnit_Meter 1  naDistanceUnit_Feet 2  naDistanceUnit_Inch  
  
#### Return Type

|  Enum  
  
#### Default

|  0  naDistanceUnit_Meter  
  
#### Examples

|  meas.ElecDistanceDelayUnit = naDistanceUnit_Meter 'Write  
edelay = meas.ElecDistanceDelayUnit 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ElecDistanceDelayUnit(tagNADistanceUnit *pVal)  
HRESULT put_ElecDistanceDelayUnit(tagNADistanceUnit newVal)  
  
#### Interface

|  IMeasurement11  
  
* * *

