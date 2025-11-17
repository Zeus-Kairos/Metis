##### Write-only

|

#####  
  
---|---  
  
## CreateCustomMeasurementEx Method

* * *

#### Description

| Creates a new custom measurement or a new 'standard' S-Parameter
measurement.  
---|---  
  
####  VB Syntax

| app.CreateCustomMeasurementEx chanNum,MeasClass,MeasName [,window]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | (object) - An [Application](../Objects/Application_Object.md) object  
chanNum | (long) -Channel number used by the new measurement; can exist or be a new channel.  
MeasClass | (string) - Measurement class of the new custom measurement object. The Measurement Class must be installed and registered on the VNA. Choose from the following (click or scroll down to view valid MeasNames for each MeasClass)

  * ["Standard"](CreateCustomMeasurementEx_Method.md#Standard)
  * "Active Hot Parameters"
  * ["Vector Mixer/Converter"](CreateCustomMeasurementEx_Method.md#Vector_Mixer_Converter)
  * ["Scalar Mixer/Converter"](CreateCustomMeasurementEx_Method.md#Scalar_Mixer_Converter)
  * ["Gain Compression"](CreateCustomMeasurementEx_Method.md#Gain_Compression)
  * ["Gain Compression Converters"](CreateCustomMeasurementEx_Method.md#Gain_Compression)
  * "Modulation Distortion"
  * ["Noise Figure Cold Source"](CreateCustomMeasurementEx_Method.md#Noise_Figure_Cold_Source)
  * ["Noise Figure Converters"](CreateCustomMeasurementEx_Method.md#Noise_Figure_Cold_Source)
  * Phase Noise
  * ["Swept IMD"](CreateCustomMeasurementEx_Method.md#Swept_IMD)
  * ["IM Spectrum"](CreateCustomMeasurementEx_Method.md#IM_Spectrum)
  * ["Swept IMD Converters"](CreateCustomMeasurementEx_Method.md#Swept_IMD)
  * ["IM Spectrum Converters"](CreateCustomMeasurementEx_Method.md#IMx_Spectrum_Converters)
  * ["Differential I/Q"](CreateCustomMeasurementEx_Method.md#Differential_I_Q)
  * ["Spectrum Analyzer"](CreateCustomMeasurementEx_Method.md#Spectrum_Analyzer)

  
MeasName | (variant) Measurement names to create: | Meas Class | Measurement Name | Description  
---|---|---  
"Standard" | "S11", "S21", and so forth "A_1","A_2", and so forth | S-parameter name Unratioed parameter names with notation: "receiver_source port" See [Balanced S-parameter measurement names](CreateMeasurement_Method.md#BalancedSparams)  
Active Hot Parameters | "HotS11" "HotS31" "HotS13" "HotS33" "IPwr" "OPwr" "Gamma" "Pmax" "Xs(3,3)" "Xt(3,3)" "Xf(3,1)" "DeltaOPwr" | [Learn about Active Hot parameters](../../../Applications/Active_Match.md#Active_Match_Measurement_Parameters)  
"Vector Mixer/Converter" | "S11" "VC21" "S22" | [Learn about VMC parameters](../../../FreqOffset/VMC_Measurements.md#offered)  
"Scalar Mixer/Converter" | "S11" "SC21" "SC12" "S22" "Ipwr" "RevIPwr" "Opwr" "RevOPwr" | [Learn about SMC parameters](../../../FreqOffset/SMC_Measurements.md#offered)  
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
"Differential I/Q" [Learn more](../../../Applications/Differential_IQ.md#DefineParameter) | Create custom parameters using [DefineParameter Method](DefineParameter_Method.md), then specify your custom parameter name here. The following are default parameters:  
"IPwrF1" "OPwrF1" "GainF1" | Input Power over F1 range Output Power over F1 range Gain over F1 range  
"Spectrum Analyzer" [Learn more](../../../Applications/Spectrum_Analyzer.md#HowMeasParams) | "a<n>" "b<n>" where <n> is the port number to measure "ImageReject<n>" where <n> is the image reject trace | Reference receiver Test port receiver  
window | (long) Optional argument. Number of the window the new custom measurement will be placed in. Choose between 1and the [maximum number of windows allowed on the VNA.](../../../S0_Start/Traces_Channels_and_Windows.md#window). If unspecified, the measurement is placed in the active window.  
  
#### Return Type

| IMeasurement  
  
#### Default

| Not Applicable  
  
#### Examples

| 'To create a scalar mixer measurement in channel 2:  
Dim MyMeas as Agilent835x.Measurement  
Set MyMeas = app.CreateCustomMeasurementEx (2, "Scalar Mixer/Converter",
"SC21") 'To create a vector mixer measurement in channel 2:  
Dim MyMeas as Agilent835x.Measurement  
Set MyMeas = app.CreateCustomMeasurementEx (2, "Vector Mixer/Converter",
"VC21")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_CreateCustomMeasurementEx (long ChannelNum, BSTR guid, VARIANT
initData, long windowNumber, IMeasurement** ppMeasurement );  
  
#### Interface

| IApplication3  
  
* * *

