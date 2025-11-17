# SweptIMD Object

* * *

### Description

Controls the Swept IMD Application settings.

See [Properties to set for each sweep type.](SweptIMD_Object.md#sweepTypes)

### Accessing the SweptIMD object

Dim app as AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application")
app.[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)(1,
"SweptIMD", "PwrMain", 1) Dim IMD Set IMD =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)  
---  
  
### See Also:

  * Example Program [Create and Cal a Swept IMD Measurement](../../COM_Example_Programs/Create_and_Cal_a_Swept_IMD_Measurement.md)

  * Use std channel commands to set [source](../Properties/Attenuator_Property.md) and [receiver attenuation](../Properties/Receiver_Attenuator_Property.md).

  * [SweptIMDCal Object](SweptIMDCal_Object.md)

  * [About the Swept IMD Application](../../../Applications/Swept_IMD.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
[SetPortMap](../Methods/SetPortMap_Method.md) |  ISweptIMD |  Sets port mapping  
  
### Property

|

### Interface

|

### Description  
  
[CompositeNormalizationMode](../Properties/CompositeNormalizationMode_Property.md) |  ISweptIMD |  Sets and returns the method by which CTB and CSO calculations are performed.  
[CompositeNormalizedCSOPower](../Properties/CompositeNormalizedCSOPower_Property.md) |  ISweptIMD |  Sets and returns the CSO Power.  
[CompositeNormalizedCTBPower](../Properties/CompositeNormalizedCTBPower_Property.md) |  ISweptIMD |  Sets and returns the CTB Power.  
[CoupleTonePower](../Properties/CoupleTonePower_Property.md) |  ISweptIMD |  ON | OFF state of power coupling for F1 and F2.  
[CSONumDistortionProducts](../Properties/CSONumDistortionProducts_Property.md) |  ISweptIMD |  Sets the N = number of distortion products value for the calculation of the CSO parameter.  
[CSOOffset Property](../Properties/CSOOffset_Property.md) |  ISweptIMD |  Sets and returns the offset that is applied to CSO measurements.  
[CTBOffset Property](../Properties/CTBOffset_Property.md) |  ISweptIMD |  Sets and returns the offset that is applied to CTB measurements.  
[CTBXMODNumCarriers](../Properties/CTBXMODNumCarriers.md) |  ISweptIMD |  Sets the N = Total number of carriers value used in the calculation of the XMOD and CTB parameter.  
[DeltaFrequency](../Properties/DeltaFrequency_Property.md) |  ISweptIMD |  Fixed tone spacing value.  
[DeltaFrequencyStart](../Properties/DeltaFrequencyStart_Property.md) |  ISweptIMD |  Start spacing of the main tones.  
[DeltaFrequencyStop](../Properties/DeltaFrequencyStop_Property.md) |  ISweptIMD |  Stop spacing of the main tones.  
[DeviceInputPort](../Properties/DeviceInputPort_Property.md) |  ISweptIMD |  Reads input port map  
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) |  ISweptIMD |  Reads output port map  
[EqualTonePower](../Properties/EqualTonePower_Property.md) |  ISweptIMD2 |  Superseded with [LevelingMethod](../Properties/LevelingMethod_Property.md) Set Equal Tone Power state.  
[F1Frequency](../Properties/F1Frequency_Property.md) |  ISweptIMD |  Frequency of the F1 tone.  
[F2Frequency](../Properties/F2Frequency_Property.md) |  ISweptIMD |  Frequency of the F1 tone.  
[FrequencyCenter](../Properties/FrequencyCenter_Property.md) |  ISweptIMD |  Center frequency of the main tones.  
[FrequencyCenterCenter](../Properties/FrequencyCenterCenter_Property.md) |  ISweptIMD |  Sweep center frequency when sweeping the main tones.  
[FrequencyCenterSpan](../Properties/FrequencyCenterspan_Property.md) |  ISweptIMD |  Frequency span when sweeping the main tones.  
[FrequencyCenterStart](../Properties/FrequencyCenterStart_Property.md) |  ISweptIMD |  Start frequency when sweeping the main tones.  
[FrequencyCenterStop](../Properties/FrequencyCenterStop_Property.md) |  ISweptIMD |  Stop frequency when sweeping the main tones.  
[Has2ndOrderTrace](../Properties/Has2ndOrderTrace_Property.md) |  ISweptIMD4 |  Reads the state of whether or not 2nd order parameters are measured.  
[HighestOrderProduct](../Properties/HighestOrderProduct_Property.md) |  ISweptIMD |  Reads the highest product that can be measured by SweptIMD.  
[HighestOrderProductInUse](../Properties/HighestOrderProductInUse_Property.md) |  ISweptIMD4 |  Reads the highest product measured by SweptIMD.  
[IMToneIFBandwidth](../Properties/IMToneIFBandwidth_Property.md) |  ISweptIMD |  IF Bandwidth for measurement of the intermodulation products.  
[LevelingMethod](../Properties/LevelingMethod_Property.md) |  ISweptIMD3 |  Set power leveling mode  
[MainToneIFBandwidth](../Properties/MainToneIFBandwidth_Property.md) |  ISweptIMD |  IF Bandwidth for measurement of the Main tones.  
[SweepType](../Properties/SweepType_imd_Property.md) |  ISweptIMD |  Type of sweep for a Swept IMD measurement.  
[TonePower](../Properties/TonePower_Property.md) |  ISweptIMD |  Power level of the Main Tones.  
[TonePowerSetAt](../Properties/TonePowerSetAt_Property.md) |  ISweptIMD2 |  Superseded with [LevelingMethod](../Properties/LevelingMethod_Property.md) Set power level at DUT Input or Output  
[TonePowerStart](../Properties/TonePowerStart_Property.md) |  ISweptIMD |  Start power level of the Main tones.  
[TonePowerStop](../Properties/TonePowerStop_Property.md) |  ISweptIMD |  Stop power level of the Main tones.  
  
### See Also

  * [RoleDevice Property](../Properties/RoleDevice_Property.md) to use an external source for f2.

The following commands are relevant for each [IMD sweep
type:](../Properties/SweepType_imd_Property.htm)

0 - naIMDToneCWSweep

  * [F1Frequency Property](../Properties/F1Frequency_Property.md)

  * [F2Frequency Property](../Properties/F2Frequency_Property.md)

  * [FrequencyCenter Property](../Properties/FrequencyCenter_Property.md)

  * [DeltaFrequency Property](../Properties/DeltaFrequency_Property.md)

  * [TonePower (1,2) Property](../Properties/TonePower_Property.md)

1 - naIMDTonePowerSweep

  * [F1Frequency Property](../Properties/F1Frequency_Property.md)

  * [F2Frequency Property](../Properties/F2Frequency_Property.md)

  * [FrequencyCenter Property](../Properties/FrequencyCenter_Property.md)

  * [DeltaFrequency Property](../Properties/DeltaFrequency_Property.md)

  * [TonePowerStart Property](../Properties/TonePowerStart_Property.md)

  * [TonePowerStop Property](../Properties/TonePowerStop_Property.md)

2 - naIMDToneCenterFreqSweep

  * [FrequencyCenterStart Property](../Properties/FrequencyCenterStart_Property.md)

  * [FrequencyCenterStop Property](../Properties/FrequencyCenterStop_Property.md)

  * [FrequencyCenterCenter Property](../Properties/FrequencyCenterCenter_Property.md)

  * [FrequencyCenterSpan Property](../Properties/FrequencyCenterspan_Property.md)

  * [DeltaFrequency Property](../Properties/DeltaFrequency_Property.md)

  * [TonePower (1,2) Property](../Properties/TonePower_Property.md)

3 - naIMDDeltaFrequencySweep

  * [DeltaFrequencyStart Property](../Properties/DeltaFrequencyStart_Property.md)

  * [DeltaFrequencyStop Property](../Properties/DeltaFrequencyStop_Property.md)

  * [FrequencyCenter Property](../Properties/FrequencyCenter_Property.md)

  * [TonePower (1,2) Property](../Properties/TonePower_Property.md)

4 - naIMDToneSegmentSweep (Not available for IMDx)

  * [DeltaFrequency Property](../Properties/DeltaFrequency_Property.md)

  * [TonePower (1,2) Property](../Properties/TonePower_Property.md)

  * Also use standard [segment sweep commands](Segment_Object.md)

5 - naLOPowerSweep (IMDx ONLY)

  * converter.[LOStartPower Property](../Properties/LOStartPower_Property.md)

  * converter.[LOStopPower Property](../Properties/LOStopPower_Property.md)

###  ISweptIMD History

Interface |  Introduced with VNA Rev:  
---|---  
ISweptIMD |  8.33  
ISweptIMD2 |  9.40  
ISweptIMD3 |  9.80  
ISweptIMD4 |  12.80  
  
* * *

