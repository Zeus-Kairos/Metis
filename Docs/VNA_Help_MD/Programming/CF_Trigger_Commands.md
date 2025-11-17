# Trigger Commands

Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Hold |  | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [Hold](COM_Reference/Methods/Hold_Method.md)  
Single |  | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [chan.Single](COM_Reference/Methods/Single_Method.md)  
Groups |  | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [chan.NumberOfGroups](COM_Reference/Methods/Number_Of_Groups_Method.md)  
Continuous |  | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [chan.Continuous](COM_Reference/Methods/Continuous_Method.md)  
Manual Trigger |  | [INITiate[:IMMediate]](GP-IB_Command_Finder/Initiate.md#immed) | [ManualTrigger](COM_Reference/Methods/Manual_Trigger_Method.md)  
Restart |  | [INITiate[:IMMediate]](GP-IB_Command_Finder/Initiate.md#immed) or [ABORT](GP-IB_Command_Finder/Abort.md) | [ManualTrigger](COM_Reference/Methods/Manual_Trigger_Method.md)  
Trigger Source | Internal | [TRIGger[:SEQuence]:SOURce](GP-IB_Command_Finder/Trigger_SCPI.md#tss) | [Source](COM_Reference/Properties/Source_Property.md)  
Manual | [TRIGger[:SEQuence]:SOURce](GP-IB_Command_Finder/Trigger_SCPI.md#tss) | [Source](COM_Reference/Properties/Source_Property.md)  
External | [TRIGger[:SEQuence]:SOURce](GP-IB_Command_Finder/Trigger_SCPI.md#tss) | [Source](COM_Reference/Properties/Source_Property.md)  
Trigger... | Setup  
Trigger Source | [TRIGger[:SEQuence]:SOURce](GP-IB_Command_Finder/Trigger_SCPI.md#tss) | [Setup.Source](COM_Reference/Properties/Source_Property.md)  
Trigger Scope | [TRIIGger[:SEQuence]:SCOPe](GP-IB_Command_Finder/Trigger_SCPI.md#tssc) | [Setup.Scope](COM_Reference/Properties/Scope_Property.md)  
Channel Trigger State |  |   
Trigger Mode CHANel SWEep POINt TRACe  SEGMent | [SENSe:SWEep:TRIGger:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Mode) | [chan.TriggerMode](COM_Reference/Properties/Trigger_Mode_Property.md)  
Continuous | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [chan.Continuous](COM_Reference/Methods/Continuous_Method.md)  
Groups | [SENSe:SWEep:GROups:COUNt](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssgc) [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [chan.NumberOfGroups](COM_Reference/Methods/Number_Of_Groups_Method.md)  
Single | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [chan.Single](COM_Reference/Methods/Single_Method.md)  
Hold | [SENSe:SWEep:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm) | [Hold](COM_Reference/Methods/Hold_Method.md)  
Meas Trigger  
Global Trigger Delay | [TRIGger:DELay](GP-IB_Command_Finder/Trigger_SCPI.md#delay) | [TriggerDelay](COM_Reference/Properties/TriggerDelay_Property.md)  
Meas Trig In BNC | [TRIGger[:SEQuence]:ROUTE:INPut](GP-IB_Command_Finder/Trigger_SCPI.md#input) | [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Handler I/O Pin 18 | [TRIGger[:SEQuence]:ROUTE:INPut](GP-IB_Command_Finder/Trigger_SCPI.md#input) | [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Pulse3 | [TRIGger[:SEQuence]:ROUTE:INPut](GP-IB_Command_Finder/Trigger_SCPI.md#input) | [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Rear SMB | [TRIGger[:SEQuence]:ROUTE:INPut](GP-IB_Command_Finder/Trigger_SCPI.md#input) [CONTrol:SIGNal:STReamline:RTRigger[:STATe]](GP-IB_Command_Finder/Control.md#SigStrRtr) |   
Backplane | [CONTrol:SIGNal:PXI:RTRigger[:STATe]](GP-IB_Command_Finder/Control.md#SigPxiRtr) |   
Level/Edge | [TRIIGger[:SEQuence]:TYPE](GP-IB_Command_Finder/Trigger_SCPI.md#type) | [ExternalTriggerConnectionBehavior](COM_Reference/Properties/ExternalTriggerConnectionBehavior_Property.md)  
Accept trigger before armed | [CONTrol:SIGNal:TRIGger:ATBA](GP-IB_Command_Finder/Control.md#atba) | [AcceptTriggerBeforeArmed](COM_Reference/Properties/AcceptTriggerBeforeArmed_Property.md)  
Meas Trig Ready | [TRIGger:STATus:READy?](GP-IB_Command_Finder/Trigger_SCPI.md#TRIGger:STATus:READy) | [ReadyForTriggerStatus](COM_Reference/Properties/ReadyForTriggerStatus_Property.md)  
Trigger ready- Rear SMB | [CONTrol:SIGNal:STReamline:RTRigger:ROUTe](GP-IB_Command_Finder/Control.md#SigStrRtrRout) |   
Trigger ready -Backplane | [CONTrol:SIGNal:PXI:RTRigger:ROUTe](GP-IB_Command_Finder/Control.md#SigPxiRtrRout) |   
Handler I/O Pin 21 | [TRIGger[:SEQuence]:ROUTE:READy](GP-IB_Command_Finder/Trigger_SCPI.md#Ready) | None  
Ready High | [TRIGger:READy:POLarity](GP-IB_Command_Finder/Trigger_SCPI.md#ReadyPolarity) | [ReadyForTriggerPolarity](COM_Reference/Properties/ReadyForTriggerPolarity_Property.md)  
Ready Low | [TRIGger:READy:POLarity](GP-IB_Command_Finder/Trigger_SCPI.md#ReadyPolarity) | [ReadyForTriggerPolarity](COM_Reference/Properties/ReadyForTriggerPolarity_Property.md)  
Aux Trig 1  
Enable | [TRIGger:CHANnel:AUXiliary:ENABle](GP-IB_Command_Finder/Trigger_SCPI.md#auxEnable) | [Enable](COM_Reference/Properties/Enable_Property.md)  
Positive Pulse | [TRIGger:CHANnel:AUXiliary:OPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxOpolarity) | [TriggerOutPolarity](COM_Reference/Properties/TriggerOutPolarity_Property.md)  
Negative Pulse | [TRIGger:CHANnel:AUXiliary:OPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxOpolarity) | [TriggerOutPolarity](COM_Reference/Properties/TriggerOutPolarity_Property.md)  
Before Acquisition | [TRIGger:CHANnel:AUXiliary:POSition](GP-IB_Command_Finder/Trigger_SCPI.md#auxPosition) | [TriggerOutPosition](COM_Reference/Properties/TriggerOutPosition_Property.md)  
After Acquisition | [TRIGger:CHANnel:AUXiliary:POSition](GP-IB_Command_Finder/Trigger_SCPI.md#auxPosition) | [TriggerOutPosition](COM_Reference/Properties/TriggerOutPosition_Property.md)  
Per Point | [TRIGger:CHANnel:AUXiliary:INTerval](GP-IB_Command_Finder/Trigger_SCPI.md#auxInterval) | [TriggerOutInterval](COM_Reference/Properties/TriggerOutInterval_Property.md)  
Rear SMB | [CONTrol:SIGNal:STReamline:TRIGger:OUTPut[:STATe]](GP-IB_Command_Finder/Control.md#SigStrTrifOutp) [CONTrol:SIGNal:STReamline:TRIGger:OUTPut:ROUTe](GP-IB_Command_Finder/Control.md#SigStrTrigOutpRout) |   
Backplane | [CONTrol:SIGNal:PXI:TRIGger:OUTPut[:STATe]](GP-IB_Command_Finder/Control.md#SigPxiTrigOutp) [CONTrol:SIGNal:PXI:TRIGger:OUTPut:ROUTe](GP-IB_Command_Finder/Control.md#SigPxiTrigOutpRout)[ ](GP-IB_Command_Finder/Control.md#SigPxiRtrRout) |   
Pulse Duration | [TRIGger:CHANnel:AUXiliary:DURation](GP-IB_Command_Finder/Trigger_SCPI.md#AuxDuration) | [TriggerOutDuration](COM_Reference/Properties/TriggerOutDuration_Property.md)  
Enable Wait-for-Device Handshake | [TRIGger:CHANnel:AUXiliary:HANDshake](GP-IB_Command_Finder/Trigger_SCPI.md#AuxHandshake) | [HandshakeEnable](COM_Reference/Properties/HandshakeEnable_Property.md)  
Positive Edge | [TRIGger:CHANnel:AUXiliary:IPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxIpolarity) | [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Negative Edge | [TRIGger:CHANnel:AUXiliary:IPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxIpolarity) | [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Delay | [TRIGger:CHANnel:AUXiliary:DELay](GP-IB_Command_Finder/Trigger_SCPI.md#AuxDelay) | [Delay](COM_Reference/Properties/Delay_trigger_Property.md)  
Aux Trig 2  
Enable | [TRIGger:CHANnel:AUXiliary:ENABle](GP-IB_Command_Finder/Trigger_SCPI.md#auxEnable) | [Enable](COM_Reference/Properties/Enable_Property.md)  
Positive Pulse | [TRIGger:CHANnel:AUXiliary:OPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxOpolarity) | [TriggerOutPolarity](COM_Reference/Properties/TriggerOutPolarity_Property.md)  
Negative Pulse | [TRIGger:CHANnel:AUXiliary:OPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxOpolarity) | [TriggerOutPolarity](COM_Reference/Properties/TriggerOutPolarity_Property.md)  
Before Acquisition | [TRIGger:CHANnel:AUXiliary:POSition](GP-IB_Command_Finder/Trigger_SCPI.md#auxPosition) | [TriggerOutPosition](COM_Reference/Properties/TriggerOutPosition_Property.md)  
After Acquisition | [TRIGger:CHANnel:AUXiliary:POSition](GP-IB_Command_Finder/Trigger_SCPI.md#auxPosition) | [TriggerOutPosition](COM_Reference/Properties/TriggerOutPosition_Property.md)  
Per Point | [TRIGger:CHANnel:AUXiliary:INTerval](GP-IB_Command_Finder/Trigger_SCPI.md#auxInterval) | [TriggerOutInterval](COM_Reference/Properties/TriggerOutInterval_Property.md)  
Pulse Duration | [TRIGger:CHANnel:AUXiliary:DURation](GP-IB_Command_Finder/Trigger_SCPI.md#AuxDuration) | [TriggerOutDuration](COM_Reference/Properties/TriggerOutDuration_Property.md)  
Enable Wait-for-Device Handshake | [TRIGger:CHANnel:AUXiliary:HANDshake](GP-IB_Command_Finder/Trigger_SCPI.md#AuxHandshake) | [HandshakeEnable](COM_Reference/Properties/HandshakeEnable_Property.md)  
Positive Edge | [TRIGger:CHANnel:AUXiliary:IPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxIpolarity) | [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Negative Edge | [TRIGger:CHANnel:AUXiliary:IPOLarity](GP-IB_Command_Finder/Trigger_SCPI.md#auxIpolarity) | [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Delay | [TRIGger:CHANnel:AUXiliary:DELay](GP-IB_Command_Finder/Trigger_SCPI.md#AuxDelay) | [Delay](COM_Reference/Properties/Delay_trigger_Property.md)  
Pulse Trigger  
Trigger Source | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
High Level | [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) | [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Low Level | [SENSe:PULSe:TTYPe](GP-IB_Command_Finder/Sense/Pulse.md#TType) | [TriggerInType](COM_Reference/Properties/TriggerInType_Property.md)  
Positive Edge | [SENSe:PULSe:TPOLarity](GP-IB_Command_Finder/Sense/Pulse.md#TPolarity) | [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Negative Edge | [SENSe:PULSe:TPOLarity](GP-IB_Command_Finder/Sense/Pulse.md#TPolarity) | [TriggerInPolarity](COM_Reference/Properties/TriggerInPolarity_Property.md)  
Synchronize ADCs using pulse trigger | [SENSe:PULSe[:STATe]](GP-IB_Command_Finder/Sense/Pulse.md#state) | [State](COM_Reference/Properties/State_pulse_Property.md)  
ADC trigger delay | [SENSe:PULSe:DELay](GP-IB_Command_Finder/Sense/Pulse.md#delay) | [Delay](COM_Reference/Properties/Delay_pulse_Property.md)

