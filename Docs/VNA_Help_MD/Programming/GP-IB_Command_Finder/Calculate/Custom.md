# Calculate:Custom Commands

* * *

Creates and modifies application measurements.

These commands are Superseded by the
[CALCulate:MEASure:DEFine](Measure.md#CALCulate:MEASure:DEFine) and
[CALCulate:MEASure:PARameter](MeasurePARameter.md#CALCulate:MEASure:PARameter)
commands.

Note: For setting up a TDR measurement class, use
[SYSTem:TDR:INITialize](../TDR_System.md#SYSTem:TDR:INITialize).

CALCulate:CUSTom: [DEFine](Custom.md#CustDef) [MODify](Custom.md#Modify)  
---  
  
See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:CUSTom:DEFine <Mname>, <type> [,param]

Applicable Models: All (Write-only) Creates a custom measurement depending on
the [configurations and options](../../../Support/Configurations.md) . The
custom measurement is not automatically displayed. You must also do the
following:

  * Use [DISP:WIND:STATe](../Display.md#dwstat) to create a window if it doesn't already exist.·
  * Use [DISP:WIND:TRAC:FEED](../Display.md#dwtf) to display the measurement
  * Select the measurement ([CALC:PAR:SEL)](Parameter.md#cps) before making additional settings.

  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<Mname> | Name of the measurement. Any non-empty, unique string, enclosed in quotes.  
<type> | (string) - Choose from the following (click or scroll down to view valid <params> for each type)

  * "Standard"
  * "Active Hot Parameters"
  * "Vector Mixer/Converter"
  * "Scalar Mixer/Converter"
  * "Gain Compression"
  * "Gain Compression Converters"
  * "Modulation Distortion"
  * "Noise Figure Cold Source"
  * "Noise Figure Converters"
  * "Swept IMD"
  * "IM Spectrum"
  * "Swept IMD Converters"
  * "Modulation Distortion Converters"
  * Phase Noise
  * "IM Spectrum Converters"
  * "Differential I/Q"
  * "Spectrum Analyzer"

  
[param] | (variant) Measurement names to create: | Meas Class | Measurement Name | Description  
---|---|---  
"Standard" | "S11", "S21", and so forth "A_1","A_2", and so forth | S-parameter name Unratioed parameter names with notation: "receiver_source port" See [Balanced S-parameter measurement names](../../../S1_Settings/Balanced_Measurements.md#Mixed Mode)  
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
Phase Noise [Learn more](../../../Applications/Enhanced_Time_Domain_Analysis/Advanced_Waveform_Analysis/Overview.md) |  |   
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
Examples | CALC:CUST:DEF 'My VC21', 'Vector Mixer/Converter','S22' calculate2:custom:define 'MyNF', 'NoiseFigure', 'NF' CALC1:CUST:DEF 'MyAM', 'Phase Noise', 'AM' 'Defines an AM Noise measurement but doesn't display.  
DISP:MEAS:FEED 1 'Displays AM Noise measurement in window number 1.  
Query Syntax | Not applicable  
[Overlapped?](../../Learning_about_GPIB/Understanding_Command_Synchronization.md) | No  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:CUSTom:MODify <param>

Applicable Models: All (Write-only) Changes the selected custom measurement to
a different parameter. This is dependent upon the [configurations and
options](../../../Support/Configurations.htm). See an example using this
command for a
[VMC](../../GPIB_Example_Programs/Create_and_Cal_a_VMC_Measurement.md) and
[SMC](../../GPIB_Example_Programs/Create_and_Cal_an_SMC_Measurement.md)
measurement  
---  
Parameters |   
<cnum> | Channel of the custom measurement to be changed. First, select the measurement using [CALC:PAR:SEL](Parameter.md#cps).  
<param> | Parameter to change the custom measurement to. Select a parameter that is valid for the type of measurement. Choose from the same arguments as [Calc:Cust:Def](Custom.md#CustDef).  
Examples | SYST:PRES CALC2:CUST:DEF 'My VC21', 'Vector Mixer/Converter' CALC:PAR:SEL 'My VC21' CALC2:CUST:MOD 'S22' CALC:CUST:DEF 'MyPN','Phase Noise','PN' 'Defines a Phase Noise measurement but doesn't display.  
DISP:WIND1:TRAC1:FEED 'MyPN' 'Displays Phase Noise measurement in window
number 1.  
CALC:PAR:SEL 'MyPN' 'Selects the 'MyPN' measurement.  
CALC:CUST:MOD 'AM' 'Changes the Phase Noise parameter to AM.  
Query Syntax | Not applicable  
[Overlapped?](../../Learning_about_GPIB/Understanding_Command_Synchronization.md) | No  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

