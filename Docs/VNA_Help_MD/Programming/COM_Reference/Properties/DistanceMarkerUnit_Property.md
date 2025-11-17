##### Write/Read

|

##### [About Distance MarkerSettings](../../../Time/TimeDomain.md#Distance)  
  
---|---  
  
## DistanceMarkerUnit Property

* * *

#### Description

|  Specifies the unit of measure for the display of marker distance values.
This settings affects the display of ALL markers for only the ACTIVE
measurement (unless Distance Maker Units are coupled using [CoupledParameters
Property](CoupledParameters_Transform_Property.htm).  
---|---  
  
####  VB Syntax

|  trans.DistanceMarkerUnit = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A [Transform](../Objects/Transform_Object.md) (object)  
value |  (Enum As NADistanceMarkerUnit) \- Distance Marker Units. Choose from 0 - naDistanceMarkerUnitMeter 1 - naDistanceMarkerUnitFeet 2 - naDistanceMarkerUnitInch  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naDistanceMarkerUnitMeter  
  
#### Examples

|  trans.DistanceMarkerUnit = naDistanceMarkerUnitFeet 'sets the  
U = trans.DistanceMarkerUnit 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DistanceMarkerUnit(tagNADistanceMarkerUnit *pVal); HRESULT
put_DistanceMarkerUnit(tagNADistanceMarkerUnit newVal);  
  
#### Interface

|  ITransform2

