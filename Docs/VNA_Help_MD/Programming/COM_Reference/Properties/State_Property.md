##### Write/Read  
  
---  
  
## State Property

* * *

#### Description

|  Turns an Object ON and OFF.  
---|---  
  
####  VB Syntax

|  object.State = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Applies to any of the following objects: [FOM](../Objects/FOM_Collection.md) [Gating](../Objects/Gating_Object.md) [InterfaceControl](../Objects/InterfaceControl_Object.md) [LimitTest](../Objects/Limit_Test_Collection.md) Port Extension- Superseded. See either:

  * [FixturingState Property](FixturingState_Property.md)
  * [PortExtState Property](PortExtState_Property.md)

[Segment](../Objects/Segment_Object.md) [Transform](../Objects/Transform_Object.md) [Equation](../Objects/MeasurementEquation_Object.md) [FIFO](../Objects/FIFO_Object.md) |  Notes:

  * LimitTest.State \- If using Global Pass/Fail status, trigger the VNA AFTER turning Limit testing ON.
  * Segment.State \- At least ONE segment must be ON or [Sweep Type](../../../S1_Settings/Sweep.md#SweepTypeDiag) is automatically set to Linear.

  
---  
value |  (boolean) - False \- Turns obj OFF True - Turns obj ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  Depends on the object: 0 - FOM 0 \- Gating 0 - InterfaceControl 0 \-
LimitTest 1 \- Segment 0 \- Transform 0 \- Equation 0 \- FIFO  
  
#### Examples

|  Seg.State = 1 'Turns the segment object ON -Write  
tran = Trans.State 'returns the state of Transform -Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_State(VARIANT_BOOL *pVal)  
HRESULT put_State(VARIANT_BOOL newVal)  
  
#### Interface

|  ISegment IInterfaceControl ITransform IGating ILimitTest IFOM IEquation
IEmbeddedLO IFIFO  
  
* * *

  

