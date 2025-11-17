##### Write/Read

|

##### [About Distance MarkerSettings](../../../Time/TimeDomain.md#Distance)  
  
---|---  
  
## DistanceMarkerMode Property

* * *

#### Description

|  Specifies the measurement type in order to determine the correct marker
distance.

  * Select Auto for S-Parameter measurements.
  * Select Reflection or Transmission for arbitrary ratio or unratioed measurements.

This settings affects the display of ALL markers for only the ACTIVE
measurement.  
---|---  
  
####  VB Syntax

|  trans.DistanceMarkerMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A [Transform](../Objects/Transform_Object.md) (object)  
value |  (enum As NADistanceMarkerMode) \- Choose from: 0 - naDistanceMarkerModeAuto 1 - naDistanceMarkerModeReflection 2 - naDistanceMarkerModeTransmission  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naDistanceMarkerModeAuto  
  
#### Examples

|  trans.DistanceMarkerMode = naDistanceMarkerModeReflection 'Write  
DMM = trans.DistanceMarkerMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DistanceMarkerMode(tagNADistanceMarkerMode *pVal); HRESULT
put_DistanceMarkerMode(tagNADistanceMarkerMode newVal);  
  
#### Interface

|  ITransform2

