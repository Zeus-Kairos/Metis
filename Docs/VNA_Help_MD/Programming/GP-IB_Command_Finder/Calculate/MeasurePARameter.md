# CALCulate:MEASure:PARameter Commands

Selects a measurement parameter.

CALCulate:MEASure PARameter  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Measurement Parameters](../../../S1_Settings/Measurement_Parameters.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:PARameter <string>

Applicable Models: All (Read-Write) Set/get a measurement parameter for the
specified (cnum/mnum) measurement. This command replaces the following
commands: [CALC:CUST:MOD](Custom.md#Modify)
[CALC:PAR:MOD:EXT](Parameter.md#ModExtend)
[CALC:FSIM:BAL:PAR:SBAL[:DEF]](FSimulatorBalun.md#parSBAL)
[CALC:FSIM:BAL:PAR:SSB[:DEF]](FSimulatorBalun.md#parSSB)
[CALC:FSIM:BAL:PAR:BBAL[:DEF]](FSimulatorBalun.md#parBBAL)
[CALC:FSIM:BAL:PAR:BALS[:DEF]](FSimulatorBalun.md#parBALS)
[CALC:FSIM:BAL:PAR:BAL[:DEF]](FSimulatorBalun.md#parBAL1) Note: For
Application Measurements see
[CALCulate:MEASure:DEFine](Measure.md#CALCulate:MEASure:DEFine)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<string> | (String ) Measurement Parameter to create. Case sensitive. For S-parameters: Any S-parameter available in the VNA Single-digit port numbers CAN be separated by "_" (underscore). For example: **" S21" or "S2_1"** Double-digit port numbers MUST be separated by underscore. For example: **" S10_1"** For ratioed measurements: Any two VNA physical receivers separated by forward slash '/' followed by comma and source port. For example: "A/R1, 3" [Learn more about ratioed measurements](../../../S1_Settings/Measurement_Parameters.md#arb_ratio) See a [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. For non-ratioed measurements: Any VNA physical receiver followed by comma and source port. For example: "A, 4" [Learn more about unratioed measurements.](../../../S1_Settings/Measurement_Parameters.md#Unratioed_Power) See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. Ratioed and Unratioed measurements can also use logical receiver notation to refer to receivers. This notation makes it easy to refer to receivers with an [external test set](../../../System/External_Testset_Control.md) connected to the VNA. You do not need to know which physical receiver is used for each test port. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation) For ADC measurements: Any ADC receiver in the VNA followed by a comma, then the source port. For example: "AI1,2" indicates the Analog Input1 with source port of 2. [Learn more about ADC receiver measurements.](../../../S1_Settings/ADC_Measurements.md) For Balanced Measurements: For 1 port balanced measurement, choose from: Sdd11, Scd11, Sdc11, Scc11 For Balanced - Single-ended measurement, choose from: Sdd11, Scd11, Sdc11, Scc11, Ssd21, Ssc21, Sds12, Scs12, Sss22, Imb, CMMR1, CMMR2

  * Imb = - S_1pos_2/S_1neg_2
  * CMMR1 = Ssd21/Ssc21
  * CMMR2 = Sds12/Scs12

For Balanced - Single-ended - Single-ended measurement, choose from: Sdd11,
Scd11, Sdc11, Scc11, Ssd21, Ssc21, Ssd31, Ssc31,Sds12, Sds13, Scs12, Scs13,
Sss22, Sss32, Sss23, Sss33, Imbal1, Imbal2, Sds12/Scs12, Sds13/Scs13 For
Single-ended - Balanced measurement, choose from: Sss11, Sds21, Scs21, Ssd12,
Ssc12, Sdd22, Scd22, Sdc22, Scc22, Imb, CMMR1, CMMR2

  * Imb = - S_2pos_1/S_2neg_1
  * CMMR1 = Sds21/Scs21
  * CMMR2 = Ssd12/Ssc12

For Balanced - Balanced measurement, choose from: Sdd11, Sdd21, Sdd12, Sdd22,
Scd11, Scd21, Scd12, Scd22, Sdc11, Sdc21, Sdc12, Sdc22, Scc11, Scc21, Scc12,
Scc22, Imb1, Imb2, CMMR

  * Imb1 = - (S_1pos_2pos  S_1pos_2neg)/(S_1neg_2pos  S_1neg_2neg)
  * Imb2 = - (S_2pos_1pos  S_2pos_1neg)/(S_2neg_1pos  S_2neg_1neg)
  * CMMR = - Sdd21/Scc21

For Single-ended - Single-ended - Balanced measurement, choose form: Sss11,
Sss21, Sss12, Sss22, Sds31, Scs31, Sds32, Scs32, Ssd13, Ssd23, Ssc13, Ssc23,
Sdd33, Scd33, Sdc33, Scc33, Imb1, Imb2, CMMR1, CMMR2

  * Imb1 = - (S_1pos_2pos  S_1pos_2neg)/(S_1neg_2pos  S_1neg_2neg)
  * Imb2 = - (S_2pos_1pos  S_2pos_1neg)/(S_2neg_1pos  S_2neg_1neg)
  * Imb3 = - S_3pos_1/S_3neg_1
  * Imb4 = - S_3pos_2/S_3neg_2
  * CMMR1 = Sds31/Scs31
  * CMMR2 = Sds32/Scs32

Note: The right definition for SSB imbalance is added as Imb3, 4. The
definition for SSB Imb1, 2 seem a mistake, but keep it remained for backward
compatibility. Choose from the following (click or scroll down to view valid
measurement parameters for each measurement class)

  * "Standard"
  * "Active Hot Parameters"
  * "Vector Mixer/Converter"
  * "Scalar Mixer/Converter"
  * "Gain Compression"
  * "Gain Compression Converters"
  * ["Modulation Distortion"](Measure.md#Modulation_Distortion)
  * "Noise Figure Cold Source"
  * "Noise Figure Converters"
  * Phase Noise
  * "Swept IMD"
  * "IM Spectrum"
  * "Swept IMD Converters"
  * "IM Spectrum Converters"
  * Impedance Measurement
  * "Differential I/Q"
  * "Spectrum Analyzer"

(variant) Measurement names to create: | Meas Class | Measurement Name | Description  
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
GCX - All Gain Compression parameters (except S21 and S12) plus the following:  
"S11" "SC21" "SC12" "S22" "Ipwr" "RevIPwr" "Opwr" "RevOPwr" | Mixer parameters  
"Modulation Distortion" [Learn more](../../../Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md#Measurement_Parameters) | Modulation Distortion:  
"POut2" | Power Out  
"PIn1" | Power In  
"MSig2" | Modulation Signal Out  
"MDist2" | Modulation Distortion Out  
"MGain21" | Modulation Gain  
"MComp21" | Modulation Compression  
"PGain21" | Power Gain  
"S11" | Linear Input Match  
"S21" | Linear Gain  
"LPIn1" | Linear Input Match  
"LPOut1" | Linear Reflected Power In  
"LPOut2" | Linear Power Out  
"A", "b1" | Port 1 test port receiver  
"B", "b2" | Port 2 test port receiver  
"R1", "a1" | Port 1 reference receiver  
"R2", "a2" | Port 2 reference receiver  
"CarrIn1" | Input Band Power  
"CarrOut2" | Output Band Power  
"CarrGain21" | Band Power Gain  
"ACPIn1" | ACP at input  
"ACPOut2" | ACP at output  
"ACPDist21" | ACP distortion, Added by DUT  
"EVMDistEq21" | EVM Equalized Distortion, Added by DUT  
"EVMDistUn21" | EVM Unequalized Distortion, Added by DUT  
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
Impedance Measurement (E5080B Only) | "Z" "Y" "Ls" "Lp" "Cs" "Cp" "Rs" "Rp" "Q" "D" | Impedance Admittance Equivalent Series Inductance Equivalent Parallel Inductance Equivalent Series Capacitance Equivalent Parallel Capacitance Equivalent Series Resistance Equivalent Parallel Resistance Q Value (Quality Factor) Dissipation Factor  
"Differential I/Q" [Learn more](../../../Applications/Differential_IQ.md#DefineParameter) | Create custom parameters using [Sens:DIQ:Par:Def](../Sense/DIQ.md#parDefine), then specify your custom parameter name here. The following are default parameters:  
"IPwrF1" "OPwrF1" "GainF1" | Input Power over F1 range Output Power over F1 range Gain over F1 range  
"Spectrum Analyzer" [Learn more](../../../Applications/Spectrum_Analyzer.md#HowMeasParams) | "a<n>" "b<n>" where <n> is the port number to measure "ImageReject<n>" where <n> is the image reject trace | Reference receiver Test port receiver  
  
Examples | CALC:MEAS:PAR "Sdd11" calculate2:measure2:parameter "Sdd11" CALC:MEAS2:DEF 'PN:Phase Noise' 'Defines a Phase Noise measurement but doesn't display.  
DISP:MEAS2:FEED 1 'Displays Phase Noise measurement in window number 1.  
CALC:MEAS2:PAR 'AM' 'Changes the Phase Noise parameter to AM in window number
1.  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:PARameter?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "S11"  
  
* * *

