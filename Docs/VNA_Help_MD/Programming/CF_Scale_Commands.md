# Scale Commands

Main | Electrical  
Delay | Constants  
---|---|---  
Main  
---  
Softkey | Sub-item | SCPI | COM  
Autoscale |  | [DISPlay:MEASure:Y[:SCALe]:AUTO](GP-IB_Command_Finder/Display.md#MeasYAuto) | [Autoscale](COM_Reference/Methods/Autoscale_Method.md)  
Autoscale All |  | [DISPlay:WINDow:Y:AUTO](GP-IB_Command_Finder/Display.md#AutoscaleAll) | [Autoscale](COM_Reference/Methods/Autoscale_Method.md)  
Scale |  | [DISPlay:MEASure:Y[:SCALe]:PDIVision](GP-IB_Command_Finder/Display.md#MeasYPdiv) | [YScale](COM_Reference/Properties/YScale_Property.md)  
Reference Level |  | [DISPlay:MEASure:Y[:SCALe]:RLEVel](GP-IB_Command_Finder/Display.md#MeasYRlev) | [ReferenceValue](COM_Reference/Properties/Reference_Value_Property.md)  
Reference Position |  | [DISPlay:MEASure:Y[:SCALe]:RPOSition](GP-IB_Command_Finder/Display.md#MeasYRpos) | [ReferencePosition](COM_Reference/Properties/Reference_Position_Property.md)  
Y-Axis Spacing |  | [DISPlay:WINDow:TRACe:Y:SPACing](GP-IB_Command_Finder/Display.md#WindYSpac) | None  
Top |  | [DISPlay:WINDow:TRACe:Y:SCALe:TOP](GP-IB_Command_Finder/Display.md#WindTracYTop) | None  
Bottom |  | [DISPlay:WINDow:TRACe:Y:SCALe:BOTTom](GP-IB_Command_Finder/Display.md#WindTracYBott) | None  
Ref Y Level |  | [DISPlay:WINDow:TRACe:Y:SCALe:RLEVel](GP-IB_Command_Finder/Display.md#rlev) | None  
Ref Y Position |  | [DISPlay:WINDow:TRACe:Y:SCALe:RPOSition](GP-IB_Command_Finder/Display.md#rpos) | None  
Ref X Level |  | [DISPlay:WINDow:TRACe:X:SCALe:RLEVel](GP-IB_Command_Finder/Display.md#DispWindTracXScalRlev) | None  
Ref X Position |  | [DISPlay:WINDow:TRACe:X:SCALe:RPOSition](GP-IB_Command_Finder/Display.md#DispWindTracXRpos) | None  
Scale Coupling... | Off | [DISPlay:WINDow:TRACe:Y[:SCALe]:COUPle:METHod](GP-IB_Command_Finder/Display.md#scaleCouplMethod) | [ScaleCouplingMethod](COM_Reference/Properties/ScaleCouplingMethod_Property.md)  
Window | [DISPlay:WINDow:TRACe:Y[:SCALe]:COUPle:METHod](GP-IB_Command_Finder/Display.md#scaleCouplMethod) | [ScaleCouplingMethod](COM_Reference/Properties/ScaleCouplingMethod_Property.md)  
All: couple between all selected windows | [DISPlay:WINDow:TRACe:Y[:SCALe]:COUPle:METHod](GP-IB_Command_Finder/Display.md#scaleCouplMethod) | [ScaleCouplingMethod](COM_Reference/Properties/ScaleCouplingMethod_Property.md)  
Selected Windows | [DISPlay:WINDow:TRACe:Y[:SCALe]:COUPle[:STATe]](GP-IB_Command_Finder/Display.md#scaleCouplState) | [ScaleCouplingState](COM_Reference/Properties/ScaleCouplingState_Property.md)  
Electrical Delay Tab Commands  
Softkey | Sub-item | SCPI | COM  
Delay Time |  | [CALCulate:MEASure:CORRection:EDELay[:TIME]](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:TIME) | [ElectricalDelay](COM_Reference/Properties/Electrical_Delay_Property.md)  
Delay Distance |  | [CALCulate:MEASure:CORRection:EDELay:DISTance](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:DISTance) | [ElecDistanceDelay](COM_Reference/Properties/ElecDistanceDelay_Property.md)  
Distance Units | Meters | [CALCulate:MEASure:CORRection:EDELay:UNIT](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:UNIT) | [ElecDistanceDelayUnit](COM_Reference/Properties/ElecDistanceDelayUnit_Property.md)  
Feet | [CALCulate:MEASure:CORRection:EDELay:UNIT](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:UNIT) | [ElecDistanceDelayUnit](COM_Reference/Properties/ElecDistanceDelayUnit_Property.md)  
Inches | [CALCulate:MEASure:CORRection:EDELay:UNIT](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:UNIT) | [ElecDistanceDelayUnit](COM_Reference/Properties/ElecDistanceDelayUnit_Property.md)  
Velocity Factor |  | [SENSe:CORRection:RVELocity:COAX](GP-IB_Command_Finder/Sense/Sense_Correction.md#scrc) | [PortVelocityFactor](COM_Reference/Properties/PortVelocityFactor_Property.md)  
Media |  | [CALCulate:MEASure:CORRection:EDELay:MEDium](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:MEDium) | [PortMedium](COM_Reference/Properties/PortMedium_Property.md)  
Wavegd Cutoff |  | [CALCulate:MEASure:CORRection:EDELay:WGCutoff](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:WGCutoff) | [PortWGCutoffFreq](COM_Reference/Properties/PortWGCutoffFreq_Property.md)  
Constants Tab Commands  
Softkey | Sub-item | SCPI | COM  
System Z0 |  | [SENSe:CORRection:IMPedance:INPut:MAGNitude](GP-IB_Command_Finder/Sense/Sense_Correction.md#imped) | [SystemImpedanceZ0](COM_Reference/Properties/SystemImpedanceZ0_Property.md)  
Phase Offset |  | [CALCulate:MEASure:OFFSet:PHASe](GP-IB_Command_Finder/Calculate/MeasureOFFSet.md#CALCulate:MEASure:OFFSet:PHASe) | [PhaseOffset](COM_Reference/Properties/Phase_Offset_Property.md)  
Mag Offset |  | [CALCulate:MEASure:OFFSet:MAGNitude](GP-IB_Command_Finder/Calculate/MeasureOFFSet.md#CALCulate:MEASure:OFFSet:MAGNitude) | [MagnitudeOffset](COM_Reference/Properties/MagnitudeOffset_Property.md)  
Mag Slope |  | [CALCulate:MEASure:OFFSet:MAGNitude:SOPe](GP-IB_Command_Finder/Calculate/MeasureOFFSet.md#CALCulate:MEASure:OFFSet:MAGNitude:SLOPe) | [MagnitudeSlopeOffset](COM_Reference/Properties/MagnitudeSlopeOffset_Property.md)

