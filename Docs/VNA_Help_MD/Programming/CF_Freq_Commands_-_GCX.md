# Freq Commands - Gain Compression Converters and Noise Figure Converters
Measurement Classes

Click [here](CF_Freq_Commands.md) to view links to Freq commands for all
Measurement Classes.

Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Start... | Input  
Calculate Input and Output frequencies | [SENSe:MIXer:CALCulate](GP-IB_Command_Finder/Sense/MIXerSCPI.md#calc) | [Calculate](COM_Reference/Methods/Calculate_cv_Method.md)  
Input to swept or fixed | [SENSe:MIXer:INPut:FREQuency:MODE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#InputMode) | [InputRangeMode](COM_Reference/Properties/InputRangeMode_cv_Property.md)  
Input start frequency | [SENSe:MIXer:INPut:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_START) | [InputStartFrequency](COM_Reference/Properties/InputStartFrequency_Property.md)  
Input stop frequency | [SENSe:MIXer:INPut:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#IF_STOP) | [InputStopFrequency](COM_Reference/Properties/InputStopFrequency_Property.md)  
Input power level | [SENSe:MIXer:INPut:POWer](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_POWer) | [InputPower](COM_Reference/Properties/InputPower_Property.md)  
Input fixed frequency | [SENSe:MIXer:INPut:FREQuency:FIXed](GP-IB_Command_Finder/Sense/MIXerSCPI.md#INPut_FIX) | [InputFixedFrequency](COM_Reference/Properties/InputFixedFrequency_Property.md)  
LO1  
LO freq fixed or swept | [SENSe:MIXer:LO:FREQuency:MODE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LoMode) | [LORangeMode](COM_Reference/Properties/LORangeMode_cv_Property.md)  
LO fixed frequency | [SENSe:MIXer:LO:FREQuency:FIXed](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_FIX) | [LOFixedFrequency](COM_Reference/Properties/LOFixedFrequency_Property.md)  
LO start frequency | [SENSe:MIXer:LO:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_Start) | [LOStartFrequency](COM_Reference/Properties/LOStartFrequency_Property.md)  
LO stop frequency | [SENSe:MIXer:LO:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#LO_stop) | [LOStopFrequency](COM_Reference/Properties/LOStopFrequency_Property.md)  
Input Greater / Less that LO | [SENSe:MIXer:LO:FREQuency:ILTI](GP-IB_Command_Finder/Sense/MIXerSCPI.md#ilti) | [IsInputGreaterThanLO](COM_Reference/Properties/InputIsGreaterThanLO_Property.md)  
Output  
Sideband (high or low) | [SENSe:MIXer:OUTPut:FREQuency:SIDeband](GP-IB_Command_Finder/Sense/MIXerSCPI.md#OUTput_SIDE) | [OutputSideband](COM_Reference/Properties/OutputSideband-Converter_Property.md)  
Output start frequency | [SENSe:MIXer:OUTPut:FREQuency:STARt](GP-IB_Command_Finder/Sense/MIXerSCPI.md#OUTput_START) | [OutputStartFrequency](COM_Reference/Properties/OutputStartFrequency_Property.md)  
Output stop frequency | [SENSe:MIXer:OUTPut:FREQuency:STOP](GP-IB_Command_Finder/Sense/MIXerSCPI.md#OUTput_STOP) | [OutputStopFrequency](COM_Reference/Properties/OutputStopFrequency_Property.md)  
Output to swept or fixed | [SENSe:MIXer:OUTPut:FREQuency:MODE](GP-IB_Command_Finder/Sense/MIXerSCPI.md#OutputMode) | [OutputRangeMode](COM_Reference/Properties/OutputRangeMode_cv_Property.md)  
Output fixed frequency | [SENSe:MIXer:OUTPut:FREQuency:FIXed](GP-IB_Command_Finder/Sense/MIXerSCPI.md#Out_Fix) | [OutputFixedFrequency](COM_Reference/Properties/OutputFixedFrequency_Property.md)  
Stop... | Input |  |   
LO1 |  |   
Output |  |   
Center... | Input |  |   
LO1 |  |   
Output |  |   
Span... | Input |  |   
LO1 |  |   
Output |  |   
CW... | [Sweep Type](CF_Setup_Commands_-_GCX.md#GCX_Setup...) |  |   
Data Acquisition Mode (Gain Compression Converters Measurement Class only) | [SENSe:GCSetup:AMODe](GP-IB_Command_Finder/Sense/Gain_Compression.md#Amode) | [AcquisitionMode](COM_Reference/Properties/AcquisitionMode_Property.md)  
X-Axis Display (Noise Figure Converters Measurement Class only) | [CALCulate:MEASure:MIXer:XAXis](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MIXer:XAXis) | [ActiveXAxisRange](COM_Reference/Properties/ActiveXAxisRange_Conv_Property.md)  
[Sweep Settings](CF_Setup_Commands_-_GCX.md#Sweep_Settings) |  |   
[GCX Setup...](CF_Setup_Commands_-_GCX.md#GCX_Setup...) (Gain Compression Converters Measurement Class only) |  |  |   
[NFX Setup...](CF_Setup_Commands_-_NFX.md#NFX_Setup...) (Noise Figure Converters Measurement Class only) |  |  | 

