# Measure

These commands are for setting up measurements.

CALCulate:MEASure [BLIMit More commands](MeasureBLIMit.md) COMPutation | DEViation CONVersion | FUNCtion [CORRection More commands](MeasureCorrection.md) [DATA More commands](MeasureDATA.md) DEFine DELete | ALL [DISTortion More commands](MeasureAMDistortion.md) EQUation | FAST[:STATe] | [:STATe] | TEXT | VALid? [FILTer More commands](MeasureFILter.md) FORMat | UNIT [FUNCtion More commands](MeasureFUNCtion.md) [GCData More commands](MasureGCData.md) [GCMeas More commands](MeasureGCMeas.md) [GDELay More commands](MeasureGDELay.md) HOLD | CLEar | [TYPE] [LIMit More commands](MeasureLIMit.md) [MARKer More commands](MeasureMARKer.md) MATH | FUNCtion | INTerpolate[:STATe] | LOCKed[:STATe]? | MEMorize [ | NORMalize](Measure.md#MathNorm) | NEW MIXer | XAXis [OFFSet More commands](MeasureOFFSet.md) [PARameter More commands](MeasurePARameter.md) [PN More commands](MeasurePhaseNoise.md) RDATa? [RLIMit More commands](MeasureRLIMit.md) [SA More commands](MeasureSA.md) [SMOothing More commands](MeasureSMOothing.md) [TRANsform More commands](MeasureTRANsform.md) [UNCertainty More commands](MeasureUncertainty.md) [X More commands](MeasureX.md) [Y More commands](MeasureY.md)  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:CONVersion:FUNCtion <char>

Applicable Models: All (Read-Write) Sets or gets the parameter after
conversion using the parameter conversion function, for the active trace of
selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Select from the following parameters after conversion:

  * "OFF"
  * "ZREFlection" \- Specifies the equivalent impedance in reflection measurement.
  * "ZTRansmit" \- Specifies the equivalent impedance (series) in transmission measurement.
  * "ZTSHunt" \- Specifies the equivalent impedance (shunt) in transmission measurement.
  * "YREFlection" \- Specifies the equivalent admittance in reflection measurement.
  * "YTRansmit" \- Specifies the equivalent admittance (series) in transmission measurement.
  * "YTSHunt" \- Specifies the equivalent admittance (shunt) in transmission measurement.
  * "INVersion" \- Specifies the inverse S-parameter (1/S).
  * "CONJugation" \- Specifies the conjugate.

  
Examples | SCPI sequence to retrieve resistance from a polar chart: CALC:MEAS:CONV:FUNC ZREFlection CALC:MEAS:FORM:REAL CALC:MEAS:DATA:FDATA? SCPI sequence to retrieve reactance from a polar chart: CALC:MEAS:CONV:FUNC ZREFlection CALC:MEAS:FORM:IMAG CALC:MEAS:DATA:FDATA?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CONVersion:FUNCtion?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "OFF"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:COMPutation:DEViation <char>

Applicable Models: All (Read-Write) Calculates the deviation from a least-
squares best fit line.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Select from the following parameters:

  * "OFF"
  * "LINear" -Fit to 1st order curve minimizing RSS deviation.
  * "PARabolic" \- Fit to 2nd order curve minimizing RSS deviation.
  * "CUBic" \- Fit to 3rd order curve minimizing RSS deviation.

  
Examples | CALC:MEAS1:COMP:DEV LIN  
calculate2:measure1:computation:deviation linear  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:COMPutation:DEViation?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "OFF"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DEFine <string>

Applicable Models: All (Write-only) Creates a measurement but does NOT display
it, on an existing or new channel. When a new channel is created, any licensed
measurement class can be used. Up to 580 (2000 for M98xxA, P50xxA/B and
E5080B, E5081A) measurements can be created. Note that each display window can
only display a limited number of traces. See [Traces, Channels, and Windows on
the VNA](../../../S0_Start/Traces_Channels_and_Windows.htm#window).

  * Use [DISP:WIND:STATe](../Display.md#dwstat) to create a window if it doesn't already exist.
  * Use [DISP:MEAS<mnum>:FEED<wnum>](../Display.md#MeasFeed) to display the measurement in window <wnum>.

This command replaces the following commands:
[CALCulate:PARameter[:DEFine]](Parameter.md#cpd)
[CALCulate:PARameter[:DEFine]:EXTended](Parameter.md#DefineExtend)
[CALCulate:CUSTom:DEFine](Custom.md#CustDef)  
---  
Parameters |   
<cnum> | Channel number of the new measurement. If unspecified, value is set to 1. If the specified channel does not exist, then a channel of the specified type will be created. If no type of channel is specified, then a standard channel will be created. If the specified channel exists, then the parameter will be added to the channel provided the existing channel supports the parameter (otherwise, an error will be generated).  
<mnum> | Measurement number for the new measurement.  If the specified measurement number is already in use, an error will be generated.  
<string> | (String ) Measurement Parameter and optional measurement class name separated by a ":" (colon). For example, "S21:Gain Compression" creates an S21 measurement and selects the Gain Compression measurement class for the channel. Note: If a measurement class of a channel does not support the defined measurement parameter, an error is generated. Case sensitive. For S-parameters: Any S-parameter available in the VNA Single-digit port numbers CAN be separated by "_" (underscore). For example: **" S21" or "S2_1"** Double-digit port numbers MUST be separated by underscore. For example: **" S10_1"** For ratioed measurements: Any two VNA physical receivers separated by forward slash '/' followed by comma and source port. For example: "A/R1, 3" [Learn more about ratioed measurements](../../../S1_Settings/Measurement_Parameters.md#arb_ratio) See a [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. For non-ratioed measurements: Any VNA physical receiver followed by comma and source port. For example: "A, 4" [Learn more about unratioed measurements.](../../../S1_Settings/Measurement_Parameters.md#Unratioed_Power) See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. Ratioed and Unratioed measurements can also use logical receiver notation to refer to receivers. This notation makes it easy to refer to receivers with an [external test set](../../../System/External_Testset_Control.md) connected to the VNA. You do not need to know which physical receiver is used for each test port. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation) For ADC measurements: Any ADC receiver in the VNA followed by a comma, then the source port. For example: "AI1,2" indicates the Analog Input1 with source port of 2. [Learn more about ADC receiver measurements.](../../../S1_Settings/ADC_Measurements.md) (string) - The following are the existing valid measurement parameters for each measurement class. The Measurement Class must be installed and registered on the VNA. (variant) Measurement names to create: | Meas Class | Measurement Name | Description  
---|---|---  
"Standard" | "S11", "S21", and so forth "A_1","A_2", and so forth | S-parameter name Unratioed parameter names with notation: "receiver_source port" See [balanced parameter](MeasurePARameter.md#CALCulate:MEASure:PARameter) names  
Active Hot Parameters | Port 1 is the Source Port (DUT input). Port 3 or Port 2 can be chosen as the output of the DUT. "HotS11" "HotS31" "HotS13" "HotS33" "IPwr" "OPwr" "Gamma" "Pmax" "Xs(3,3)" "Xt(3,3)" "Xf(3,1)" "DeltaOPwr" | [Learn about Active Hot parameters](../../../Applications/Active_Match.md#Active_Match_Measurement_Parameters)  
"Vector Mixer/Converter" | For output port Y (input port must be 1): "S11" "VCY1" "SYY" | [Learn about VMC parameters](../../../FreqOffset/VMC_Measurements.md#offered) Note: Input and output ports are set up using the [Mixer Setup](../../../Applications/MixerConverter_Setup.md#MixerSetupTab) dialog. If the ports are not set up using the Mixer Setup dialog, then ports 1 and 2 are the default input and output ports and the only ports that can be used.  
"Scalar Mixer/Converter" | For input port X and output port Y: "SCXY" "SCYX" "SXX" "SYY" "Ipwr" "RevIPwr" "Opwr" "RevOPwr" | [Learn about SMC parameters](../../../FreqOffset/SMC_Measurements.md#offered) Note: Input and output ports are set up using the [Mixer Setup](../../../Applications/MixerConverter_Setup.md#MixerSetupTab) dialog. If the ports are not set up using the Mixer Setup dialog, then ports 1 and 2 are the default input and output ports and the only ports that can be used.  
"Gain Compression" [Learn more](../../../Applications/Gain_Compression_Application.md#Parameters) "Gain Compression Converters" [Learn more](../../../Applications/Gain_Compression_for_Converters.md#MeasParams) | GCA and GCX:  
"CompIn21" | Input power at the compression point.  
"CompOut21" | Output power at the compression point.  
"CompGain21" | Gain at the compression point.  
"CompS11" |  Input Match at the compression point  
"RefS21" | Linear Gain  
"DeltaGain21" | CompGain21 -Linear Gain  
"S11", "S21", "S12", "S22" | Standard S-parameters; measured at port 1 and port 2  
GCX \- All Gain Compression parameters (except S21 and S12) plus the
following:  
"S11" "SC21" "SC12" "S22" "Ipwr" "RevIPwr" "Opwr" "RevOPwr" | Mixer parameters  
"Modulation Distortion" Modulation Distortion Converters [Learn more](../../../Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md#Measurement_Parameters) | Modulation Distortion and Modulation Distortion Converters:  
"PIn1" | Power In  
"POut1" | Reflected Power In  
"POut2" | Power Out  
"PModFile" | Power of modulation file  
"MSig2" | Modulation Signal Out  
"MDist2" | Modulation Distortion Out  
"MDistIR2" | Modulation Distortion Input-referred  
"MGain21" | Modulation Gain  
"MComp21" | Modulation Compression  
"PGain21" | Power Gain  
"LMatch2" | Load match of VNA port  
"CarrIn1" | Input Band Power  
"CarrOut2" | Output Band Power  
"CarrGain21" | Band Power Gain  
"NPRIn1" | NPR at Input  
"NPROut2" | NPR at Output  
"NPRDist21" | NPR Distortion, Added by DUT  
"NPRPwrIn1" | NPR Input Power  
"NPRPwrOut2" | NPR Output Power  
"ACPIn1" | ACP at input  
"ACPOut2" | ACP at output  
"ACPDist21" | ACP distortion, Added by DUT  
"ACPPwrIn1" | ACP Input Power  
"ACPPwrOut2" | ACP Output Power  
"EVMDistEq21" | EVM Equalized Distortion, Added by DUT  
"EVMDistUn21" | EVM Unequalized Distortion, Added by DUT  
"EVMPwrIn1" | EVM Input Power  
"EVMPwrOut2" | EVM Output Power  
"ModFilter" | Measurement Modulation Filter  
"A", "b1" | Port 1 test port receiver  
"B", "b2" | Port 2 test port receiver  
"C", "b3" | Port 3 test port receiver  
"D", "b4" | Port 4 test port receiver  
"R1", "a1" | Port 1 reference receiver  
"R2", "a2" | Port 2 reference receiver  
"R3", "a3" | Port 3 reference receiver  
"R4", "a4" | Port 4 reference receiver  
Modulation Distortion ONLY \- NOT Modulation Distortion Converters  
"S11" | Linear Input Match  
"S21" | Linear Gain  
"LPIn1" | Linear Input Match  
"LPOut1" | Linear Reflected Power In  
"LPOut2" | Linear Power Out  
"Noise Figure Cold Source" [Learn more](../../../Applications/Noise_Figure.md#parameters) "Noise Figure Converters" [Learn more](../../../Applications/Noise_Figure_on_Converters.md) | Noise Figure AND NFX:  
"NF" | Noise figure  
"ENR" | Validate noise source measurements.  
"T-Eff" | Effective noise temperature.  
"DUTRNP" "DUTRNPI" | DUT noise power ratio. (Noise power expressed in Kelvin divided by 290).  
"SYSRNP" "SYSRNPI" | System noise power ratio  
"DUTNPD" "DUTNPDI" | DUT noise power density. (Noise power expressed in dBm/Hz).  
"SYSNPD" "SYSNPDI" | System noise power density.   
"OvrRng"  
(Opt 029 Only) | Indication that the noise receiver is being over powered.  
"T-Rcvr" (Opt 029 Only) | Temperature reading (in Kelvin) of the noise receiver board.  
Noise Figure ONLY - NOT NFX:  
"S11", "S21", "S12", "S22" | Standard S-parameters; measured with the port1 and port2 noise switches set for noise mode.  
"A_1","A_2" ...and so forth. | Unratioed parameters; with notation:  
"receiver, source port"  
"GammaOpt" | Optimum Complex Reflection Coefficient  
"Rn" | Noise Resistance  
"NFMin" | Minimum noise figure that occurs at GammaOpt  
NFX ONLY:  
"S11" "SC21" "SC12" "S22" "Ipwr" "RevIPwr" "Opwr" "RevOPwr" | Mixer parameters  
"ALO1"," BLO1" ...and so forth. | Test port receiver at LO1 frequency  
"R1_1", "B_2" ..and so forth. | Unratioed parameters with notation: "receiver_source port"  
Phase Noise [Learn more](../../../Applications/Phase_Noise/Overview.md) |  |   
PN | Phase Noise  
AM | AM Noise  
"Swept IMD" "Swept IMD Converters" [Learn more](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.md#Parameters) | There are over 150 possible Swept IMD parameters, too many to list here. Build the parameters with the [Swept IMD Parameter](../../../Applications/Swept_IMD.md#HowParams) dialog, then copy the parameter name to the remote command. The following are a few example parameters:  
"PwrMainLo" | Absolute power of the Low tone at the DUT output.  
"IM3" | Power of the third product relative to the average power of the f1 and f2 tones measured at the DUT output.  
"OIP3" | Theoretical power level at which the third product will be the same power level as the average of the main tones at the output of the DUT.  
"IM Spectrum" [Learn more](../../../Applications/IMSpectrum.md#Parameters) | "Output" | View signals OUT of the DUT and into VNA port 2 (B receiver).  
"Input" | View signals IN to the DUT (R1 receiver).  
"Reflection" | View signals reflected off the DUT input and back into VNA port 1 (A receiver)  
"IMx Spectrum Converters" [Learn more](../../../Applications/IM_Spectrum_for_Converters.md#Parameters) | "Output" | View signals OUT of the DUT and into VNA port 2 (B receiver)  
"Differential I/Q" [Learn more](../../../Applications/Differential_IQ.md#DefineParameter) | Create custom parameters using [Sens:DIQ:Par:Def](../Sense/DIQ.md#parDefine), then specify your custom parameter name here. The following are default parameters:  
"IPwrF1" "OPwrF1" "GainF1" | Input Power over F1 range Output Power over F1 range Gain over F1 range  
"Spectrum Analyzer" [Learn more](../../../Applications/Spectrum_Analyzer.md#HowMeasParams) | "a<n>" "b<n>" where <n> is the port number to measure "ImageReject<n>" where <n> is the image reject trace | Reference receiver Test port receiver  
"Vector Signal Analyzer" Learn more | "a<n>" "b<n>" where <n> is the port number to measure | Reference receiver Test port receiver  
TDR | Use [SYSTem:TDR:PRESet](../TDR_System.md#SYSTem:TDR:PRESet) instead of CALC:MEAS:DEFine  
Examples | CALC1:MEAS2:DEF "S11" 'Defines an S11 measurement for channel 1, measurement number 2. CALC4:MEAS3:DEF "S21:Gain Compression" 'Defines an S21 measurement for channel 4, measurement number 3, and creates a GCA channel. CALC2:MEAS:DEF "R1,1:Standard" 'Defines an R1,1 measurement for channel 2, measurement number 1 (default), and creates a Standard channel. SYST:FPRest  
CALC1:MEAS1:DEF "NF:Noise Figure Cold Source" 'Defines a Noise Figure
measurement for channel 2, measurement number 2, and creates a Noise Figure
channel.  
DISP:WIND1 ON  
DISP:MEAS1:FEED 1  
CALC2:MEAS2:DEF "CompIn21:Gain Compression" 'Defines an input power at
Compression point but doesn't display on channel 2.  
DISP:WIND2 ON  
DISP:MEAS2:FEED 2 'CompIn21 measurement in window number 2.  
CALC2:MEAS3:DEF "CompOut21:Gain Compression" 'Defines an output power at
Compression point but doesn't display on channel 2  
DISP:MEAS3:FEED 2 'CompOut21 measurement in window number 2  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DELete

Applicable Models: All  (Write-only) Deletes the specified measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number.   
Examples | CALC:MEAS2:DEL  
calculate2:measure2:delete  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate:MEASure:DELete:ALL

Applicable Models: All (Write-only) Deletes all measurements on the VNA.  
---  
Parameters |   
Examples | CALC:MEAS:DEL:ALL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:EQUation:FAST[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return equation editor trace
update delay. This command delays updating the equation editor trace until all
trace references have finished updating to ensure that all data is present.
Note: This command does not work in application channels. In addition, this
command does not work with the standard channel when the channel is in HOLD
and then SINGLE sweeps are sent.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: OFF (0)  Do not delay equation editor trace update. ON (1) Delay equation editor trace update.  
Examples | CALC:MEAS:EQU:FAST 1  
calculate2:measure1:equation:fast OFF  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:EQUation:FAST[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

CALCulate<cnum>:MEASure<mnum>:EQUation[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON and OFF the equation on selected
measurement for the specified channel. If the equation is not valid, then
processing is not performed. Use [CALC:EQUation:VALid?](Equation.md#valid) to
ensure that the equation is valid.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | **ON** (or 1) - turns equation ON. **OFF** (or 0) - turns equation OFF.  
Examples | CALC:MEAS:EQU 1 calculate2:measure1:equation:state 0  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:EQUation[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

CALCulate<cnum>:MEASure<mnum>:EQUation:TEXT <string>

Applicable Models: All (Read-Write) Specifies an equation or expression to be
used on the selected measurement for the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<string> | Any valid equation or expression. [See Equation Editor.](../../../S4_Collect/Equation_Editor.md)  
Examples | 'Equation (includes '=') CALC:MEAS:EQU:TEXT "foo=S11/S21" 'Expression  
calculate2:measure1:equation:text "S11/S21"  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:EQUation:TEXT?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:MEASure<mnum>:EQUation:VALid?

Applicable Models: All (Read-Only) Returns a boolean value to indicate if the
current equation on the selected measurement for the specified channel is
valid. For equation processing to occur, the equation must be valid and ON
([CALC:EQU:STAT 1](Equation.md#state)).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:EQU:VAL? calculate2:measure1:equation:valid?  
Return Type | Boolean 1 - equation is valid 0 - equation is NOT valid  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:MEASure<mnum>:FORMat <char>

Applicable Models: All (Read-Write) Sets the display format for the
measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from:

  * MLINear
  * MLOGarithmic
  * PHASe
  * UPHase 'Unwrapped phase
  * IMAGinary
  * REAL
  * POLar
  * SMITh
  * SADMittance 'Smith Admittance
  * SWR
  * GDELay 'Group Delay
  * KELVin
  * FAHRenheit
  * CELSius
  * PPHase 'Positive Phase
  * COMPlex

  
Examples | CALC:MEAS:FORM MLIN  
calculate2:measure1:format polar  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FORMat?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MLOG  
  
* * *

CALCulate<cnum>:MEASure<mnum>:FORMat:UNIT <dataFormat>, <units>

Applicable Models: All (Read-Write) Sets and returns the units for the
specified data format. Measurements with display formats other than those
specified are not affected.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<dataFormat> | Choose from:

  * MLOG \- Log magnitude
  * MLIN \- Linear magnitude

  
<units> | For unratioed MLOG measurements, choose from:

  * dB Units are displayed in decibels.
  * DBM Units are displayed in dBm. 0 dBm = 0.001 watt
  * DBMV Units are displayed in dBmV. 0 dBmV = 0.001 volt  
DBmV value depends on the reference impedance: dBmV = dBm + 30 + 10*log10(Z0)

  * DBMA Units are displayed in dBmA. 0 dBmA = 0.001 Ampere
  * DBUV Units are displayed in dBuV. 0 dBuV = 1 uV   
DBuV value depends on the reference impedance: dBuV = dBm + 90 + 10*log10(Z0)

For unratioed MLIN measurements, choose from:

  * UNIT - No units. Linear magnitude without conversion
  * W \- Units are displayed in Watts
  * V \- Units are displayed in Volts
  * A \- Units are displayed in Amperes

  
Examples | CALC:MEAS:FORM:UNIT MLOG, DBM  
calculate2:measure1:format:unit mlog,dbmv  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FORMat:UNIT? <dataFormat>  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MLOG, DBM  
  
* * *

## CALCulate<ch>:MEASure<mnum>:HOLD:CLEar

Applicable Models: All (Write-only) Resets the currently-stored data points to
the live data trace and restarts the currently-selected Trace Hold type.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:HOLD:CLE calculate2:measure1:hold:clear  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:HOLD:TYPE <value>

Applicable Models: All (Read-Write) Sets the type of trace hold to perform.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Trace Hold type. Choose from: OFF \- Disables the Trace Hold feature. MINimum \- Sets Trace Hold to store the lowest measured data points. MAXimum \- Sets Trace Hold to store the highest measured data points.  
Examples | CALC:MEAS:HOLD:TYPE MAX calculate2:measure1:hold:type minimum  
Query Syntax | CALCulate<ch>:MEASure<mnum>:HOLD:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MATH:FUNCtion <char>

Applicable Models: All (Read-Write) Sets math operations on the currently
selected measurement and the trace stored in memory. (There MUST be a trace
stored in Memory. See CALC:MEAS:MATH MEM)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | The math operation to be applied. Choose from the following:  
| NORMal | Trace data only  
---|---|---  
| ADD | Data + Memory  
| SUBTract | Data - Memory  
| MULTiply | Data * Memory  
| DIVide | Data / Memory  
Examples | CALC:MEAS:MATH:FUNC NORM  
calculate2:measure1:math:function subtract  
---|---  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MATH:FUNCtion?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NORMal  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MATH:INTerpolate[:STATe]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and reads the
state of the memory data interpolation. [Learn
more](../../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation).  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Turn memory data interpolation OFF. 1 - ON \- Turn memory data interpolation ON.  
Examples | CALC2:MEAS:MATH:INT 1  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MATH:INTerpolate?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MATH:LOCKed[:STATe]?

Applicable Models: All (Read-only) Returns whether the measurement number is
the locked trace created by Data-> New Trace under Math. A locked trace
indicates that the trace will not update from sweep to sweep. [Learn
more](../../../S4_Collect/Math_Operations.htm#Data-_New_Trace).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC2:MEAS3:MATH:LOCK:STAT?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MATH:LOCKed:STATe?  
Return Type | Boolean 0 \- Measurement is not locked. 1 \- Measurement is locked.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MATH:MEMorize

Applicable Models: All (Write-only) Puts the currently selected measurement
trace into memory. (Data-> Memory).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:MATH:MEM  
calculate2:measure1:math:memorize  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MATH:NORMalize

Applicable Models: All (Write-only) Execute the normalized for specified
measurement  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:MATH:NORM  
calculate2:measure1:math:normalize  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MATH:NEW [<mnum2>][, <windType>]

Applicable Models: All (Read-Write) Create a new data trace to be saved from
the same trace data (Data-> New Trace under Math). The query command returns
the measurement number of the memory trace created by the most recent
execution of the CALC:MEAS:MATH:NEW command. The query form takes no
parameters.  The CALC<cnum>:MEAS<mnum>:DATA returns the trace values. [Learn
more](../../../S4_Collect/Math_Operations.htm#Data-_New_Trace). When the
number of traces per window exceeds the limit, returns an error +113,
"Exceeded the maximum number of traces per windowz".  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number. The query command ignores <mnum>. If the measurement number is provided, the new measurement is created with that identifying number. If the measurement number is not provided, the new measurement uses the next available measurement number.  
<mnum2> | (Optional) The new measurement (trace number) is created with that identifying number..   
<windType> | (Optional) Feed the new measurement depending on this parameter.

  * NONE: No feed (Default) When not fed, the measurement is not visible on the display until it is placed into a window with the [**DISP:WIND:TRAC:FEED**](../Display.md#dwtf) command.
  * ACTive: Feed to active window
  * NEW: Feed to new window

  
Examples | CALC:MEAS:MATH:NEW  
calculate2:measure2:math:new 2, ACT  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MATH:NEW?  
  
This command is useful for determining the new measurements number in the
case where the optional <mnum2> parameter was not provided in a
CALC:MEAS:MATH:NEW command.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

CALCulate<ch>:MEASure<mnum>:MIXer:XAXis <char>

Applicable Models: All (Read-Write) Sets or returns the swept parameter to
display on the X-axis for the selected
[FCA](../../../FreqOffset/FCA_Use.md#Xaxis) and GCX measurement.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<mnum> | Measurement number for each measurement.   
<char> | Parameter to display on the X-axis. Choose from: INPut \- Input frequency span OUTPut \- Output frequency span LO_1 \- First LO frequency span LO_2 \- Second LO frequency span  
Examples | CALC:MEAS:MIX:XAX INPUT  
calculate2:measure1:mixer:xaxis output See an example that creates, selects,
and calibrates an
[SMC](../../GPIB_Example_Programs/Create_and_Cal_an_SMC_Measurement.md) and
[VMC](../../GPIB_Example_Programs/Create_and_Cal_a_VMC_Measurement.md)
measurement using SCPI.  
Query Syntax | CALCulate<ch>:MEASure<mnum>:MIXer:XAXis?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | INPut  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RDATA? <char>

Applicable Models: All (Read-only) Returns receiver data for the selected
measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from any physical receiver in the VNA. For example: "A" Also, REF - returns data for either R1 or R2 data depending on the source port of the selected measurement. See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. Note: Logical receiver notation is NOT allowed with this command. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation)  
Example | GPIB.Write "INITiate:CONTinuous OFF"  
GPIB.Write "INITiate:IMMediate;*wai"  
GPIB.Write "CALCulate:MEASure2:RDATA? A" GPIB.Write "CALCulate:MEASure2:RDATA?
REF"  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd) \- Two numbers per data point  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

