# Cal Commands - Active Hot Parameters

Click [here](CF_Cal_Commands.md) to view links to Cal commands for all
Measurement Classes.

Main | Cal Sets  
& Cal Kits | Fixtures  
---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
[Cal All...](CF_Cal_Commands_-_Standard.md#Cal_All) |  |  |   
[Correction](CF_Cal_Commands_-_Standard.md#Correction) |  |  |   
Src Power Correct | ON/OFF | [SOURce:POWer:CORRection[:STATe]](GP-IB_Command_Finder/SourceCorrection.md#state) | [SourcePowerCorrection](COM_Reference/Properties/SourcePowerCorrection_Property.md)  
Interpolation | ON/OFF | [SENSe:CORRection:INTerpolate[:STATe]](GP-IB_Command_Finder/Sense/Sense_Correction.md#scis) | [InterpolateCorrection](COM_Reference/Properties/Interpolate_Correction_Property.md)  
Correction Properties... |  | None | [Properties](COM_Reference/Properties/Properties_Property.md)  
Cal Sets & Cal Kits Tab Commands  
Softkey | Sub-item | SCPI | COM  
[Cal Set...](CF_Cal_Commands_-_Standard.md#Cal_Set) |  | [CSET](GP-IB_Command_Finder/CSET.md) |   
Cal Set Viewer | ON/OFF | [DISPlay:TOOL:CSET[:STATe]](GP-IB_Command_Finder/Display.md#DISPlay:TOOLbar:CSET:STATe) | None  
[Cal Kit...](CF_Cal_Commands_-_Standard.md#Cal_Kit) |  |  |   
[ECal...](CF_Cal_Commands_-_Standard.md#E_Cal) |   
[Cal Pod...](CF_Cal_Commands_-_Standard.md#Cal_Pod) |  |  |   
Fixtures Tab Commands  
Softkey | Sub-item | SCPI | COM  
Apply Fixtures | ON/OFF | [CALCulate:FSIMulator:STATe](GP-IB_Command_Finder/Calculate/FSimulator.md#FSimState) | [FixturingState](COM_Reference/Properties/FixturingState_Property.md)  
Power Comp... | Port N | [CALC:FSIM:SEND:POW:PORT:COMP](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#PowerPortComp) | [EnablePowerCompensation](COM_Reference/Properties/EnablePowerCompensation_Property.md)  
[Fixture Setup](CF_Cal_Commands_-_Standard.md#Fixture_Setup) |  |  |   
Cal Plane Manager... | Characterize a fixture | [CSET:FIXTure:CHARacterize](GP-IB_Command_Finder/CSET.md#fixtureCharacter) | [CharacterizeFixture](COM_Reference/Methods/CharacterizeFixture_Method.md)  
Creates a single S2P file from two existing files | [CSET:FIXTure:CASCade](GP-IB_Command_Finder/CSET.md#FIXTureCASCade) | [CascadeS2PFiles](COM_Reference/Methods/CascadeS2PFiles_Method.md)

