[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

Trace | [Channel](XTraceChanTopic.md#Channel) | Display-Window Setup | Display-Sheet Setup | Display Setup | External Devices | External Sources | Source Modulation | PMAR | External DC Source | External Pulse Generators | New Measurement | Delete Measurement | Manage Meas | [Balanced Meas](XTraceChanTopic.md#Balanced)   
Hardware: [Interface Control](XTraceChanTopic.md#InterfCont) | [External Test Set](XTraceChanTopic.md#External) | [RF / IF Path Config](XTraceChanTopic.md#Path) | [DSP (PNA-X)](XTraceChanTopic.md#IFDsp)

Description | SCPI | COM  
---|---|---  
Trace  
New Trace | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
Select Trace | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | [View](COM_Reference/Properties/View_Property.md)  
Measure | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Trace Title | [DISPlay:WINDow:TRACe:TITLe:DATA](GP-IB_Command_Finder/Display.md#TraceTitleData) [DISPlay:WINDow:TRACe:TITLe[:STATe]](GP-IB_Command_Finder/Display.md#TraceTitleState) | [Title](COM_Reference/Properties/Title_Property.md) [TraceTitleState](COM_Reference/Properties/TraceTitleState_Property.md)  
Add Trace | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
Delete Trace | [DISPlay:WINDow:TRACe:DELete](GP-IB_Command_Finder/Display.md#tdel) | None  
Move Trace | [DISPlay:WINDow:TRACe:MOVE](GP-IB_Command_Finder/Display.md#traceMove) | [Move](COM_Reference/Methods/Move_Method.md)  
Hold Trace | [CALCulate:MEASure:HOLD:TYPE](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:HOLD:TYPE) [CALCulate:MEASure:HOLD:CLEar](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:HOLD:CLEar) | [TraceHoldType](COM_Reference/Properties/TraceHoldType_Property.md) [TraceHoldClear](COM_Reference/Methods/TraceHoldClear_Method.md)  
Set/get the number of traces of selected channel | [CALCulate:PARameter:COUNt](GP-IB_Command_Finder/Calculate/Parameter.md#Count) | None  
Trace Maximize | [DISPlay:TMAX](GP-IB_Command_Finder/Display.md#TMax) | [TraceMax](COM_Reference/Properties/TraceMax_Property.md)  
  
Channel  
---  
Add | None | [chans.Add](COM_Reference/Methods/Add_channels_Method.md)  
Make Active | None | [app.ActiveChannel](COM_Reference/Properties/Active_Channel_Property.md)  
Read Channel Number | [SYSTem:ACTive:CHANnel?](GP-IB_Command_Finder/System.md#ActiveChannel) | [chan.ChannelNumber](COM_Reference/Properties/Channel_Number_Property.md)  
Read UNUSED channel numbers | None | [chans.UnusedChannelNumbers](COM_Reference/Properties/UnusedChannelNumbers_Property.md)  
Read used channel numbers | None | [chans.UsedChannelNumbers](COM_Reference/Properties/UsedChannelNumbers_Property.md)  
Read number of Channels | None | [chans.Count](COM_Reference/Properties/Count_Property.md)  
Copy all Channel settings | [SYSTem:MACRo:COPY:CHANnel](GP-IB_Command_Finder/System.md#COPY_CHANnel) | [chan.CopyToChannel](COM_Reference/Methods/CopyToChannel_Method.md)  
Copy ONLY mechanical switches and attenuator settings. | [SENSe:PATH:CONFig:COPY](GP-IB_Command_Finder/Sense/Path.md#copy) | [CopyFrom](COM_Reference/Methods/CopyFrom_Method.md)  
Delete a channel | [SYSTem:CHANnels:DELete](GP-IB_Command_Finder/System.md#ChanDelete) | [Remove Method](COM_Reference/Methods/Remove_Method.md) [RemoveChannelNumber](COM_Reference/Methods/RemoveChannelNumber_Method.md)  
Set and return the group of channels | [SYSTem:CHANnels:COUPle:GROup](GP-IB_Command_Finder/System.md#SYSTem:CHANnels:COUPle:GROup) | None  
Set and return the Multi DUT parallel measurement state | [SYSTem:CHANnels:COUPle:PARallel[:ENABle]](GP-IB_Command_Finder/System.md#SYSTem:CHANnels:COUPle:PARallel:ENABle) | None  
Get the information if the parallel measurement is executed in the last sweep | [SYSTem:CHANnels:COUPle:PARallel:STATe?](GP-IB_Command_Finder/System.md#SYSTem:CHANnels:COUPle:PARallel:STATe) | None  
Set up multiple channels for manual trigger | [SYSTem:CHANnels:SINGle](GP-IB_Command_Finder/System.md#SYSTem:CHANnels:SINGle) | None  
  
Display \- Window Setup  
---  
Select Window | [DISPlay:WINDow:TRACe:SELect](GP-IB_Command_Finder/Display.md#tselect) | [ActivateWindow](COM_Reference/Methods/ActivateWindow_Method.md)  
Window Title | [DISPlay:WINDow:TITLe[:STATe]](GP-IB_Command_Finder/Display.md#titstate) | [TitleState](COM_Reference/Properties/Title_State_Property.md)  
Add Window | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) | [Add](COM_Reference/Methods/Add_NAWindows_Method.md)  
Delete Window | [DISPlay:WINDow[:STATe]](GP-IB_Command_Finder/Display.md#dwstat) | None  
Move Window | [DISPlay:WINDow:TRACe:MOVE](GP-IB_Command_Finder/Display.md#traceMove) | [Move](COM_Reference/Methods/Move_Method.md)  
Window Layout | [DISPlay:ARRange](GP-IB_Command_Finder/Display.md#arrange) | [ArrangeWindows](COM_Reference/Properties/Arrange_Windows_Property.md)  
Window Max | [DISPlay:WINDow:SIZe](GP-IB_Command_Finder/Display.md#WinSize) | [WindowState](COM_Reference/Properties/Window_State_Property.md)  
Return Window Number(s) | [DISPlay:CATalog?](GP-IB_Command_Finder/Display.md#cat) | [win.WindowNumber](COM_Reference/Properties/WindowNumber_Property.md)  
Read the window number of the selected trace | [CALCulate:PARameter:WNUMber](GP-IB_Command_Finder/Calculate/Parameter.md#wnum) | [win.WindowNumber](COM_Reference/Properties/WindowNumber_Property.md)  
Creates N windows | [DISPlay:SPLit](GP-IB_Command_Finder/Display.md#Split) | None  
Feed specified measurement to specified window | [DISPlay:WINDow:TRACe:FEED:MNUMber](GP-IB_Command_Finder/Display.md#DISPlay:WINDow:TRACe:FEED:MNUMber) | None  
Returns the next unused trace number | [DISPlay:WINDow:TRACe:NEXT[:NUMBer]](GP-IB_Command_Finder/Display.md#DISPlay:WINDow:TRACe:NEXT:NUMBer) | None  
Set graph divisions | [DISPlay:WINDow:Y[:SCALe]:DIVisions](GP-IB_Command_Finder/Display.md#YDivisions) | None  
  
Display \- Sheet Setup  
---  
Select Sheet | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) | None  
Sheet Title | [DISPlay:SHEet:TITle:DATA](GP-IB_Command_Finder/Display.md#SheetTitle) | None  
Add Sheet | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) [DISPlay:WINDow:FEED](GP-IB_Command_Finder/Display.md#SheetFeed) | None  
Delete Sheet | [DISPlay:SHEet:STATe](GP-IB_Command_Finder/Display.md#SheetState) | None  
Sheet Layout | [DISPlay:SHEet:ARRange](GP-IB_Command_Finder/Display.md#SheetArrange) | None  
Get list of window numbers which the sheet contains | [DISPlay:SHEet:CATalog?](GP-IB_Command_Finder/Display.md#SheetCatalog) | None  
Feed specified window to a sheet | [DISPlay:WINDow:FEED](GP-IB_Command_Finder/Display.md#SheetFeed) | None  
Return active sheet number | [SYSTem:ACTive:SHEet](GP-IB_Command_Finder/System.md#SYSTem:ACTive:SHEet) | None  
Return list of visible sheets | [SYSTem:SHEets:CATalog?](GP-IB_Command_Finder/System.md#SYSTem:SHEet:CATalog) | None  
  
Display Setup  
---  
Trace Status | [DISPlay:WINDow:ANNotation[:TRACe][:STATe]](GP-IB_Command_Finder/Display.md#trstatus) | None  
Y-axis Labels | [DISPlay:WINDow:ANNotation:Y[:STATe]](GP-IB_Command_Finder/Display.md#AnnYstate) | None  
Show Marker Readout | [DISPlay:WINDow:ANNotation:MARKer[:STATe]](GP-IB_Command_Finder/Display.md#mstatus) | [MarkerReadout](COM_Reference/Properties/MarkerReadout_Property.md)  
Large Readout | [DISPlay:WINDow:ANNotation:MARKer:SIZE](GP-IB_Command_Finder/Display.md#size) | [MarkerReadoutSize](COM_Reference/Properties/MarkerReadoutSize_Property.md)  
Readouts Per Trace | [DISPlay:WINDow:ANNotation:MARKer:NUMBer](GP-IB_Command_Finder/Display.md#MarkerNumber) | [MarkerReadoutsPerTrace](COM_Reference/Properties/MarkerReadoutsPerTrace_Property.md)  
Sets the marker readouts to coupled (one combination annotation) or not coupled (one annotation per trace). | [DISPlay:WINDow:ANNotation:MARKer:COUPle](GP-IB_Command_Finder/Display.md#AnnMarkStat) | None  
Shows the marker readouts only for active trace or for all traces. | [DISPlay:WINDow:ANNotation:MARKer:VISible](GP-IB_Command_Finder/Display.md#DISPlayWINDowANNotationMARKerVISible) | None  
Symbol \- Triangle, Flag, and Line | [DISPlay:WINDow:ANNotation:MARKer:SYMBol](GP-IB_Command_Finder/Display.md#MarkerSymbol) | [MarkerSymbol](COM_Reference/Properties/MarkerSymbol_Property.md)  
Decimal Places - Stimulus and Response | [DISPlay:WINDow:ANNotation:MARKer:RESolution:STIMulus](GP-IB_Command_Finder/Display.md#MarkerResoStimulus) [DISPlay:WINDow:ANNotation:MARKer:RESolution:RESPonse](GP-IB_Command_Finder/Display.md#MarkerResolResponse) | [MarkerReadoutStimulusPlaces](COM_Reference/Properties/MarkerReadoutStimulusPlaces_Property.md)  
Readout Position - X and Y | [DISPlay:WINDow:ANNotation:MARKer:XPOSition](GP-IB_Command_Finder/Display.md#MarkerXposition) [DISPlay:WINDow:ANNotation:MARKer:YPOSition](GP-IB_Command_Finder/Display.md#MarkerYposition) | [MarkerReadoutXPosition](COM_Reference/Properties/MarkerReadoutXPosition_Property.md) [MarkerReadoutYPosition](COM_Reference/Properties/MarkerReadoutYPosition_Property.md)  
Marker Colors | [DISPlay:COLor:TRACe:MARKer](GP-IB_Command_Finder/Display_Colors.md#marker) | [Markers](COM_Reference/Properties/Markers_Property.md)  
N Trace: Markers | [DISPlay:COLor:TRACe:MARKer](GP-IB_Command_Finder/Display_Colors.md#marker) | [Markers](COM_Reference/Properties/Markers_Property.md)  
N Trace: Memory Markers | [DISPlay:COLor:TRACe:MMARker](GP-IB_Command_Finder/Display_Colors.md#mmarker) | [MemoryMarkers](COM_Reference/Properties/MemoryMarkers_Property.md)  
Reset Color | [DISPlay:COLor:RESet](GP-IB_Command_Finder/Display_Colors.md#reset) | None  
Save Theme | [DISPlay:COLor:STORe](GP-IB_Command_Finder/Display_Colors.md#store) | [StoreTheme](COM_Reference/Methods/StoreTheme_Method.md)  
Recall Theme | [DISPlay:COLor:LOAD](GP-IB_Command_Finder/Display_Colors.md#load) | [LoadTheme](COM_Reference/Methods/LoadTheme_Method.md)  
Reset Theme | [DISPlay:COLor:RESet](GP-IB_Command_Finder/Display_Colors.md#reset) | [ResetTheme](COM_Reference/Methods/ResetTheme_Method.md)  
Grid Lines - Solid | Dotted | [DISPlay:WINDow:TRACe:GRATicule:GRID:LTYPe](GP-IB_Command_Finder/Display.md#GridLtype) | [GridLineType](COM_Reference/Properties/GridLineType_Property.md)  
Y-axis Divisions - 2 to 30 | [DISPlay:WINDow:TRACe:Y[:SCALe]:PDIVision](GP-IB_Command_Finder/Display.md#pdiv) | [YScale](COM_Reference/Properties/YScale_Property.md)  
Show Table - None, Marker, Limit, Ripple, and Segment | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Toolbar Softkey | [DISPlay:TOOLbar:KEYS[:STATe]](GP-IB_Command_Finder/Display.md#keys) | [ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Toolbar Hardkey | [DISPlay:TOOLbar:KEYS[:STATe]](GP-IB_Command_Finder/Display.md#keys) | [ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Toolbar Port Extensions | [DISPlay:TOOLbar:EXTensions[:STATe]](GP-IB_Command_Finder/Display.md#extensions) | [ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Toolbar Transform | [DISPlay:TOOLbar:TRANsform[:STATe]](GP-IB_Command_Finder/Display.md#transform) | [ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Toolbar Marker | [DISPlay:TOOLbar:MARKer[:STATe]](GP-IB_Command_Finder/Display.md#toolMarker) | [ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Toolbar Cal Set Viewer | [DISPlay:TOOLbar:CSET[:STATe]](GP-IB_Command_Finder/Display.md#DISPlay:TOOLbar:CSET:STATe) | None  
Active Entry Toolbar | [DISPlay:TOOLbar:ENTry[:STATe]](GP-IB_Command_Finder/Display.md#toolEntry) | [ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Toolbar Status Bar | [DISPlay:ANNotation[:STATus]](GP-IB_Command_Finder/Display.md#annstatus) | [ShowStatusBar](COM_Reference/Methods/Show_Status_Bar_Method.md)  
Status Bar | [DISPlay:ANNotation[:STATus]](GP-IB_Command_Finder/Display.md#annstatus) | [ShowStatusBar](COM_Reference/Methods/Show_Status_Bar_Method.md)  
Status Bar Clock | [SYSTem:CLOCk[:STATe]](GP-IB_Command_Finder/System.md#clock) | None  
Default Colors | [DISPlay:COLor:RESet](GP-IB_Command_Finder/Display_Colors.md#reset) | [ResetTheme](COM_Reference/Methods/ResetTheme_Method.md)  
Background Colors | [DISPlay:COLor:BACKground](GP-IB_Command_Finder/Display_Colors.md#back) | [Background](COM_Reference/Properties/Background_Property.md)  
Active Background Color | [DISPlay:COLor:ABACkground](GP-IB_Command_Finder/Display_Colors.md#ActiveBack) | [ActiveBackground](COM_Reference/Properties/ActiveBackground_Property.md)  
Grid Colors | [DISPlay:COLor:GRAT2](GP-IB_Command_Finder/Display_Colors.md#grat2) | [Grid](COM_Reference/Properties/Grid_Property.md)  
Active Labels, Grid Frame Colors | [DISPlay:COLor:GRAT1](GP-IB_Command_Finder/Display_Colors.md#grat1) | [ActiveLabels](COM_Reference/Properties/ActiveLabels_Property.md)  
Inactive Window Labels Colors | [DISPlay:COLor:ILABel](GP-IB_Command_Finder/Display_Colors.md#inLabel) | [InactiveLabels](COM_Reference/Properties/InactiveLabels_Property.md)  
Failed Trace Colors | [DISPlay:COLor:LIM1](GP-IB_Command_Finder/Display_Colors.md#limit) | [FailedTraces](COM_Reference/Properties/FailedTraces_Property.md)  
N Trace: Data and Limits Colors | [DISPlay:COLor:TRACe:DATA](GP-IB_Command_Finder/Display_Colors.md#traceData) | [DataAndLimits](COM_Reference/Properties/DataAndLimits_Property.md)  
N Trace: Memory | [DISPlay:COLor:TRACe:MEMory](GP-IB_Command_Finder/Display_Colors.md#memory) | [Memory](COM_Reference/Properties/Memory_Property.md)  
Display Update | [DISPlay:UPDate[:STATe]](GP-IB_Command_Finder/Display.md#DISPlay:UPDate:STATe) [DISPlay:UPDate:IMMediate](GP-IB_Command_Finder/Display.md#UpdateImmediate) | None  
  
Configure External Devices  
---  
Adds an external device to the system. | [SYSTem:CONFigure:EDEVice:ADD](GP-IB_Command_Finder/SystConfigExternalDevice.md#Add) | [Add (External Device)](COM_Reference/Methods/Add_External_Device_Method.md)  
Returns names of all configured devices | [SYSTem:CONFigure:EDEV:iceCAT?](GP-IB_Command_Finder/SystConfigExternalDevice.md#cat) | [Items](COM_Reference/Properties/Items_Property.md)  
Set driver for the external device. | [SYSTem:CONFigure:EDEVice:DRIVer](GP-IB_Command_Finder/SystConfigExternalDevice.md#Driver) | [Driver](COM_Reference/Properties/Driver_Property.md)  
Set type of device. | [SYSTem:CONFigure:EDEVice:DTYPe](GP-IB_Command_Finder/SystConfigExternalDevice.md#DTYPe) | [DeviceType](COM_Reference/Properties/DeviceType_Property.md)  
Configuration path for external device. | [SYSTem:CONFigure:EDEVice:IOConfig](GP-IB_Command_Finder/SystConfigExternalDevice.md#ioconf) | [IOConfiguration](COM_Reference/Properties/IOConfiguration_Property.md)  
Enable or disable communication with device. | [SYSTem:CONFigure:EDEVice:IOENable](GP-IB_Command_Finder/SystConfigExternalDevice.md#IOEnable) | [IOEnable](COM_Reference/Properties/IOEnable_Property.md)  
Enable/disable an SMU channel. | [SYSTem:CONFigure:EDEVice:SMU:CHANnel[1-4]:STATe](GP-IB_Command_Finder/SystConfigExternalDevice.md#SYSTem:CONFigure:EDEVice:SMU:CHANnel:STATe) | [ChanActive](COM_Reference/Properties/ChanActive_Property.md)  
Sets and returns the name of the External Device. | None | [Name](COM_Reference/Properties/Name_ExtDev_Property.md)  
Activation state of the device. | [SYSTem:CONFigure:EDEVice:STATe](GP-IB_Command_Finder/SystConfigExternalDevice.md#State) | [Active](COM_Reference/Properties/Active_ExtDev_Property.md)  
Time out value for external device. | [SYSTem:CONFigure:EDEVice:TOUT](GP-IB_Command_Finder/SystConfigExternalDevice.md#Tout) | [TimeOut](COM_Reference/Properties/TimeOut_Property.md)  
Remove a device | [SYSTem:CONFigure:EDEVice:REMove](GP-IB_Command_Finder/SystConfigExternalDevice.md#Remove) | [Remove](COM_Reference/Methods/Remove_Method.md)  
Save configuration file | [SYSTem:CONFigure:EDEVice:SAVE](GP-IB_Command_Finder/SystConfigExternalDevice.md#save) | [SaveFile](COM_Reference/Methods/SaveFile_ED_Method.md)  
Load configuration file | [SYSTem:CONFigure:EDEVice:LOAD](GP-IB_Command_Finder/SystConfigExternalDevice.md#load) | [LoadFile](COM_Reference/Methods/LoadFile_ED_Method.md)  
Returns if specified device responds | [SYSTem:CONFigure:EDEVice:EXISts?](GP-IB_Command_Finder/SystConfigExternalDevice.md#EdevExists) | [IsDevicePresent](COM_Reference/Properties/IsDevicePresent_Property.md)  
  
External Source Config  
---  
Set Dwell per Point | [SYSTem:CONFigure:EDEVice:SOURce:DPP](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceDPP) | [DwellPerPoint](COM_Reference/Properties/DwellPerPoint_Property.md)  
Set Trigger Mode | [SYSTem:CONFigure:EDEVice:SOURce:TMODe](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceTMODE) | [Trigger Mode](COM_Reference/Properties/Trigger_Mode_Property.md)  
Set Trigger Port | [SYSTem:CONFigure:EDEVice:SOURce:TPORt](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceTport) | [TriggerPort](COM_Reference/Properties/TriggerPort_Property.md)  
Set Modulation Control | [SYSTem:CONFigure:EDEVice:SOURce:MODulation:CONTrol](GP-IB_Command_Finder/SystConfigExternalDevice.md#ESourceTport) | None  
  
Source Modulation  
---  
Sets and reads the frequency of the arbitrary waveform generator. | [SOURce:MODulation:ARB:CLOCk:SRATe](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:DARB:CLOCk) | None  
Sets and reads the I data for I/Q modulation. | [SOURce:MODulation:ARB:DATA:I](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:DARB:DATA:I) | None  
Sets and reads the Q data for I/Q modulation. | [SOURce:MODulation:ARB:DATA:Q](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:DARB:DATA:Q) | None  
Set and read the modulation state. | [SOURce:MODulation[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:STATe) | None  
Checks if pulse source exists. | [SOURce:PULSe:EXISts?](GP-IB_Command_Finder/source.md#SOURce:PULSe:EXISts) | None  
Turns pulse modulation on and off with an external source. | [SOURce:PULSe:MODulation[:STATe]](GP-IB_Command_Finder/source.md#SOURce:PULSe:STATe) | None  
Sets and reads the maximum number of iterations for an ACP modulation calibration. | [SOURce:MODulation:CORRection:COLLection:ACP:ITERations](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACP:ITERations) | None  
Sets and reads the calibration plane for an ACP modulation calibration.  | [SOURce:MODulation:CORRection:COLLection:ACP:RECeiver](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACP:PLANe) | None  
Sets and reads the calibration span for an ACP modulation calibration. | [SOURce:MODulation:CORRection:COLLection:ACP:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACP:SPAN) | None  
Set and read the ACP modulation calibration state. | [SOURce:MODulation:CORRection:COLLection:ACP:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACP:STATe) | None  
Sets and reads the desired ACP calibration tolerance for the ACP modulation calibration. | [SOURce:MODulation:CORRection:COLLection:ACP:TOLerance](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACP:TOLerance) | None  
Sets the Notch location.  | [SOURce:MODulation:CORRection:COLLection:ACQuire](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACQuire) | None  
Returns a message indicating if the calibration was successful or not. | [SOURce:MODulation:CORRection:COLLection:ACQuire:STATus?](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:ACQuire:STATus) | None  
Sets and reads the maximum number of iterations for a flatness modulation calibration. | [SOURce:MODulation:CORRection:COLLection:FLATness:ITERations](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:FLATness:ITERations) | None  
Sets and reads the calibration plane for flatness modulation calibration.  | [SOURce:MODulation:CORRection:COLLection:FLATness:RECeiver](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:FLATness:PLANe) | None  
Sets and reads the calibration span for a flatness modulation calibration. | [SOURce:MODulation:CORRection:COLLection:FLATness:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:FLATness:SPAN) | None  
Set and read the flatness modulation calibration state. | [SOURce:MODulation:CORRection:COLLection:FLATness:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:FLATness:STATe) | None  
Sets and reads the desired flatness calibration tolerance for the flatness modulation calibration. | [SOURce:MODulation:CORRection:COLLection:FLATness:TOLerance](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:FLATness:TOLerance) | None  
Sets and reads the maximum number of iterations to provide the deepest notch. | [SOURce:MODulation:CORRection:COLLection:NOTch:ITERations](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:NOTch:ITERations) | None  
Sets and reads the calibration plane for an notch modulation calibration.  | [SOURce:MODulation:CORRection:COLLection:NOTch:RECeiver](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:NOTch:PLANe) | None  
Sets and reads the calibration span for a notch modulation calibration. | [SOURce:MODulation:CORRection:COLLection:NOTch:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:NOTch:SPAN) | None  
Set and read the notch modulation calibration state. | [SOURce:MODulation:CORRection:COLLection:NOTch:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:NOTch:ENABle) | None  
Sets and reads the desired notch calibration tolerance for the notch modulation calibration. | [SOURce:MODulation:CORRection:COLLection:NOTch:TOLerance](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:NOTch:TOLerance) | None  
Sets and reads the maximum number of iterations for a power modulation calibration. | [SOURce:MODulation:CORRection:COLLection:POWer:ITERations](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:POWer:ITERations) | None  
Sets and reads the calibration plane for a power modulation calibration.  | [SOURce:MODulation:CORRection:COLLection:POWer:RECeiver](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:POWer:PLANe) | None  
Sets and reads the calibration span for a power modulation calibration. | [SOURce:MODulation:CORRection:COLLection:POWer:SPAN](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:POWer:SPAN) | None  
Set and read the power modulation calibration state. | [SOURce:MODulation:CORRection:COLLection:POWer:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:POWer:STATe) | None  
Sets and reads the desired power calibration tolerance for the power modulation calibration. | [SOURce:MODulation:CORRection:COLLection:POWer:TOLerance](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:POWer:TOLerance) | None  
Set and read the modulation correction state. | [SOURce:MODulation:CORRection[:STATe]](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:STATe) | None  
Returns a list of modulation files (*.mdx). | [SOURce:MODulation:FILE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:FILE) | None  
Loads the specified modulation file.  | [SOURce:MODulation:LOAD](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:LOAD) | None  
Saves the specified modulation file.  | [SOURce:MODulation:SAVE](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:SAVE) | None  
Enables fast calibration. | [SOURce:MODulation:CORRection:COLLection:FAST:ENABle](GP-IB_Command_Finder/SourceModulation.md#SOURce:MODulation:CORRection:COLLection:FAST:ENABle) | None  
  
Power Meter As Receiver (PMAR) Config [See commands to configure and specify a
Non- PMAR Power Sensor](CalTopic.htm#Sensors)  
---  
Enable use of internal cal factors | [SYSTem:CONFigure:EDEVice:PMAR:CFACtors[:STATe]](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:CFACtors:STATe) | [UseInternalCalFactors](COM_Reference/Properties/UseInternalCalFactors_Property.md)  
Enable min and max freqs | [SYSTem:CONFigure:EDEVice:PMAR:FLIMit](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarFLimit) | [LimitFrequency](COM_Reference/Properties/LimitFrequency_Property.md)  
Set Max freq | [SYSTem:CONFigure:EDEVice:PMAR:FMAXimum](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarFMAX) | [MaximiumFrequency](COM_Reference/Properties/MaximiumFrequency_sourceCal_Property.md)  
Set Min freq | [SYSTem:CONFigure:EDEVice:PMAR:FMINimum](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarFmin) | [MinimumFrequency](COM_Reference/Properties/MinimumFrequency_sourceCal_Property.md)  
Set max number of PM readings | [SYSTem:CONFigure:EDEVice:PMAR:READing:COUNt](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarReadCount) | [ReadingsPerPoint](COM_Reference/Properties/ReadingsPerPoint_Property.md)  
Set tolerance level | [SYSTem:CONFigure:EDEVice:PMAR:READing:NTOLerance](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarReadNtol) | [ReadingsTolerance](COM_Reference/Properties/ReadingsTolerance_Property.md)  
Select sensor | [SYSTem:CONFigure:EDEVice:PMAR:SENSor](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarSens) | [SensorIndex](COM_Reference/Properties/SensorIndex_Property.md)  
Set Cal Factor data | [SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:DATA](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarCFACDate) | [ReferenceCalFactor](COM_Reference/Properties/ReferenceCalFactor_Property.md)  
Set Cal Factor frequencies | [SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:FREQuency](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarCFACFreq) | [Frequency](COM_Reference/Properties/Frequency_Property.md)  
Set Power loss data | [SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:DATA](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarLossData) | [Loss](COM_Reference/Properties/Loss_sourceCal_Property.md)  
Set Power loss frequencies | [SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:FREQuency](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarLossFreq) | [Frequency](COM_Reference/Properties/Frequency_Property.md)  
Enable Power loss data | [SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:STATe](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarLossState) | [UsePowerLossSegments](COM_Reference/Properties/UsePowerLossSegments_Property.md)  
Set reference cal factor | [SYSTem:CONFigure:EDEVice:PMAR:TABLe:RFACtor](GP-IB_Command_Finder/SystConfigExtPMAR.md#pmarRFAC) | [ReferenceCalFactor](COM_Reference/Properties/ReferenceCalFactor_Property.md)  
Set Zero method | [SYSTem:CONFigure:EDEVice:PMAR:ZERO](GP-IB_Command_Finder/SystConfigExtPMAR.md#zero) | None  
Perform Cal | [SYSTem:CONFigure:EDEVice:PMAR:CALibrate](GP-IB_Command_Finder/SystConfigExtPMAR.md#Calibrate) | None  
Returns a list of available power meters that have power uncertainty. | [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:CATalog?](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNC:CAT) | [UncertaintyModelCatalog?](COM_Reference/Properties/UncertaintyModelCatalog_Property.md)  
Sets and returns a custom model uncertainty file containing all of the power meter uncertainty properties. | [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:FILE](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNC:FILE) | [UncertaintyFile](COM_Reference/Properties/UncertaintyFile_Property.md)  
Returns a list of available power meters that have power uncertainty. | [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:MODel](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNC:MOD) | [UncertaintyModel](COM_Reference/Properties/UncertaintyModel_Property.md)  
Returns the power level for best accuracy. | [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:PLEVel?](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:PLEVel) | [PowerForBestAccuracy](COM_Reference/Properties/PowerForBestAccuracy_Property.md)  
Returns the power meter reading uncertainty. | [SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:READ?](GP-IB_Command_Finder/SystConfigExtPMAR.md#SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:READ) | [PowerMtrReadingUncertainty](COM_Reference/Properties/PowerMtrReadingUncertainty_Property.md)  
  
External DC Source/Meter [See DC Source sweep commands](XStimulusTopic.md#DC) |  |   
---|---|---  
Correction ON/OFF | [SYSTem:CONFigure:EDEVice:DC:CORRection](GP-IB_Command_Finder/SystConfigExtDC.md#CorrectionState) | [DCCorrection](COM_Reference/Properties/DCCorrection_Property.md)  
Offset correction value. | [SYSTem:CONFigure:EDEVice:DC:OFFSet](GP-IB_Command_Finder/SystConfigExtDC.md#offset) | [DCOffset](COM_Reference/Properties/DCOffset_Property.md)  
Scale correction value. | [SYSTem:CONFigure:EDEVice:DC:SCALe](GP-IB_Command_Finder/SystConfigExtDC.md#scale) | [DCScale](COM_Reference/Properties/DCScale_Property.md)  
DC Type (Units). | [SYSTem:CONFigure:EDEVice:DC:TYPE](GP-IB_Command_Finder/SystConfigExtDC.md#TYPE) | [DCType](COM_Reference/Properties/DCType_Property.md)  
Dwell Before/After Point | [SYSTem:CONFigure:EDEVice:DC:DPOint](GP-IB_Command_Finder/SystConfigExtDC.md#DwellPoint) | [PointDwell](COM_Reference/Properties/PointDwell_Property.md)  
Dwell Before Sweep value | [SYSTem:CONFigure:EDEVice:DC:DSWeep](GP-IB_Command_Finder/SystConfigExtDC.md#DwellSweep) | [SweepDwell](COM_Reference/Properties/SweepDwell_Property.md)  
Set and return the maximum output current value of the external DC Source | [SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent) | [CurrentLimit](COM_Reference/Properties/CurrentLimit.md)  
Set and return the maximum output voltage value of the external DC Source | [SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage) | [VoltageLimit](COM_Reference/Properties/VoltageLimit.md)  
Set and return the DC Meter/DC Source Abort Sweep command | [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt) | [AbortSweepCmd](COM_Reference/Properties/AbortSweepCmd_Property.md)  
Set and return the DC Meter/DC Source After Sweep command | [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer) | [AfterSweepCmd](COM_Reference/Properties/AfterSweepCmd_Property.md)  
Set and return the DC Meter/DC Source Before Sweep command | [SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore) | [BeforeSweepCmd](COM_Reference/Properties/BeforeSweepCmd_Property.md)  
Set and return the DC Meter/DC Source Error Query command | [SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor) | [ErrorQuery](COM_Reference/Properties/ErrorQuery_Property.md)  
Set and return the DC Meter/DC Source Disable I/O command | [SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT) | [ExitCmd](COM_Reference/Properties/ExitCmd_Property.md)  
Set and return the DC Meter/DC Source ID Query command | [SYSTem:CONFigure:EDEVice:DC:QUERy:ID](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:QUERy:ID) | [IDQuery](COM_Reference/Properties/IDQuery_Property.md)  
Set and return the DC Meter/DC Source Enable I/O command | [SYSTem:CONFigure:EDEVice:DC:COMMand:INIT](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:INIT) | [InitCmd](COM_Reference/Properties/InitCmd_Property.md)  
Set and return the DC Source maximum output | [SYSTem:CONFigure:EDEVice:DC:MAX:VALue](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MAX:VALue) | [MaxOutput](COM_Reference/Properties/MaxOutput_Property.md)  
Set and return the DC Source maximum output state | [SYSTem:CONFigure:EDEVice:DC:MAX[:STATe]](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MAX_:STATe) | [MaxOutputState](COM_Reference/Properties/MaxOutputState_Property.md)  
Set and return the DC Source minimum output | [SYSTem:CONFigure:EDEVice:DC:MIN:VALue](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MIN:VALue) | [MinOutput](COM_Reference/Properties/MinOutput_Property.md)  
Set and return the DC Source minimum output state | [SYSTem:CONFigure:EDEVice:DC:MIN[:STATe]](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:MIN_:STATe) | [MinOutputState](COM_Reference/Properties/MinOutputState_Property.md)  
Set and return the Point Read commands and Point Set commands | [SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET](GP-IB_Command_Finder/SystConfigExtDC.md#SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET) | [PointCmd](COM_Reference/Properties/PointCmd_Property.md)  
  
External Pulse Generators |  |   
---|---|---  
PG Names catalog | [SENSe:PULSe:CATalog?](GP-IB_Command_Finder/Sense/Pulse.md#catalog) | [PulseGeneratorNames](COM_Reference/Properties/PulseGeneratorNames_Property.md)  
Read the integer of the name | Not applicable | [PulseGeneratorID](COM_Reference/Properties/PulseGeneratorID_Property.md)  
Set output channel | [SYSTem:CONFigure:EDEVice:PULSe:CHAN](GP-IB_Command_Finder/SystConfigExtPulseGen.md#chan) | [OutputChannel](COM_Reference/Properties/OutputChannel_Property.md)  
Set output Hi amplitude (volts) | [SYSTem:CONFigure:EDEVice:PULSe:HAMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#hamp) | [HighAmplitude](COM_Reference/Properties/HighAmplitude_Property.md)  
Set output Low amplitude (volts) | [SYSTem:CONFigure:EDEVice:PULSe:LAMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#lamp) | [LowAmplitude](COM_Reference/Properties/LowAmplitude_Property.md)  
Set load impedance | [SYSTem:CONFigure:EDEVice:PULSe:LIMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#limp) | [LoadImpedance](COM_Reference/Properties/LoadImpedance_Property.md)  
Set source impedance | [SYSTem:CONFigure:EDEVice:PULSe:SIMP](GP-IB_Command_Finder/SystConfigExtPulseGen.md#simp) | [SourceImpedance](COM_Reference/Properties/SourceImpedance_Property.md)  
Master Mode | [SYSTem:CONFigure:EDEVice:PULSe:MMODe](GP-IB_Command_Finder/SystConfigExtPulseGen.md#Mmode) | [MasterMode](COM_Reference/Properties/MasterMode_Property.md)  
Optional Name/ID argument added to some Pulse gen commands. | [SENSe:PULSe](GP-IB_Command_Finder/Sense/Pulse.md) | [PulseGenerator Object](COM_Reference/Objects/PulseGenerator_Object.md)  
  
New Measurement  
---  
Create S-Parameter Meas. | [CALCulate:MEASure::DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [app.CreateSParameterEx](COM_Reference/Methods/Create_SParameterEX_Method.md)  
Create Measurement | [CALCulate:MEASure::DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [app.CreateMeasurement](COM_Reference/Methods/CreateMeasurement_Method.md)  
Add Measurement | None | [meass.Add](COM_Reference/Methods/Add_measurement_Method.md)  
List Measurements | [CALCulate:PARameter:CATalog:EXTended](GP-IB_Command_Finder/Calculate/Parameter.md#ParCatExtended) | None  
Delete Measurement  
Delete a measurement | [CALCulate:MEASure::DELete](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DELete) | [Measurements.Remove](COM_Reference/Methods/Remove_Method.md)  
Delete ALL measurements | [CALCulate:MEASure::DELete:ALL](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DELete:ALL) | None  
Manage Measurements  
Get a handle to a Trace | None | [win.ActiveTrace](COM_Reference/Properties/Active_Trace_Property.md)  
Select a Measurement Parameter | [CALCulate:PARameter:SELect](GP-IB_Command_Finder/Calculate/Parameter.md#cps) | [app.ActiveMeasurement](COM_Reference/Properties/Active_Measurement_Property.md)  
Read Channel Number | [SYSTem:ACTive:CHANnel?](GP-IB_Command_Finder/System.md#ActiveChannel) | [chan.ChannelNumber](COM_Reference/Properties/Channel_Number_Property.md)  
Read Channel Numbers in use | [SYSTem:CHANnels:CATalog?](GP-IB_Command_Finder/System.md#ChanCat) | None  
Read Number of Measurements | None | [chans.Count](COM_Reference/Properties/Count_Property.md)  
Read Measurement Parameter | None | [meas.Parameter](COM_Reference/Properties/Parameter_Property.md)  
Set / Read Measurement Name | [SYSTem:ACTive:MEASurement (read-only)](GP-IB_Command_Finder/System.md#ActMeas) | [meas.Name](COM_Reference/Properties/Name_Meas_Property.md)  
Read Active Measurement Number | [SYSTem:ACTive:MEASurement:NUMBer?](GP-IB_Command_Finder/System.md#ActMeasNumber) | [meas.Number](COM_Reference/Properties/Number_meas_Property.md)  
Change Parameter | [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) | [meas.ChangeParameter](COM_Reference/Methods/Change_Parameter_Method.md)  
Returns the Measurement Class name | [SENSe:CLASs:NAME?](GP-IB_Command_Finder/Sense/Class.md#name) | [Get_MeasurementClass](COM_Reference/Properties/MeasurementClass_Property.md)  
Read the window number of the selected trace | [CALCulate:PARameter:WNUMber](GP-IB_Command_Finder/Calculate/Parameter.md#wnum) | None  
Read the trace number of the selected trace | [CALCulate:PARameter:TNUMber?](GP-IB_Command_Finder/Calculate/Parameter.md#Tnum) | None  
Maximize (Isolate) trace | [DISPlay:TMAX](GP-IB_Command_Finder/Display.md#TMax) | [TraceMax](COM_Reference/Properties/TraceMax_Property.md)  
Move a trace to another window | [DISPlay:WINDow:TRACe:MOVE](GP-IB_Command_Finder/Display.md#traceMove) | [Trace.Move](COM_Reference/Methods/Move_Method.md)  
Trace Hold | [CALCulate:MEASure:HOLD:TYPE](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:HOLD:TYPE) | [TraceHoldType](COM_Reference/Properties/TraceHoldType_Property.md)  
Trace Hold Clear | [CALCulate:MEASure:HOLD:CLEar](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:HOLD:CLEar) | [TraceHoldClear](COM_Reference/Methods/TraceHoldClear_Method.md)  
Deletes the trace associated with the specified measurement number | [DISPlay:MEASure:DELete](GP-IB_Command_Finder/Display.md#MeasDelete) | None  
Create a new trace in the specified window | [DISPlay:MEASure:FEED](GP-IB_Command_Finder/Display.md#MeasFeed) | None  
Turn the memory trace ON or OFF for the specified measurement | [DISPlay:MEASure:MEMory[:STATe]](GP-IB_Command_Finder/Display.md#MeasMem) | None  
Move a trace associated with measurement number to the specified window | [DISPlay:MEASure:MOVE](GP-IB_Command_Finder/Display.md#MeasMove) | None  
Activate the specified measurement to be selected | [DISPlay:MEASure:SELect](GP-IB_Command_Finder/Display.md#MeasSelect) | None  
Turn trace display associated with the specified measurement ON or OFF | [DISPlay:MEASure[:STATe]](GP-IB_Command_Finder/Display.md#MeasState) | None  
Set or return the title for the specified measurement | [DISPlay:MEASure:TITLe:DATA](GP-IB_Command_Finder/Display.md#MeasTitleData) | None  
Turn the measurement title ON or OFF | [DISPlay:MEASure:TITLe[:STATe]](GP-IB_Command_Finder/Display.md#MeasTitle) | None  
Autoscale the specified trace in the specified measurement | [DISPlay:MEASure:Y[:SCALe]:AUTO](GP-IB_Command_Finder/Display.md#MeasYAuto) | None  
Set the Y axis Scale Per Division value of the specified trace associated with the specified measurement | [DISPlay:MEASure:Y[:SCALe]:PDIVision](GP-IB_Command_Finder/Display.md#MeasYPdiv) | None  
Set the Y axis Reference Level of the specified trace associated with the specified measurement | [DISPlay:MEASure:Y[:SCALe]:RLEVel](GP-IB_Command_Finder/Display.md#MeasYRlev) | None  
Set the Reference Position of the specified trace associated with the specified measurement | [DISPlay:MEASure:Y[:SCALe]:RPOSition](GP-IB_Command_Finder/Display.md#MeasYRpos) | None  
[All Measurement Classes / Applications](MixerTopic.md) |  |   
  
Balanced Measurements and Fixturing  
---  
Configure Topology | [CALCulate:FSIMulator:BALun](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md) | [BalancedTopology Object](COM_Reference/Objects/BalancedTopology_Object.md)  
Configure Balanced Measurement | [CALCulate:FSIMulator:BALun](GP-IB_Command_Finder/Calculate/FSimulatorBalun.md) | [BalancedMeasurement Object](COM_Reference/Objects/BalancedMeasurement_Object.md)  
Maps the physical VNA ports to a device of balanced and single-ended logical ports for multi-port systems with greater than 4 ports | [CALCulate:DTOPology](GP-IB_Command_Finder/Calculate/Calculate_DTOPology_Command.md) | [SetCustomDUTTopology](COM_Reference/Methods/SetCustomDUTTopology_Method.md)  
  
Interface Control  
---  
Interface Control ON|OFF | [CONTrol:CHANnel:INTerface:CONTrol[:STATe]](GP-IB_Command_Finder/Control.md#InterfaceState) | [IC.State](COM_Reference/Properties/State_Property.md)  
Recall Interface Control file | [CONTrol:CHANnel:INTerface:CONTrol:CONFig:RECall](GP-IB_Command_Finder/Control.md#InterfaceRecall) | [IC.ConfigurationFile](COM_Reference/Properties/ConfigurationFile_Property.md)  
  
External Testset Control (also for E5092A)  
---  
Returns a list of currently supported test sets. | [SENSe:MULTiplexer:CATalog?](GP-IB_Command_Finder/Sense/Multiplexer.md#Catalog) | [tsts.TestsetCalalog](COM_Reference/Methods/TestsetCatalog_Method.md)  
Load config file and Restart VNA. | [SYSTem:CONFigure](GP-IB_Command_Finder/System.md#config) | [app.Configure](COM_Reference/Methods/Configure_Method.md)  
Loads a test set configuration file. (and SCPI only - sets ID value). | [SENSe:MULTiplexer:TYPE](GP-IB_Command_Finder/Sense/Multiplexer.md#type) | [ts.Add](COM_Reference/Methods/Add_Testset_Method.md)  
Returns the test set model | [SENSe:MULTiplexer:TYPE](GP-IB_Command_Finder/Sense/Multiplexer.md#type) | [ts.Type](COM_Reference/Properties/Type_ts_Property.md)  
Returns the test set ID number. | None | [ts.ID](COM_Reference/Properties/ID_Property.md)  
Returns the number of input ports | [SENSe:MULTiplexer:INCount?](GP-IB_Command_Finder/Sense/Multiplexer.md#incount) | None  
Switches an input to one of the valid outputs (E5091A only). | None | [OutputPort](COM_Reference/Properties/OutputPort_Property.md)  
Returns the total number of ports on the test set. | [SENSe:MULTiplexer:COUNt?](GP-IB_Command_Finder/Sense/Multiplexer.md#count) | [NumberOfPorts](COM_Reference/Properties/NumberOfPorts_Property.md)  
Sets and returns the address for the external test set at the specified ID. | [SENSe:MULTiplexer:ADDRess](GP-IB_Command_Finder/Sense/Multiplexer.md#address) | None  
Turns ON/OFF the port mapping and control line output. | [SENSe:MULTiplexer:STATe](GP-IB_Command_Finder/Sense/Multiplexer.md#state) | [Enabled](COM_Reference/Properties/Enabled_Property.md)  
Sets and returns the port mappings for ALL ports. | [SENSe:MULTiplexer:ALLPorts](GP-IB_Command_Finder/Sense/Multiplexer.md#AllPorts) | [OutputPorts](COM_Reference/Properties/OutputPorts_Property.md)  
Sets and returns the mapping for a single port. | [SENSe:MULTiplexer:PORT:SELect](GP-IB_Command_Finder/Sense/Multiplexer.md#PortSelect) | [ts.SelectPort](COM_Reference/Properties/SelectPort_Property.md)  
Returns the label on a given channel. | [SENSe:MULTiplexer:LABel](GP-IB_Command_Finder/Sense/Multiplexer.md#label) | [Label](COM_Reference/Properties/Label_Testset_Property.md)  
Turns ON/OFF status bar display of test set properties. | [SENSe:MULTiplexer:DISPlay](GP-IB_Command_Finder/Sense/Multiplexer.md#display) | [ShowProperties](COM_Reference/Properties/ShowProperties_Property.md)  
Sets the control lines. | [SENSe:MULTiplexer:OUTPut](GP-IB_Command_Finder/Sense/Multiplexer.md#outputData) | [ControlLines](COM_Reference/Properties/ControlLines_Property.md)  
Returns the selections available for a given logical port. | [SENSe:MULTiplexer:PORT:CATalog?](GP-IB_Command_Finder/Sense/Multiplexer.md#portCat) | [PortCatalog](COM_Reference/Properties/PortCatalog_Property.md)  
Reads a Cal Set for the Test Set model. | [SENSe:CORRection:CSET:TSET:ALLPorts?](GP-IB_Command_Finder/Sense/CorrCset.md#AllPorts) | [calset.OutputPorts](COM_Reference/Properties/OutputPorts_calset_Property.md)  
Reads a Cal Set for the Port Mapping. | [SENSe:CORRection:CSET:TSET:TYPE?](GP-IB_Command_Finder/Sense/CorrCset.md#TsetType) | [calset.TestSetType](COM_Reference/Properties/TestSetType_Property.md)  
All Sense Multiplexer commands | [SENSe:MULTiplexer](GP-IB_Command_Finder/Sense/Multiplexer.md) | [TestsetControl Object](COM_Reference/Objects/TestsetControl_Object.md)  
All Control Multiplexer commands (E5092A only) | [CONTrol:MULTiplexer](GP-IB_Command_Finder/Control_Multiplexer.md) | None  
  
RF / IF Path Configuration (PNA-X)  
---  
Catalog configuration names | [SENSe:PATH:CONFig:CATalog?](GP-IB_Command_Finder/Sense/Path.md#catalog) | [Configurations](COM_Reference/Properties/Configurations_Property.md)  
Load a configuration | [SENSe:PATH:CONFig:SELect](GP-IB_Command_Finder/Sense/Path.md#select) | [LoadConfiguration](COM_Reference/Methods/LoadConfiguration_Method.md)  
Store a configuration | [SENSe:PATH:CONFig:STORe](GP-IB_Command_Finder/Sense/Path.md#store) | [StoreConfiguration](COM_Reference/Methods/StoreConfiguration_Method.md)  
Delete a configuration | [SENSe:PATH:CONFig:DELete](GP-IB_Command_Finder/Sense/Path.md#delete) | [DeleteConfiguration](COM_Reference/Methods/DeleteConfiguration_Method.md)  
Read the name of a configuration | [SENSe:PATH:CONFig:NAME?](GP-IB_Command_Finder/Sense/Path.md#name) | [Name config](COM_Reference/Properties/Name_config_Property.md)  
Write descriptive text | [SENSe:PATH:CONFig:DTEXt](GP-IB_Command_Finder/Sense/Path.md#dtext) | [DescriptiveText](COM_Reference/Properties/DescriptiveText_Property.md)  
Catalog all elements | [SENSe:PATH:CONFig:ELEMent:CATalog?](GP-IB_Command_Finder/Sense/Path.md#elementCat) | [Elements](COM_Reference/Properties/Elements_Property.md)  
Catalog all settings | [SENSe:PATH:CONFig:ELEMent:VALue:CATalog?](GP-IB_Command_Finder/Sense/Path.md#value) | [Values](COM_Reference/Properties/Values_Property.md)  
Set element | [SENSe:PATH:CONFig:ELEMent](GP-IB_Command_Finder/Sense/Path.md#state) | [Element](COM_Reference/Properties/Element_Property.md)  
Set value for an element | [SENSe:PATH:CONFig:ELEMent](GP-IB_Command_Finder/Sense/Path.md#state) | [Value](COM_Reference/Properties/Value_element_Property.md)  
Read name of current element | [SENSe:PATH:CONFig:ELEMent](GP-IB_Command_Finder/Sense/Path.md#state) | [element.Name](COM_Reference/Properties/Name_element_Property.md)  
[RF Path configuration elements / values](RF_PathConfig.md) [IF Path
configuration elements /
values](../IFAccess/IF_Path_Configuration.htm#elements) [Power Range
commands](DataTopic.htm#Power_Range) [All Pulse
commands](XStimulusTopic.htm#Pulse)  
  
DSP Settings (PNA-X Remote only)  
---  
Sets ADC capture mode: auto or manual | [SENSe:IF:FILTer:CMODe](GP-IB_Command_Finder/Sense/XSensIF.md#CaptMode) | [ADCCaptureMode](COM_Reference/Properties/ADCCaptureMode_Property.md)  
Sets and returns method for specifying the way the IF Frequency is determined. | [SENSe:IF:FREQuency:AUTO](GP-IB_Command_Finder/Sense/XSensIF.md#FreqAuto) | [IFFrequencyMode](COM_Reference/Properties/IFFrequencyMode_Property.md)  
Sets and returns the IF frequency. | [SENSe:IF:FREQuency](GP-IB_Command_Finder/Sense/XSensIF.md#freqValue) | [IFFrequency](COM_Reference/Properties/IFFrequency_Property.md)  
Returns the Maximum allowed IFFrequency | [SENSe:IF:FREQuency](GP-IB_Command_Finder/Sense/XSensIF.md#freqValue) | [MaximumIFFrequency](COM_Reference/Properties/MaximumIFFrequency_Property.md)  
Returns the Minimum allowed IFFrequency | [SENSe:IF:FREQuency](GP-IB_Command_Finder/Sense/XSensIF.md#freqValue) | [MinimumIFFrequency](COM_Reference/Properties/MinimumIFFrequency_Property.md)  
Returns errors with manual digital filter settings | [SENSe:IF:FILTer:ERRors?](GP-IB_Command_Finder/Sense/XSensIF.md#Errors) | [FilterErrors](COM_Reference/Properties/FilterErrors_Property.md)  
Sets digital filter mode. | [SENSe:IF:FILTer:AUTO](GP-IB_Command_Finder/Sense/XSensIF.md#auto) | [FilterMode](COM_Reference/Properties/FilterMode_Property.md)  
Sets Stage1Coefficients | [SENSe:IF:FILTer:STAGE<n>:COEFicients](GP-IB_Command_Finder/Sense/XSensIF.md#coef) | [Stage1Coefficients](COM_Reference/Properties/Stage1Coefficients_Property.md)  
Sets Stage1 NCO frequency | [SENSe:IF:FILTer:STAGe1:FREQuency](GP-IB_Command_Finder/Sense/XSensIF.md#stgFreq) | [Stage1Frequency](COM_Reference/Properties/Stage1Frequency_Property.md)  
Returns the maximum value of any single stage1coefficient. | [SENSe:IF:FILTer:STAGe<n>:COEFicients](GP-IB_Command_Finder/Sense/XSensIF.md#coef) | [Stage1MaximumCoefficient](COM_Reference/Properties/Stage1MaximumCoefficient_Property.md)  
Returns the maximum number of Stage1 coefficients | [SENSe:IF:FILTer:STAGe<n>:COUNt?](GP-IB_Command_Finder/Sense/XSensIF.md#count) | [Stage1MaximumCoefficientCount](COM_Reference/Properties/Stage1MaximumCoefficientCount_Property.md)  
Returns the minimum number of Stage1 coefficients | [SENSe:IF:FILTer:STAGe<n>:COUNt?](GP-IB_Command_Finder/Sense/XSensIF.md#count) | [Stage1MinimumCoefficientCount](COM_Reference/Properties/Stage1MinimumCoefficientCount_Property.md)  
Sets Stage2Coefficients | [SENSe:IF:FILTer:STAGe<n>:COEFicients](GP-IB_Command_Finder/Sense/XSensIF.md#coef) | [Stage2Coefficients](COM_Reference/Properties/Stage2Coefficients_Property.md)  
Returns the maximum value of any single stage2coefficient. | [SENSe:IF:FILTer:STAGe<n>:COEFicients](GP-IB_Command_Finder/Sense/XSensIF.md#coef) | [Stage2MaximumCoefficient](COM_Reference/Properties/Stage2MaximumCoefficient_Property.md)  
Returns the maximum number of Stage2 coefficients | [SENSe:IF:FILTer:STAGe<n>:COUNt?](GP-IB_Command_Finder/Sense/XSensIF.md#count) | [Stage2MaximumCoefficientCount](COM_Reference/Properties/Stage2MaximumCoefficientCount_Property.md)  
Returns the minimum number of Stage2 coefficients | [SENSe:IF:FILTer:STAGe<n>:COUNt?](GP-IB_Command_Finder/Sense/XSensIF.md#count) | [Stage2MinimumCoefficientCount](COM_Reference/Properties/Stage2MinimumCoefficientCount_Property.md)  
Sets and returns stage3 filter type | [SENSe:IF:FILTer:STAGe3:TYPE](GP-IB_Command_Finder/Sense/XSensIF.md#stg3Type) | [Stage3FilterType](COM_Reference/Properties/Stage3FilterType_Property.md)  
Returns the names of supported types of Stage3 filters. | [SENSe:IF:FILTer:STAGe3:CATalog?](GP-IB_Command_Finder/Sense/XSensIF.md#stg3Cat) | [Stage3FilterTypes](COM_Reference/Properties/Stage3FilterTypes_Property.md)  
Sets and returns the parameter value of the current filter type. | [SENSe:IF:FILTer:STAGe3:PARameter](GP-IB_Command_Finder/Sense/XSensIF.md#stg3Param) | [Stage3Parameter](COM_Reference/Properties/Stage3Parameter_Property.md)  
Returns maximum parameter value for the current filter type. | [SENSe:IF:FILTer:STAGe3:PARameter](GP-IB_Command_Finder/Sense/XSensIF.md#stg3Param) | [Stage3ParameterMaximum](COM_Reference/Properties/Stage3ParameterMaximum_Property.md)  
Returns minimum parameter value for the current filter type. | [SENSe:IF:FILTer:STAGe3:PARameter](GP-IB_Command_Finder/Sense/XSensIF.md#stg3Param) | [Stage3ParameterMinimum](COM_Reference/Properties/Stage3ParameterMinimum_Property.md)  
Returns the names of parameters for the current filter type. | [SENSe:IF:FILTer:STAGe3:PCATalog?](GP-IB_Command_Finder/Sense/XSensIF.md#stg3Pcat) | [Stage3Parameters](COM_Reference/Properties/Stage3Parameters_Property.md)  
  
* * *

