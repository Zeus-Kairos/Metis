# Transform Object

* * *

### Description

Contains the methods and properties that control Time Domain transforms.

### Accessing the Transform Object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim trans As Transform  
Set trans = app.ActiveMeasurement.Transform

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Time Domain Topics](../../../Time/TimeDomain.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

Note: [Sweep Type](../Properties/Sweep_Type_Property.md) must be set to
Linear before setting Time Domain Transform (state) ON.

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[SetFrequencyLowPass](../Methods/Set_Frequency_LowPass_Method.md) |  ITransform |  Sets low frequencies for low pass.  
  
### Properties

|

###

|

### Description  
  
[Alignment](../Properties/Alignment_Property.md) |  ITransform3 |  Sets or returns the alignment of the time domain measurement.  
[Center](../Properties/Center_Property.md) |  ITransform |  Sets or returns the Center time. Shared with the Gating Object  
[CoupledParameters](../Properties/CoupledParameters_Gate_Property.md) |  ITransform2 |  Select Transform parameters to couple  
[DistanceMarkerMode](../Properties/DistanceMarkerMode_Property.md) |  ITransform2 |  Sets the measurement type in order to determine the correct marker distance.  
[DistanceMarkerUnit](../Properties/DistanceMarkerUnit_Property.md) |  ITransform2 |  Sets the unit of measure for the display of marker distance values.  
[ImpulseWidth](../Properties/Impulse_Width_Property.md) |  ITransform |  Sets or returns the Impulse Width of Time Domain transform windows.  
[KaiserBeta](../Properties/Kaiser_Beta_Property.md) |  ITransform |  Sets or returns the Kaiser Beta of Time Domain transform windows.  
[Mode](../Properties/Mode_Property.md) |  ITransform |  Sets the type of transform.  
[Span](../Properties/Span_Property.md) |  ITransform |  Sets or returns the Span time. Shared with the Gating Object  
[Start](../Properties/Start_Property.md) |  ITransform |  Sets or returns the Start time. Shared with the Gating Object  
[State](../Properties/State_Property.md) |  ITransform |  Turns an Object ON and OFF.  
[StepRiseTime](../Properties/Step_Rise_Time_Property.md) |  ITransform |  Sets or returns the Rise time of the stimulus in Low Pass Step Mode.  
[Stop](../Properties/Stop_Property.md) |  ITransform |  Sets or returns the Stop time. Shared with the Gating Object  
  
###  ITransform History

Interface |  Introduced with VNA Rev:  
---|---  
ITransform |  1.0  
ITransform2 |  4.2  
ITransform3 |  12.70

