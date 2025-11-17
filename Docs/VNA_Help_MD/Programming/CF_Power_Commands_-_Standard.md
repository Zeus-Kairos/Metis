# Power Commands - Standard Measurement Class

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main |  Port Power |  Leveling  
& Offsets |  Attenuators  
---|---|---|---  
  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI |  COM  
Power Level |  | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) [DISPlay:GUI:POWer:SPIN:RESolution](GP-IB_Command_Finder/Display.md#DISPlay:GUI:POWer:SPIN:RESolution) |  [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md) [PowerSpinResolution](COM_Reference/Properties/PowerSpinResolution_Property.md)  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Start Power |  | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) |  [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power |  | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) |  [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
Power and Attenuators... | Power ON (All Channels) | None |  None  
Port Powers Coupled | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) |  [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
Name | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
State | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Port Power | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Start Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) |  [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) |  [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
Leveling Mode | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Channel Power Slope | [SOURce:POWer[:LEVel]:SLOPe:STATe](GP-IB_Command_Finder/source.md#slpON) [SOURce:POWer[:LEVel]:SLOPe](GP-IB_Command_Finder/source.md#slope) |  [PowerSlopeState](COM_Reference/Properties/PowerSlopeState_Property.md) [PowerSlope](COM_Reference/Properties/Power_Slope_Property.md)  
Offsets and Limits...  
Power Limit - State | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) |  [State](COM_Reference/Properties/State_Property.md)  
Power Limit - Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) |  [Limit](COM_Reference/Properties/Limit_Property.md)  
Source Power | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Power Offset | [SOURce:POWer:ALC[:MODE]:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) |  [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Port Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) |  [StartPower](COM_Reference/Properties/Start_Power_Property.md) [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
Receiver Leveling... (VNAs with Pre-Sweep Mode, Point Mode, and Prior Sweep
Mode)  
Controlled Source |  [SOURce:POWer:ALC[:MODE]:RECeiver:REFerence](GP-IB_Command_Finder/SourceRxLeveling.md#RecRef) |  [ReferenceReceiver](COM_Reference/Properties/ReferenceReceiver_Property.md)  
Enable Leveling |  [SOURce:POWer:ALC[:MODE]:RECeiver](GP-IB_Command_Finder/SourceRxLeveling.md#RecLevMode) |  [State](COM_Reference/Properties/State_rx_Property.md)  
Leveling Receiver |  [SOURce:POWer:ALC[:MODE]:RECeiver:REFerence](GP-IB_Command_Finder/SourceRxLeveling.md#RecRef) |  [ReferenceReceiver](COM_Reference/Properties/ReferenceReceiver_Property.md)  
Leveling Type |  [SOURce:POWer:ALC[:MODE]:RECeiver:ACQuisition:MODE](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ACQ:MODE) |  None  
Max Power |  [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE:MAX](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMax) |  [PowerMax](COM_Reference/Properties/PowerMax_Property.md)  
Min Power |  [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE:MIN](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMin) |  [PowerMin](COM_Reference/Properties/PowerMin_Property.md)  
Enable Safe Mode Leveling Using Max Step Size |  [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMode) |  [SafeMode](COM_Reference/Properties/SafeMode_Property.md)  
Max step size |  [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE:STEP](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeStep) |  [PowerStep](COM_Reference/Properties/PowerStep_Property.md)  
Update Source Power Calibration with Leveling Data |  [SOURce:POWer:ALC[:MODE]:RECeiver:LSPC](GP-IB_Command_Finder/SourceRxLeveling.md#LSPC) |  [LastLevelingAsSPC](COM_Reference/Properties/LastLevelingAsSPC_Property.md)  
Source ALC Hardware |  [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Leveling Tolerance |  [SOURce:POWer:ALC[:MODE]:RECeiver:TOLerance](GP-IB_Command_Finder/SourceRxLeveling.md#recToler) |  [Tolerance](COM_Reference/Properties/Tolerance_Property.md)  
Leveling Max Iterations |  [SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:VALue](GP-IB_Command_Finder/SourceRxLeveling.md#recIteration) [SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:ENABle](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ITERation:ENABle) |  [IterationNumber](COM_Reference/Properties/IterationNumber_Property.md) None  
Leveling Receiver Frequency |  [SOURce:POWer:ALC[:MODE]:RECeiver:FTYPe](GP-IB_Command_Finder/SourceRxLeveling.md#FType) |  [FrequencyType](COM_Reference/Properties/FrequencyType_Property.md)  
Leveling IFBW |  [SOURce:POWer:ALC[:MODE]:RECeiver:FAST](GP-IB_Command_Finder/SourceRxLeveling.md#RecFast) [SOURce:POWer:ALC[:MODE]:RECeiver:IFBW](GP-IB_Command_Finder/SourceRxLeveling.md#recIFBW) |  [LevelingIFBW](COM_Reference/Properties/LevelingIFBW_Property.md)  
|  |   
|  |   
|  |   
|  |   
Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) |  [Element](COM_Reference/Properties/Element_Property.md)  
Port Power Tab Commands  
Softkey | Sub-item | SCPI |  COM  
Select | Port 1 |  None |  None  
Port 2 |  None |  None  
Port 3 |  None |  None  
Port 4 |  None |  None  
Port 1 Src2 |  None |  None  
Source3 |  None |  None  
Power Level |  | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Start Power |  | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) |  [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power |  | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) |  [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
Source State | AUTO | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
ON | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
OFF | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) |  [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Coupling | ON | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) |  [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
OFF | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) |  [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
Leveling & Offsets Tab Commands  
Softkey | Sub-item | SCPI |  COM  
Select | Port 1 |  None |  None  
Port 2 |  None |  None  
Port 3 |  None |  None  
Port 4 |  None |  None  
Port 1 Src2 |  None |  None  
Source3 |  None |  None  
Slope | ON/OFF | [SOURce:POWer[:LEVel]:SLOPe:STATe](GP-IB_Command_Finder/source.md#slpON) |  [PowerSlopeState](COM_Reference/Properties/PowerSlopeState_Property.md)  
Power Slope | [SOURce:POWer[:LEVel]:SLOPe](GP-IB_Command_Finder/source.md#slope) |  [PowerSlope](COM_Reference/Properties/Power_Slope_Property.md)  
Offset |  | [SOURce:POWer:CORRection:OFFSet:MAGNitude](GP-IB_Command_Finder/SourceCorrection.md#offset) |  [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Limit | ON/OFF | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) |  [State](COM_Reference/Properties/State_Property.md)  
Power Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) |  [Limit](COM_Reference/Properties/Limit_Property.md)  
Offsets and Limits... | Limit Source Pwr - State | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) |  [State](COM_Reference/Properties/State_Property.md)  
Limit Source Pwr- Limit Always | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) |  [Limit](COM_Reference/Properties/Limit_Property.md)  
Limit Source Pwr - Limit During Cal | [SYSTem:POWer:LIMit:CALibration](GP-IB_Command_Finder/System.md#PowLimCal) | None  
Source Power | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) |  [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Power Offset | [SOURce:POWer:ALC[:MODE]:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) |  [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Port Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) |  [StartPower](COM_Reference/Properties/Start_Power_Property.md) [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
ALC Hardware |  Internal |  [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Open Loop |  [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) |  [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Receiver Leveling... |  |  |   
Attenuators Tab Commands  
Softkey | Sub-item | SCPI |  COM  
Source Port 1 |  | [SOURce:POWer1:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Source Port 2 |  | [SOURce:POWer2:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Source Port 3 |  | [SOURce:POWer3:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Source Port 4 |  | [SOURce:POWer4:ATTenuation](GP-IB_Command_Finder/source.md#attval) |  [Attenuator](COM_Reference/Properties/Attenuator_Property.md)  
Receiver A |  | [SENSe:POWer:ATTenuation](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Receiver B |  | [SENSe:POWer:ATTenuation](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Receiver C |  | [SENSe:POWer:ATTenuation](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)  
Receiver D |  | [SENSe:POWer:ATTenuation](GP-IB_Command_Finder/Sense/Power.md) |  [ReceiverAttenuator](COM_Reference/Properties/Receiver_Attenuator_Property.md)

