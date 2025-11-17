##### Write/Read

|

##### [About Time Domain Trace
Coupling](../../../Time/TimeDomain.htm#Coupling)  
  
---|---  
  
## CoupledParameters Property (Transform)

* * *

#### Description

|  Specifies the time domain transform parameters to be coupled. The settings
for those parameters will be copied from the active measurement to all other
measurements on the channel. To turn coupling ON and OFF, use
[CoupleChannelParams Property](CoupleChannelParams_Property.md) To specify
Gating parameters to couple, use [Gate.CoupledParameters
Property](CoupledParameters_Gate_Property.htm)  
---|---  
  
####  VB Syntax

|  trans.CoupledParameters = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A [Transform](../Objects/Transform_Object.md) (object)  
value |  (Enum As NATransformCoupledParams) \- Parameters to couple. To specify more than one parameter, add the numbers. Choose from: 1 - naTransformStimulusCoupled (Start, Stop, Center, and Span TIME settings.) 2 - naTransformStateCoupled (ON / OFF) 4 - naTransformWindowCoupled (Kaiser Beta / Impulse Width) 8 - naTransformModeCoupled (Low Pass Impulse, Low Pass Step, Band Pass) 16 - naTransformDistMkrUnitCoupled (Distance maker Units)  
  
#### Return Type

|  Enum  
  
#### Default

|  29  
  
#### Examples

|  trans.CoupledParameters = 31 'Couple all parameters  
CP = trans.CoupledParameters 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CoupledParameters(long *lParams); HRESULT
put_CoupledParameters(long lParams);  
  
#### Interface

|  ITransform2

