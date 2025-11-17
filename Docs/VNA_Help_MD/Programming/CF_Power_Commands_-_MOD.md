# Power Commands - Modulation Distortion and Modulation Distortion Converters
Measurement Class

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main | Leveling  
& Offsets  
---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Carrier Level |  | [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel) | None  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
S-Param Input Pwr |  | [SENSe:DISTortion:SWEep:POWer:SPARam:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:SPARam:LEVel) [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT) | None None  
Start Power |  | [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel) [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT) | None None  
Stop Power |  | [SENSe:DISTortion:SWEep:POWer:CARRier:LEVel](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel) | None  
[Power and Attenuators...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |  |   
[MOD Setup...](CF_Setup_Commands_-_MOD.md) |  |  |   
[MODX Setup...](CF_Setup_Commands_-_MOD.md) |  |  |   
Leveling & Offsets Tab Commands  
Softkey | Sub-item | SCPI | COM  
Offset |  | [SOURce:POWer:CORRection:OFFSet:MAGNitude](GP-IB_Command_Finder/SourceCorrection.md#offset) | [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Limit | ON/OFF | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) | [State](COM_Reference/Properties/State_Property.md)  
Power Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) | [Limit](COM_Reference/Properties/Limit_Property.md)  
[Offsets and Limits...](CF_Power_Commands_-_Standard.md#Offsets_and_Limits) |  |  |   
Receiver Leveling... | Receiver Leveling... (VNAs with Pre-Sweep Mode, Point Mode, and Prior Sweep Mode)  
Controlled Source | [SOURce:POWer:ALC[:MODE]:RECeiver:REFerence](GP-IB_Command_Finder/SourceRxLeveling.md#RecRef) | [ReferenceReceiver](COM_Reference/Properties/ReferenceReceiver_Property.md)  
Enable Leveling | [SOURce:POWer:ALC[:MODE]:RECeiver](GP-IB_Command_Finder/SourceRxLeveling.md#RecLevMode) | [State](COM_Reference/Properties/State_rx_Property.md)  
Leveling Receiver | [SOURce:POWer:ALC[:MODE]:RECeiver:REFerence](GP-IB_Command_Finder/SourceRxLeveling.md#RecRef) | [ReferenceReceiver](COM_Reference/Properties/ReferenceReceiver_Property.md)  
Leveling Type | [SOURce:POWer:ALC[:MODE]:RECeiver:ACQuisition:MODE](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ACQ:MODE) | None  
Max Power | [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE:MAX](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMax) | [PowerMax](COM_Reference/Properties/PowerMax_Property.md)  
Min Power | [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE:MIN](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMin) | [PowerMin](COM_Reference/Properties/PowerMin_Property.md)  
Enable Safe Mode Leveling Using Max Step Size | [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeMode) | [SafeMode](COM_Reference/Properties/SafeMode_Property.md)  
Max step size | [SOURce:POWer:ALC[:MODE]:RECeiver:SAFE:STEP](GP-IB_Command_Finder/SourceRxLeveling.md#recSafeStep) | [PowerStep](COM_Reference/Properties/PowerStep_Property.md)  
Update Source Power Calibration with Leveling Data | [SOURce:POWer:ALC[:MODE]:RECeiver:LSPC](GP-IB_Command_Finder/SourceRxLeveling.md#LSPC) | [LastLevelingAsSPC](COM_Reference/Properties/LastLevelingAsSPC_Property.md)  
Source ALC Hardware | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Leveling Tolerance | [SOURce:POWer:ALC[:MODE]:RECeiver:TOLerance](GP-IB_Command_Finder/SourceRxLeveling.md#recToler) | [Tolerance](COM_Reference/Properties/Tolerance_Property.md)  
Leveling Max Iterations | [SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:VALue](GP-IB_Command_Finder/SourceRxLeveling.md#recIteration) [SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:ENABle](GP-IB_Command_Finder/SourceRxLeveling.md#SOURce:POWer:ALC:MODE:RECeiver:ITERation:ENABle) | [IterationNumber](COM_Reference/Properties/IterationNumber_Property.md) None  
Leveling IFBW | [SOURce:POWer:ALC[:MODE]:RECeiver:IFBW](GP-IB_Command_Finder/SourceRxLeveling.md#recIFBW) | [LevelingIFBW](COM_Reference/Properties/LevelingIFBW_Property.md)  
Leveling Receiver Frequency | [SOURce:POWer:ALC[:MODE]:RECeiver:FTYPe](GP-IB_Command_Finder/SourceRxLeveling.md#FType) | [FrequencyType](COM_Reference/Properties/FrequencyType_Property.md)  
|  |   
|  |   
|  |   
|  | 

