# Converter Object

* * *

Note: The Converter Object replaces the [IMixer
Interface](IMixer_Interface.htm).

### Description

Contains the methods and properties to setup a mixer for ALL [VNA
Mixer/Converter applications](../../../Applications/MixerConverter_Setup.htm).

### Accessing the Converter Interface

Dim app as AgilentPNA835x.Application Dim chan as Channel Set chan =
app.ActiveChannel Dim converter as Converter Set converter =chan.Converter  
---  
  
### Scratch vs Applied Mixer Properties

Each mixer configuration has two sets of properties:

  1. Scratch mixer contains the properties that have been set, but NOT YET applied. Send the [Apply Method](../Methods/Apply_Method.md) to copy these properties to the Applied mixer.
  2. Applied mixer contains the properties that makeup the current mixer configuration.

Power settings are immediately applied to both the Scratch and Applied mixer.
A successful [Calculate](../Methods/Calculate_Method.md) also performs an
Apply. Note: Queries always return the Applied mixer properties. Therefore,
first send [Apply Method](../Methods/Apply_Method.md) before querying new
settings.  
---  
  
### See Also

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Mixer Setup UI topic](../../../Applications/MixerConverter_Setup.md)

### Methods

|

### Interface

[See History](IMixer_Interface.md#History) | 

### Description  
  
---|---|---  
[AddSegment](../Methods/AddSegment_Method.md) |  Converter5 |  Add segments to the segment table (FCA Only)  
[Apply](../Methods/Apply_Method.md) |  Converter |  Applies mixer settings.  
[AssignSourceToRole](../Methods/AssignSourceToRole_Method.md) |  Converter |  Assigns a configured source to the specified role.  
[Calculate](../Methods/Calculate_cv_Method.md) |  Converter |  Automatically calculate Input and Output frequencies for mixer setup.  
[DeleteAllSegments](../Methods/DeleteAllSegments_Method.md) |  Converter5 |  Remove all segments from the segment table. (FCA Only)  
[DeleteSegment](../Methods/DeleteSegment_Method.md) |  Converter5 |  Remove segments from the segment table.(FCA Only)  
[DiscardChanges](../Methods/DiscardChanges_Method.md) |  Converter |  Cancels changes that have been made to the Converter setup.  
[GetSourceByRole](../Methods/GetSourceByRole_Method.md) |  Converter |  Returns the name of a source that is assigned to the specified role.  
[GetSourceRoles](../Methods/GetSourceRoles_Method.md) |  Converter |  Returns the defined role names ("RF2", "LO1").  
[LoadFile](../Methods/LoadFile_Method.md) |  Converter |  Loads a previously-configured mixer attributes file (.mxr)  
[ReCalculate](../Methods/ReCalculate_Method.md) |  Converter5 |  Repeats the last calculation that was performed.  
[SaveFile](../Methods/SaveFile_Method.md) |  Converter |  Saves the settings for the mixer/converter test setup to a mixer attributes file.  
[SegmentCalculate](../Methods/SegmentCalculate_Method.md) |  Converter5 |  Performs calculate on a specific segment. (FCA Only)  
  
### Properties

|

###

|

### Description  
  
[ActiveXAxisRange](../Properties/ActiveXAxisRange_Conv_Property.md) |  Converter |  Sets or returns the swept frequency range to display on the X-axis.  
[AvoidSpurs](../Properties/AvoidSpurs_Property.md) |  Converter5 |  Sets and returns the state of the avoid spurs feature.  
[ConverterEmbeddedLO](ConverterEmbeddedLO_Object.md) |  Converter2 |  Provides access to the [ConverterEmbeddedLO Object](ConverterEmbeddedLO_Object.md)  
[DeviceInputPort](../Properties/DeviceInputPort_Property.md) |  Converter6 |  Read the VNA port number which is connected to the DUT Input.  
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) |  Converter6 |  Read the VNA port number which is connected to the DUT Output.  
[EnablePhase](../Properties/EnablePhase_Property.md) |  Converter3 |  Sets and returns the state of SMC + Phase measurements and calibrations. (SMC Only)  
[IFDenominator](../Properties/IFDenominator_Property.md) |  Converter4 |  Sets or returns the denominator value of the IF Fractional Multiplier.  
[IFNumerator](../Properties/IFNumerator_Property.md) |  Converter4 |  Sets or returns the numerator value of the IF Fractional Multiplier.  
[IFSideband](../Properties/IFSideband-Converter_Property.md) |  Converter4 |  Select sum or difference for IF product.  
[IFStartFrequency](../Properties/IFStartFrequency_Property.md) |  Converter4 |  Sets or returns the IF start frequency.  
[IFStopFrequency](../Properties/IFStopFrequency_Property.md) |  Converter4 |  Sets or returns the IF stop frequency.  
[IncludeReverseSweep](../Properties/IncludeReverseSweep_Property.md) |  Converter4 |  Sets whether to include SC12 sweeps during measurements.  
[InputDenominator](../Properties/InputDenominator_Property.md) |  Converter |  Sets or returns the denominator value of the Input Fractional Multiplier.  
[InputFixedFrequency](../Properties/InputFixedFrequency_Property.md) |  Converter |  Sets or returns the mixer fixed Input frequency value.  
[InputNumerator](../Properties/InputNumerator_Property.md) |  Converter |  Sets or returns the numerator value of the Input Fractional Multiplier.  
[InputPower](../Properties/InputPower_Property.md) |  Converter |  Sets or returns the value of the Input Power.  
[InputRangeMode](../Properties/InputRangeMode_cv_Property.md) |  Converter |  Sets or returns the Input sweep mode.  
[InputStartFrequency](../Properties/InputStartFrequency_Property.md) |  Converter |  Sets or returns the start frequency of the mixer input.  
[InputStartPower](../Properties/InputStartPower_Property.md) |  Converter4 |  Sets and returns the Start Power value of the mixer Input Power.  
[InputStopFrequency](../Properties/InputStopFrequency_Property.md) |  Converter |  Sets or returns the stop frequency of the mixer input.  
[InputStopPower](../Properties/InputStopPower_Property.md) |  Converter4 |  Sets and returns the Stop Power value of the mixer Input Power.  
[IsInputGreaterThanLO](../Properties/InputIsGreaterThanLO_Property.md) |  Converter |  Specifies whether to use the Input frequency that is greater than the LO or less than the LO.  
[LODenominator](../Properties/LODenominator_Property.md) |  Converter |  Sets or returns the denominator value of the LO Fractional Multiplier.  
[LOFixedFrequency](../Properties/LOFixedFrequency_Property.md) |  Converter |  Sets or returns the fixed frequency of the specified LO.  
[LOName](../Properties/LOName_Property.md) |  Converter |  Sets or returns the LO name.  
[LONumerator](../Properties/LONumerator_Property.md) |  Converter |  Sets or returns the numerator value of the LO Fractional Multiplier.  
[LOPower](../Properties/LOPower_Property.md) |  Converter |  Sets or returns the value of the LO Power.  
[LORangeMode](../Properties/LORangeMode_cv_Property.md) |  Converter |  Sets or returns the LO sweep mode to fixed or swept.  
[LOStage](../Properties/LOStage_Property.md) |  Converter |  Returns the number of stages.  
[LOStartFrequency](../Properties/LOStartFrequency_Property.md) |  Converter |  Sets or returns the start frequency of the specified LO.  
[LOStartPower](../Properties/LOStartPower_Property.md) |  Converter |  Sets or returns the start value of a LO Power sweep.  
[LOStopFrequency](../Properties/LOStopFrequency_Property.md) |  Converter |  Sets or returns the start frequency of the specified LO.  
[LOStopPower](../Properties/LOStopPower_Property.md) |  Converter |  Sets or returns the stop value of a LO Power sweep.  
[NominalIncidentPowerState](../Properties/NominalIncidentPowerState_Property.md) |  Converter3 |  Sets or returns whether to use nominal power or measure actual incident power. (SMC ONLY)  
[NormalizePoint](../Properties/NormalizePoint_SMC_Property.md) |  Converter3 |  Sets or returns the data point used for normalizing an SMC phase measurement. (SMC Only)  
[OutputFixedFrequency](../Properties/OutputFixedFrequency_Property.md) |  Converter |  Sets or returns the fixed frequency of the mixer output.  
[OutputRangeMode](../Properties/OutputRangeMode_cv_Property.md) |  Converter |  Sets or returns the Output sweep mode.  
[OutputSideband](../Properties/OutputSideband-Converter_Property.md) |  Converter |  Sets or returns the value of the output sideband.  
[OutputStartFrequency](../Properties/OutputStartFrequency_Property.md) |  Converter |  Sets or returns the start frequency of the mixer output.  
[OutputStopFrequency](../Properties/OutputStopFrequency_Property.md) |  Converter |  Sets or returns the stop frequency of the mixer output.  
[SegmentCount](../Properties/SegmentCount_Property.md) |  Converter5 |  Read the number of segments. (FCA Only)  
[SegmentFixedFrequency](../Properties/SegmentFixedFrequency_Property.md) |  Converter5 |  Set and read the CW Frequency for mixer segments in CW Sweep mode. (FCA Only)  
[SegmentFixedPower](../Properties/SegmentFixedPower_Property.md) |  Converter5 |  Set and return the fixed power level for all ranges for mixer segments. (FCA Only)  
[SegmentIFBandwidth](../Properties/SegmentIFBandwidth_Property.md) |  Converter5 |  Set and return the IF Bandwidth for the sweep segment. (FCA Only)  
[SegmentIsInputGreaterThanLO](../Properties/SegmentIsInputGreaterThanLO_Property.md) |  Converter5 |  Set and return whether to use the Input frequency that is greater than the LO. (FCA Only)  
[SegmentMixingMode](../Properties/SegmentMixingMode_Property.md) |  Converter5 |  Set and return whether to set the mixing mode to high side or low side. (FCA Only)  
[SegmentPoints](../Properties/SegmentPoints_Property.md) |  Converter5 |  Sets and returns the number of data points to be measured in the sweep segment. (FCA Only)  
[SegmentRangeMode](../Properties/SegmentRangeMode_Property.md) |  Converter5 |  Sets or returns the sweep mode of the segment (all ranges). (FCA Only)  
[SegmentStartFrequency](../Properties/SegmentStartFrequency_Property.md) |  Converter5 |  Set and return the Start frequency for mixer segments. (FCA Only)  
[SegmentState](../Properties/SegmentState_Property.md) |  Converter5 |  Set and return the ON/OFF state for mixer segments. (FCA Only)  
[SegmentStopFrequency](../Properties/SegmentStopFrequency_Property.md) |  Converter5 |  Set and return the Stop frequency for mixer segments. (FCA Only)  
  
### Converter History

Interface |  Introduced with VNA Rev:  
---|---  
Converter |  8.55  
Converter2 |  9.0  
Converter3 |  9.2  
Converter4 |  9.30  
Converter5 |  9.33  
Converter6 |  9.40  
  
* * *

