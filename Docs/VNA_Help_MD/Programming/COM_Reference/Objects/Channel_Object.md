# Channel Object

* * *

See [SourcePowerCalData Interface](Channel_Object.md#ISourcePowerCalData) for
putting and getting typed source power calibration data.

### Description

The channel object is like the engine that produces data. Channel settings
consist of stimulus values like frequency, power, IF bandwidth, and number of
points.

### Accessing the Channel object

You can get a handle to a channel in a number of ways. But first you have to
make sure that the channel exists. When you first startup the analyzer, there
is one S11 measurement on channel 1. Thus there is only one channel in
existence. You can do the following:

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim chan As IChannel  
Set chan = app.ActiveChannel

or

Set chan = app.Channels(2)

The first method returns the channel object that is driving the active
measurement. If there is no measurement, there may not be a channel. Once a
channel is created, it does not go away. So if there once was a measurement
(hence a channel), the channel will still be available.

If there is no channel you can create one in a couple ways. You can do the
following:

Pna.CreateMeasurement( ch1, "S11", port1, window2)

or

Pna.Channels.Add(2)

The latter will have no visible effect on the analyzer. It will simply create
channel 2 if it does not already exist.

See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

[See History](Channel_Object.md#history) | 

### Description  
  
---|---|---  
[Abort](../Methods/Abort_Method.md) | IChannel | Aborts the current measurement sweep on the channel.  
[ApplySourcePowerCorrectionTo](../Methods/ApplySourcePowerCorrectionTo_Method.md) | IChannel11 | Copies an existing Source Power Calibration to another channel.  
[AveragingRestart](../Methods/Averaging_Restart_Method.md) | IChannel | Clears and restarts averaging of the measurement data.  
[Continuous](../Methods/Continuous_Method.md) | IChannel | The channel continuously responds to trigger signals.  
[CopyToChannel](../Methods/CopyToChannel_Method.md) | IChannel2 | Sets up another channel as a copy of this objects channel.  
[FrequencySpanFull](../Methods/FrequencySpanFull_Method.md) | IChannel25 | Sets the frequency span to the entire frequency range of the analyzer.  
[GetConverter](../Methods/GetConverter_Method.md) | IChannel17 | Returns a handle to a Converter object.  
[GetErrorCorrection](../Methods/Get_ErrorCorrection_Method.md) | IChannel8 | Returns the channel error correction state.  
[GetNumberOfGroups](../Methods/Get_NumberOfGroups_Method.md) | IChannel4 | Returns the [number of groups](../Methods/Number_Of_Groups_Method.md) a channel has yet to acquire.  
[GetPortNumber](../Methods/GetPortNumber_Method.md) | IChannel13 | Returns the port number for the specified string port name.  
[GetRxLevelingConfiguration](../Methods/GetRxLevelingConfiguration_Method.md) | IChannel17 | Returns a handle to a RxLevelingConfiguration object  
[getSourcePowerCalData](../Methods/get_SourcePowerCalData_Method.md) | IChannel | Superseded with [Get SourcePowerCalDataEx](../Methods/Get_SourcePowerCalDataEx_Method.md)  
[getSourcePowerCalDataEx](../Methods/Get_SourcePowerCalDataEx_Method.md) | IChannel4 | Returns requested source power calibration data, if it exists.  
[GetSupportedALCModes](../Methods/GetSupportedALCModes_Method.md) | IChannel10 | Returns a list of supported ALC modes  
[GetXAxisValues](../Methods/Get_X-axis_Values_Method.md) | IChannel | Returns the channel's X-axis values into a dimensioned Variant array.  
[GetXAxisValues2](../Methods/Get_X-Axis_Values_2.md) | IChannel | Returns the channel's X-axis values into a dimensioned NON-Variant array.  
[Hold](../Methods/Hold_Method.md) | IChannel | Puts the Channel in Hold - not sweeping.  
[Next_IFBandwidth](../Methods/Next_IF_Bandwidth_Method.md) | IChannel | A function that returns the Next higher IF Bandwidth value.  
[NumberOfGroups](../Methods/Number_Of_Groups_Method.md) | IChannel | Sets the Number of trigger signals the channel will receive.  
[Preset](../Methods/Preset_Method.md) | IChannel | Resets the channel to factory defined settings.  
[PreviousIFBandwidth](../Methods/Previous_IF_Bandwidth_Method.md) | IChannel | Returns the previous IF Bandwidth value.  
[putSourcePowerCalData](../Methods/put_SourcePowerCalData_Method.md) | IChannel | Superseded with [Put SourcePowerCalDataEx Method](../Methods/Put_SourcePowerCalDataEx_Method.md)  
[putSourcePowerCalDataEx](../Methods/Put_SourcePowerCalDataEx_Method.md) | IChannel4 | Inputs source power calibration data to this channel for a specific source port.  
[SelectCalSet](../Methods/SelectCalSet_Method.md) | IChannel | Specifies the Cal Set to use for the Channel  
[Single](../Methods/Single_Method.md) | IChannel | Channel responds to one trigger signal from any source (internal, external, or manual). Then channel switches to Hold.  
[UnselectCalset](../Methods/UnselectCalset_Method.md) | IChannel24 | Unselects a Cal Set from the specified channel.  
  
### Properties

|

### Interface

|

### Description  
  
[ALCLevelingMode](../Properties/ALCLevelingMode_Property.md) | IChannel10 | Set or return the ALC leveling mode.  
[AlternateSweep](../Properties/Alternate_Sweep_Property.md) | IChannel | Sets sweeps to either alternate or chopped.  
[Attenuator](../Properties/Attenuator_Property.md) | IChannel | Sets or returns the value of the attenuator control for the specified port number.  
[AttenuatorMode](../Properties/Attenuator_Mode_Property.md) | IChannel | Sets or returns the mode of operation of the attenuator control for the specified port number.  
[AuxiliaryTrigger](AuxTrigger_Object.md) | IChannel10 | Provides access to Auxiliary Triggering  
[Averaging](../Properties/Averaging_Property.md) | IChannel | Turns trace averaging ON or OFF for all measurements on the channel.  
[AveragingCount](../Properties/AveragingCount_Property.md) | IChannel | Returns the number of sweeps that have been averaged into the measurements.  
[AveragingFactor](../Properties/Averaging_Factor_Property.md) | IChannel | Specifies the number of measurement sweeps to combine for an average.  
[AverageMode](../Properties/AverageMode_Property.md) | IChannel16 | Sets Point or Sweep averaging.  
[BalancedTopology](BalancedTopology_Object.md) | IChannel6 | Provides access to the topology of a balanced DUT.  
[Calibrator](Calibrator_Object.md) | IChannel4 | Provides access to Unguided calibration.  
[CalSet](CalSet_Object.md) | IChannel7 | Provides access to the contents of a Cal Set  
[centerFrequency](../Properties/CenterFreq_Property.md) | IChannel | Sets or returns the center frequency of the channel. Shared with the Segment Object  
[CenterFrequencyStepSize](../Properties/CenterFrequencyStepSize_Property.md) | IChannel25 | Sets and reads the center frequency step size of the analyzer.  
[CenterFrequencyStepSizeMode](../Properties/CenterFrequencyStepSizeMode_Property.md) | IChannel25 | Sets and reads how the center frequency step size is determined.  
[channelNumber](../Properties/Channel_Number_Property.md) | IChannel | Returns the Channel number. Shared with the Measurement Object  
[Converter](Converter_Object.md) | IChannel21 | Provides access to a mixer/converter object.  
[CorrectionMethods](CorrectionMethods_Object.md) | IChannel21 | Provides access to channel correction properties.  
[CoupleChannelParams](../Properties/CoupleChannelParams_Property.md) | IChannel5 | Turns ON and OFF Time Domain Trace Coupling.  
[CouplePorts](../Properties/Couple_Ports_Property.md) | IChannel | Turns ON and OFF port power coupling.  
[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md) | IChannel12 | Provides access to custom application objects.  
[CWFrequency](../Properties/CW_Frequency_Property.md) | IChannel | Set the Continuous Wave (CW) frequency.  
[DCStimulus](DCStimulus_Object.md) | IChannel23 | Provides access to the DCStimulus object.  
[DefinedRoles](../Properties/DefinedRoles_Property.md) | IChannel22 | Returns the roles for which sources can be used for the channel.  
[DwellTime](../Properties/Dwell_Time_Property.md) | IChannel | Sets or returns the dwell time for the channel. Shared with the Segment Object  
[ErrorCorrection](../Properties/ErrorCorrection_Channel_Property.md) | IChannel7 | Attempts to sets error correction ON or OFF for all of the measurements on the channel.  
[ExternalTriggerDelay](../Properties/ExternalTriggerDelay_Property.md) | IChannel6 | Sets or returns the external trigger delay value for the channel.  
[FastCWPointCount](../Properties/FastCWPointCount_Property.md) | IChannel16 | Enables Fast CW sweep and sets the number of data points for the channel.  
[Fixturing](Fixturing_Object.md) | IChannel6 | Provides access to Port Ext, Embedding, and De-embedding functions.  
[FOM Collection](FOM_Collection.md) | IChannel9 | Provides access to Frequency Offset Measurements  
[FrequencyOffsetDivisor](../Properties/FrequencyOffsetDivisor_Property.md) | IChannel2 |   
[FrequencyOffsetFrequency](../Properties/FrequencyOffsetFrequency_Property.md) | IChannel2 |   
[FrequencyOffsetMultiplier](../Properties/FrequencyOffsetMultiplier_Property.md) | IChannel2 | Superseded with [FOM](FOM_Collection.md) and [FOMRange](FOMRange_Object.md)  
[FrequencyOffsetCWOverride](../Properties/FrequencyOffsetCWOverride_Property.md) | IChannel2 |   
[FrequencyOffsetState](../Properties/FrequencyOffsetState_Property.md) | IChannel2 |   
[FrequencySpan](../Properties/Frequency_Span_Property.md) | IChannel | Sets or returns the frequency span of the channel. Shared with the Segment Object.  
[FrequencyStep](../Properties/FrequencyStep_Property.md) | IChannel24 | Sets the frequency step size across the selected frequency range.  
[IFBandwidth](../Properties/IF_Bandwidth_Property.md) | IChannel | Sets or returns the IF Bandwidth of the channel. Shared with the Segment Object.  
[IFConfiguration](IIFConfiguration_Object.md) | IChannel4 | Provides access to the IF gain and source path settings for the H11 Option.  
[IsBlocked](../Properties/IsBlocked_Property.md) | IChannel19 | Returns whether or not a channel is blocked from sweeping.  
[IsContinuous](../Properties/IsContinuous_Property.md) | IChannel4 | Returns whether or not a channel is in [continuous](../Methods/Continuous_Method.md) mode.  
[IsHold](../Properties/IsHold_Property.md) | IChannel4 | Returns whether or not a channel is in [hold](../Methods/Hold_Method.md) mode.  
[LowFrequencyExtension](../Properties/LowFrequencyExtension_Property.md) | IChannel26 | Enables low frequency extension (LFE).  
[MeasurementClass](../Properties/MeasurementClass_Property.md) | IChannel15 | Returns the measurement class name.  
[MultiDimensionalSweep](MultiDimensionalSweep_Object.md) | IChannel27 | Provides access to the MultiDimensionalSweep Object.  
[NumberOfPoints](../Properties/Number_of__Points_Property.md) | IChannel | Sets or returns the Number of Points of the channel. Shared with the Segment Object.  
[Parent](../Properties/Parent_Property.md) | IChannel | Returns a handle to the parent object of the channel.  
[PathConfiguration](PathConfiguration_Object.md) | IChannel10 | Provides access to path configuration switches and setting.  
[PathConfigurationManager](PathConfigurationManager_Object.md) | IChannel10 | Provides access to path configuration file management.  
[PhaseControl](PhaseControl_Object.md) | IChannel21 | Provides access to the PhaseControl object.  
[PointSweepState](../Properties/PointSweepState_Property.md) | IChannel16 | Turns point sweep ON or OFF for all measurements on the channel.  
[PowerSlope](../Properties/Power_Slope_Property.md) | IChannel | Sets or returns the Power Slope value.  
[PowerSlopeState](../Properties/PowerSlopeState_Property.md) | IChannel18 | Turns power slope ON or OFF  
[PulseGenerator](PulseGenerator_Object.md) | IChannel10 | Provides access to pulse generator configuration.  
[PulseGeneratorID](../Properties/PulseGeneratorID_Property.md) | IChannel23 | Returns the ID for the specified Pulse Generator name.  
[PulseGeneratorNames](../Properties/PulseGeneratorNames_Property.md) | IChannel23 | Returns a list of configured Pulse Generator names.  
[PulseMeasControl](PulseMeasControl_Object.md) | IChannel20 | Provides access to pulse measurement settings.  
[R1InputPath](../Properties/R1inputPath_Property.md) | IChannel2 | Throws internal reference switch.  
[ReceiverAttenuator](../Properties/Receiver_Attenuator_Property.md) | IChannel | Sets or returns the value of the specified receiver attenuator control.  
[ReduceIFBandwidth](../Properties/ReduceIFBW_Property.md) | IChannel5 | Sets or returns the state of the [Reduced IF Bandwidth at Low Frequencies](../../../S2_Opt/Trce_Noise.md#IFDiag) setting.  
[RoleDevice](../Properties/RoleDevice_Property.md) | IChannel22 | Sets and returns the source to be used in the specified role.  
[RXLevelingConfiguration](RXLevelingConfiguration_Object.md) | IChannel21 | Provides access to the ReceiverLeveling Object  
[Segments](Segments_Collection.md) | IChannel | Provides access to the Collection for iterating through the sweep segments of a channel.  
[SignalProcessingModuleFour](SignalProcessingModuleFour_Object.md) | IChannel10 | Provides access to the SignalProcessingModuleFour object.  
[SourcePortCount](../Properties/SourcePortCount_Property.md) | IChannel13 | Returns the number of source ports.  
[SourcePortFixedFrequency](../Properties/SourcePortFixedFrequency_Property.md) | IChannel27 | Set and read the fixed frequency value for a specific port.   
[SourcePortMode](../Properties/SourcePortMode_Property.md) | IChannel9 | Sets the state of the VNA sources. (AUTO | ON | OFF)  
[SourcePortNames](../Properties/SourcePortNames_Property.md) | IChannel13 | Returns the string names of source ports.  
[SourcePortStartFrequency](../Properties/SourcePortStartFrequency_Property.md) | IChannel27 | Set and read the start frequency value for a specific port.   
[SourcePortStopFrequency](../Properties/SourcePortStopFrequency_Property.md) | IChannel27 | Set and read the stop frequency value for a specific port.   
[SourcePowerCalPowerOffset](../Properties/SourcePowerCalPowerOffset_Property.md) | IChannel4 | Sets or returns a power level offset from the VNA test port power.  
[SourcePowerCorrection](../Properties/SourcePowerCorrection_Property.md) | IChannel | Turns source power correction ON or OFF for a specific source port.  
[StartFrequency](../Properties/Start_Frequency_Property.md) | IChannel | Sets or returns the start frequency of the channel. Shared with the Segment Object  
[StartPower](../Properties/Start_Power_Property.md) | IChannel | Sets the start power of the analyzer when sweep type is set to Power Sweep.  
[StartPowerEx](../Properties/StartPowerEx_Property.md) | IChannel13 | Sets and reads the power sweep start power value for a specific port.  
[StopFrequency](../Properties/Stop_Frequency_Property.md) | IChannel | Sets or returns the stop frequency of the channel. Shared with the Segment Object  
[StopPower](../Properties/Stop_Power_Property.md) | IChannel | Sets the Stop Power of the analyzer when sweep type is set to Power Sweep.  
[StopPowerEx](../Properties/StopPowerEx_Property.md) | IChannel13 | Sets and reads the power sweep stop power value for a specific port.  
[SweepDelay](../Properties/Sweep_Delay_Property.md) | IChannel19 | Sets the time to wait just before acquisition begins for each sweep.  
[SweepGenerationMode](../Properties/Sweep_Generation_Mode_Property.md) | IChannel | Sets the method used to generate a sweep: continuous ramp (analog) or discrete steps (stepped).  
[SweepSpeedMode](../Properties/SweepSpeedMode_Property.md) | IChannel14 | Set or returns the sweep speed mode.  
[SweepTime](../Properties/Sweep_Time_Property.md) | IChannel | Sets the Sweep time of the analyzer.  
[SweepType](../Properties/Sweep_Type_Property.md) | IChannel | Sets the type of X-axis sweep that is performed on a channel.  
[TestPortPower](../Properties/Test_Port_Power_Property.md) | IChannel | Sets or returns the RF power level for the channel. Shared with the Segment Object  
[TriggerMode](../Properties/Trigger_Mode_Property.md) | IChannel | Determines the measurement that occurs when a trigger signal is sent to the channel.  
[UserRangeMax](../Properties/User_Range_Max_Property.md) | IChannel | Superseded \- Use meas.[UserRangeMax](../Properties/User_Range_Max_Property.md) Sets the stimulus stop value for the specified User Range.  
[UserRangeMin](../Properties/User_Range_Min_Property.md) | IChannel | Superseded \- Use meas.[UserRangeMin](../Properties/User_Range_Min_Property.md) Sets the stimulus start value for the specified User Range.  
[XAxisPointSpacing](../Properties/XAxisPointSpacing_Property.md) | IChannel | Sets X-Axis point spacing for the active channel.  
  
### IChannel History

Interface | Introduced with VNA Rev:  
---|---  
IChannel | 1.0  
IChannel2 | 3.0  
IChannel3 | 4.0  
IChannel4 | 4.0  
IChannel5 | 4.2  
IChannel6 | 5.0  
IChannel7 | 5.2  
IChannel8 | 6.0  
IChannel9 | 7.0  
IChannel10 | 7.2  
IChannel11 | 7.5  
IChannel12 | 8.0  
IChannel13 | 8.2  
IChannel14 | 8.33  
IChannel15 | 8.33  
IChannel16 | 8.35  
IChannel17 | 8.55  
IChannel19 | 9.20  
IChannel20 | 9.20  
IChannel21 | 9.30  
IChannel22 | 9.42  
IChannel23 | 9.50  
IChannel24 | 10.40  
IChannel25 | 10.45  
IChannel26 | 12.80  
IChannel27 | 13.25  
  
ISourcePowerCalData Interface

* * *

### Description

Contains methods for putting source power calibration data in and getting
source power calibration data out of the analyzer using typed data. The
methods in this interface transfer data more efficiently than methods that use
variant data. However, this interfaces is only usable from VB6, C, & C++. All
other programming languages must use the methods on the Channel Object.

Note: Interface ISourcePowerCalData is abbreviated as ISPCD in the following
table.

### Methods

|

### Interface

[See History](Channel_Object.md#history1) | 

### Description  
  
---|---|---  
[getSourcePowerCalDataScalar](../Methods/get_SourcePowerCalDataScalar_Method.md) | ISPCD | Superseded \- use [PutSourcePowerCalDataScalarEx Method](../Methods/Put_SourcePowerCalDataScalarEx_Method.md)  
[getSourcePowerCalDataScalarEx](../Methods/Get_SourcePowerCalDataScalarEx_Method.md) | ISPCD2 | Returns requested source power calibration data, if it exists.  
[putSourcePowerCalDataScalar](../Methods/put_SourcePowerCalDataScalar_Method.md) | ISPCD | Superseded \- use [PutSourcePowerCalDataEx Method](../Methods/Put_SourcePowerCalDataEx_Method.md)  
[putSourcePowerCalDataScalarEx](../Methods/Put_SourcePowerCalDataScalarEx_Method.md) | ISPCD2 | Inputs source power calibration data to a channel, for a specific source port.  
  
### Properties

|

###

|

### Description  
  
None |  |   
  
### ISourcePowerCalData History

Interface | Introduced with VNA Rev:  
---|---  
ISourcePowerCalData | 2.0  
ISourcePowerCalData2 | 4.0

