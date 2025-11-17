# Power Commands - Gain Compression and Gain Compression Converters
Measurement Classes

Only the Main, Compression Levels, and Leveling & Offsets Power commands
corresponding to the Gain Compressions and Gain Compression Converters
measurement classes are documented here. The Attenuators commands are
identical to the Attenuator commands for the Standard measurement class and
can be accessed by clicking [here](CF_Power_Commands_-
_Standard.htm#Attenuators_Tab_Commands) or by clicking on the softtab on the
graphic below.

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main | Compress  
Levels | Leveling  
& Offsets | [Attenuators](CF_Power_Commands_-_Standard.md#Attenuators_Tab_Commands)  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Linear Input Pwr |  | [SENSe:GCSetup:POWer:LINear:INPut:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#InpPwer) | [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Start Power |  | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) | [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power |  | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
[Power and Attenuators...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |  |   
[GCA Setup...](CF_Setup_Commands_-_GCA.md#Gain_Compression_Setup_Commands) (Gain Compression Measurement Class only) |  |  |   
[GCX Setup...](CF_Setup_Commands_-_GCX.md#GCX_Setup...) (Gain Compression Converters Measurement Class only) |  |  |   
Compress Levels Tab Commands  
Softkey | Sub-item | SCPI | COM  
Comp Method | Linear Gain | [SENSe:GCSetup:POWer:LINear:INPut:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#InpPwer) | [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Max Gain | [SENSe:GCSetup:COMPression:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#compLevel) | [CompressionLevel](COM_Reference/Properties/CompressionLevel_Property.md)  
Backoff | [SENSe:GCSetup:COMPression:BACKoff:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#backoff) | [CompressionBackoff](COM_Reference/Properties/CompressionBackoff_Property.md)  
XY | [SENSe:GCSetup:COMPression:DELTa:X](GP-IB_Command_Finder/Sense/Gain_Compression.md#deltaX) [SENSe:GCSetup:COMPression:DELTa:Y](GP-IB_Command_Finder/Sense/Gain_Compression.md#deltaY) | [CompressionDeltaX](COM_Reference/Properties/CompressionDeltaX_Property.md) [CompressionDeltaY](COM_Reference/Properties/CompressionDeltaY_Property.md)  
Saturation | [SENSe:GCSetup:COMPression:SATuration:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#SatLevel) | [CompressionSaturation](COM_Reference/Properties/CompressionSaturation_Property.md)  
Linear Input Pwr |  | [SENSe:GCSetup:POWer:LINear:INPut:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#InpPwer) | [InputLinearPowerLevel](COM_Reference/Properties/InputLinearPowerLevel_Property.md)  
Reverse Pwr |  | [SENSe:GCSetup:POWer:REVerse:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#REVpower) | [ReverseLinearPowerLevel](COM_Reference/Properties/ReverseLinearPowerLevel_Property.md)  
Compression Level |  | [SENSe:GCSetup:COMPression:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#compLevel) | [CompressionLevel](COM_Reference/Properties/CompressionLevel_Property.md)  
Back Off Level |  | [SENSe:GCSetup:COMPression:BACKoff:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#backoff) | [CompressionBackoff](COM_Reference/Properties/CompressionBackoff_Property.md)  
Delta X |  | [SENSe:GCSetup:COMPression:DELTa:X](GP-IB_Command_Finder/Sense/Gain_Compression.md#deltaX) | [CompressionDeltaX](COM_Reference/Properties/CompressionDeltaX_Property.md)  
Delta Y |  | [SENSe:GCSetup:COMPression:DELTa:Y](GP-IB_Command_Finder/Sense/Gain_Compression.md#deltaY) | [CompressionDeltaY](COM_Reference/Properties/CompressionDeltaY_Property.md)  
Saturation |  | [SENSe:GCSetup:COMPression:SATuration:LEVel](GP-IB_Command_Finder/Sense/Gain_Compression.md#SatLevel) | [CompressionSaturation](COM_Reference/Properties/CompressionSaturation_Property.md)  
Leveling & Offsets Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | Port 1 | None | None  
Port 2 | None | None  
Port 3 | None | None  
Port 4 | None | None  
Port 1 Src2 | None | None  
Source3 | None | None  
Offset |  | [SOURce:POWer:ALC[:MODE]:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) | [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Limit | ON/OFF | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) | [State](COM_Reference/Properties/State_Property.md)  
Power Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) | [Limit](COM_Reference/Properties/Limit_Property.md)  
[Offsets and Limits...](CF_Power_Commands_-_Standard.md#Offsets_and_Limits) |  |  |   
ALC Hardware | Internal | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Open Loop | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
[Receiver Leveling...](CF_Power_Commands_-_Standard.md#Receiver_Leveling) |  |  | 

