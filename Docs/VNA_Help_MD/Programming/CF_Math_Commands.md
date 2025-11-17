# Math Commands

Memory |  Analysis |  Time  
Domain |  Time  
Gating  
---|---|---|---  
  
Memory Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Data -> Memory |  | [CALCulate:MEASure:MATH:MEMorize](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:MEMorize) | [DataToMemory](COM_Reference/Methods/DataToMemory_Method.md)  
Normalize |  | [CALCulate:MEASure:MATH:NORMalize](GP-IB_Command_Finder/Calculate/Measure.md#MathNorm) | None  
Data Math | Off | [CALCulate:MEASure:MATH:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:FUNCtion) | [TraceMath](COM_Reference/Properties/Trace_Math_Property.md)  
Data / Memory | [CALCulate:MEASure:MATH:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:FUNCtion) | [TraceMath](COM_Reference/Properties/Trace_Math_Property.md)  
Data * Memory | [CALCulate:MEASure:MATH:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:FUNCtion) | [TraceMath](COM_Reference/Properties/Trace_Math_Property.md)  
Data - Memory | [CALCulate:MEASure:MATH:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:FUNCtion) | [TraceMath](COM_Reference/Properties/Trace_Math_Property.md)  
Data + Memory | [CALCulate:MEASure:MATH:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:FUNCtion) | [TraceMath](COM_Reference/Properties/Trace_Math_Property.md)  
Display | Data Trace | [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) | [View](COM_Reference/Properties/View_Property.md)  
Memory Trace | [DISPlay:WINDow:TRACe:MEMory](GP-IB_Command_Finder/Display.md#memstate) | [View](COM_Reference/Properties/View_Property.md)  
Data and Memory |  [DISP:MEASure:TYPE](GP-IB_Command_Finder/Display.md#MeasType) or execute following both commands  [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) [DISPlay:WINDow:TRACe:MEMory](GP-IB_Command_Finder/Display.md#memstate) | [View](COM_Reference/Properties/View_Property.md)  
8510 Mode | ON/OFF | None | None  
Interpolate | ON/OFF | [CALCulate:MEASure:MATH:INTerpolate[:STATe]](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:INTerpolate:STATe) | [InterpolateMemoryIsDefault](COM_Reference/Properties/InterpolateMemoryIsDefault_Property.md)  
Data -> New Trace |  |  [CALCulate:MEASure:MATH:NEW](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:NEW) [CALCulate:MEASure:MATH:LOCKed[:STATe]?](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:LOCKed:STATe) |  None None  
Analysis Tab Commands  
Softkey | Sub-item | SCPI | COM  
Conversions | Off | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Z-Reflect | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Z-Transmit | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Z-Trans-Shunt | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Y-Reflect | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Y-Transmit | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Y-Trans-Shunt | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
1 / S | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Conjugation | [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) | None  
Equation Editor... | On/Off | [CALCulate:MEASure:EQUation[:STATe]](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Equation | [CALCulate:MEASure:EQUation:TEXT](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:TEXT) | [Text](COM_Reference/Properties/Text_Property.md)  
Enable Equation | [CALCulate:MEASure:EQUation[:STATe]](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Functions | [CALCulate:EQUation:LIBRary:FUNCtions](GP-IB_Command_Finder/Calculate/Equation.md#LibraryFunctions) | [GetLibraryFunctions](COM_Reference/Methods/GetLibraryFunctions_Method.md)  
Trace Data | None | None  
Parameter | None | None  
Store Equation | None | None  
Delete Equation | None | None  
Use Short Names | None | None  
Fast Processing | [CALCulate:MEASure:EQUation:FAST](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:FAST) | [FastProcessing](COM_Reference/Properties/FastProcessing_Property.md)  
Enable Matlab | None | None  
Import... |  |   
Import Library | [CALCulate:EQUation:LIBRary:IMPort](GP-IB_Command_Finder/Calculate/Equation.md#LibraryImport) | [ImportLibrary](COM_Reference/Methods/ImportLibrary_Method.md)  
Remove Library | [CALCulate:EQUation:LIBRary:REMove](GP-IB_Command_Finder/Calculate/Equation.md#LibraryRemove) | [RemoveLibrary](COM_Reference/Methods/RemoveLibrary_Method.md)  
Python... |  |   
Python Installed | [CALCulate:EQUation:LIBRary:PYTHon[:STATe]?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryPythonState) |  None  
Python Modules | [CALCulate:EQUation:LIBRary:PYTHon:MODules?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryPythonModules) |  None  
Python Version | [CALCulate:EQUation:LIBRary:PYTHon:VERsion?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryPythonVersion) |  None  
Statistics... | On/Off | [CALCulate:MEASure:FUNCtion:STATistics[:STATe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:STATistics:STATe) | [ShowStatistics](COM_Reference/Properties/Show_Statistics_Property.md)  
Statistics - Mean, Standard Deviation, Peak to Peak | [CALCulate:MEASure:FUNCtion:TYPE](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:TYPE) | None  
User Range - Full Span, User 1 to 16 | [CALCulate:MEASure:FUNCtion:DOMain:USER[:RANGe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DOMain:USER:RANGe) | [StatisticsRange](COM_Reference/Properties/Statistics_Range_Property.md)  
Start | [CALCulate:MEASure:FUNCtion:DOMain:USER:STARt](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DOMain:USER:STARt) | [UserRangeMin](COM_Reference/Properties/User_Range_Min_Property.md)  
Stop | [CALCulate:MEASure:FUNCtion:DOMain:USER:STOP](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DOMain:USER:STOP) | [UserRangeMax](COM_Reference/Properties/User_Range_Max_Property.md)  
Show Smith Chart statistics in Ohms |  [CALCulate:MEASure:FUNCtion:STATistics:RESistance[:STATe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:STATistics:RESistance:STATe) |  None  
AM Distortion |  AM Distortion |  |   
Off |  [CALCulate:MEASure:DISTortion:MODE](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:MODE) |  None  
AM-PM |  [CALCulate:MEASure:DISTortion:MODE](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:MODE) |  None  
AM-AM |  [CALCulate:MEASure:DISTortion:MODE](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:MODE) |  None  
Y-axis = Slope Calculated Over Aperture |  [CALCulate:MEASure:DISTortion:SLOPe[:STATe]](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:SLOPe:STATe) [CALCulate:MEASure:DISTortion:SLOPe:APERture](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:SLOPe:APERture) |  None None  
X-axis = Backoff For Compression Level |  [CALCulate:MEASure:DISTortion:BACKoff[:STATe]](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:BACKoff:STATe) [CALCulate:MEASure:DISTortion:BACKoff:COMPression](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:BACKoff:COMPression) |  None None  
Trace Deviation |  Off |  [CALCulate:MEASure:COMPutation:DEViation](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:COMPutation:DEViation) |  [TraceDeviationType](COM_Reference/Properties/TraceDeviationType_Property.md)  
Linear |  [CALCulate:MEASure:COMPutation:DEViation](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:COMPutation:DEViation) |  [TraceDeviationType](COM_Reference/Properties/TraceDeviationType_Property.md)  
Parabolic |  [CALCulate:MEASure:COMPutation:DEViation](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:COMPutation:DEViation) |  [TraceDeviationType](COM_Reference/Properties/TraceDeviationType_Property.md)  
Cubic |  [CALCulate:MEASure:COMPutation:DEViation](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:COMPutation:DEViation) |  [TraceDeviationType](COM_Reference/Properties/TraceDeviationType_Property.md)  
Uncertainty Analysis... | Trace | [CALCulate:MEASure:UNCertainty:DISPlay:CFACtor](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:CFACtor) | [CoverageFactor](COM_Reference/Properties/CoverageFactor_Property.md)  
Trace Type | [CALCulate:MEASure:UNCertainty:DISPlay:TYPE](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:TYPE) | [DisplayType](COM_Reference/Properties/DisplayType_Property.md)  
Settings | [CALCulate:MEASure:UNCertainty:MODE:NOISe](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:NOISe) [CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat) [CALCulate:MEASure:UNCertainty:MODE:ETERm](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:ETERm) | [MeasurementNoiseUncertainty](COM_Reference/Properties/MeasurementNoiseUncertainty_Property.md) [CableRepeatabilityUncertainty](COM_Reference/Properties/CableRepeatabilityUncertainty_Property.md) [ErrorTermUncertainty](COM_Reference/Properties/ErrorTermUncertainty_Property.md)  
Add Trace | None | None  
Apply to all traces | None | None  
Limits... | Limit  
Limit Test  
Limit Test ON | [CALCulate:MEASure:LIMit[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Limit Line ON | [CALCulate:MEASure:LIMit:DISPlay[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:DISPlay:STATe) | [LineDisplay](COM_Reference/Properties/LineDisplay_Property.md)  
Sound ON Fail | [CALCulate:MEASure:LIMit:SOUNd[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SOUNd:STATe) | [SoundOnFail](COM_Reference/Properties/SoundOnFail_Property.md)  
Pass/Fail Position  
X Pass/Fail Position | [DISPlay:WINDow:ANNotation:LIMit:XPOSition](GP-IB_Command_Finder/Display.md#limitX) | [LimitTestXPosition](COM_Reference/Properties/LimitTestXPosition_Property.md)  
Y Pass/Fail Position | [DISPlay:WINDow:ANNotation:LIMit:YPOSition](GP-IB_Command_Finder/Display.md#limitY) | [LimitTestYPosition](COM_Reference/Properties/LimitTestYPosition_Property.md)  
Limit Table  
Show Table | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Load Table | [MMEMory:LOAD:LIMit](GP-IB_Command_Finder/Memory.md#LoadLimit) | None  
Save Table | [MMEMory:STORe:LIMit](GP-IB_Command_Finder/Memory.md#StoreLimit) | None  
Global Pass/Fail  
Global Pass/Fail ON | [DISPlay:FSIGn](GP-IB_Command_Finder/Display.md#fsign) | [DisplayGlobalPassFail](COM_Reference/Properties/DisplayGlobalPassFail_Property.md)  
Ripple  
Ripple Test  
Ripple Test ON | [CALCulate:MEASure:RLIMit:STATe](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:STATe) | None  
Ripple Line ON | [CALCulate:MEASure:RLIMit:DISPlay:LINE:STATe](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DISPlay:LINE:STATe) | None  
Sound ON Fail | [CALCulate:MEASure:LIMit:SOUNd[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SOUNd:STATe) | [SoundOnFail](COM_Reference/Properties/SoundOnFail_Property.md)  
Ripple Result  
Type - Off, Absolute or Margin | [CALCulate:MEASure:RLIMit:DISPlay:TYPE](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DISPlay:TYPE) | None  
Segment | [CALCulate:MEASure:RLIMit:DATA](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DATA) | None  
Ripple Table  
Show Table | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Load Table | [MMEMory:LOAD:RLIMit](GP-IB_Command_Finder/Memory.md#LoadRlimit) | None  
Save Table | [MMEMory:STORe:RLIMit](GP-IB_Command_Finder/Memory.md#StoreRlimit) | None  
Bandwidth  
Bandwidth Test  
Bandwidth Test ON | [CALCulate:MEASure:BLIMit:STATe](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:STATe) | None  
Bandwidth Marker ON | [CALCulate:MEASure:BLIMit:DISPlay:MARKer:STATe](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:DISPlay:MARKer:STATe) | None  
Sound ON Fail | [CALCulate:MEASure:LIMit:SOUNd[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SOUNd:STATe) | [SoundOnFail](COM_Reference/Properties/SoundOnFail_Property.md)  
N dB Points | [CALCulate:MEASure:BLIMit:BWIDth:THReshold](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:BWIDth:THReshold) | None  
Min Bandwidth | [CALCulate:MEASure:BLIMit:MINimum](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:MIN) | None  
Max Bandwidth | [CALCulate:MEASure:BLIMit:MAXimum](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:MAX) | None  
Limit Table | Off | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Limit | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Ripple | [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) | [ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Compression Analysis... (Gain Compression and Gain Compression Converters Measurement Classes only) | Compression Analysis | [CALCulate:MEASure:GCMeas:ANALysis:ENABle](GP-IB_Command_Finder/Calculate/MeasureGCMeas.md#CALCulate:MEASure:GCMeas:ANALysis:ENABle) | [AnalysisEnable](COM_Reference/Properties/AnalysisEnable_Property.md)  
Analysis Frequency | [CALCulate:MEASure:GCMeas:ANALysis:CWFRequency](GP-IB_Command_Finder/Calculate/MeasureGCMeas.md#CALCulate:MEASure:GCMeas:ANALysis:CWFRequency) | [AnalysisCWFreq](COM_Reference/Properties/AnalysisCWFreq_Property.md)  
Use Discrete Frequencies | [CALCulate:MEASure:GCMeas:ANALysis:DISCrete[:STATe]](GP-IB_Command_Finder/Calculate/MeasureGCMeas.md#CALCulate:MEASure:GCMeas:ANALysis:DISCrete:STATe) | [AnalysisIsDiscreteFreq](COM_Reference/Properties/AnalysisIsDiscreteFreq_Property.md)  
Use Measured Pin | [CALCulate:MEASure:GCMeas:ANALysis:XAXis](GP-IB_Command_Finder/Calculate/MeasureGCMeas.md#CALCulate:MEASure:GCMeas:ANALysis:XAXis) | [AnalysisXAxis](COM_Reference/Properties/AnalysisXAxis_Property.md)  
Use Source Pwr Settings | [CALCulate:MEASure:GCMeas:ANALysis:XAXis](GP-IB_Command_Finder/Calculate/MeasureGCMeas.md#CALCulate:MEASure:GCMeas:ANALysis:XAXis) | [AnalysisXAxis](COM_Reference/Properties/AnalysisXAxis_Property.md)  
Time Domain Tab Commands  
Softkey | Sub-item | SCPI | COM  
Transform | ON/OFF | [CALCulate:MEASure:TRANsform:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Start Time |  | [CALCulate:MEASure:TRANsform:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STARt) | [Start](COM_Reference/Properties/Start_Property.md)  
Stop Time |  | [CALCulate:MEASure:TRANsform:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STOP) | [Stop](COM_Reference/Properties/Stop_Property.md)  
Center Time |  | [CALCulate:MEASure:TRANsform:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:CENTer) | [Center](COM_Reference/Properties/Center_Property.md)  
Span Time |  | [CALCulate:MEASure:TRANsform:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:SPAN) | [Span](COM_Reference/Properties/Span_Property.md)  
TD Mode | Low Pass Impulse | [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Low Pass Step | [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Band Pass | [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) | [Mode](COM_Reference/Properties/Mode_Property.md)  
TD Toolbar | ON/OFF | [DISPlay:TOOLbar:TRANsform[:STATe]](GP-IB_Command_Finder/Display.md#transform) | [app.ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Time Domain Setup... | Transform  
Transform On | [CALCulate:MEASure:TRANsform:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Start | [CALCulate:MEASure:TRANsform:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STARt) | [Start](COM_Reference/Properties/Start_Property.md)  
Stop | [CALCulate:MEASure:TRANsform:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STOP) | [Stop](COM_Reference/Properties/Stop_Property.md)  
Center | [CALCulate:MEASure:TRANsform:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:CENTer) | [Center](COM_Reference/Properties/Center_Property.md)  
Span | [CALCulate:MEASure:TRANsform:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:SPAN) | [Span](COM_Reference/Properties/Span_Property.md)  
Low Pass Impulse | [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Low Pass Step | [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Band Pass | [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) | [Mode](COM_Reference/Properties/Mode_Property.md)  
Set Low Pass Frequencies | [CALCulate:MEASure:TRANsform:TIME:LPFREQuency](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:LPFREQuency) | [SetFrequencyLowPass](COM_Reference/Methods/Set_Frequency_LowPass_Method.md)  
Gating  
Gating On | [CALCulate:MEASure:FILTer[:GATE]:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Start | [CALCulate:MEASure:FILTer[:GATE]:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STARt) | [Start](COM_Reference/Properties/Start_Property.md)  
Stop | [CALCulate:MEASure:FILTer[:GATE]:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STOP) | [Stop](COM_Reference/Properties/Stop_Property.md)  
Center | [CALCulate:MEASure:FILTer[:GATE]:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:CENTer) | [Center](COM_Reference/Properties/Center_Property.md)  
Span | [CALCulate:MEASure:FILTer[:GATE]:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SPAN) | [Span](COM_Reference/Properties/Span_Property.md)  
Gate Type | [CALCulate:MEASure:FILTer[:GATE]:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:TYPE) | [Type](COM_Reference/Properties/Type_Gate_Property.md)  
Gate Shape | [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) | [Shape](COM_Reference/Properties/Shape_Property.md)  
Coupling  
Coupling On | [SENSe:COUPle:PARameter[:STATe]](GP-IB_Command_Finder/Sense/Couple.md#Trans) | [CoupleChannelParams](COM_Reference/Properties/CoupleChannelParams_Property.md)  
Transform Parameters  
Stimulus | [CALCulate:MEASure:TRANsform:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:COUPle:PARameters) | [CoupledParameters](COM_Reference/Properties/CoupledParameters_Transform_Property.md)  
State (On/Off) | [CALCulate:MEASure:TRANsform:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:COUPle:PARameters) | [CoupledParameters](COM_Reference/Properties/CoupledParameters_Transform_Property.md)  
Window | [CALCulate:MEASure:TRANsform:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:COUPle:PARameters) | [CoupledParameters](COM_Reference/Properties/CoupledParameters_Transform_Property.md)  
Mode | [CALCulate:MEASure:TRANsform:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:COUPle:PARameters) | [CoupledParameters](COM_Reference/Properties/CoupledParameters_Transform_Property.md)  
Distance Marker Unit | [CALCulate:MEASure:TRANsform:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:COUPle:PARameters) | [CoupledParameters](COM_Reference/Properties/CoupledParameters_Transform_Property.md)  
Gating Parameters  
Stimulus | [CALCulate:MEASure:FILTer[:GATE]:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:COUPle:PARameters) | [CoupledParameters (Gating)](COM_Reference/Properties/CoupledParameters_Gate_Property.md)  
State (On/Off) | [CALCulate:MEASure:FILTer[:GATE]:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:COUPle:PARameters) | [CoupledParameters (Gating)](COM_Reference/Properties/CoupledParameters_Gate_Property.md)  
Shape | [CALCulate:MEASure:FILTer[:GATE]:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:COUPle:PARameters) | [CoupledParameters (Gating)](COM_Reference/Properties/CoupledParameters_Gate_Property.md)  
Type | [CALCulate:MEASure:FILTer[:GATE]:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:COUPle:PARameters) | [CoupledParameters (Gating)](COM_Reference/Properties/CoupledParameters_Gate_Property.md)  
Marker  
Auto | [CALCulate:MEASure:TRANsform:TIME:MARKer:MODE](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:MODE) | [DistanceMarkerMode](COM_Reference/Properties/DistanceMarkerMode_Property.md)  
Reflection (divide by 2) | [CALCulate:MEASure:TRANsform:TIME:MARKer:MODE](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:MODE) | [DistanceMarkerMode](COM_Reference/Properties/DistanceMarkerMode_Property.md)  
Transmission | [CALCulate:MEASure:TRANsform:TIME:MARKer:MODE](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:MODE) | [DistanceMarkerMode](COM_Reference/Properties/DistanceMarkerMode_Property.md)  
Meters (m) | [CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT) | [DistanceMarkerUnit](COM_Reference/Properties/DistanceMarkerUnit_Property.md)  
Feet (ft) | [CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT) | [DistanceMarkerUnit](COM_Reference/Properties/DistanceMarkerUnit_Property.md)  
Inches (in) | [CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT) | [DistanceMarkerUnit](COM_Reference/Properties/DistanceMarkerUnit_Property.md)  
Velocity Factor | [SENSe:CORRection:EXTension:PORT:VELFactor](GP-IB_Command_Finder/Sense/CorrExtension.md#sysVelocity) | [VelocityFactor](COM_Reference/Properties/Velocity_Factor_Property.md)  
Advanced  
Window Type | [CALCulate:MEASure:TRANsform:TIME:WINDow[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:WINDow:TYPE) | None  
Kaiser Beta | [CALCulate:MEASure:TRANsform:TIME:KBESsel](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:KBESsel) | [KaiserBeta](COM_Reference/Properties/Kaiser_Beta_Property.md)  
Impulse Width | [CALCulate:MEASure:TRANsform:TIME:IMPulse:WIDTh](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEAsure:TRANsform:TIME:IMPulse:WIDTh) | [ImpulseWidth](COM_Reference/Properties/Impulse_Width_Property.md)  
Alignment Type | [CALCulate:MEASure:TRANsform:TIME:ALIGnment](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:ALIGnment) | [Alignment](COM_Reference/Properties/Alignment_Property.md)  
Limit Start/Stop Times to Avoid Aliasing | [CALCulate:MEASure:TRANsform:TIME:CLIP](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:CLIP) | None  
Time Gating Tab Commands  
Softkey | Sub-item | SCPI | COM  
Gating | ON/OFF | [CALCulate:MEASure:FILTer[:GATE]:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Gate Start |  | [CALCulate:MEASure:FILTer[:GATE]:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STARt) | [Start](COM_Reference/Properties/Start_Property.md)  
Gate Stop |  | [CALCulate:MEASure:FILTer[:GATE]:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STOP) | [Stop](COM_Reference/Properties/Stop_Property.md)  
Gate Center |  | [CALCulate:MEASure:FILTer[:GATE]:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:CENTer) | [Center](COM_Reference/Properties/Center_Property.md)  
Gate Span |  | [CALCulate:MEASure:FILTer[:GATE]:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SPAN) | [Span](COM_Reference/Properties/Span_Property.md)  
Gate Type | Band Pass | [C](GP-IB_Command_Finder/Calculate/Filter.md#type)[CALCulate:MEASure:FILTer[:GATE]:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:TYPE) | [Type](COM_Reference/Properties/Type_Gate_Property.md)  
Notch | [CALCulate:MEASure:FILTer[:GATE]:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:TYPE) | [Type](COM_Reference/Properties/Type_Gate_Property.md)  
Gate Shape | Maximum | [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) | [Shape](COM_Reference/Properties/Shape_Property.md)  
Wide | [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) | [Shape](COM_Reference/Properties/Shape_Property.md)  
Normal | [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) | [Shape](COM_Reference/Properties/Shape_Property.md)  
Minimum | [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) | [Shape](COM_Reference/Properties/Shape_Property.md)  
Gating Setup... | Gating  
Gating On | [CALCulate:MEASure:FILTer[:GATE]:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STATe) | [State](COM_Reference/Properties/State_Property.md)  
Start | [CALCulate:MEASure:FILTer[:GATE]:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STARt) | [Start](COM_Reference/Properties/Start_Property.md)  
Stop | [CALCulate:MEASure:FILTer[:GATE]:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STOP) | [Stop](COM_Reference/Properties/Stop_Property.md)  
Center | [CALCulate:MEASure:FILTer[:GATE]:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:CENTer) | [Center](COM_Reference/Properties/Center_Property.md)  
Span | [CALCulate:MEASure:FILTer[:GATE]:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SPAN) | [Span](COM_Reference/Properties/Span_Property.md)  
Gate Type | [CALCulate:MEASure:FILTer[:GATE]:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:TYPE) | [Type](COM_Reference/Properties/Type_Gate_Property.md)  
Gate Shape | [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) | [Shape](COM_Reference/Properties/Shape_Property.md)

