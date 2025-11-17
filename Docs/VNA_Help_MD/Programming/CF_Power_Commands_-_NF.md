# Power Commands - Noise Figure Cold Source and Noise Figure Converters
Measurement Classes

Only the Main and Leveling & Offsets Power commands corresponding to the Noise
Figure Source and Noise Figure Converters measurement classes are documented
here. The Port Power and Attenuators commands are identical to the Port Power
and Attenuator commands for the Standard measurement class and can be accessed
by clicking on the softtab on the graphic below.

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main | [Port Power](CF_Power_Commands_-_Standard.md#Port_Power_Tab_Commands) | Leveling  
& Offsets | [Attenuators](CF_Power_Commands_-_Standard.md#Attenuators_Tab_Commands)  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Power Level |  | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) [DISPlay:GUI:POWer:SPIN:RESolution](GP-IB_Command_Finder/Display.md#DISPlay:GUI:POWer:SPIN:RESolution) | [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md) [PowerSpinResolution](COM_Reference/Properties/PowerSpinResolution_Property.md)  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Noise Source (Keypress only works for noise sources connected to the 28 V of the VNA. For USB noise sources, the SCPI command must be used.) | ON/OFF | [OUTPut:MANual:NOISe[:STATe]](GP-IB_Command_Finder/Output.md#NoiseState) | [NoiseSourceState](COM_Reference/Properties/NoiseSourceState_Property.md)  
[Power and Attenuators...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |  |   
[NF Setup...](CF_Setup_Commands_-_NF.md#NF_Setup...) (Noise Figure Measurement Class only) |  |  |   
[NFX Setup...](CF_Setup_Commands_-_NFX.md#NFX_Setup...) (Noise Figure Converters Measurement Class only) |  |  |   
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
Offset |  | [SOURce:POWer:ALC[:MODE]:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) | [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Limit | ON/OFF | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) | [State](COM_Reference/Properties/State_Property.md)  
Power Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) | [Limit](COM_Reference/Properties/Limit_Property.md)  
[Offsets and Limits...](CF_Power_Commands_-_Standard.md#Offsets_and_Limits) |  |  |   
ALC Hardware | Internal | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
Open Loop | [SOURce:POWer:ALC[:MODE]](GP-IB_Command_Finder/source.md#ALCMode) | [ALCLevelingMode](COM_Reference/Properties/ALCLevelingMode_Property.md)  
[Receiver Leveling...](CF_Power_Commands_-_Standard.md#Receiver_Leveling) |  |  | 

