# IMSpectrum Object

* * *

### Description

Controls the IM Spectrum settings.

### Accessing the IMSpectrum object

Dim app as AgilentPNA835x.Application
app.[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)(1,
"IMSpectrum", "Output", 1) Dim IMSpec Set IMSpec =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)  
---  
  
### See Also:

  * Example Program Create and Cal a IM Spectrum Measurement

  * [About IM Spectrum Measurements](IMSpectrum_Object.md)

  * [SweptIMD Object](SweptIMD_Object.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
[SetPortMap](../Methods/SetPortMap_Method.md) |  IIMSpectrum |  Sets limited port mapping  
  
### Property

|

### Interface

|

### Description  
  
[CoupleTonePower](../Properties/CoupleTonePower_Property.md) |  IIMSpectrum |  ON | OFF state of power coupling for F1 and F2.  
[DeviceInputPort](../Properties/DeviceInputPort_Property.md) |  IIMSpectrum |  Read input port map  
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) |  IIMSpectrum |  Read output port map  
[DeltaFrequency](../Properties/DeltaFrequency_Property.md) |  IIMSpectrum |  Fixed tone spacing value.  
[EqualTonePower](../Properties/EqualTonePower_Property.md) |  IIMSpectrum2 |  Superseded with [LevelingMethod](../Properties/LevelingMethod_Property.md) Set Equal Tone Power state.  
[F1Frequency](../Properties/F1Frequency_Property.md) |  IIMSpectrum |  Frequency of the F1 tone.  
[F2Frequency](../Properties/F2Frequency_Property.md) |  IIMSpectrum |  Frequency of the F2 tone.  
[FrequencyCenter](../Properties/FrequencyCenter_Property.md) |  IIMSpectrum |  Center frequency of the main tones.  
[LevelingMethod](../Properties/LevelingMethod_Property.md) |  IIMSpectrum3 |  Set tone power leveling mode  
[ResolutionBW](../Properties/ResolutionBW_Property.md) |  IIMSpectrum |  Resolution Bandwidth for the measurement.  
[SpectrumCenterFrequency](../Properties/SpectrumCenterFrequency_Property.md) |  IIMSpectrum |  Receiver Center frequency  
[SpectrumSpanFrequency](../Properties/SpectrumSpanFrequency_Property.md) |  IIMSpectrum |  Receiver frequency span.  
[SpectrumStartFrequency](../Properties/SpectrumStartFrequency_Property.md) |  IIMSpectrum |  Receiver Start frequency.  
[SpectrumStopFrequency](../Properties/SpectrumStopFrequency_Property.md) |  IIMSpectrum |  Receiver Stop frequency.  
[TonePowerSetAt](../Properties/TonePowerSetAt_Property.md) |  IIMSpectrum2 |  Superseded with [LevelingMethod](../Properties/LevelingMethod_Property.md) Set power at DUT input or Output  
[TrackingChannel](../Properties/TrackingChannel_Property.md) |  IIMSpectrum |  IMD channel number to which the IM Spectrum channel is coupled.  
[TrackingEnable](../Properties/TrackingEnable_Property.md) |  IIMSpectrum |  Enables tracking with an IMD channel.  
[TrackingManualStepEnable](../Properties/TrackingManualStepEnable_Property.md) |  IIMSpectrum |  Step sweep mode for the IM Spectrum channel.  
[TrackingStepIndex](../Properties/TrackingStepIndex_Property.md) |  IIMSpectrum |  IMD data point number at which the IM spectrum measurement occurs.  
[SweepOrder](../Properties/SweepOrder_Property.md) |  IIMSpectrum |  IM product to view when [SweepType](../Properties/SweepType_imd_Property.md) = NTH is specified.  
[SweepType](../Properties/SweepType_ims_Property.md) |  IIMSpectrum |  Type of sweep for an IMSpectrum measurement.  
[TonePower](../Properties/TonePower_Property.md) |  IIMSpectrum |  Power level of the Main Tones  
  
###  IIMSpectrum History

Interface |  Introduced with VNA Rev:  
---|---  
IIMSpectrum |  8.35  
IIMSpectrum2 |  9.40  
  
* * *

  

