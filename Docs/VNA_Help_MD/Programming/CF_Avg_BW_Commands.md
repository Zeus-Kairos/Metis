# Avg BW Commands

Main | Smoothing | Delay  
Aperture  
---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Averaging | On/Off | [SENSe:AVERage[:STATe]](GP-IB_Command_Finder/Sense/Average_SCPI.md#cas) [SENSe:AVERage:COUNt](GP-IB_Command_Finder/Sense/Average_SCPI.md#cac) ([STATus:OPERation:AVERaging](GP-IB_Command_Finder/Status.md#avg11)) | [Averaging](COM_Reference/Properties/Averaging_Property.md) [AveragingFactor](COM_Reference/Properties/Averaging_Factor_Property.md)  
Averaging Restart |  | [SENSe:AVERage:CLEar](GP-IB_Command_Finder/Sense/Average_SCPI.md#cacl) | [AveragingRestart](COM_Reference/Methods/Averaging_Restart_Method.md)  
Average Type |  | [SENSe:AVERage:MODE](GP-IB_Command_Finder/Sense/Average_SCPI.md#cac) | [AverageMode](COM_Reference/Properties/AverageMode_Property.md)  
IF Bandwidth |  | [SENSe:BANDwidth | BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) | [IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Vector Avg (Spectrum Analyzer Measurement Class only) |  | [SENSe:SA:COHerence:VECtor:AVERage:VALue](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:VECTor:AVERage:VALue) [SENSe:SA:](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:VECTor:AVERage:STATe)[COHerence:VECtor:AVERage:STATe](GP-IB_Command_Finder/Sense/SA.md#SENSe:SA:COHerence:VECTor:AVERage:VALue) |   
Noise BW (Modulation Distortion Measurement Class only) |  | [SENSe:SA:BANDwidth:NOISe](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:BANDwidth:NOISe) [SENSe:SA:BANDwidth:NOISe:AUTO](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:SA:BANDwidth:NOISe:AUTO) | None None  
Detector Type (Spectrum Analyzer Measurement Class only) |  | [SENSe:SA:DETector:FUNCtion](GP-IB_Command_Finder/Sense/SA.md#detFunction) | [DetectorFunction](COM_Reference/Properties/DetectorFunction_Property.md)  
Main Tone IFBW (Swept IMD and Swept IMD Converters Measurement Classes only) |  | [SENSe:IMD:IFBWidth:MAIN](GP-IB_Command_Finder/Sense/IMD.md#ifbwMain) | [MainToneIFBandwidth](COM_Reference/Properties/MainToneIFBandwidth_Property.md)  
IM Tone IFBW (Swept IMD and Swept IMD Converters Measurement Classes only) |  | [SENSe:IMD:IFBWidth:IMTone](GP-IB_Command_Finder/Sense/IMD.md#ifbwTone) | [IMToneIFBandwidth](COM_Reference/Properties/IMToneIFBandwidth_Property.md)  
|  |  | [ReduceIFBandwidth](COM_Reference/Properties/ReduceIFBW_Property.md)  
Noise Avg  (Noise Figure and Noise Figure Converters Measurement Classes only) |  | [SENSe:NOISe:AVERage](GP-IB_Command_Finder/Sense/Noise.md#Average) | [NoiseAverageFactor](COM_Reference/Properties/NoiseAverageFactor_Property.md)  
Noise BW  (Noise Figure and Noise Figure Converters Measurement Classes only) | 720.000 kHz | [SENSe:NOISe:BWIDth](GP-IB_Command_Finder/Sense/Noise.md#bwid) | [NoiseBandwidth](COM_Reference/Properties/NoiseBandwidth_Property.md)  
1.20000 MHz  
RBW Ratio  (Phase Noise Measurement Class only) |  | [SENSe:PN:BWIDth[:RESolution]:RATio](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:BWIDth:RESolution:RATio) | None  
Smoothing Tab Commands  
Softkey | Sub-item | SCPI | COM  
Smoothing | ON/OFF | [CALCulate:MEASure:SMOothing[:STATe]](GP-IB_Command_Finder/Calculate/MeasureSMOothing.md#CALCulate:MEASure:SMOothing:STATe) | [Smoothing](COM_Reference/Properties/Smoothing_Property.md)  
Smooth Percent |  | [CALCulate:MEASure:SMOothing:APERture](GP-IB_Command_Finder/Calculate/MeasureSMOothing.md#CALCulate:MEASure:SMOothing:APERture) | [SmoothingAperture](COM_Reference/Properties/Smoothing_Aperture_Property.md)  
Smooth Points |  | [CALCulate:MEASure:SMOothing:POINts](GP-IB_Command_Finder/Calculate/MeasureSMOothing.md#CALCulate:MEASure:SMOothing:POINts) | None  
Delay Aperture Tab Commands  
Softkey | Sub-item | SCPI | COM  
Aperture Percent |  | [CALCulate:MEASure:GDELay:PERCent](GP-IB_Command_Finder/Calculate/MeasureGDELay.md#CALCulate:MEASure:GDELay:PERCent) | [Percent](COM_Reference/Properties/Percent_Property.md)  
Aperture Points |  | [CALCulate:MEASure:GDELay:POINts](GP-IB_Command_Finder/Calculate/MeasureGDELay.md#CALCulate:MEASure:GDELay:POINts) | [Points](COM_Reference/Properties/Points_Property.md)  
Aperture Freq |  | [CALCulate:MEASure:GDELay:FREQuency](GP-IB_Command_Finder/Calculate/MeasureGDELay.md#CALCulate:MEASure:GDELay:FREQuency) | [Frequency](COM_Reference/Properties/Frequency_GD_Property.md)

