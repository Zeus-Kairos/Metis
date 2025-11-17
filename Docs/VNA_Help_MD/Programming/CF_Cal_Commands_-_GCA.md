# Cal Commands - Gain Compression and Gain Compression Converters Measurement
Classes

Click [here](CF_Cal_Commands.md) to view links to Cal commands for all
Measurement Classes.

Main | Port  
Extension | Cal Sets  
& Cal Kits | Fixtures  
---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
[Smart Cal...](CF_Cal_Commands_-_Standard.md#Smart_Cal) |  |  |   
Other Cals | [Cal All...](CF_Cal_Commands_-_Standard.md#Cal_All) |  |   
[Source Power Cal...](CF_Cal_Commands_-_Standard.md#Source_Power_Cal) |  |   
[Correction](CF_Cal_Commands_-_Standard.md#Correction) |  |  |   
Src Power Correct | ON/OFF | [SOURce:POWer:CORRection[:STATe]](GP-IB_Command_Finder/SourceCorrection.md#state) | [SourcePowerCorrection](COM_Reference/Properties/SourcePowerCorrection_Property.md)  
Interpolation | ON/OFF | [SENSe:CORRection:INTerpolate[:STATe]](GP-IB_Command_Finder/Sense/Sense_Correction.md#scis) | [InterpolateCorrection](COM_Reference/Properties/Interpolate_Correction_Property.md)  
Correction Methods... |  | [CALCulate:MEASure:CORRection:TYPE](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:TYPE) | [meas.CalibrationTypeID](COM_Reference/Properties/CalibrationTypeID_property.md)  
Properties... |  | None | [Properties](COM_Reference/Properties/Properties_Property.md)  
Port Extension Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | Port N | [SENSe:CORRection:EXTension:PORT](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) | [portExt.Port1](COM_Reference/Properties/Port_1_Property.md) [portExt.Port2](COM_Reference/Properties/Port_2_Property.md)  
Port Extension | ON/OFF | [SENSe:CORRection:EXTension](GP-IB_Command_Finder/Sense/CorrExtension.md#ExtState) | [portExtension.State](COM_Reference/Properties/State_Property.md)  
Time |  | [SENSe:CORRection:EXTension:PORT:TIME](GP-IB_Command_Finder/Sense/CorrExtension.md#PortTime) | [PortDelay](COM_Reference/Properties/PortDelay_Property.md)  
Distance |  | [SENSe:CORRection:EXTension:PORT:DISTance](GP-IB_Command_Finder/Sense/CorrExtension.md#portDist) | [PortDistance](COM_Reference/Properties/PortDistance_Property.md)  
Velocity Factor |  | [SENSe:CORRection:RVELocity:COAX](GP-IB_Command_Finder/Sense/Sense_Correction.md#scrc) | [app.VelocityFactor](COM_Reference/Properties/Velocity_Factor_Property.md)  
DC Loss |  | [SENSe:CORRection:EXTension:PORT:LDC](GP-IB_Command_Finder/Sense/CorrExtension.md#LossDC) | [fix.PortLossDC](COM_Reference/Properties/PortLossDC_Property.md)  
[Port Extensions...](CF_Cal_Commands_-_Standard.md#Port_Extensions) |  |  |   
[Auto Port Extension...](CF_Cal_Commands_-_Standard.md#Auto_Port_Extension) |  |  |   
Cal Sets & Cal Kits Tab Commands  
Softkey | Sub-item | SCPI | COM  
[Cal Set...](CF_Cal_Commands_-_Standard.md#Cal_Set) |  | [CSET](GP-IB_Command_Finder/CSET.md) |   
Cal Set Viewer | ON/OFF | [DISPlay:TOOL:CSET[:STATe]](GP-IB_Command_Finder/Display.md#DISPlay:TOOLbar:CSET:STATe) | None  
[Cal Kit...](CF_Cal_Commands_-_Standard.md#Cal_Kit) |  |  |   
[ECal](CF_Cal_Commands_-_Standard.md#E_Cal) |  |  |   
[Cal Pod...](CF_Cal_Commands_-_Standard.md#Cal_Pod) |  |  |   
Fixtures Tab Commands  
Softkey | Sub-item | SCPI | COM  
Apply Fixtures | ON/OFF | [CALCulate:FSIMulator:STATe](GP-IB_Command_Finder/Calculate/FSimulator.md#FSimState) | [FixturingState](COM_Reference/Properties/FixturingState_Property.md)  
Power Comp... | Port N | [CALC:FSIM:SEND:POW:PORT:COMP](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#PowerPortComp) | [EnablePowerCompensation](COM_Reference/Properties/EnablePowerCompensation_Property.md)  
Fixture Setup | Change order of operations | [CALCulate:FSIMulator:SENDed:OORDer](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#oorder) | None  
2 and 4-port Extrapolate | [CALCulate:FSIMulator:SNP:EXTRapolate](GP-IB_Command_Finder/Calculate/FSimulator.md#extrapolate) | [EnableSnPDataExtrapolation](COM_Reference/Properties/EnableSnPDataExtrapolation_Property.md)  
2-Port Fixturing  
Port matching ON and OFF | [CALCulate:FSIMulator:SENDed:PMCircuit:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#PMCState) | [PortMatchingState](COM_Reference/Properties/PortMatchingState_Property.md)  
Reverse ports | [CALCulate:FSIMulator:SENDed:DEEM:PORT<n>:SNP:REVerse](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ReversePorts) | [Reverse2PortAdapter](COM_Reference/Properties/Reverse2PortAdapter_Property.md)  
Sets Port Matching circuit model | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:TYPE](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcType) | [PortMatchingCktModel](COM_Reference/Properties/PortMatchingCktModel_Property.md)  
Sets Port Matching 'S2P' file name | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcFileName) | [strPortMatch_S2PFile](COM_Reference/Properties/strPortMatch_S2PFile_Property.md)  
Sets Capacitance 'C' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:C](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcC) | [PortMatching_C](COM_Reference/Properties/PortMatching_C_Property.md)  
Sets Conductance 'G' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:G](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcG) | [PortMatching_G](COM_Reference/Properties/PortMatching_G_Property.md)  
Sets Inductance 'L' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:L](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcL) | [PortMatching_L](COM_Reference/Properties/PortMatching_L_Property.md)  
Sets Resistance 'R' value | [CALCulate:FSIMulator:SENDed:PMCircuit:PORT:PARameters:R](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#pmcR) | [PortMatching_R](COM_Reference/Properties/PortMatching_R_Property.md)  
De-embed ON and OFF | [CALCulate:FSIMulator:SENDed:DEEMbed:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#DeemState) | [Port2PdeembedState](COM_Reference/Properties/Port2PdeembedState_Property.md)  
Sets De-embedding circuit model | [CALCulate:FSIMulator:SENDed:DEEMbed:PORT](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#deembedType) | [Port2PdeembedCktModel](COM_Reference/Properties/Port2PdeembedCktModel_Property.md)  
Sets De-embedding 'S2P' file name | [CALCulate:FSIMulator:SENDed:DEEM:PORT:USER:FILename](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#deembedFileName) | [strPort2Pdeembed_S2PFile](COM_Reference/Properties/strPort2Pdeembed_S2PFile_Property.md)  
Port Impedance ON and OFF | [CALCulate:FSIMulator:SENDed:ZCONversion:STATe](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZState) | [PortArbzState](COM_Reference/Properties/PortArbzState_Property.md)  
Port Z Real | [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:REAL](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZReal) | [PortArbzReal](COM_Reference/Properties/PortArbzReal_Property.md)  
Port Z Imag | [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:IMAG](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZImag) | [PortArbzImag](COM_Reference/Properties/PortArbzImag_Property.md)  
Port Z Real and Imag | [CALCulate:FSIMulator:SENDed:ZCONversion:PORT:Z0](GP-IB_Command_Finder/Calculate/FSimulatorSend.md#ZValue) | [PortArbzZ0](COM_Reference/Properties/PortArbzZ0_Property.md)  
Remote ONLY  
Create Cal Set with De-embeded fixture removed | [CSET:FIXTure:DEEMbed](GP-IB_Command_Finder/CSET.md#deembed) | [Deembed](COM_Reference/Methods/Deembed_Method.md)  
Create Cal Set with Matching network included | [CSET:FIXTure:EMBed](GP-IB_Command_Finder/CSET.md#embed) | [Embed](COM_Reference/Methods/Embed_Method.md)  
[Cal Plane Manager...](CF_Cal_Commands_-_Standard.md#Cal_Plane_Manager) |  |  | 

