# Setup Commands - Active Hot Parameters

Only the Main Setup commands corresponding to the Active Hot Parameters
measurement class are documented here. All other commands are identical to the
Setup commands for the Standard measurement class and can be accessed by
clicking [here](CF_Setup_Commands_-_Standard.md) or by clicking on the
softtabs on the graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main | [Layout](CF_Setup_Commands_-_Standard.md#Customize_Meas_Commands) | [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) | [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) | [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Sweep Setup... | Sweep  
Sweep Type | [SENSe:ACTive:SWEep:TYPE](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:TYPE) | [SweepType](COM_Reference/Properties/SweepType_Property.md)  
Source |  |   
Start Frequency | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Center Frequency | [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) | [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Stop Frequency | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
Frequency Span | [SENSe:FREQuency:SPAN](GP-IB_Command_Finder/Sense/Frequency.md#span) | [FrequencySpan](COM_Reference/Properties/Frequency_Span_Property.md)  
Frequency Sweep | [SENSe:ACTive:SWEep:TYPE](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:TYPE) | [SweepType](COM_Reference/Properties/SweepType_Property.md)  
Number of Frequencies | [SENSe:SWEep:STEP](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Step) | [FrequencyStep](COM_Reference/Properties/FrequencyStep_Property.md)  
Power Level | [SENSe:ACTive:DISPlay:TRACe:IPWer](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:DISPlay:TRACe:IPWer) | [DisplayInputPower](COM_Reference/Properties/DisplayInputPower_Property.md)  
Start Power | [SENSe:ACTive:SWEep:POWer:STARt](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:POWer:STARt) | [StartPowerIn3DSweep](COM_Reference/Properties/StartPowerIn3DSweep_Property.md)  
Stop Power | [SENSe:ACTive:SWEep:POWer:STOP](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:POWer:STOP) | [StopPowerIn3DSweep](COM_Reference/Properties/StopPowerIn3DSweep_Property.md)  
Number Of Powers | [SENSe:ACTive:SWEep:POWer:STEP](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:POWer:STEP) | [PowerStepsIn3DSweep](COM_Reference/Properties/PowerStepsIn3DSweep_Property.md)  
CW Frequency | [SENSe:FREQuency:CW](GP-IB_Command_Finder/Sense/Frequency.md#cw) | [CWFrequency](COM_Reference/Properties/CW_Frequency_Property.md)  
Extraction |  |   
IF Bandwidth | [SENSe:BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) | [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Absolute Power | [SENSe:ACTive:TTONe:MODE](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:TTONe:MODE) [SENSe:ACTive:TTONe:ABSolute](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:TTONe:ABSolute) | [ExtractionToneMode](COM_Reference/Properties/ExtractionToneMode_Property.md) [AbsoluteExtractionToneLevel](COM_Reference/Properties/AbsoluteExtractionToneLevel_Property.md)  
Relative to Input Power | [SENSe:ACTive:TTONe:MODE](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:TTONe:MODE) [SENSe:ACTive:TTONe:RELative](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:TTONe:RELative) | [ExtractionToneMode](COM_Reference/Properties/ExtractionToneMode_Property.md) [RelativeExtractionToneLevel](COM_Reference/Properties/RelativeExtractionToneLevel_Property.md)  
Number of Phases | [SENSe:ACTive:SWEep:PHASe:POINt](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:PHASe:POINts) | [PhaseSweepPoints](COM_Reference/Properties/PhaseSweepPoints_Property.md)  
DC |  |   
[DC Sources...](XTraceChanTopic.md#DC) |  |   
RF Path  
Power On - all channels | None | None  
Source |  |   
Source Port | None | [SelectPort](COM_Reference/Properties/SelectPort_Property.md)  
Source Attenuator | [SOURce:POWer<port>:ATTenuation](GP-IB_Command_Finder/source.md#attval) | [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver A Attenuator | [SENSe:POWer:ATTenuator](../GUI_Reference/Power.md) | [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
ALC Hardware | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Receiver Leveling | [SOURce:POWer:ALC[:MODE]:RECeiver](GP-IB_Command_Finder/SourceRxLeveling.md#RecLevMode) | [State](COM_Reference/Properties/State_rx_Property.md)  
Extraction |  |   
Extraction Port | None | [SelectPort](COM_Reference/Properties/SelectPort_Property.md)  
Source Attenuator | [SOURce:POWer<port>:ATTenuation](GP-IB_Command_Finder/source.md#attval) | [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver C Attenuator | [SENSe:POWer:ATTenuator](../GUI_Reference/Power.md) | [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
ALC Hardware | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Receiver Leveling | [SOURce:POWer:ALC[:MODE]:RECeiver](GP-IB_Command_Finder/SourceRxLeveling.md#RecLevMode) | [State](COM_Reference/Properties/State_rx_Property.md)  
[RF Path Config...](XTraceChanTopic.md#Path) |  |   
X-axis  
Active | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
Select all traces | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | [View](COM_Reference/Properties/View_Property.md)  
X-axis display | [SENSe:ACTive:SWEep:TYPE](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:SWEep:TYPE) | [SweepType](COM_Reference/Properties/SweepType_Property.md)  
Fixed Parameters |  |   
Input Power | [SENSe:ACTive:DISPlay:TRACe:IPWer](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:DISPlay:TRACe:IPWer) | [DisplayInputPower](COM_Reference/Properties/DisplayInputPower_Property.md)  
Frequency | [SENSe:FREQuency:CENTer](GP-IB_Command_Finder/Sense/Frequency.md#cent) | [CenterFrequency](COM_Reference/Properties/CenterFreq_Property.md)  
Enable Interpolation | [SENSe:ACTive:DISP:INTerpolate[:STATe]](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:DISP:INTerpolate:STATe) | [DisplayInterpolationState](COM_Reference/Properties/DisplayInterpolationState_Property.md)  
Name (DC source) | None | None  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Quick Start... | S-Param | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Balanced | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [BalSMeasurement](COM_Reference/Properties/BalSMeasurement_Property.md) [BBalMeasurement](COM_Reference/Properties/BBalMeasurement_Property.md) [SBalMeasurement](COM_Reference/Properties/SBalMeasurement_Property.md) [SSBMeasurement](COM_Reference/Properties/SSBMeasurement_Property.md)  
Other | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)

