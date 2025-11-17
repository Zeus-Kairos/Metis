# Power Commands - Spectrum Analyzer Measurement Class

Only the Main, Port Power, and Leveling & Offsets Power commands corresponding
to the Spectrum Analyzer measurement class are documented here. The
Attenuators commands are identical to the Attenuator commands for the Standard
measurement class and can be accessed by clicking [here](CF_Power_Commands_-
_Standard.htm#Attenuators_Tab_Commands) or by clicking on the softtab on the
graphic below.

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main | Port Power | Leveling  
& Offsets | [Attenuators](CF_Power_Commands_-_Standard.md#Attenuators_Tab_Commands)  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
[Power and Attenuators...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |  |   
[SA Setup...](CF_Setup_Commands_-_SA.md) |  |  |   
Port Power Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | Port 1 | None | None  
Port 2 | None | None  
Port 3 | None | None  
Port 4 | None | None  
Port 1 Src2 | None | None  
Source3 | None | None  
Power Level |  | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) | [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Source State | AUTO | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
ON | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
OFF | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Coupling | ON | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) | [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
OFF | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) | [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
Leveling & Offsets Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | Port 1 | None | None  
Port 2 | None | None  
Port 3 | None | None  
Port 4 | None | None  
Port 1 Src2 | None | None  
Source3 | None | None  
Slope | ON/OFF | [SOURce:POWer[:LEVel]:SLOPe:STATe](GP-IB_Command_Finder/source.md#slpON) | [PowerSlopeState](COM_Reference/Properties/PowerSlopeState_Property.md)  
Power Slope | [SOURce:POWer[:LEVel]:SLOPe](GP-IB_Command_Finder/source.md#slope) | [PowerSlope](COM_Reference/Properties/Power_Slope_Property.md)  
Offset |  | [SOURce:POWer:CORRection:OFFSet:MAGNitude](GP-IB_Command_Finder/SourceCorrection.md#offset) | [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Limit | ON/OFF | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) | [State](COM_Reference/Properties/State_Property.md)  
Power Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) | [Limit](COM_Reference/Properties/Limit_Property.md)  
[Offsets and Limits...](CF_Power_Commands_-_Standard.md#Offsets_and_Limits) |  |  |   
ALC Hardware | Internal | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Open Loop | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)

