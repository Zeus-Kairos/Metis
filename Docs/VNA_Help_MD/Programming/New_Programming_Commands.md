# New Programming Commands

This topic lists new programming commands, starting with the latest VNA
firmware version and going back to version A.16.20.xx. For earlier versions,
see [Programming Commands History](Programming_Commands_History.md).

* * *

The following are new programming commands for VNA release A.19.30.xx [See
What's New](../Whats_New.htm).

AFR Commands |  SCPI |  COM  
---|---|---  
Sets or gets the description of the AFR DUT Gate Domain (single-ended or differential). |  [AFR:ADVanced:DUTGate:DOMain](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AFRAdvDutgDom) |  None  
Turns ON or OFF the Fitting Thru after AFR DUT Gate. |  [AFR:ADVanced:DUTGate:ILFitting:MANual[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvDutgIlfManStat) |  None  
Applies advanced algorithm to fixture impedance mismatching cases for better results. |  [AFR:ADVanced:FIXTure:IMPedance:FTUNe[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvFixtImpFtunStat) |  None  
Turns on or off the option "Automatically iterate when Impedance Method Auto is checked.". |  [AFR:ADVanced:AUTO:ITERate:METHod:CHECk[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvAutoIterMethChecStat) |  None  
Turns on or off the option "Automatically iterate when Calibration Reference Z0 is set to System Z0 or custom value." |  [AFR:ADVanced:AUTO:ITERate:REFZ:SET[:STATe]](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvAutoIterRefzSetStat) |  None  
Gets the AFR Version. |  [AFR:ADVanced:VERSion?](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvVers) |  None  
This command sets or reads the gating mode in 1-port characterization. |  [AFR:ADVanced:REFLection:GATing:MODE](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatMode) |  None  
This command gets or sets the N parameter in 1-port characterization. |  [AFR:ADVanced:REFLection:GATing:MODE:MINimum:NVALue](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatModeMinNval) |  None  
This command gets or sets the position parameter in 1-port characterization. |  [AFR:ADVanced:REFLection:GATing:MODE:CUSTom:POSition](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatModeCustPos) |  None  
This command gets or sets the spike tolerance parameter in 1-port characterization. |  [AFR:ADVanced:REFLection:GATing:SPIKe:TOLerance](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflGatSpikTol) |  None  
This command gets or sets the start ratio for IL fitting at low frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:LOW:STARt](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowStar) |  None  
This command gets or sets the stop ratio for IL fitting at low frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:LOW:STOP](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowStop) |  None  
This command gets or sets the ratio of the merge center for IL fitting at low frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:LOW:MCENter](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowMcen) |  None  
This command gets or sets the ratio of the merge span for IL fitting at low frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:LOW:MSPan](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfLowMsp) |  None  
This command gets or sets the start ratio for IL fitting at high frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:HIGH:STARt](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighStar) |  None  
This command gets or sets the stop ratio for IL fitting at high frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:HIGH:STOP](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighStop) |  None  
This command gets or sets the ratio of the merge center for IL fitting at high frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:HIGH:MCENter](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighMcen) |  None  
This command gets or sets the ratio of the merge span for IL fitting at high frequency range 1-port characterization. |  [AFR:ADVanced:REFLection:ILFitting:HIGH:MSPan](GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md#AdvReflIlfHighMsp) |  None  
  
Sense Noise Commands |  SCPI |  COM  
---|---|---  
Selects and queries the connected U7229x series USB Low Noise Amplifier, identified by its device ID. |  [SENSe<ch>:NOISe::AMPLifier:[:SELect] <string>](GP-IB_Command_Finder/Sense/Noise.md#Amplifier) |  None  
Returns a comma separated list of connected U7229x series USB Low Noise Amplifiers. |  [SENSe<ch>:NOISe::AMPLifier:CATalog?](GP-IB_Command_Finder/Sense/Noise.md#AmplifierCatalog) |  None  
  
External Source Commands |  SCPI |  COM  
---|---|---  
Returns the base name from the decorated name. For example, "N5186A Ch 3" returns N5186A. |  [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:BASE](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_BASE) |  None  
This returns the total number of channels possible. Currently, this is always 4. |  [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:COUNt](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_COUNt) |  None  
Returns the decorated name of the device for a particular channel. For example, SYST:CONF:EDEV:CHAN3:NAME? "N5186A" returns N5186A Ch 3. |  [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:NAME](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_NAME) |  None  
Returns the channel number from the decorated name. For example: "N5186A Ch 3" returns 3. |  [SYSTem:CONFigure:EDEVice:CHANnel<cnum>:NUMBer](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_NUMBer) |  None  
Turns on or off channels on a particular external source. |  [SYSTem:CONFigure:EDEVice:CHANnel<cnum>[:STATe]](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_STATe) |  None  
Turns on or off channel phase synchronization on an external source supporting this feature. |  [SYSTem:CONFigure:EDEVice:CHANnel:SYNC](GP-IB_Command_Finder/SystConfigExternalDevice.md#CHANnel_SYNC) |  None  
  
* * *

The following are new programming commands for VNA release A.19.10.xx [See
What's New](../Whats_New.htm).

Source Modulation Commands |  SCPI |  COM  
---|---|---  
Preserve Burst Characteristics of Original Signal |  [SOURce:MODulation:FILE:SIGNal:OPTimize:BURSt:PREServe:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce_MODulation_FILE_SIGNal_OPTimize_BURSt_PREServe) |  None  
Enable Spectral Leakage Tapering Window With [x] Taps |  [SOURce:MODulation:FILE:SIGNal:OPTimize:FILTer:TAPS](GP-IB_Command_Finder/SourceModulation.md#SOURce_MODulation_FILE_SIGNal_OPTimize_FILTer_TAPS) |  None  
  
* * *

The following are new programming commands for VNA release A.17.60.xx [See
What's New](../Whats_New.htm).

Display Commands |  SCPI |  COM  
---|---|---  
Returns a comma separated list of the sheet numbers in use in the order they appear in the GUI. |  [DISPlay:SHEet<num>:LIST?](GP-IB_Command_Finder/Display.md#SheetList) |  None  
  
Sense Correction Commands |  SCPI |  COM  
---|---|---  
Set and read the state of the noise receiver pulling during calibration. |  [SENSe<ch>:CORRection:COLLect:NOISe:RECeiver:PULL[:STATe] <bool>](GP-IB_Command_Finder/Sense/Sense_Correction.md#SENS:CORR:COLL:NOISe:REC:PULL) |  None  
  
Math Commands |  SCPI |  COM  
---|---|---  
Returns a boolean value to indicate if Python is installed. |  [CALCulate:EQUation:LIBRary:PYTHon[:STATe]?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryPythonState) |  None  
Returns all importable Python packages and their version numbers as provided by sys.path. |  [CALCulate:EQUation:LIBRary:PYTHon:MODules?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryPythonModules) |  None  
Returns a string containing the Python version number if Python is installed, else returns an empty string. |  [CALCulate:EQUation:LIBRary:PYTHon:VERsion?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryPythonVersion) |  None  
  
Guided Calibration GUI |  SCPI  
---|---  
Applies Smith Chart to the display format during a Guided Calibration.  |  [SENSse:CORection:COLLect:GUIDed:DISPlay:SMITh](GP-IB_Command_Finder/Sense/CorrGuided.md#DispSmit)  
Clears the flags for windows to be shown during calibrations. |  [SENSse:CORection:COLLect:GUIDed:DISPlay:WINDow:AOFF](GP-IB_Command_Finder/Sense/CorrGuided.md#DispWindAoff)  
Set the 'show' state of the window to be displayed during a calibration to view the measurements/channels. |  [SENSse:CORection:COLLect:GUIDed:WINDow:DISPlay[:STATe]](GP-IB_Command_Finder/Sense/CorrGuided.md#DispWindStat)  
Clears ALL flags for channels to sweep during calibration. |  [SENSse:CORection:COLLect:GUIDed:SWEep:CHANnel:AOFF](GP-IB_Command_Finder/Sense/CorrGuided.md#SweepAoff)  
Returns a list of property values that can be queried for the specified Cal Set |  [SENSse:CORection:COLLect:GUIDed:SWEep:CHANnel[:STATe]](GP-IB_Command_Finder/Sense/CorrGuided.md#SweepChan)  
  
General ECal Control |  SCPI  
---|---  
Returns the list of port labels on the selected ECal module. |  [CONTrol:ECAL:MODule<num>:PORT:CATalog?](GP-IB_Command_Finder/Control.md#ECalModPortCat)  
Returns a list of state or port labels for ECal. |  [CONTrol:ECAL:MODule<num>:PORT:STATe:CATalog?](GP-IB_Command_Finder/Control.md#EcalModPortStatCal)  
Sets the internal state of the ECal module. |  [CONTrol:ECAL:MODule<num>:PORT:STATe[:SELect]](GP-IB_Command_Finder/Control.md#EcalModPortStateSel)  
  
ECal Temperature Query |  SCPI  
---|---  
Reads the temperature condition at microcircuit in the specified ECal module. |  [SENSe:CORRection:CKIT:ECAL:TEMPerature:CONDition](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#ECalTempCond)  
Reads the temperature at microcircuit in the specified ECal module. |  [SENSe:CORRection:CKIT:ECAL:TEMPerature[:VALue]](GP-IB_Command_Finder/Sense/CorrCKIT_SCPI.md#EcalTempVal)  
  
X-axis Annotation Preference |  SCPI  
---|---  
Set and read the scope for the stimulus information on the display title bar. |  [DISPlay:WINDow:ANNotation:XAXis:SCOPe](GP-IB_Command_Finder/Display.md#AnnXaxScop)  
  
Hybrid Source Commands |  SCPI |  COM  
---|---|---  
Enable Pulse (Input) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:PULSe:ENABle](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:PULS:ENAB) |  None  
Enable Pulse (LO) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:PULSe:ENABle](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:PULS:ENAB) |  None  
Lock Dependent Sources |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LOCK:STATe](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LOCK:STAT) |  None  
Freq Max (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:FREQuency:MAX](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:FREQ:MAX) |  None  
Freq Min (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:FREQuency:MIN](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:FREQ:MIN) |  None  
Gain (SSB Mixer) * |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:GAIN](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:GAIN) |  None  
Equation (SSB Mixer) |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:MIXer:SIDeband](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:MIX:SID) |  None  
  
* This command is updated from firmware Rev A.17.00.xx.

* * *

The following are new programming commands for VNA release A.17.20.xx [See
What's New](../Whats_New.htm).

Source Modulation Commands |  SCPI |  COM  
---|---|---  
Returns the detailed messages generated by modulation correction. |  [SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACQuire:DETails?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACQuire:DETails) |  None  
Enable or disable the option that new Cal will update the currently active correction. |  [SOURce<cnum>:MODulation<port>:CORRection:COLLection:UPDate:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:UPDate:ENABle) |  None  
  
Save and Recall Calibration Configuration Commands |  SCPI |  COM  
---|---|---  
Returns a text description (string) of the current calibration settings. |  [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:DESCription?](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_DESC) |  None  
Loads the calibration configurations from file and commits all settings. |  [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD[:IMMediate] <string>](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_LOAD) |  None  
Returns a text description (string) of the calibration settings contained in the specified filename. |  [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD:DESCription? <string>](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_LOAD_DESC) |  None  
Save the current guided calibration settings to file. |  [SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:SAVE <string>](GP-IB_Command_Finder/Sense/CorrGuided.md#CONFig_SAVE) |  None  
  
Trigger Mode Command |  SCPI |  COM  
---|---|---  
Segment trigger is now a choice. |  [SENSe:SWEep:TRIGger:MODE](GP-IB_Command_Finder/Sense/Sweep_SCPI.md#Mode) |  None  
  
Segment Material Handler Port A Output Commands |  SCPI |  COM  
---|---|---  
Enable/disable Handler Port A by segment. |  [SENSe:SEGMent:HANDler:A:CONTrol <bool>](GP-IB_Command_Finder/Sense/Segment.md#handler_A_control_state) |  None  
Set an 8-bit value for the Handler A segment. |  [SENSe:SEGMent:HANDler:A <num>](GP-IB_Command_Finder/Sense/Segment.md#handler_A_control_value) |  None  
  
Multiple Memory Trace Commands (Data -> New Trace)  
---  
Returns whether the measurement number of the new measurement is locked. |  [CALCulate:MEASure:MATH:LOCKed?](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:LOCKed:STATe) |  None  
Allows several memory traces to be saved from the same trace data. |  [CALCulate:MEASure:MATH:NEW](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:NEW) |  None  
  
Simulator Dummy DUT Commands |  SCPI |  COM  
---|---|---  
Set/get trace sNp file for dummy DUT. |  [SYStem:SIMulator:DUT:FILE](GP-IB_Command_Finder/System.md#SimDutFil) |  None  
Add some noise on simulator measurement. Preset & Save/Recall does not work for this command |  [SYStem:SIMulator:DUT:NOISe:STATe](GP-IB_Command_Finder/System.md#SimDutNois) |  None  
  
CSET Commands |  SCPI |  COM  
---|---|---  
Returns the IF Bandwidth value for the specified Cal Set |  [CSET:FREQuency:BWIDth?](GP-IB_Command_Finder/CSET.md#FreqBwid) |  None  
Returns a specified start or stop frequency for converter/mixer Cal Sets |  [CSET:FREQuency:CONVerter?](GP-IB_Command_Finder/CSET.md#FreqConv) |  None  
Returns a comma separated list of doubles with all the start or stop values for the frequency segments |  [CSET:FREQuency:SEGment?](GP-IB_Command_Finder/CSET.md#FreqSegm) |  None  
Returns either the start or stop swept frequency for the specified Cal Set |  [CSET:FREQuency:SWEPT?](GP-IB_Command_Finder/CSET.md#FreqSwept) |  None  
Returns a list of property values that can be queried for the specified Cal Set |  [CSET:PROPerties:CATalog?](GP-IB_Command_Finder/CSET.md#Prop:Cat) |  None  
Returns the number of frequency points |  [CSET:PROPerties:POINt?](GP-IB_Command_Finder/CSET.md#PropPoin) |  None  
Returns a comma separated list of doubles holding the power value for every calibrated port. |  [CSET:PROPerties:PORT:ATTENuation?](GP-IB_Command_Finder/CSET.md#PropPortAtten) |  None  
Returns a comma separated list of strings holding the gain value for every calibrated port. |  [CSET:PROPerties:PORT:GAIN?](GP-IB_Command_Finder/CSET.md#PropPortGain) |  None  
Returns a comma separated list of integers holding the calibrated port numbers. |  [CSET:PROPerties:PORT:LIST?](GP-IB_Command_Finder/CSET.md#PropPortList) |  None  
Returns a comma separated list of doubles holding the power value for every calibrated port. |  [CSET:PROPerties:PORT:POWer?](GP-IB_Command_Finder/CSET.md#PropPortPow) |  None  
Returns the security level associated with the specified Cal Set |  [CSET:PROPerties:SECurity:LEVel?](GP-IB_Command_Finder/CSET.md#PropSecLev) |  None  
Returns the sweep mode for the specified Cal Set |  [CSET:PROPerties:SWEep:MODE?](GP-IB_Command_Finder/CSET.md#PropSweMode) |  None  
Returns the sweep type for the specified Cal Set |  [CSET:PROPerties:SWEep:TYPE?](GP-IB_Command_Finder/CSET.md#PropSweType) |  None  
  
* * *

The following are new programming commands for VNA release A.17.00.xx [See
What's New](../Whats_New.htm).

Math Commands |  SCPI |  COM  
---|---|---  
For Smith Chart format, changes trace statistic units from Log Mag (dB) to impedance (ohms) on the screen. |  [CALCulate:MEASure:FUNCtion:STATistics:RESistance[:STATe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:STATistics:RESistance:STATe) |  None  
|  |   
SourceDPD Commands  
Enable or disable automatic waveform compaction. Compacting the waveform enables faster optimization. |  [SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:DYNGain:OPTimize:COMPact:AUTO](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:COMPact:AUTO) |  None  
Sets the waveform compaction level. Compacting the waveform enables faster optimization. |  [SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:DYNGain:OPTimize:COMPact:LEVel](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:COMPact:LEVel) |  None  
Sets the NMSE Optimization Goal in dB. If enabled, the optimizer attempts to minimize parameters while still resulting in an NMSE less than the value entered. |  [SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:DYNGain:OPTimize:NMSE:GOAL](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:NMSE:GOAL) |  None  
Enable or disable the NMSE Optimization Goal. If enabled, the optimizer attempts to minimize parameters while still resulting in an NMSE less than the value entered. |  [SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:DYNGain:OPTimize:NMSE:INCLude](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:NMSE:INCLude) |  None  
|  |   
External Device Commands for Hybrid Source  
Sets the nominal gain of the SSB mixer system. The nominal gain value is used to set the input source power in order to get the desired output source power. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:GAIN:NOMinal](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:OUTP:GAIN) |  None  
For an SSB Mixer, the center of the input modulated signal is offset from DC by the carrier frequency. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:CARRier](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:FREQ:CARR) |  None  
If there is a multiplier placed between the Input Source and the SSB mixer, then use this command to specify the multiplication factor. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:MULTiplier](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:FREQ:MULT) |  None  
Select external or internal sources for the input source. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:NAME](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:NAME) |  None  
Sets the maximum power allowed for the Input Source. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:POWer:LIMit](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:INP:POW:LIM) |  None  
If there is a multiplier placed between the LO Source and the SSB mixer, then use this command to specify the multiplication factory. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:FREQuency:MULTiplier](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:FREQ:MULT) |  None  
Select external or internal sources for the LO source. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:NAME](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:NAME) |  None  
Sets the output power of the LO. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:POWer](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:LO:POWer) |  None  
Currently provides two selections: SSB Mixer (default) and Multiplier. The External Device dialog changes appearance and available settings according to the Hybrid Type you select. |  [SYSTem:CONFigure:EDEVice:SOURce:HYBRid:TYPE](GP-IB_Command_Finder/SystConfigExternalDevice.md#HYBR:TYPE) |  None  
  
* * *

The following are new programming commands for VNA release A.16.20.xx [See
What's New](../Whats_New.htm).

IMD Receiver Configuration Commands |  SCPI |  COM  
---|---|---  
Sets and returns the number of receivers to use in the receiver configuration. |  [SENSe:IMD:RECeiver:CONFig:REFerence COUNt](GP-IB_Command_Finder/Sense/IMD.md#SENSe:IMD:RECeiver:CONFig:REFerence:COUNt) |  None  
|  |   
Modulation Distortion Commands  
Include or exclude the NF nominal value. |  [SENSe:DISTortion:PATH:DUT:NOMinal:NF:INCLude](GP-IB_Command_Finder/Sense/Distortion_Measurement.md#SENSe:DISTortion:PATH:DUT:NOMinal:NF:INCLlude) |  None  
|  |   
Digital Predistortion Commands  
Sets and reads the scaling factor used for the waveform. |  [SOURce:DPD:DAC:SCALing](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:DAC:SCALing) |  None  
Calibrate the DPD model from the setting define using the model commands. |  [SOURce:DPD:MODel:CALibrate](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:CAL) |  None  
Sets and reads the interpolation type used in the AM/AM and AM/PM segments for the Dynamic Gain model. |  [SOURce:DPD:MODel:DYNGain:INTerpolate:TYPE](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DNYGain:INTerpolate:TYPE) |  None  
Sets and reads the number of input future time samples to use for calculating the current output sample. |  [SOURce:DPD:MODel:DYNGain:MEMory:FUTure](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:MEMory:FUTure) |  None  
Sets and reads the number of memory operators used for characterizing the device in the Dynamic Gain model. |  [SOURce:DPD:MODel:DYNGain:MEMory:OPERator:M[1-4]:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:MEMory:OPERator:M:ENABle) |  None  
Sets and reads the number of input past time samples to use for calculating the current output sample in the Dynamic Gain model. |  [SOURce:DPD:MODel:DYNGain:MEMory:PAST](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:DYNGain:MEMory:PAST) |  None  
Sets and reads the number of Memory Stepsize. |  [SOURce:DPD:MODel:DYNGain:MEMory:STEP](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:MEMory:STEP) |  None  
Enable or disable the DPD model optimization. |  [SOURce:DPD:MODel:DYNGain:OPTimize:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:OPTimize:ENABle) |  None  
Include or exclude memory operators when optimizing the DPD model. |  [SOURce:DPD:MODel:DYNGain:OPTimize:MEMory:OPERator:INCLude](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:DYNGain:OPTimize:MEMory:OPERator:INCLude) |  None  
Sets and reads the number of power segments. |  [SOURce:DPD:MODel:DYNGain:POWer:SEGMent:COUNt](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:POWer:SEGMent:COUN) |  None  
Sets and reads the minimum points per power segment |  [SOURce:DPD:MODel:DYNGain:POWer:SEGMent:POINt:COUNt:MINimum](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:DYNGain:POWer:SEGMent:POINt:COUNt:MIN) |  None  
Create the model using Direct DPD from file or Direct DPD measurement. |  [SOURce:DPD:MODel:USE:DIRect](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MODel:USE:DIRect) |  None  
Sets and reads the maximum PAPR Expansion. |  [SOURce:DPD:PAPR:EXPansion:MAXimum](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:PAPR:EXPansion:MAXimum) |  None  
Sets and reads the backoff power level used during the linear gain S21 measurement for the DPD Dynamic Gain model. |  [SOURce:DPD:MEASure:LINGain:POWer:BACKoff](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MEASure:LINGain:POWer:BACKoff) |  None  
Enable or disable the DUT Linear Gain measurement during the DPD Direct. |  [SOURce:DPD:MEASure:LINGain:ENABle](GP-IB_Command_Finder/SourceDPD.md#SOURce:DPD:MEASure:LINGain:ENABle) |  None  
|  |   
Link VNA to 89600 VSA Command  
Automatically save the VSA state file and embed it into VNA state file |  [SENSe:VSA:SAVe:INCLude[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:SAVe:INCLude:STATe) |  None  
Sets to stream ideal input power to VSA measurement channel. |  [SENSe:VSA:DATA:MOD:PINWav[:STATe]](GP-IB_Command_Finder/Sense/VSA.md#SENSe:VSA:DATA:MOD:PINWav:STATe) |  None  
|  |   
Misc. Commands  
Sets and reads the source correction type. |  [SOURce:CORRection[:SELect]](GP-IB_Command_Finder/SourceModulation.md#SOURce:CORRection:SELec) |  None  
  
* * *

