# Power Commands - Swept IMD and Swept IMD Converters Measurement Class

Only the Main and Leveling & Offsets Power commands corresponding to the Swept
IMD and Swept IMD Converters measurement classes are documented here. The Port
Power and Attenuators commands are identical to the Port Power and Attenuator
commands for the Standard measurement class and can be accessed by clicking on
the softtab on the graphic below.

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main | [Port Power](CF_Power_Commands_-_Standard.md#Port_Power_Tab_Commands) | Leveling  
& Offsets | [Attenuators](CF_Power_Commands_-_Standard.md#Attenuators_Tab_Commands)  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Tone Power |  | [SENSe:IMD:TPOWer:F1](GP-IB_Command_Finder/Sense/IMD.md#TPowf1) [SENSe:IMD:TPOWer:F2](GP-IB_Command_Finder/Sense/IMD.md#TPowF2) | [TonePower](COM_Reference/Properties/TonePower_Property.md) [TonePower](COM_Reference/Properties/TonePower_Property.md)  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Start Power |  | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) | [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power |  | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
[Power and Attenuators...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |  |   
[IMD Setup...](CF_Setup_Commands_-_IMD.md#Swept_IMD_Setup_Commands) (Swept IMD Measurement Class only) |  |  |   
[IMDX Setup...](CF_Setup_Commands_-_IMDX.md#IMDX_Setup...) (Swept IMD Converters Measurement Class only) |  |  |   
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

