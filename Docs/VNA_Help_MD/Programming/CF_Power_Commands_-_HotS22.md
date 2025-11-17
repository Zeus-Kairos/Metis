# Power Commands - Active Hot Parameters

Only the Main and Leveling & Offsets Power commands corresponding to the
Active Hot Parameters measurement classes are documented here. The Port Power
and Attenuators commands are identical to the Attenuator commands for the
Standard measurement class and can be accessed by clicking
[here](CF_Power_Commands_-_Standard.md) or by clicking on the softtab on the
graphic below.

Click [here](CF_Power_Commands.md) to view links to Power commands for all
Measurement Classes.

Main | [Port Power](CF_Power_Commands_-_Standard.md#Port_Power_Tab_Commands) | Leveling  
& Offsets | [Attenuators](CF_Power_Commands_-_Standard.md#Attenuators_Tab_Commands)  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Power Level |  | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) [DISPlay:GUI:POWer:SPIN:RESolution](GP-IB_Command_Finder/Display.md#DISPlay:GUI:POWer:SPIN:RESolution) | [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md) [PowerSpinResolution](COM_Reference/Properties/PowerSpinResolution_Property.md)  
RF Power | ON/OFF | [OUTPut[:STATe]](GP-IB_Command_Finder/Output.md#RFOUt) [SENSe:ACTive:DISPlay:TRACe:IPWer](GP-IB_Command_Finder/Sense/XMatch.md#SENSe:HOTS:DISPlay:TRACe:IPWer) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md) [DisplayInputPower](COM_Reference/Properties/DisplayInputPower_Property.md)  
Start Power |  | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) | [StartPower](COM_Reference/Properties/Start_Power_Property.md)  
Stop Power |  | [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StopPower](COM_Reference/Properties/Stop_Power_Property.md)  
[Power and Attenuators...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |  |   
[AHP Setup...](CF_Freq_Commands_-_HotS22.md#AHP_Setup...) |  |  |   
Leveling & Offsets Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | Port 1 | None | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Port 2 | None | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Port 3 | None | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Port 4 | None | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Slope | ON/OFF | [SOURce:POWer[:LEVel]:SLOPe:STATe](GP-IB_Command_Finder/source.md#slpON) | [PowerSlopeState](COM_Reference/Properties/PowerSlopeState_Property.md)  
Power Slope | [SOURce:POWer[:LEVel]:SLOPe](GP-IB_Command_Finder/source.md#slope) | [PowerSlope](COM_Reference/Properties/Power_Slope_Property.md)  
Offset |  | [SOURce:POWer:CORRection:OFFSet:MAGNitude](GP-IB_Command_Finder/SourceCorrection.md#offset) | [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Limit | ON/OFF | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) | [State](COM_Reference/Properties/State_Property.md)  
Power Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) | [Limit](COM_Reference/Properties/Limit_Property.md)  
Offsets and Limits... | Power Limit - State | [SYSTem:POWer:LIMit:STATe](GP-IB_Command_Finder/System.md#PowerLimState) | [State](COM_Reference/Properties/State_Property.md)  
Power Limit - Limit | [SYSTem:POWer:LIMit](GP-IB_Command_Finder/System.md#powerLimit) | [Limit](COM_Reference/Properties/Limit_Property.md)  
Source Power | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) | [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
Power Offset | [SOURce:POWer:ALC[:MODE]:RECeiver:OFFSet](GP-IB_Command_Finder/SourceRxLeveling.md#recOffset) | [PowerOffset](COM_Reference/Properties/PowerOffset_Property.md)  
Port Power | [SOURce:POWer:PORT:STARt](GP-IB_Command_Finder/source.md#PortStart) [SOURce:POWer:PORT:STOP](GP-IB_Command_Finder/source.md#PortStop) | [StartPower](COM_Reference/Properties/Start_Power_Property.md) [StopPower](COM_Reference/Properties/Stop_Power_Property.md)

