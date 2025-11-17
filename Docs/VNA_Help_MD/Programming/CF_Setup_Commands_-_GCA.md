# Setup Commands - Gain Compression Measurement Class

Only the Main and Layout Setup commands corresponding to the Gain Compression
measurement class are documented here. All other commands are identical to the
Setup commands for the Standard measurement class and can be accessed by
clicking [here](CF_Setup_Commands_-_Standard.md) or by clicking on the
softtabs on the graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main | Layout | [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) | [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) | [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
GCA Setup... | Frequency  
Sweep Type  
Linear Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Log Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) | [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Data Acquisition Mode  
SMART Sweep | [SENSe:GCSetup:AMODe](GP-IB_Command_Finder/Sense/Gain_Compression.md#Amode) | [AcquisitionMode](COM_Reference/Properties/AcquisitionMode_Property.md)  
Sweep Power Per Frequency (2D) | [SENSe:GCSetup:AMODe](GP-IB_Command_Finder/Sense/Gain_Compression.md#Amode) | [AcquisitionMode](COM_Reference/Properties/AcquisitionMode_Property.md)  
Sweep Frequency Per Power (2D) | [SENSe:GCSetup:AMODe](GP-IB_Command_Finder/Sense/Gain_Compression.md#Amode) | [AcquisitionMode](COM_Reference/Properties/AcquisitionMode_Property.md)  
Sweep Settings  
Number of Points | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) | [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
IF Bandwidth | [SENSe:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) | [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Start | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Center | [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) | [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Span | [SENSe:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Frequency.md#span) | [FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
DUT Input Port  
Input Port | [SENSe:GCSetup:PMAP](GP-IB_Command_Finder/Sense/Gain_Compression.md#portMap) | [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Linear Input Power | [SENSe:GCSetup:POWer:LINear:INPut:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#InpPwer) | [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Source Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
DUT Output Port  
Output Port | [SENSe:GCSetup:PMAP](GP-IB_Command_Finder/Sense/Gain_Compression.md#portMap) | [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Reverse Power | [SENSe:GCSetup:POWer:REVerse:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#REVpower) | [ReverseLinearPowerLevel](COM_Reference/Properties/ReverseLinearPowerLevel_Property.md)  
Source Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Power Sweep  
Start (Min) Power | [SENSe:GCSetup:POWer:STARt:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#startPower) | [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop (Max) Power | [SENSe:GCSetup:POWer:STOP:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#stopPower) | [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
Power Points | [SENSe:GCSetup:SWEep:FREQuency:POINts](GP-IB_Command_Finder/Sense/Gain_Compression.md#powerPoints) | [NumberOfPowerPoints](COM_Reference/Properties/NumberOfPowerPoints_Property.md)  
Power Step | None | None  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Compression  
Compression Method  
Compression from Linear Gain | [SENSe:GCSetup:COMPression:ALGorithm](GP-IB_Command_Finder/Sense/Gain_Compression.md#CompAlgorithm) | [CompressionAlgorithm](COM_Reference/Properties/CompressionAlgorithm_Property.md)  
Compression from Max Gain | [SENSe:GCSetup:COMPression:ALGorithm](GP-IB_Command_Finder/Sense/Gain_Compression.md#CompAlgorithm) | [CompressionAlgorithm](COM_Reference/Properties/CompressionAlgorithm_Property.md)  
Compression from Back Off | [SENSe:GCSetup:COMPression:ALGorithm](GP-IB_Command_Finder/Sense/Gain_Compression.md#CompAlgorithm) | [CompressionAlgorithm](COM_Reference/Properties/CompressionAlgorithm_Property.md)  
X/Y Compression | [SENSe:GCSetup:COMPression:ALGorithm](GP-IB_Command_Finder/Sense/Gain_Compression.md#CompAlgorithm) | [CompressionAlgorithm](COM_Reference/Properties/CompressionAlgorithm_Property.md)  
Compression from Saturation | [SENSe:GCSetup:COMPression:ALGorithm](GP-IB_Command_Finder/Sense/Gain_Compression.md#CompAlgorithm) | [CompressionAlgorithm](COM_Reference/Properties/CompressionAlgorithm_Property.md)  
Magnitude Level | [SENSe:GCSetup:COMPression:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#compLevel) | [CompressionLevel](COM_Reference/Properties/CompressionLevel_Property.md)  
Back Off | [SENSe:GCSetup:COMPression:BACKoff:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#backoff) | [CompressionBackoff](COM_Reference/Properties/CompressionBackoff_Property.md)  
Delta X | [SENSe:GCSetup:COMPression:DELTa:X](GP-IB_Command_Finder/Sense/Gain_Compression.md#deltaX) | [CompressionDeltaX](COM_Reference/Properties/CompressionDeltaX_Property.md)  
Delta Y | [SENSe:GCSetup:COMPression:DELTa:Y](GP-IB_Command_Finder/Sense/Gain_Compression.md#deltaY) | [CompressionDeltaY](COM_Reference/Properties/CompressionDeltaY_Property.md)  
From Max Pout | [SENSe:GCSetup:COMPression:SATuration:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#SatLevel) | [SaturationLevel](COM_Reference/Properties/SaturationLevel_Property.md)  
Magnitude Only | [SENSe:GCSetup:COMPression:PHASe:MODE](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:COMPression:PHASe:MODE) | None  
Phase Only | [SENSe:GCSetup:COMPression:PHASe:MODE](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:COMPression:PHASe:MODE) | None  
Magnitude or Phase | [SENSe:GCSetup:COMPression:PHASe:MODE](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:COMPression:PHASe:MODE) | None  
Phase Level | [SENSe:GCSetup:COMPression:PHASe:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:COMPression:PHASe:LEVel) | None  
Phase Details... |  |   
Compute Linear Power from Percent of Span | [SENSe:GCSetup:POWer:LINear:INPut:COMPute:APERture](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:POWer:LINear:INPut:COMPute:APERture) | None  
Force Source Power Out Port 1 | [SENSe:GCSetup:PMAP:SOURce:OVERride](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:PMAP:SOURce:OVERride) | None  
SMART Sweep  
Tolerance | [SENSe:GCSetup:SMARt:TOLerance](GP-IB_Command_Finder/Sense/Gain_Compression.md#smartToler) | [SmartSweepTolerance](COM_Reference/Properties/SmartSweepTolerance_Property.md)  
Maximum Iterations | [SENSe:GCSetup:SMARt:MITerations](GP-IB_Command_Finder/Sense/Gain_Compression.md#smartMiter) | [SmartSweepMaximumIterations](COM_Reference/Properties/SmartSweepMaximumIterations_Property.md)  
Show Iterations | [SENSe:GCSetup:SMARt:SITerations](GP-IB_Command_Finder/Sense/Gain_Compression.md#Siterations) | [SmartSweepShowIterations](COM_Reference/Properties/SmartSweepShowIterations_Property.md)  
Read DC at Compression Point | [SENSe:GCSetup:SMARt:CDC](GP-IB_Command_Finder/Sense/Gain_Compression.md#SENSe:GCSetup:SMARt:CDC) | [ReadDCAtCompression](COM_Reference/Properties/ReadDCAtCompression_Property.md)  
Safe Mode... |  |   
Safe Mode | [SENSe:GCSetup:SAFE:ENABle](GP-IB_Command_Finder/Sense/Gain_Compression.md#SafeEnable) | [SafeSweepEnable](COM_Reference/Properties/SafeSweepEnable_Property.md)  
Coarse Increment | [SENSe:GCSetup:SAFE:CPADjustment](GP-IB_Command_Finder/Sense/Gain_Compression.md#SafeCourse) | [SafeSweepCoarsePowerAdjustment](COM_Reference/Properties/SafeSweepCoarsePowerAdjustment_Property.md)  
Fine Increment | [SENSe:GCSetup:SAFE:FPADjustment](GP-IB_Command_Finder/Sense/Gain_Compression.md#SafeFine) | [SafeSweepFinePowerAdjustment](COM_Reference/Properties/SafeSweepFinePowerAdjustment_Property.md)  
Fine Threshold | [SENSe:GCSetup:SAFE:FTHReshold](GP-IB_Command_Finder/Sense/Gain_Compression.md#safeThresh) | [SafeSweepFineThreshold](COM_Reference/Properties/SafeSweepFineThreshold_Property.md)  
Max Output Power | [SENSe:GCSetup:SAFE:MLimit](GP-IB_Command_Finder/Sense/Gain_Compression.md#SaveMaxPwr) | [SafeSweepMaximumLimit](COM_Reference/Properties/SafeSweepMaximumLimit_Property.md)  
2D Sweep  
Compression Point Interpolation | [SENSe:GCSetup:COMPression:INTerpolation](GP-IB_Command_Finder/Sense/Gain_Compression.md#comInterp) | [CompressionInterpolation](COM_Reference/Properties/CompressionInterpolation_Property.md)  
|  |   
End of Sweep Condition | [SENSe:GCSetup:EOSoperation](GP-IB_Command_Finder/Sense/Gain_Compression.md#eos) | [EndOfSweepOperation](COM_Reference/Properties/EndOfSweepOperation_Property.md)  
Settling Time | [SENSe:GCSetup:SMARt:STIMe](GP-IB_Command_Finder/Sense/Gain_Compression.md#Settling) | [SmartSweepSettlingTime](COM_Reference/Properties/SmartSweepSettlingTime_Property.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Quick Start... | S-Param | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Layout Tab Commands  
Softkey | Sub-item | SCPI | COM  
New Trace |  | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
New Channel |  | None | [chans.Add](COM_Reference/Methods/Add_channels_Method.md)  
New Window |  | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) | [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
New Sheet |  | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) | None  
Delete | TrN | [DISPlay:WINDow:TRACe:DELete](GP-IB_Command_Finder/Display.md#tdel) | None  
ChN | [SYSTem:CHANnels:DELete](GP-IB_Command_Finder/System.md#ChanDelete) | [RemoveChannelNumber](COM_Reference/Methods/RemoveChannelNumber_Method.md)  
WinN | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) | [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
Select | TrN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | None  
ChN | None | None  
WinN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | None  
Measure... | S21, S11, S12, S22, AI1, AI2, CompIn21, CompOut21, DeltaGain21, CompGain21, CompS11, Ref21, CompAI1, CompAI2 | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)

