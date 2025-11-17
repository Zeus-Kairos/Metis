# Setup Commands - Phase Noise Measurement Class

Only the Main Setup commands corresponding to the Phase Noise measurement
class are documented here. All other commands are identical to the Setup
commands for the Standard measurement class and can be accessed by clicking
[here](CF_Setup_Commands_-_Standard.md) or by clicking on the softtabs on the
graphic below.

Click [here](CF_Setup_Commands.md) to view links to Setup commands for all
Measurement Classes.

Main | [Layout](CF_Setup_Commands_-_Standard.md#Customize_Meas_Commands) | [System  
Setup](CF_System_Commands.htm#System_Setup_Tab_Commands) | [Internal  
Hardware](CF_Setup_Commands_-_Standard.htm#Internal_Hardware_Commands) | [External  
Hardware](CF_Setup_Commands_-_Standard.htm#External_Hardware_Commands)  
---|---|---|---|---  
Main Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Phase Noise Setup... | Sweep Tab  
Noise Type Phase Noise Residual Noise |  [SENSe:PN:NTYPe PNOise](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:MTYPe) [SENSe:PN:NTYPe RESidual](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:MTYPe) |  None None  
Carrier Frequency | [SENSe:PN:SWEep:CARRier:FREQuency](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:SWEep:CARRier:FREQuency) | None  
|  |   
|  |   
|  |   
|  |   
Carrier Threshold | [SENSe:PN:ADJust:CONFigure:LEVel:THReshold](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:ADJust:CONFigure:LEVel:THReshold) | None  
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
Start Offset | [SENSe:FREQuency:STARt](GP-IB_Command_Finder/Sense/Frequency.md#start) | [StartFrequency](COM_Reference/Properties/Start_Frequency_Property.md)  
Stop Offset | [SENSe:FREQuency:STOP](GP-IB_Command_Finder/Sense/Frequency.md#stop) | [StopFrequency](COM_Reference/Properties/Stop_Frequency_Property.md)  
RBW Ratio | [SENSe:PN:BWIDth[:RESolution]:RATio](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:BWIDth:RESolution:RATio) | None  
FFT Avg Factor | [SENSe:PN:FAVerage:FACTor](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:FAVerage:FACTor) | None  
Noise Mode | [SENSe:PN:SWEep:NOISe:MODE](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:SWEep:ACCuracy) | None  
RF Path Tab  
VNA Input | [SENSe:PN:RECeiver](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:RECeiver) | None  
DUT Input (for Residual Phase) | [SENSe:PN:RESidual:INPut](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:RESidual:INPut) | None  
DUT Output (for Residual Phase) | [SENSe:PN:RESidual:OUTput](GP-IB_Command_Finder/Sense/Phase_Noise.md#SENSe:PN:RESidual:OUTput) | None  
Rcvr Atten | [SOURce:POWer:ATTenuation:RECeiver:TEST](GP-IB_Command_Finder/source.md#SOURce:POWer:ATTenuation:RECeiver:TEST) | None  
RF Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Source Tab  
Power On (All Channels)/State | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Port Powers Coupled | [SOURce:POWer:COUPle](GP-IB_Command_Finder/source.md#cplON) | [CouplePorts](COM_Reference/Properties/Couple_Ports_Property.md)  
State | [SOURce:POWer:MODE](GP-IB_Command_Finder/source.md#Mode) | [SourcePortMode](COM_Reference/Properties/SourcePortMode_Property.md)  
Frequency | SOURce:FREQuency[:FIXed] | None  
Power | [SOURce:POWer[:LEVel][:IMMediate][:AMPLitude]](GP-IB_Command_Finder/source.md#pwrval) | [TestPortPower](COM_Reference/Properties/Test_Port_Power_Property.md)  
[Pulse Setup...](CF_Sweep_Commands_-_SA.md) |  |   
RF Path Configuration... | [SENSe:PATH:CONFig:ELEMent[:STATe]](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
[Power and Attenuator...](CF_Power_Commands_-_Standard.md#Power_and_Attenuators) |  |   
[External Devices...](CF_Setup_Commands_-_Standard.md#External_Hardware_Commands) |  |   
Spurious Tab  
Show Spurious Table | [DISPlay:WINDow:TABLe:SPURious:ENABle](GP-IB_Command_Finder/Display.md#DISPlay:WINDow:TABLe:SPURious:ENABle) | None  
Table Sort Order | [CALCulate:MEASure:PN:SPURious:SORT](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SPURious:SORT) | None  
Select Trace | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Enable Spur Analysis | [CALCulate:MEASure:PN:SPURious:ANALysis[:STATe]](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SPURious:ANALysis:STATe) | None  
Spur Sensibility | [CALCulate:MEASure:PN:SPURious:SENSibility](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SPURious:SENSibility) | None  
Min. Spur Level | [CALCulate:MEASure:PN:SPURious:THReshold:LEVel:MINimum](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SPURious:THReshold:LEVel:MINimum) | None  
Omit Displayed Spur | [CALCulate:MEASure:PN:SPURious:OMISsion[:STATe]](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SPURious:OMISsion:STATe) | None  
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
|  |   
Integrated Noise Tab  
Show Integrated Noise Table | [DISPlay:WINDow:TABLe:INOise:ENABle](GP-IB_Command_Finder/Display.md#DISPlay:WINDow:TABLe:INOise:ENABle) | None  
Weighting Filter Setup...  
Frequency | None | None  
Weighting Value | None | None  
Add | None | None   
Delete | None | None   
Delete All | None | None   
Save Table | None | None   
Load Table | None | None  
Select Trace | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Range | Specified in each CALC:MEAS:PN:INT:RANG[1-4]... command | None   
Type | [CALCulate:MEASure:PN:INTegral:RANGe[1-4]:TYPE](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:INTegral:RANGe:TYPE) | None   
Start | [CALCulate:MEASure:PN:INTegral:RANGe[1-4]:STARt](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:INTegral:RANGe:STARt) | None  
Stop | [CALCulate:MEASure:PN:INTegral:RANGe[1-4]:STOP](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:INTegral:RANGe:STOP) | None  
Weighting Filter | [CALCulate:MEASure:PN:INTegral:RANGe[1-4]:WEIGhting](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:INTegral:RANGe:WEIGhting) | None  
Spot Noise Tab  
Show Spot Noise Table | [DISPlay:WINDow:TABLe:SNOise:ENABle](GP-IB_Command_Finder/Display.md#DISPlay:WINDow:TABLe:SNOise:ENABle) | None  
Select Traces | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Define Spot Frequencies | [CALCulate:MEASure:PN:SNOise:USER[1-6]:X](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SNOise:USER:X) [CALCulate:MEASure:PN:SNOise:USER[1-6][:STATe]](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SNOise:USER:STATe) | None None  
Decade Edges | [CALCulate:MEASure:PN:SNOise:DECades[:STATe]](GP-IB_Command_Finder/Calculate/MeasurePhaseNoise.md#CALCulate:MEASure:PN:SNOise:DECades:STATe) | None

