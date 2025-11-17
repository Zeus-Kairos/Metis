##### Write/Read

|

##### [About Electrical Delay](../../../S2_Opt/Phase_Accy.md#ed)  
  
---|---  
  
## ElecDistanceDelay Property

* * *

#### Description

|  Sets the electrical delay in physical length (distance) for the selected
measurement.  
---|---  
  
####  VB Syntax

|  meas.ElecDistanceDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (double) \- Electrical Delay in distance. Set units using [ElecDistanceDelayUnit](ElecDistanceDelayUnit_Property.md).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### VB Examples

|  meas.ElecDistanceDelay = 1e-3 'Write  
edelay = meas.ElecDistanceDelay 'Read  
  
#### C# Examples

|  Meas.ElecDistanceDelay = 1e-3 'Write // This property returns an object,
and the object must be cast to a double to access the value. Edelay =
(double)meas.ElecDistanceDelay 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ElecDistanceDelay(VARIANT *pVal)  
HRESULT put_ElecDistanceDelay(VARIANT newVal)  
  
#### Interface

|  IMeasurement11  
  
* * *

  

