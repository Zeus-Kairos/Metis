# Setup Commands - Noise Figure Measurement Class

Only the Main and Layout Setup commands corresponding to the Noise Figure
measurement class are documented here. All other commands are identical to the
Setup commands for the Standard measurement class and can be accessed by
clicking [here](CF_Setup_Commands_-_Standard.md) or by clicking on the
softtabs on the graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main |  Layout |  [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) |  [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) |  [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI |  COM  
NF Setup... | Frequency  
Sweep Type  
Linear Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Log Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
CW Frequency | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Segment Sweep | [SENSe:SWEep:TYPE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssty) |  [SweepType](COM_Reference/Properties/Sweep_Type_Property.md)  
Sweep Settings  
Number of Points | [SENSe:SWEep:POINts](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssp) |  [NumberOfPoints](COM_Reference/Properties/Number_of__Points_Property.md)  
IF Bandwidth | [SENSe:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) |  [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Start | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) |  [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) |  [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Center | [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) |  [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Span | [SENSe:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Frequency.md#span) |  [FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Power  
Power On (All Channels) | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) |  [SourcePowerState](COM_Reference/Properties/Source_Power_State_Property.md)  
DUT Input Port |  |   
Input Port | [SENSe:NOISe:PMAP](GP-IB_Command_Finder/Sense/Noise.md#pmapSet) |  [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Power Level | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Source Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
DUT Output Port  
Output Port | [SENSe:NOISe:PMAP](GP-IB_Command_Finder/Sense/Noise.md#pmapSet) |  [SetPortMap](COM_Reference/Methods/SetPortMap_Method.md)  
Power Level | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Source Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
Noise Figure  
Bandwidth/Average |  |   
Noise Bandwidth | [SENSe:NOISe:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Noise.md#bwid) |  [NoiseBandwidth](COM_Reference/Properties/NoiseBandwidth_Property.md)  
Average Number | [SENSe:NOISe:AVERage[:COUNt]](GP-IB_Command_Finder/Sense/Noise.md#Average) |  [NoiseAverageFactor](COM_Reference/Properties/NoiseAverageFactor_Property.md)  
Average ON | [SENSe:NOISe:AVERage:STATe](GP-IB_Command_Finder/Sense/Noise.md#avgState) |  [NoiseAverageState](COM_Reference/Properties/NoiseAverageState_Property.md)  
Use Narrowband Compensation | [SENSe:NOISe:NARRowband[:STATe]](GP-IB_Command_Finder/Sense/Noise.md#Narrowband) |  [NarrowBand](COM_Reference/Properties/NarrowBand_Property.md)  
Noise Receiver  
External Noise Amplifier | [SENSe:NOISe:AMPLifier](GP-IB_Command_Finder/Sense/Noise.md#Amplifier) |  None  
NA Receiver (Port 2) | [SENSe:NOISe:RECeiver](GP-IB_Command_Finder/Sense/Noise.md#Receiver) |  [NoiseReceiver](COM_Reference/Properties/NoiseReceiver_Property.md)  
Noise Receiver | [SENSe:NOISe:RECeiver](GP-IB_Command_Finder/Sense/Noise.md#Receiver) |  [NoiseReceiver](COM_Reference/Properties/NoiseReceiver_Property.md)  
Receiver Gain | [SENSe:NOISe:GAIN](GP-IB_Command_Finder/Sense/Noise.md#gain) |  [NoiseGain](COM_Reference/Properties/NoiseGain_Property.md)  
Source Temperature |  [SENSe:NOISe:TEMPerature:SOURce](GP-IB_Command_Finder/Sense/Noise.md#SENSe:NOISe:TEMPerature:SOURce) [SENSe:NOISe:TEMPerature:SOURce:AUTO](GP-IB_Command_Finder/Sense/Noise.md#SENSe:NOISe:TEMPerature:SOURce:AUTO) |  None None  
Ambient Temperature | [SENSe:NOISe:TEMPerature:AMBient](GP-IB_Command_Finder/Sense/Noise.md#TempAmb) |  [AmbientTemperature](COM_Reference/Properties/AmbientTemperature_Property.md)  
Impedance States  
Max Acquired Impedance States | [SENSe:NOISe:IMPedance:COUNt](GP-IB_Command_Finder/Sense/Noise.md#ImpCount) |  [ImpedanceStates](COM_Reference/Properties/ImpedanceStates_Property.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Quick Start... | S-Param | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Layout Tab Commands  
Softkey | Sub-item | SCPI |  COM  
New Trace |  | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) |  [View](COM_Reference/Properties/View_Property.md)  
New Channel |  | None |  [chans.Add](COM_Reference/Methods/Add_channels_Method.md)  
New Window |  | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) |  [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
New Sheet |  | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) |  None  
Delete | TrN | [DISPlay:WINDow:TRACe:DELete](GP-IB_Command_Finder/Display.md#tdel) |  None  
ChN | [SYSTem:CHANnels:DELete](GP-IB_Command_Finder/System.md#ChanDelete) |  [RemoveChannelNumber](COM_Reference/Methods/RemoveChannelNumber_Method.md)  
WinN | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) |  [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
Select | TrN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) |  None  
ChN | None |  None  
WinN | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) |  None  
Measure... |  | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)

