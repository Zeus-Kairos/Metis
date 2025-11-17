##### Write/Read

|

##### [About Time Domain Trace
Coupling](../../../Time/TimeDomain.htm#Coupling)  
  
---|---  
  
## CoupledParameters Property (Gating)

* * *

#### Description

|  Specifies the time domain gating parameters to be coupled. The settings for
those parameters will be copied from the active measurement to all other
measurements on the channel. To turn coupling ON and OFF, use
[CoupleChannelParams Property](CoupleChannelParams_Property.md) To specify
Transform parameters to couple, use [Transform.CoupledParameters
Property](CoupledParameters_Transform_Property.htm)  
---|---  
  
####  VB Syntax

|  gate.CoupledParameters = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A [Gating](../Objects/Gating_Object.md) (object)  
value |  (Enum As NAGatingCoupledParams) \- Parameters to couple. To specify more than one parameter, add the numbers. Choose from: 1 - naGatingStimulusCoupled (Start, Stop, Center, and Span TIME settings.) 2 - naGateStateCoupled (ON / OFF) 4 - naGatingShapeCoupled (Minimum, Normal, Wide, and Maximum) 8 - naGatingTypeCoupled (Bandpass and Notch)  
  
#### Return Type

|  Enum  
  
#### Default

|  29  
  
#### Examples

|  gate.CoupledParameters = 15 'Couple all parameters  
CP = gate.CoupledParameters 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CoupledParameters(long *lParams); HRESULT
put_CoupledParameters(long lParams);  
  
#### Interface

|  IGating2

