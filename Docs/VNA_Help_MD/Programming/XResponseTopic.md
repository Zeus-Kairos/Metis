[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

[Measurements](XTraceChanTopic.md#New) | [Balanced Meas](XTraceChanTopic.md#Balanced) | Auxiliary | Conversions | Format | Scale| [Elect Delay](XResponseTopic.md#Delay) | Constants | Math | Equation Editor | Statistics | AM Distortion | Trace Deviation | Uncertainty Analysis | Limits | Bandwidth Tests | Ripple Tests | Transform | Gating | Window | Coupling | Distance Markers | Avg | [IFBW](XResponseTopic.md#IF) | [Smoothing](XResponseTopic.md#Smoothing) | Group Delay | [Cal](CalTopic.md) | Marker Functions | Marker Search Functions

Show | Hide: [Status Bar](XResponseTopic.md#StatusBar) | [Toolbar](XResponseTopic.md#Toolbars) | [Tables](XResponseTopic.md#Tables) | [Marker Disp](XResponseTopic.md#MarkerDisplay)

Description |  SCPI |  COM  
---|---|---  
Speed up Measurements !  
Measurement Trace On|Off |  [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) |  [meas.View](COM_Reference/Properties/View_Property.md)  
Display Update On|Off |  [DISPlay:ENABle](GP-IB_Command_Finder/Display.md#enable) |  None  
Window Update On|Off |  [DISPlay:WINDow:ENABle](GP-IB_Command_Finder/Display.md#wenable) |  None  
Analyzer Visible On|Off |  [DISPlay:VISible](GP-IB_Command_Finder/Display.md#visible) |  [app.Visible](COM_Reference/Properties/Visible_Property.md)  
Measurement display update |  [CALCulate:PARameter:SELect<name>[,fast]](GP-IB_Command_Finder/Calculate/Parameter.md#cps) [CALCulate:PARameter:MNUMber[:SELect] <num>[,fast]](GP-IB_Command_Finder/Calculate/Parameter.md#MnumSel) |  None  
  
Auxiliary  
---  
AuxInN Source Port N |  [CALCulate:MEASure:PARameter](GP-IB_Command_Finder/Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter) |  [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
  
Conversions  
---  
Off |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Z-Reflect |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Z-Transmit |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Z-Trans-Shunt |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Y-Reflect |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Y-Transmit |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Y-Trans-Shunt |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
1 / S |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
Conjugation |  [CALCulate:MEASure:CONVersion:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:CONVersion:FUNCtion) |  None  
  
Format  
---  
Log Mag |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Lin Mag |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Phase |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Delay |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Smith |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Polar |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
SWR |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Real |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Imaginary |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Unwrapped Phase |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Positive Phase |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Inverted Smith |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
Group Delay Aperture Points |  [CALCulate:MEASure:GDELay:POINts](GP-IB_Command_Finder/Calculate/MeasureGDELay.md#CALCulate:MEASure:GDELay:POINts) |  [Points](COM_Reference/Properties/Points_Property.md)  
Group Delay Aperture Percent of Span |  [CALCulate:MEASure:GDELay:PERCent](GP-IB_Command_Finder/Calculate/MeasureGDELay.md#CALCulate:MEASure:GDELay:PERCent) |  [Percent](COM_Reference/Properties/Percent_Property.md)  
Group Delay Aperture Frequency |  [CALCulate:MEASure:GDELay:FREQuency](GP-IB_Command_Finder/Calculate/MeasureGDELay.md#CALCulate:MEASure:GDELay:FREQuency) |  [Frequency](COM_Reference/Properties/Frequency_Property.md)  
Set Preference to 2 points |  [SYSTem:PREFerences:ITEM:GDELay:TWOPoint](GP-IB_Command_Finder/System_Preferences.md#groupDelay) |  [TwoPointGroupDelayAperture](COM_Reference/Properties/TwoPointGroupDelayAperture_Property.md)  
Set or return the units for the specified data format |  [CALCulate:MEASure:FORMat:UNIT](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat:UNIT) |  [FormatUnit](COM_Reference/Properties/FormatUnit_Property.md)  
Temperature |  [CALCulate:MEASure:FORMat](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:FORMat) |  [Format](COM_Reference/Properties/Format_Property.md)  
  
Scale  
---  
AutoScale |  [DISPlay:WINDow:TRACe:Y:AUTO](GP-IB_Command_Finder/Display.md#yauto) |  [Autoscale](COM_Reference/Methods/Autoscale_Method.md)  
AutoScale All |  [DISPlay:WINDow:Y:AUTO](GP-IB_Command_Finder/Display.md#AutoscaleAll) |  [Autoscale](COM_Reference/Methods/Autoscale_Method.md)  
Per Division |  [DISPlay:WINDow:TRACe:Y:PDIVision](GP-IB_Command_Finder/Display.md#pdiv) |  [YScale](COM_Reference/Properties/YScale_Property.md)  
Reference Level |  [DISPlay:WINDow:TRACe:Y:RLEVel](GP-IB_Command_Finder/Display.md#rlev) |  [ReferenceValue](COM_Reference/Properties/Reference_Value_Property.md)  
Reference Position |  [DISPlay:WINDow:TRACe:Y:RPOSition](GP-IB_Command_Finder/Display.md#rpos) |  [ReferencePosition](COM_Reference/Properties/Reference_Position_Property.md)  
  
Scale Coupling  
---  
Set method |  [DISPlay:WINDow:TRACe:Y:COUPle:METHod](GP-IB_Command_Finder/Display.md#scaleCouplMethod) |  [ScaleCouplingMethod](COM_Reference/Properties/ScaleCouplingMethod_Property.md)  
Enable window |  [DISPlay:WINDow:TRACe:Y:COUPle](GP-IB_Command_Finder/Display.md#scaleCouplState) |  [ScaleCouplingState](COM_Reference/Properties/ScaleCouplingState_Property.md)  
  
Electrical Delay  
---  
Electrical Delay |  [CALCulate:MEASure:CORRection:EDELay:TIME](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:TIME) |  [meas.ElectricalDelay](COM_Reference/Properties/Electrical_Delay_Property.md)  
Delay in distance |  [CALCulate:MEASure:CORRection:EDELay:DISTance](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:DISTance) |  [ElecDistanceDelay](COM_Reference/Properties/ElecDistanceDelay_Property.md)  
Set units for distance |  [CALCulate:MEASure:CORRection:EDELay:UNIT](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:UNIT) |  [ElecDistanceDelayUnit](COM_Reference/Properties/ElecDistanceDelayUnit_Property.md)  
Velocity Factor |  [SENSe:CORRection:RVELocity:COAX](GP-IB_Command_Finder/Sense/Sense_Correction.md#scrc) |  [PortVelocityFactor](COM_Reference/Properties/PortVelocityFactor_Property.md)  
Media |  [CALCulate:MEASure:CORRection:EDELay:MEDium](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:MEDium) |  [PortMedium](COM_Reference/Properties/PortMedium_Property.md)  
Wavegd Cutoff |  [CALCulate:MEASure:CORRection:EDELay:WGCutoff](GP-IB_Command_Finder/Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:EDELay:WGCutoff) |  [PortWGCutoffFreq](COM_Reference/Properties/PortWGCutoffFreq_Property.md)  
  
Constants  
---  
System Z0 |  [SENSe:CORRection:IMPedance:INPut:MAGNitude](GP-IB_Command_Finder/Sense/Sense_Correction.md#imped) |  [SystemImpedanceZ0](COM_Reference/Properties/SystemImpedanceZ0_Property.md)  
Phase Offset |  [CALCulate:MEASure:OFFSet:PHASe](GP-IB_Command_Finder/Calculate/MeasureOFFSet.md#CALCulate:MEASure:OFFSet:PHASe) |  [PhaseOffset](COM_Reference/Properties/Phase_Offset_Property.md)  
Mag Offset |  [CALCulate:MEASure:OFFSet:MAGNitude](GP-IB_Command_Finder/Calculate/MeasureOFFSet.md#CALCulate:MEASure:OFFSet:MAGNitude) |  [MagnitudeOffset](COM_Reference/Properties/MagnitudeOffset_Property.md)  
Mag Slope |  [CALCulate:MEASure:OFFSet:MAGNitude:SOPe](GP-IB_Command_Finder/Calculate/MeasureOFFSet.md#CALCulate:MEASure:OFFSet:MAGNitude:SLOPe) |  [MagnitudeSlopeOffset](COM_Reference/Properties/MagnitudeSlopeOffset_Property.md)  
  
Math  
---  
Data Trace ON|OFF |  [DISPlay:WINDow:TRACe[:STATe]](GP-IB_Command_Finder/Display.md#tstat) |  [meas.View](COM_Reference/Properties/View_Property.md)  
Memory Trace ON|OFF |  [DISPlay:WINDow:TRACe:MEMory](GP-IB_Command_Finder/Display.md#memstate) |  [meas.View](COM_Reference/Properties/View_Property.md)  
Data =>Memory |  [CALCulate:MEASure:MATH:MEMorize](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:MEMorize) |  [meas.DataToMemory](COM_Reference/Methods/DataToMemory_Method.md)  
Memory data interpolation ON|OFF |  [CALCulate:MEASure:MATH:INTerpolate[:STATe]](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:INTerpolate:STATe) |  [InterpolateMemoryIsDefault](COM_Reference/Properties/InterpolateMemoryIsDefault_Property.md)  
Data Math (Add|Sub|Mult|Div) |  [CALCulate:MEASure:MATH:FUNCtion](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:MATH:FUNCtion) |  [TraceMath](COM_Reference/Properties/Trace_Math_Property.md)  
  
Equation Editor  
---  
Delay data processing to end of sweep |  [CALCulate:MEASure:EQUation:FAST](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:FAST) |  [FastProcessing](COM_Reference/Properties/FastProcessing_Property.md)  
Turn ON / OFF equation |  [CALCulate:MEASure:EQUation[:STATe]](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:STATe) |  [State](COM_Reference/Properties/State_Property.md)  
Set equation |  [CALCulate:MEASure:EQUation:TEXT](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:TEXT) |  [Text](COM_Reference/Properties/Text_Property.md)  
Return validity of equation |  [CALCulate:MEASure:EQUation:VALid?](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:EQUation:VALid) |  [Valid](COM_Reference/Properties/Valid_Property.md)  
Returns the functions in DLL |  [CALCulate:EQUation:LIBRary:FUNCtions](GP-IB_Command_Finder/Calculate/Equation.md#LibraryFunctions) |  [GetLibraryFunctions](COM_Reference/Methods/GetLibraryFunctions_Method.md)  
Imports the functions in DLL |  [CALCulate:EQUation:LIBRary:IMPort](GP-IB_Command_Finder/Calculate/Equation.md#LibraryImport) |  [ImportLibrary](COM_Reference/Methods/ImportLibrary_Method.md)  
Is DLL Imported? |  [CALCulate:EQUation:LIBRary:IMPort?](GP-IB_Command_Finder/Calculate/Equation.md#LibraryImport) |  [IsLibraryImported](COM_Reference/Methods/IsLibraryImported_Method.md)  
Remove a DLL |  [CALCulate:EQUation:LIBRary:REMove](GP-IB_Command_Finder/Calculate/Equation.md#LibraryRemove) |  [RemoveLibrary](COM_Reference/Methods/RemoveLibrary_Method.md)  
  
Statistics  
---  
Show Smith Chart statistics in Ohms |  [CALCulate:MEASure:FUNCtion:STATistics:RESistance[:STATe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:STATistics:RESistance:STATe) |  None  
Statistics ON|OFF |  [CALCulate:MEASure:FUNCtion:STATistics[:STATe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:STATistics:STATe) |  [meas.ShowStatistics](COM_Reference/Properties/Show_Statistics_Property.md)  
Statistics Range |  [CALCulate:MEASure:FUNCtion:DOMain:USER[:RANGe]](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DOMain:USER:RANGe) |  [meas.StatisticsRange](COM_Reference/Properties/Statistics_Range_Property.md)  
Domain Range Start |  [CALCulate:MEASure:FUNCtion:DOMain:USER:STARt](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DOMain:USER:STARt) |  [UserRangeMin](COM_Reference/Properties/User_Range_Min_Property.md)  
Domain Range Stop |  [CALCulate:MEASure:FUNCtion:DOMain:USER:STOP](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DOMain:USER:STOP) |  [UserRangeMax](COM_Reference/Properties/User_Range_Max_Property.md)  
Set Type (Pk-Pk|StdDev|Mean) |  [CALCulate:MEASure:FUNCtion:TYPE](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:TYPE) |  Set individually  
Get All Statistics Data |  [CALCulate:MEASure:FUNCtion:DATA?](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DATA) |  [meas.GetFilterStatistics](COM_Reference/Methods/Get_Filter_Statistics_Method.md)  
Get Standard Deviation |  [CALCulate:MEASure:FUNCtion:DATA?](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DATA) |  [meas.StandardDeviation](COM_Reference/Properties/Standard_Deviation_Property.md)  
Get Mean |  [CALCulate:MEASure:FUNCtion:DATA?](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DATA) |  [meas.Mean](COM_Reference/Properties/Mean_Property.md)  
Get Peak to Peak |  [CALCulate:MEASure:FUNCtion:DATA?](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:DATA) |  [meas.PeakToPeak](COM_Reference/Properties/PeakToPeak_Property.md)  
Get formatted data array of multiple traces |  [CALCulate:DATA:MFData](GP-IB_Command_Finder/Calculate/Data.md#DataMfdata) |  None  
Get corrected data array of multiple traces |  [CALCulate:DATA:MSData](GP-IB_Command_Finder/Calculate/Data.md#DataMsdata) |  None  
Executes the statistical analysis |  [CALCulate:MEASure:FUNCtion:EXECute](GP-IB_Command_Finder/Calculate/MeasureFUNCtion.md#CALCulate:MEASure:FUNCtion:EXECute) |  None  
  
AM Distortion Commands |  |   
---|---|---  
Sets and returns the compression level. |  [CALCulate:MEASure:DISTortion:BACKoff:COMPression](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:BACKoff:COMPression) |  None  
Enable/disable compression calculation. |  [CALCulate:MEASure:DISTortion:BACKoff[:STATe]](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:BACKoff:STATe) |  None  
Displays phase or amplitude distortion. |  [CALCulate:MEASure:DISTortion:MODE](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:MODE) |  None  
Sets the aperture value over which the phase or gain slope will be calculated. |  [CALCulate:MEASure:DISTortion:SLOPe:APERture](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:SLOPe:APERture) |  None  
Enables/disables phase slope (AMPM) or gain slope (AMAM) over the slope aperture to be displayed. |  [CALCulate:MEASure:DISTortion:SLOPe[:STATe]](GP-IB_Command_Finder/Calculate/MeasureAMDistortion.md#CALCulate:MEASure:DISTortion:SLOPe:STATe) |  None  
  
Trace Deviation  
---  
Calculates the deviation from a least-squares best fit line |  [CALCulate:MEASure:COMPutation:DEViation](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:COMPutation:DEViation) |  [TraceDeviationType](COM_Reference/Properties/TraceDeviationType_Property.md)  
|  |   
  
Uncertainty Analysis  
---  
Trace |  [CALCulate:MEASure:UNCertainty:DISPlay:CFACtor](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:CFACtor) |  [CoverageFactor](COM_Reference/Properties/CoverageFactor_Property.md)  
Trace Type |  [CALCulate:MEASure:UNCertainty:DISPlay:TYPE](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:TYPE) |  [DisplayType](COM_Reference/Properties/DisplayType_Property.md)  
Noise |  [CALCulate:MEASure:UNCertainty:MODE:NOISe](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:NOISe) |  [MeasurementNoiseUncertainty](COM_Reference/Properties/MeasurementNoiseUncertainty_Property.md)  
Repeatability |  [CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat) |  [CableRepeatabilityUncertainty](COM_Reference/Properties/CableRepeatabilityUncertainty_Property.md)  
Calibration |  [CALCulate:MEASure:UNCertainty:MODE:ETERm](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:ETERm) |  [ErrorTermUncertainty](COM_Reference/Properties/ErrorTermUncertainty_Property.md)  
Save uncertainty data |  [CALCulate:MEASure:UNCertainty:SAVE](GP-IB_Command_Finder/Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:SAVE) |  [WriteUncertaintyFile](COM_Reference/Methods/WriteUncertaintyFile_Method.md)  
  
Limits  
---  
Display Lines ON|OFF |  [CALCulate:MEASure:LIMit:DISPlay[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:DISPlay:STATe) |  [LineDisplay](COM_Reference/Properties/LineDisplay_Property.md)  
Fail Sound ON|OFF |  [CALCulate:MEASure:LIMit:SOUNd[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SOUNd:STATe) |  [SoundOnFail](COM_Reference/Properties/SoundOnFail_Property.md)  
Testing ON|OFF |  [CALCulate:MEASure:LIMit[:STATe]](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:STATe) |  [Trans.State](COM_Reference/Properties/State_Property.md)  
Limit Test Failed |  [CALCulate:MEASure:LIMit:FAIL?](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:FAIL) |  [meas.LimitTestFailed](COM_Reference/Properties/LimitTestFailed_Property.md)  
Count Limit Lines |  None |  [chans.Count](COM_Reference/Properties/Count_Property.md)  
Read Test Results |  [GP-IB_Command_Finder/Status](GP-IB_Command_Finder/Status.md) |  [limts.GetTestResult](COM_Reference/Methods/Get_Test_Result_Method.md)  
Set / Read entire Limit Line |  [CALCulate:MEASure:LIMit:DATA](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:DATA) |  None  
Limit Line Type (Max|Min) |  [CALCulate:MEASure:LIMit:SEGMent:TYPE](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SEGMent:TYPE) |  [limts.Type](COM_Reference/Properties/Type_limit_Property.md)  
Begin Stimulus |  [CALCulate:MEASure:LIMit:SEGMent:STIMulus:STARt](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SEGMent:STIMulus:STARt) |  [limtseg.BeginStimulus](COM_Reference/Properties/Begin_Stimulus_Property.md)  
End Stimulus |  [CALCulate:MEASure:LIMit:SEGMent:STIMulus:STOP](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SEGMent:STIMulus:STOP) |  [limtseg.EndStimulus](COM_Reference/Properties/End_Stimulus_Value.md)  
Begin Response |  [CALCulate:MEASure:LIMit:SEGMent1:AMPLitude:STARt](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SEGMent:AMPLitude:STARt) |  [limtseg.BeginResponse](COM_Reference/Properties/Begin_Response_Property.md)  
End Response |  [CALCulate:MEASure:LIMit:SEGMent1:AMPLitude:STOP](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:SEGMent:AMPLitude:STOP) |  [limtseg.EndResponse](COM_Reference/Properties/End_Response_Property.md)  
Read the bandwidth test results for the active trace of selected channel. |  [CALCulate:MEASure:LIMit:REPort:ALL](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:REPort:ALL) [CALCulate:LIMit:REPort:ALL](GP-IB_Command_Finder/Calculate/Limit.md#CALCulate:LIMit:REPort:ALL) |  None  
Read the stimulus values at all the measurement points that failed the limit test for the active trace of selected channel. |  [CALCulate:MEASure:LIMit:REPort:DATA](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:REPort:DATA) [CALCulate:LIMit:REPort:DATA](GP-IB_Command_Finder/Calculate/Limit.md#CALCulate:LIMit:REPort:DATA) |  None  
Reads the number of the measurement points that failed the limit test, for the active trace of selected channel. |  [CALCulate:MEASure:LIMit:REPort:POINts](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:REPort:POINts) [CALCulate:LIMit:REPort:POINts](GP-IB_Command_Finder/Calculate/Limit.md#CALCulate:LIMit:REPort:POINts) |  None  
Delete all limit line data |  [CALCulate:MEASure:LIMit:DATA:DELete](GP-IB_Command_Finder/Calculate/MeasureLIMit.md#CALCulate:MEASure:LIMit:DATA:DELete) |  None  
Show Limit table |  [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) |  [win.ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Global Pass/Fail  
Show / hide the pass/fail dialog. |  [DISPlay:FSIGn](GP-IB_Command_Finder/Display.md#fsign) |  [app.DisplayGlobalPassFail](COM_Reference/Properties/DisplayGlobalPassFail_Property.md)  
Sets the policy used to compute the global pass/fail value. |  [CONTrol:HANDler:PASSfail:POLicy](GP-IB_Command_Finder/ControlHandler.md#policy) [CONTrol:AUXiliary:PASSfail:POLicy](GP-IB_Command_Finder/ControlAux.md#policy) |  [obj.PassFailPolicy](COM_Reference/Properties/PassFailPolicy_Property.md)  
Reads the most recent pass/fail status value. |  [CONTrol:HANDler:PASSfail:STATus?](GP-IB_Command_Finder/ControlHandler.md#status) [CONTrol:AUXiliary:PASSfail:STATus?](GP-IB_Command_Finder/ControlAux.md#status) |  [obj.PassFailStatus](COM_Reference/Properties/PassFailStatus_Property.md)  
Sets the logic of the AuxIO PassFail line. |  [CONTrol:HANDler:PASSfail:LOGic](GP-IB_Command_Finder/ControlHandler.md#HandPassFailLogic) [CONTrol:AUXiliary:PASSfail:LOGic](GP-IB_Command_Finder/ControlAux.md#logic) |  [obj.PassFailLogic](COM_Reference/Properties/PassFailLogic_Property.md)  
Sets the default logical pass/fail state. |  [CONTrol:HANDler:PASSfail:MODE](GP-IB_Command_Finder/ControlHandler.md#HandPassFailMode) [CONTrol:AUXiliary:PASSfail:MODE](GP-IB_Command_Finder/ControlAux.md#mode) |  [obj.PassFailMode](COM_Reference/Properties/PassFailMode_Property.md)  
Sets the scope (Global or channel) of AuxIO pass/fail testing. |  [CONTrol:HANDler:PASSfail:SCOPe](GP-IB_Command_Finder/ControlHandler.md#HandPassFailScope) [CONTrol:AUXiliary:PASSfail:SCOPe](GP-IB_Command_Finder/ControlAux.md#scope) |  [obj.PassFailScope](COM_Reference/Properties/PassFailScope_Property.md)  
  
Bandwidth Tests  
---  
Set bandwidth threshold value of bandwidth test. |  [CALCulate:MEASure:BLIMit:BWIDth:THReshold](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:BWIDth:THReshold) |  None  
Turn ON/OFF the bandwidth value display of the bandwidth test. |  [CALCulate:MEASure:BLIMit:BWIDth:DISPlay:MARker:STATe](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:DISPlay:MARKer:STATe) |  None  
Get the bandwidth limit test results. |  [CALCulate:MEASure:BLIMit:FAIL](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:FAIL) |  None  
Set/get the upper limit value of the bandwidth test. |  [CALCulate:MEASure:BLIMit:MAXimum](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:MAX) |  None  
Set/get the lower limit value of the bandwidth test. |  [CALCulate:MEASure:BLIMit:MINimum](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:MIN) |  None  
Get the bandwidth value of the bandwidth test. |  [CALCulate:MEASure:BLIMit:REPort:DATA](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:REPort:DATA) |  None  
Turn ON/OFF the bandwidth test function. |  [CALCulate:MEASure:BLIMit:STATe](GP-IB_Command_Finder/Calculate/MeasureBLIMit.md#CALCulate:MEASure:BLIMit:STATe) |  None  
  
Ripple Tests  
---  
Set or return the ripple limit table |  [CALCulate:MEASure:RLIMit:DATA](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DATA) |  None  
Turn ON/OFF the ripple limit line display |  [CALCulate:MEASure:RLIMit:DISPlay::LINE:STATe](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DISPlay:LINE:STATe) |  None  
Set/get the ripple limit band |  [CALCulate:MEASure:RLIMit:DISPlay:SELect](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DISPlay:SELect) |  None  
Set/get the display type of ripple value |  [CALCulate:MEASure:RLIMit:DISPlay:TYPE](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:DISPlay:SELect) |  None  
Read the ripple test result |  [CALCulate:MEASure:RLIMit:FAIL](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:FAIL) |  None  
Read the ripple value |  [CALCulate:MEASure:RLIMit:REPort:DATA](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:REPort:DATA) |  None  
Turn ON/OFF the ripple test function |  [CALCulate:MEASure:RLIMit:STATe](GP-IB_Command_Finder/Calculate/MeasureRLIMit.md#CALCulate:MEASure:RLIMit:STATe) |  None  
  
Transform  
---  
Sets the alignment of the time domain measurement. |  [CALCulate:MEASure:TRANsform:TIME:ALIGnment](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:ALIGnment) |  [Alignment](COM_Reference/Properties/Alignment_Property.md)  
Transform ON|OFF |  [CALCulate:MEASure:TRANsform:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STATe) |  [trans.State](COM_Reference/Properties/State_Property.md)  
Mode (LowPass, BandPass) |  [CALCulate:MEASure:TRANsform:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:TYPE) |  [trans.Mode](COM_Reference/Properties/Mode_Property.md)  
Start Time |  [CALCulate:MEASure:TRANsform:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STARt) |  [trans.Start](COM_Reference/Properties/Start_Property.md)  
Stop Time |  [CALCulate:MEASure:TRANsform:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STOP) |  [trans.Stop](COM_Reference/Properties/Stop_Property.md)  
Center |  [CALCulate:MEASure:TRANsform:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:CENTer) |  [trans.Center](COM_Reference/Properties/Center_Property.md)  
Span |  [CALCulate:MEASure:TRANsform:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:SPAN) |  [trans.Span](COM_Reference/Properties/Span_Property.md)  
Step Rise Time |  [CALCulate:MEASure:TRANsform:TIME:STEP:RTIMe](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:STEP:RTIMe) |  [trans.StepRiseTime](COM_Reference/Properties/Step_Rise_Time_Property.md)  
Set Low Pass Frequency |  [CALCulate:MEASure:TRANsform:TIME:LPFREQuency](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:LPFREQuency) |  [trans.SetFrequencyLowPass](COM_Reference/Methods/Set_Frequency_LowPass_Method.md)  
Set/get the impulse width |  [CALCulate:MEASure:TRANsform:TIME:IMPulse:WIDTh](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEAsure:TRANsform:TIME:IMPulse:WIDTh) |  [trans.ImpulseWidth](COM_Reference/Properties/Impulse_Width_Property.md)  
TD Toolbar |  [DISPlay:TOOLbar:TRANsform[:STATe]](GP-IB_Command_Finder/Display.md#transform) |  [app.ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Sets the window type for time domain transform. |  [CALCulate:MEASure:TRANsform:TIME:WINDow[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:WINDow:TYPE) |  None  
  
Gating  
---  
ON|OFF |  [CALCulate:MEASure:FILTer[:GATE]:TIME:STATe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STATe) |  [gate.State](COM_Reference/Properties/State_Property.md)  
Type (BandPass, Notch) |  [CALCulate:MEASure:FILTer[:GATE]:TIME[:TYPE]](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:TYPE) |  [gate.Type](COM_Reference/Properties/Type_Gate_Property.md)  
Shape |  [CALCulate:MEASure:FILTer[:GATE]:TIME:SHAPe](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SHAPe) |  [gat.Shape](COM_Reference/Properties/Shape_Property.md)  
Start |  [CALCulate:MEASure:FILTer[:GATE]:TIME:STARt](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STARt) |  [gate.Start](COM_Reference/Properties/Start_Property.md)  
Stop |  [CALCulate:MEASure:FILTer[:GATE]:TIME:STOP](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:STOP) |  [gate.Stop](COM_Reference/Properties/Stop_Property.md)  
Center |  [CALCulate:MEASure:FILTer[:GATE]:TIME:CENTer](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:CENTer) |  [gate.Center](COM_Reference/Properties/Center_Property.md)  
Span |  [CALCulate:MEASure:FILTer[:GATE]:TIME:SPAN](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:TIME:SPAN) |  [gate.Span](COM_Reference/Properties/Span_Property.md)  
Set gate coupling parameters |  [CALCulate:MEASure:FILTer[:GATE]:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:COUPle:PARameters) |  [gate.CoupledParameters](COM_Reference/Properties/CoupledParameters_Gate_Property.md)  
  
Window  
---  
Kaiser Beta |  [CALCulate:MEASure:TRANsform:TIME:KBESsel](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:KBESsel) |  [trans.KaiserBeta](COM_Reference/Properties/Kaiser_Beta_Property.md)  
Impulse Width |  [CALCulate:MEASure:TRANsform:TIME:IMPulse:WIDTh](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEAsure:TRANsform:TIME:IMPulse:WIDTh) |  [trans.ImpulseWidth](COM_Reference/Properties/Impulse_Width_Property.md)  
  
Coupling  
---  
Enable trace coupling |  [SENSe:COUPle:PARameter[:STATe]](GP-IB_Command_Finder/Sense/Couple.md#Trans) |  [CoupleChannelParams](COM_Reference/Properties/CoupleChannelParams_Property.md)  
Set transform coupling parameters |  [CALCulate:MEASure:TRANsform:COUPle:PARameters](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:COUPle:PARameters) |  [trans.CoupledParameters](COM_Reference/Properties/CoupledParameters_Transform_Property.md)  
  
Distance Markers  
---  
Specify measurement type for distance markers |  [CALCulate:MEASure:TRANsform:TIME:MARKer:MODE](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:MODE) |  [trans.DistanceMarkerMode](COM_Reference/Properties/DistanceMarkerMode_Property.md)  
Specify units for distance markers |  [CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT](GP-IB_Command_Finder/Calculate/MeasureTRANsform.md#CALCulate:MEASure:TRANsform:TIME:MARKer:UNIT) |  [trans.DistanceMarkerUnit](COM_Reference/Properties/DistanceMarkerUnit_Property.md)  
Set and return marker distance value |  [CALCulate:MEASure:MARKer:DISTance](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:DISTance) |  [mark.Distance](COM_Reference/Properties/Distance_Property.md)  
  
Averaging  
---  
Average ON|OFF |  [SENSe:AVERage[:STATe]](GP-IB_Command_Finder/Sense/Average_SCPI.md#cas) |  [chan.Averaging](COM_Reference/Properties/Averaging_Property.md)  
Average Factor |  [SENSe:AVERage:COUNt](GP-IB_Command_Finder/Sense/Average_SCPI.md#cac) |  [chan.AveragingFactor](COM_Reference/Properties/Averaging_Factor_Property.md)  
Return the Average Count |  None ([STATus:OPERation:AVERaging](GP-IB_Command_Finder/Status.md#avg11)) |  [chan.AveragingCount](COM_Reference/Properties/AveragingCount_Property.md)  
Average Type |  [SENSe:AVERage:MODE](GP-IB_Command_Finder/Sense/Average_SCPI.md#cac) |  [AverageMode](COM_Reference/Properties/AverageMode_Property.md)  
Average Restart |  [SENSe:AVERage:CLEar](GP-IB_Command_Finder/Sense/Average_SCPI.md#cacl) |  [chan.AveragingRestart](COM_Reference/Methods/Averaging_Restart_Method.md)  
  
IF Bandwidth  
---  
IF Bandwidth |  [SENSe:BANDwidth | BWIDth[:RESolution]](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#res) |  [chan.IFBandwidth](COM_Reference/Properties/IF_Bandwidth_Property.md)  
Previous IF Bandwidth |  None |  [chan.Previous_IFBandwidth](COM_Reference/Methods/Previous_IF_Bandwidth_Method.md)  
Next IFBandwidth |  None |  [chan.Next_IFBandwidth](COM_Reference/Methods/Next_IF_Bandwidth_Method.md)  
Reduce IF BW |  [SENSe:BANDwidth | BWIDth:TRACk](GP-IB_Command_Finder/Sense/Sense_Bandwidth.md#track) |  [chan.ReduceIFBandwidth](COM_Reference/Properties/ReduceIFBW_Property.md)  
  
Smoothing  
---  
Smoothing ON|OFF |  [CALCulate:MEASure:SMOothing[:STATe]](GP-IB_Command_Finder/Calculate/MeasureSMOothing.md#CALCulate:MEASure:SMOothing:STATe) |  [meas.Smoothing](COM_Reference/Properties/Smoothing_Property.md)  
Smoothing Percent |  [CALCulate:MEASure:SMOothing:APERture](GP-IB_Command_Finder/Calculate/MeasureSMOothing.md#CALCulate:MEASure:SMOothing:APERture) |  [meas.SmoothingAperture](COM_Reference/Properties/Smoothing_Aperture_Property.md)  
Smoothing Points |  [CALCulate:MEASure:SMOothing:POINts](GP-IB_Command_Finder/Calculate/MeasureSMOothing.md#CALCulate:MEASure:SMOothing:POINts) |  None  
  
Marker Functions  
---  
ON|OFF |  [CALCulate:MEASure:MARKer[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:STATe) |  [meas.MarkerState](COM_Reference/Properties/MarkerState_Property.md)  
Delete All Markers |  [CALCulate:MEASure:MARKer:AOFF](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:AOFF) |  [meas.DeleteAllMarkers](COM_Reference/Methods/DeleteAllMarkers_Method.md)  
Delete Marker |  [CALCulate:MEASure:MARKer[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:STATe) |  [meas.DeleteMarker](COM_Reference/Methods/Delete_Marker_Method.md)  
Delta Marker |  [CALCulate:MEASure:MARKer:DELTa](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:DELTa) |  [mark.DeltaMarker](COM_Reference/Properties/DeltaMarker_Property.md)  
Viewing Marker readouts |  [Display](XResponseTopic.md#MarkerDisplay) |  [Display](XResponseTopic.md#MarkerDisplay)  
Get a handle to Ref marker |  None |  [meas.GetReferenceMarker](COM_Reference/Methods/Get_Reference_Marker_Method.md)  
Reference Marker  
Reference Marker On | Off |  [CALCulate:MEASure:MARKer:REFerence[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:REFerence:STATe) |  [meas.ReferenceMarkerState](COM_Reference/Properties/ReferenceMarkerState_Property.md)  
Set and read X-axis location |  [CALCulate:MEASure:MARKer:REFerence:X](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:REFerence:X) |  [GetReferenceMarker.Stimulus](COM_Reference/Properties/Stimulus_Property.md)  
Set and read Y-axis location |  [CALCulate:MEASure:MARKer:REFerence:Y](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:REFerence:Y) |  [GetReferenceMarker.Value](COM_Reference/Properties/Value_Property.md)  
Advanced Settings  
Interpolate All Markers (Discrete) |  None |  [meas.Interpolate](COM_Reference/Methods/Interpolate_Markers_Method.md)  
Interpolate Individ. Marker (Discrete) |  [CALCulate:MEASure:MARKer:DISCrete](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:DISCrete) |  [mark.Interpolated](COM_Reference/Properties/Interpolated_Property.md)  
Type (Normal | Fixed) |  [CALCulate:MEASure:MARKer:TYPE](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:TYPE) |  [mark.Type](COM_Reference/Properties/Type_Marker_Property.md)  
Format Individ. Marker |  [CALCulate:MEASure:MARKer:FORMat](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FORMat) |  [mark.Format](COM_Reference/Properties/Format_Marker_Property.md)  
Coupled Markers |  [CALCulate:MEASure:MARKer:COUPling[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:COUPling:STATe) |  [app.CoupledMarkers](COM_Reference/Properties/CoupledMarkers_Property.md)  
Coupled Markers Method |  [CALCulate:MEASure:MARKer:COUPling:METHod](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:COUPling:METHod) |  [CoupledMarkersMethod](COM_Reference/Properties/CoupledMarkersMethod_Property.md)  
Read/Set Data Point number |  [CALCulate:MEASure:MARKer:BUCKet](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BUCKet) |  [mark.BucketNumber](COM_Reference/Properties/Bucket_Number_Property.md)  
Read/Set X-axis value |  [CALCulate:MEASure:MARKer:X](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:X) |  [mark.Stimulus](COM_Reference/Properties/Stimulus_Property.md)  
Read/Set Y-axis value |  [CALCulate:MEASure:MARKer:Y](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:Y) |  [mark.Value](COM_Reference/Properties/Value_Property.md)  
Function  
Marker=> SA |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [toSA](COM_Reference/Methods/toSA_Method.md)  
Marker=> Span |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  None  
Marker=> Center (Freq) |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [mark.SetCenter](COM_Reference/Methods/Set_Center_Method.md)  
Marker=> CW Freq and change sweep type |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [mark.SetCW](COM_Reference/Methods/Set_CW_Method.md)  
Marker=> Start (Freq) |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [mark.SetStart](COM_Reference/Methods/Set_Start_Method.md)  
Marker=> Stop (Freq) |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [mark.SetStop](COM_Reference/Methods/Set_Stop_Method.md)  
Marker=> Elect. Delay |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [mark.SetElectricalDelay](COM_Reference/Methods/SetElectricalDelay_Method.md)  
Marker=> Ref. Level |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [mark.SetReferenceLevel](COM_Reference/Methods/SetReferenceLevel_Method.md)  
Marker=> CW Freq - No sweep type change |  [CALCulate:MEASure:MARKer:SET](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:SET) |  [SetCWFreq](COM_Reference/Methods/SetCWFreq_Method.md)  
  
SA Band Marker Settings  
---  
Read Band Power |  [CALCulate:MEASure:SA:MARKer:BPOWer:DATA?](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BPOWer:DATA) |  [BandpowerData](COM_Reference/Methods/BandpowerData_Method.md)  
Read Band Power Span |  [CALCulate:MEASure:SA:MARKer:BPOWer:SPAN](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BNOise:SPAN) |  [BandpowerSpan](COM_Reference/Properties/BandpowerSpan_Property.md)  
Set Band Power State |  [CALCulate:MEASure:SA:MARKer:BPOWer[:STATe]](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BPOWer:STATe) |  [BandpowerState](COM_Reference/Properties/BandpowerState_Property.md)  
Read Band Noise |  [CALCulate:MEASure:SA:MARKer:BNOise:DATA?](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BNOise:DATA) |  [BandnoiseData](COM_Reference/Methods/BandnoiseData_Method.md)  
Read Band Noise Span |  [CALCulate:MEASure:SA:MARKer:BNOise:SPAN](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BNOise:SPAN) |  [BandnoiseSpan](COM_Reference/Properties/BandnoiseSpan_Property.md)  
Set Band Noise State |  [CALCulate:MEASure:SA:MARKer:BNOise[:STATe]](GP-IB_Command_Finder/Calculate/MeasureSA.md#CALCulate:MEASure:SA:MARKer:BNOise:STATe) |  [BandnoiseState](COM_Reference/Properties/BandnoiseState_Property.md)  
  
Compression Marker Search  
---  
Compression Marker level found. |  [CALCulate:MEASure:MARKer:FUNCtion:COMPression:LEVel](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:COMPression:LEVel) |  [CompressionLevel](COM_Reference/Properties/CompressionLevel_mkr_Property.md)  
Read Compression Marker Input power |  [CALCulate:MEASure:MARKer:FUNCtion:COMPression:PIN](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:COMPression:PIN) |  [CompressionPin](COM_Reference/Properties/CompressionPin_Property.md)  
Read Compression Marker Output power |  [CALCulate:MEASure:MARKer:FUNCtion:COMPression:POUT](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:COMPression:POUT) |  [CompressionPout](COM_Reference/Properties/CompressionPout_Property.md)  
Search function |  [CALCulate:MEASure:MARKer:FUNCtion[:SELect]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:SELect) |  [SearchCompressionPoint](COM_Reference/Methods/SearchCompressionPoint_Method.md)  
Turn ON|OFF the compression state |  [CALCulate:MEASure:MARKer:FUNCtion:COMPression[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:COMPression:STATe) |  None  
Execute function |  [CALCulate:MEASure:MARKer:FUNCtion:EXECute](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:EXECute) |  [SearchCompressionPoint](COM_Reference/Methods/SearchCompressionPoint_Method.md)  
  
PSAT Marker Search  
---  
Initiate a PSAT search |  [CALCulate:MEASure:MARKer:PSATuration:BACKoff](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:BACKoff) |  [SearchPowerSaturation](COM_Reference/Methods/SearchPowerSaturation_Method.md)  
Set and read PSAT backoff |  [CALCulate:MEASure:MARKer:PSATuration:BACKoff](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:BACKoff) |  [PMaxBackOff](COM_Reference/Properties/PMaxBackOff_Property.md)  
Read PSat Out |  [CALCulate:MEASure:MARKer:PSATuration:POUT?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:POUT) |  [POut](COM_Reference/Properties/POut_Property.md)  
Read PSat In |  [CALCulate:MEASure:MARKer:PSATuration:PIN?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:PIN) |  [Pin](COM_Reference/Properties/Pin_Property.md)  
Read PMax Out |  [CALCulate:MEASure:MARKer:PSATuration:POUT:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:POUT:MAXimum) |  [PMaxOut](COM_Reference/Properties/PMaxOut_Property.md)  
Read PMax In |  [CALCulate:MEASure:MARKer:PSATuration:PIN:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:PIN:MAXimum) |  [PMaxIn](COM_Reference/Properties/PMaxIn_Property.md)  
Read Gain Sat |  [CALCulate:MEASure:MARKer:PSATuration:GAIN?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:GAIN) |  [GainSaturation](COM_Reference/Properties/GainSaturation_Property.md)  
Read Gain Max |  [CALCulate:MEASure:MARKer:PSATuration:GAIN:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:GAIN:MAXimum) |  [GainMax](COM_Reference/Properties/GainMax_Property.md)  
Read Gain Linear |  [CALCulate:MEASure:MARKer:PSATuration:GAIN:LINear?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:GAIN:LINear) |  [GainLinear](COM_Reference/Properties/GainLinear_Property.md)  
Read Comp Sat |  [CALCulate:MEASure:MARKer:PSATuration:COMPression:SATuration?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:COMPression:SATuration) |  [CompressionSaturation](COM_Reference/Properties/CompressionSaturation_Property.md)  
Read Comp Max |  [CALCulate:MEASure:MARKer:PSATuration:COMPression:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:COMPression:SATuration) |  [CompressionMax](COM_Reference/Properties/CompressionMax_Property.md)  
Turn ON|OFF PSAT marker search |  [CALCulate:MEASure:MARKer:PSATuration[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PSATuration:STATe) |  None  
  
PNOP Marker Search  
---  
Initiate a PNOP search |  [CALCulate:MEASure:MARKer:PNOP:BACKoff](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:BACKoff) |  [SearchPowerNormalOperatingPoint](COM_Reference/Methods/SearchPowerNormalOperatingPoint_Method.md)  
PNOP backoff |  [CALCulate:MEASure:MARKer:PNOP:BACKoff](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:BACKoff) |  [BackOff](COM_Reference/Properties/BackOff_Property.md)  
PNOP Power Offset |  [CALCulate:MEASure:MARKer:PNOP:POFFset](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:POFFset) |  [PinOffset](COM_Reference/Properties/PinOffset_Property.md)  
Read Pnop Out |  [CALCulate:MEASure:MARKer:PNOP:POUT?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:POUT) |  [POut](COM_Reference/Properties/POut_Property.md)  
Read Pnop in |  [CALCulate:MEASure:MARKer:PNOP:PIN?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:PIN) |  [Pin](COM_Reference/Properties/Pin_Property.md)  
Read Pnop Gain |  [CALCulate:MEASure:MARKer:PNOP:GAIN?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:GAIN) |  [Gain](COM_Reference/Properties/Gain_Property.md)  
Read Pnop Comp |  [CALCulate:MEASure:MARKer:PNOP:COMPression?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:COMPression) |  [Compression](COM_Reference/Properties/Compression_Property.md)  
Read PMax Out |  [CALCulate:MEASure:MARKer:PNOP:POUT:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:POUT:MAXimum) |  [PMaxOut](COM_Reference/Properties/PMaxOut_Property.md)  
Read PMax In |  [CALCulate:MEASure:MARKer:PNOP:PIN:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:PIN:MAXimum) |  [PMaxIn](COM_Reference/Properties/PMaxIn_Property.md)  
Read Gain Max |  [CALCulate:MEASure:MARKer:PNOP:GAIN:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:GAIN:MAXimum) |  [GainMax](COM_Reference/Properties/GainMax_Property.md)  
Read Comp Max |  [CALCulate:MEASure:MARKer:PNOP:COMPression:MAXimum?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:COMPression:MAXimum) |  [CompressionMax](COM_Reference/Properties/CompressionMax_Property.md)  
Read PBO Out |  [CALCulate:MEASure:MARKer:PNOP:BACKoff:POUT?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:BACKoff:POUT) |  [BackOffPout](COM_Reference/Properties/BackOffPout_Property.md)  
Read PBO In |  [CALCulate:MEASure:MARKer:PNOP:BACKoff:PIN?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:BACKoff:PIN) |  [BackOffPIn](COM_Reference/Properties/BackOffPIn_Property.md)  
Read PBO Gain |  [CALCulate:MEASure:MARKer:PNOP:BACKoff:GAIN?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:BACKoff:GAIN) |  [BackOffGain](COM_Reference/Properties/BackOffGain_Property.md)  
Turn ON|OFF PNOP marker search |  [CALCulate:MEASure:MARKer:PNOP[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:PNOP:STATe) |  None  
  
Basic Marker Search Functions  
---  
Execute Search |  [CALCulate:MEASure:MARKer:FUNCtion:EXECute](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:EXECute) |  [SearchFunction](COM_Reference/Properties/Search_Function_Property.md)  
Select Search Function |  [CALCulate:MEASure:MARKer:FUNCtion[:SELect]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:SELect) |  select and execute each Search...  
Maximum |  [CALCulate:MEASure:MARKer:FUNCtion[:SELect]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:SELect) |  [mark.SearchMax](COM_Reference/Methods/Search_Max_Method.md)  
Minimum |  [CALCulate:MEASure:MARKer:FUNCtion[:SELect]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:SELect) |  [mark.SearchMin](COM_Reference/Methods/Search_Min_Method.md)  
Target (Value) |  [CALCulate:MEASure:MARKer:FUNCtion:TARGet[:VALue]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:TARGet:VALue) |  [mark.TargetValue](COM_Reference/Properties/TargetValue_Property.md)  
Select transition type |  [CALCulate:MEASure:MARKer:FUNCtion:TARGet:TRANsition](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:TARGet:TRANsition) |  None  
Excursion Value |  [CALCulate:MEASure:MARKer:FUNCtion:PEAK:EXCursion](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:PEAK:EXCursion) |  [mark.PeakExcursion](COM_Reference/Properties/Peak_Excursion_Property.md)  
Threshold Value |  [CALCulate:MEASure:MARKer:FUNCtion:PEAK:THReshold](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:PEAK:THReshold) |  [mark.PeakThreshold](COM_Reference/Properties/Peak_Threshold_Property.md)  
Set or return polarity of the peak search |  [CALCulate:MEASure:MARKer:FUNCtion:PEAK:POLarity](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:PEAK:POLarity) |  None  
Assign Marker to Domain |  [CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER[:RANGe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:RANGe_) |  [mark.UserRange](COM_Reference/Properties/User_Range_Property.md)  
Domain Range Start |  [CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STARt](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STARt) |  [mark.UserRangeMin](COM_Reference/Properties/User_Range_Min_Property.md)  
Domain Range Stop |  [CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STOP](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STOP) |  [mark.UserRangeMax](COM_Reference/Properties/User_Range_Max_Property.md)  
Tracking |  [CALCulate:MEASure:MARKer:FUNCtion:TRACKing](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:TRACking) |  [mark.Tracking](COM_Reference/Properties/Tracking_Property.md) [mark.SearchFunction](COM_Reference/Properties/Search_Function_Property.md)  
  
Bandwidth & Notch Marker Search  
---  
Bandwidth (Target) |  [CALCulate:MEASure:MARKer:BWIDth:THReshold](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:THReshold) |  [meas.BandwidthTarget](COM_Reference/Properties/Bandwidth_Target_Property.md)  
Search Filter Bandwidth |  [CALCulate:MEASure:MARKer:BWIDth[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:STATe) |  [meas.SearchFilterBandwidth](COM_Reference/Methods/Search_Filter_Bandwidth_Method.md)  
Read Filter BandWidth |  [CALCulate:MEASure:MARKer:BWIDth:DATA?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:DATA) |  [meas.FilterBW](COM_Reference/Properties/Filter_BW_Property.md)  
Read Filter Center Freq |  [CALCulate:MEASure:MARKer:BWIDth:DATA?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:DATA) |  [meas.FilterCF](COM_Reference/Properties/Filter_CF_Property.md)  
Read Filter Loss |  [CALCulate:MEASure:MARKer:BWIDth:DATA?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:DATA) |  [meas.FilterLoss](COM_Reference/Properties/Filter_Loss_Property.md)  
Read Filter Q |  [CALCulate:MEASure:MARKer:BWIDth:DATA?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:DATA) |  [meas.FilterQ](COM_Reference/Properties/Filter_Q_Property.md)  
Set bandwidth marker function reference to either MARKer or PEAK |  [CALCulate:MEASure:MARKer:BWIDth:REF](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:BWIDth:REF) |  None  
Read notch search result |  [CALCulate:MEASure:MARKer:NOTCh:DATA?](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:NOTCh:DATA) |  None  
Notch Search |  [CALCulate:MEASure:MARKer:NOTCh[:STATe]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:NOTCh:STATe) |  None  
Notch Ref To |  [CALCulate:MEASure:MARKer:NOTCh:REF](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:NOTCh:REF) |  None  
Notch Level |  [CALCulate:MEASure:MARKer:NOTCh:THReshold](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:NOTCh:THReshold) |  None  
  
Multi Peak & Target Marker Search  
---  
Multi Peak Search |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:EXECute](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:EXECute) |  None  
Peak Threshold |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:PEAK:THReshold](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:PEAK:THReshold) |  None  
Peak Excursion |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:PEAK:EXCursion](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:PEAK:EXCursion) |  None  
Peak Polarity |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:PEAK:POLarity](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:PEAK:POLarity) |  None  
Multi Target Search |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:EXECute](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:EXECute) |  None  
Target Value |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:TARGet[:VALue]](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:TARGet:VALue) |  None  
Set or return search type of the multi search |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:SELect](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:SELect) |  None  
Turn ON|OFF search tracking |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:TRACking](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:TRACking) |  None  
Transition |  [CALCulate:MEASure:MARKer:FUNCtion:MULTi:TARGet:TRANsition](GP-IB_Command_Finder/Calculate/MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:MULTi:TARGet:TRANsition) |  None  
  
Status Bar  
---  
Status Bar On|Off |  [DISPlay:ANNotation[:STATus]](GP-IB_Command_Finder/Display.md#annstatus) |  [app.ShowStatusBar](COM_Reference/Methods/Show_Status_Bar_Method.md)  
Toolbars/ Title Bars  
Toolbars On|Off |  [DISPlay:TOOLbar:ENTRy](GP-IB_Command_Finder/Display.md#toolEntry) [DISPlay:TOOLbar:MARKer](GP-IB_Command_Finder/Display.md#toolMarker) [DISPlay:TOOLbar:KEYS[:STATe]](GP-IB_Command_Finder/Display.md#keys) [DISPlay:TOOLbar:EXT[:STATe]](GP-IB_Command_Finder/Display.md#extensions) [DISPlay:TOOLbar:TRAN[:STATe]](GP-IB_Command_Finder/Display.md#transform) |  [app.ShowToolbar](COM_Reference/Methods/Show_Toolbar_Method.md)  
Title Bars On|Off |  None |  [app.ShowTitleBars](COM_Reference/Methods/Show_Title_Bars_Method.md)  
Tables  
Tables On|Off |  [DISPlay:WINDow:TABLe](GP-IB_Command_Finder/Display.md#tabl) |  [win.ShowTable](COM_Reference/Methods/Show_Table_Method.md)  
Data/Memory Trace  
Memory Trace On|Off |  [DISPlay:WINDow:TRACe:MEMory](GP-IB_Command_Finder/Display.md#memstate) |  [meas.View](COM_Reference/Properties/View_Property.md)  
  
Marker (readout) Display  
---  
Marker Readout On|Off |  [DISPlay:WINDow:ANNotation:MARKer[:STATe]](GP-IB_Command_Finder/Display.md#mstatus) |  [win.MarkerReadout](COM_Reference/Properties/MarkerReadout_Property.md)  
Marker Readout Size |  [DISPlay:WINDow:ANNotation:MARKer:SIZE](GP-IB_Command_Finder/Display.md#size) |  [win.MarkerReadoutSize](COM_Reference/Properties/MarkerReadoutSize_Property.md)  
Readouts Per Trace |  [DISPlay:WINDow:ANNotation:MARKer:NUMBer](GP-IB_Command_Finder/Display.md#MarkerNumber) |  [MarkerReadoutsPerTrace](COM_Reference/Properties/MarkerReadoutsPerTrace_Property.md)  
Stimulus decimal places |  [DISPlay:WINDow:ANNotation:MARKer:RESolution:STIMulus](GP-IB_Command_Finder/Display.md#MarkerResoStimulus) |  [MarkerReadoutStimulusPlaces](COM_Reference/Properties/MarkerReadoutStimulusPlaces_Property.md)  
Response decimal places |  [DISPlay:WINDow:ANNotation:MARKer:RESolution:RESPonse](GP-IB_Command_Finder/Display.md#MarkerResolResponse) |  [MarkerReadoutResponsePlaces](COM_Reference/Properties/MarkerReadoutResponsePlaces_Property.md)  
Readout position: X-axis |  [DISPlay:WINDow:ANNotation:MARKer:XPOSition](GP-IB_Command_Finder/Display.md#MarkerXposition) |  [MarkerReadoutXPosition](COM_Reference/Properties/MarkerReadoutXPosition_Property.md)  
Readout position: Y-axis |  [DISPlay:WINDow:ANNotation:MARKer:YPOSition](GP-IB_Command_Finder/Display.md#MarkerYposition) |  [MarkerReadoutYPosition](COM_Reference/Properties/MarkerReadoutYPosition_Property.md)  
Marker symbol |  [DISPlay:WINDow:ANNotation:MARKer:SYMBol](GP-IB_Command_Finder/Display.md#MarkerSymbol) |  [MarkerSymbol](COM_Reference/Properties/MarkerSymbol_Property.md)  
  
* * *

