# Sense:IMS Commands

* * *

Controls IM Spectrum measurement configuration.

SENSe:IMS: [PMAP](IMS.md#pmap) | [INPut](IMS.md#pmapIn) | [OUTPut](IMS.md#pmapOut) [RBW](IMS.md#RBW) RESPonse | [STARt](IMS.md#RecStart) | [STOP](IMS.md#RecStop) | [CENTer](IMS.md#RecCenter) | [SPAN](IMS.md#RecSpan) STIMulus | [DFRequency](IMS.md#StimDFR) | [FCENter](IMS.md#StimFCenter) | [F1FRequency](IMS.md#Stimf1) | [F2FRequency](IMS.md#StimF2) | TOPWer | [F1](IMS.md#TPowrF1) | [F2](IMS.md#tPowerF2) SWEep: | [TYPE](IMS.md#SweepType) | [ORDer](IMS.md#SweepOrder) TPOWer | [COUPle[:STATe]](IMS.md#TPowerCouple) | [EQUal](IMS.md#Equal) | [LEV](IMS.md#tPowerLevel) | [SET](IMS.md#TpowerSet) TRACking | [CHANnel](IMS.md#TrackChan) | [MSENable](IMS.md#TrackMSenable) | [SINDex](IMS.md#TrackSindex) | [STATe](IMS.md#TrackState)  
---  
  
Click on a keyword to view the command details.

See Also

  * [About IM Spectrum measurements](../../../Applications/IMSpectrum.md)

  * [IMD Application](../../../Applications/Swept_IMD.md)

  * [Learn about Measurement Class](../../../S1_Settings/Measurement_Classes.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:IMS:PMAP <input>,<output>

Applicable Models: N522xB, N524xB (Write-only) Sets the input port and output
port of an IMS or IMSx channel. This setting is necessary only when using the
limited port mapping feature. [Learn
more.](../../../Applications/SweptIMDLimitedPortMapping.htm)  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<input> | VNA port connected to the DUT Input. Choose from 1 or 3. When input is 3, an external combiner must be used.  
<output> | VNA port connected to the DUT Output. When input is 1, output must be 2. When input is 3, output must be 4.  
Examples | SENS:IMS:PMAP 3,4 sense2:ims:pmap 3,4  
Query Syntax | Not Applicable  
Default | 1,2  
  
* * *

## SENSe<cnum>:IMS:PMAP:INPut?

Applicable Models: N522xB, N524xB (Read-only) Returns the VNA test port to be
connected to the DUT input for an IMS or IMSx channel. Set the VNA port to DUT
mapping using SENS:IMS:PMAP  
---  
Parameters |   
<cnum> | IMS channel number. If unspecified, value is set to 1.  
Examples | SENS:IMS:PMAP:INP? sense2:ims:pmap:input?  
Default | 1  
  
* * *

## SENSe<cnum>:IMS:PMAP:OUTPut?

Applicable Models: N522xB, N524xB (Read-only) Returns the VNA test port to be
connected to the DUT output for an IMS or IMSx channel. Set the VNA port to
DUT mapping using SENS:IMS:PMAP  
---  
Parameters |   
<cnum> | IMS channel number. If unspecified, value is set to 1.  
Examples | SENS:IMS:PMAP:OUTP? sense2:ims:pmap:output?  
Default | 2  
  
* * *

## SENSe<cnum>:IMS:RBW <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the Resolution
Bandwidth for the IM Spectrum measurement.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Resolution BW in Hz. Choose from: 60k | 100k | 150k | 300k, 600k | 1.0M | 3.0M If an invalid number is specified, the VNA will round up to the closest valid number.  
Examples | SENS:IMS:RBW 600e3 sense2:ims:rbw 1MHz  
Query Syntax | SENSe<cnum>:IMS:RBW?  
Return Type | Numeric  
Default | 600 kHz  
  
* * *

## SENSe<cnum>:IMS:RESPonse:STARt <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the receiver
Start frequency for the IM Spectrum measurement. Valid ONLY when Tracking is
NOT enabled and when Sweep Type = Linear. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Start frequency in Hz. Choose a frequency within the range of the VNA.  
Examples | SENS:IMS:RESP:STAR 1e9 sense2:ims:response:start 100e6  
Query Syntax | SENSe<cnum>:IMS:RESPonse:STARt?  
Return Type | Numeric  
Default | 950 MHz  
  
* * *

## SENSe<cnum>:IMS:RESPonse:STOP <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the receiver
Stop frequency for the IM Spectrum measurement. Valid ONLY when Tracking is
NOT enabled and when Sweep Type = Linear. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Stop frequency in Hz. Choose a frequency within the range of the VNA.  
Examples | SENS:IMS:RESP:STOP 26e9 sense2:ims:response:stop 100e6  
Query Syntax | SENSe<cnum>:IMS:RESPonse:STOP?  
Return Type | Numeric  
Default | 1.05 MHz  
  
* * *

## SENSe<cnum>:IMS:RESPonse:CENTer <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the receiver
Center frequency for the IM Spectrum measurement. Valid ONLY when Tracking is
NOT enabled and when Sweep Type = Linear. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Center frequency in Hz. Choose a frequency within the range of the VNA.  
Examples | SENS:IMS:RESP:CENT 26e9 sense2:ims:response:center 100e6  
Query Syntax | SENSe<cnum>:IMS:RESPonse:CENTer?  
Return Type | Numeric  
Default | 1.0 GHz  
  
* * *

## SENSe<cnum>:IMS:RESPonse:SPAN <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the Span of
receiver frequencies for the IM Spectrum measurement. Valid ONLY when Tracking
is NOT enabled and when Sweep Type = Linear. Otherwise, this setting is
ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Frequency span in Hz. All receiver frequencies should be within the range of the VNA.  
Examples | SENS:IMS:RESP:SPAN 10e9 sense2:ims:response:span 100e6  
Query Syntax | SENSe<cnum>:IMS:RESPonse:SPAN?  
Return Type | Numeric  
Default | 100 MHz  
  
* * *

## SENSe<cnum>:IMS:STIMulus:DFRequency <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the DeltaF
(tone spacing) for the IM Spectrum measurement. Valid ONLY when Tracking is
NOT enabled. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Delta frequency in Hz. All stimulus settings MUST be within the frequency range of the VNA.  
Examples | SENS:IMS:STIM:DFR 1e6 sense2:ims:stimulus:dfrequency 100e6  
Query Syntax | SENSe<cnum>:IMS:STIMulus:DFRequency?  
Return Type | Numeric  
Default | 10 MHz  
  
* * *

## SENSe<cnum>:IMS:STIMulus:FCENter <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the Center
frequency for the IM Spectrum measurement. Valid ONLY when Tracking is NOT
enabled. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Center frequency in Hz. All stimulus settings MUST be within the frequency range of the VNA.  
Examples | SENS:IMS:STIM:FCEN 1e6 sense2:ims:stimulus:fcenter 100e6  
Query Syntax | SENSe<cnum>:IMS:STIMulus:FCENter?  
Return Type | Numeric  
Default | 1.0 GHz  
  
* * *

## SENSe<cnum>:IMS:STIMulus:F1FRequency <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the F1
frequency for the IM Spectrum measurement. Valid ONLY when Tracking is NOT
enabled. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | F1 frequency in Hz. All stimulus settings MUST be within the frequency range of the VNA.  
Examples | SENS:IMS:STIM:F1FR 1e6 sense2:ims:stimulus:f1frequency 100e6  
Query Syntax | SENSe<cnum>:IMS:STIMulus:F1FRequency?  
Return Type | Numeric  
Default | 995 MHz  
  
* * *

## SENSe<cnum>:IMS:STIMulus:F2FRequency <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the F2
frequency for the IM Spectrum measurement. Valid ONLY when Tracking is NOT
enabled. Otherwise, this setting is ignored.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | F2 frequency in Hz. All stimulus settings MUST be within the frequency range of the VNA.  
Examples | SENS:IMS:STIM:F2FR 1e6 sense2:ims:stimulus:f2frequency 100e6  
Query Syntax | SENSe<cnum>:IMS:STIMulus:F2FRequency?  
Return Type | Numeric  
Default | 1.005 MHz  
  
* * *

## SENSe<cnum>:IMS:STIMulus:TPOWer:F1 <value>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the power
level of the F1 tone. When [SENS:IMS:TPOW:COUP ON](IMS.md#TPowerCouple) (tone
power is coupled), setting either F1 or F2 power sets both. This setting is
ignored if [SENS:IMS:TRAC:STAT](IMS.md#TrackState) is enabled.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<value> | F1 tone power level in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples | SENS:IMS:STIM:TPOW:F1 -10 sense2:ims:stimulus:tpower:f1 0  
Query Syntax | SENSe<cnum>:IMS:STIMulus:TPOWer:F1?  
Return Type | Numeric  
Default | -20  
  
* * *

## SENSe<cnum>:IMS:STIMulus:TPOWer:F2 <value>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the power
level of the F2 tone. When [SENS:IMS:TPOW:COUP ON](IMS.md#TPowerCouple) (tone
power is coupled), setting either F1 or F2 power sets both. This setting is
ignored if [SENS:IMS:TRAC:STAT](IMS.md#TrackState) is enabled.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<value> | F2 tone power level in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples | SENS:IMS:STIM:TPOW:F2 -10 sense2:ims:stimulus:tpower:f2 0  
Query Syntax | SENSe<cnum>:IMS:STIMulus:TPOWer:F2?  
Return Type | Numeric  
Default | -20  
  
* * *

## SENSe<cnum>:IMS:SWEep:TYPE <char>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the method in
which the spectrum of signals to view are specified. When Tracking is enabled
the frequency of the main tones (f1 and f2) are always determined by the Swept
IMD channel.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<char> | IM Spectrum sweep type. Choose from:

  * LINear When Tracking is enabled, allows tuning the Response Settings (receiver) to any values within the frequency range of the VNA. When Tracking is NOT enabled also allows setting the Stimulus (sources) to any values within the frequency range or the VNA.
  * SECond The receiver is tuned to view the 2nd order products (f2-f1 and f1+f2) of the main tones that are currently specified in Stimulus Settings. When Tracking is enabled, the main tones are specified in the Swept IMD channel.
  * THIRd The receiver is tuned to view the 3rd order products (2f1 -f2 and 2f2-f1) of the main tones that are currently specified in Stimulus Settings. When Tracking is enabled, the main tones are specified in the Swept IMD channel.
  * NTH The frequency range is set to N * DeltaF. This algorithm will NOT tune the receivers to view the EVEN order products.

  
Examples | SENS:IMS:SWEep:TYPE LIN sense2:ims:sweep:type nth  
Query Syntax | SENSe<cnum>:IMS:SWEep:TYPE?  
Return Type | Character  
Default | NTH  
  
* * *

## SENSe<cnum>:IMS:SWEep:ORDer <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the order
number of signals to view when [SENS:IMS:SWE:TYPE NTH](IMS.md#SweepType) is
specified.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<num> | Order number of IM products to view. The frequency range is set to N (this number) x DeltaF (set with [SENS:IMS:STIM:DFR](IMS.md#StimDFR)).  
Examples | SENS:IMS:SWEep:ORD 5 sense2:ims:sweep:order 12  
Query Syntax | SENSe<cnum>:IMS:SWEep:ORDer?  
Return Type | Numeric  
Default | 9  
  
* * *

## SENSe<cnum>:IMS:TPOWer:COUPle[:STATe] <bool>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the state of
power coupling for F1 and F2.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<bool> | Tone power level coupling. Choose from: ON (or 1) \- F1 and F2 power is coupled. OFF (or 0) \- F1 and F2 power is NOT coupled. Set power levels individually.  
Examples | SENS:IMS:TPOW:COUP 0 sense2:ims:tpower:couple:state ON  
Query Syntax | SENSe<cnum>:IMS:TPOWer:COUPle[:STATe]?  
Return Type | Boolean  
Default | ON  
  
* * *

## SENSe<cnum>:IMS:TPOWer:EQUalize:STATe <bool> \- Superseded

Applicable Models: N522xB, N524xB (Read-Write) This command is replaced with
[SENS:IMS:TPOW:LEV](IMS.md#tPowerLevel) Sets and returns the state of Equal
Tone Power setting. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<bool> | Equal Tone Power state. Choose from: ON (or 1) \- Equalize f1 and f2 power. OFF (or 0) \- Do NOT equalize f1 and f2 power. Use source power cal.  
Examples | SENS:IMS:TPOW:EQU 0 sense2:ims:tpower:equalize:state ON  
Query Syntax | SENSe<cnum>:IMS:TPOWer:EQUalize:STATe?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<cnum>:IMS:TPOWer:LEVel <char>

Applicable Models: N522xB, N524xB (Read-Write) This command replaces
SENS:IMS:TPOW:EQU and SENS:IMS:TPOW:SET Sets and returns the tone power
leveling mode.  
---  
Parameters |   
<cnum> | Channel number of the IMD measurement. If unspecified, value is set to 1.  
<char> | Choose from: NONE \- (Set Input Power) The specified f1 and f2 power levels are set at the DUT input. INPUT \- (Set Input Power, receiver leveling) The specified f1 and f2 power levels are set at the DUT input using receiver leveling at the input reference receiver. EQUAL \- (Set Input Power, equal tones at output) The specified f1 and f2 power levels are set at the DUT input and a measurement is made at the output. OUTPUT \- (Set Output Power, receiver leveling) The specified f1 and f2 power levels are set at the DUT output. [Learn more about these choices](../../../Applications/Swept_IMD.md#PowerTabDiag).  
Examples | SENS:IMS:TPOW:LEV INPUT sense2:ims:tpower:level output  
Query Syntax | SENSe<cnum>:IMS:TPOWer:LEV?  
Return Type | Character  
Default | NONE  
  
* * *

## SENSe<cnum>:IMS:TPOWer:SET <char> \- Superseded

Applicable Models: N522xB, N524xB (Read-Write) This command is replaced with
[SENS:IMS:TPOW:LEV](IMS.md#tPowerLevel) Sets and returns whether tone power
is specified at the DUT input or output.  
---  
Parameters |   
<cnum> | Channel number of the IMSpectrum measurement. If unspecified, value is set to 1.  
<char> | Choose from: INPUT - Specified power level is set at the DUT input. OUTPUT - Specified power level is set at the DUT output.  
Examples | SENS:IMS:TPOW:SET INPUT sense2:ims:tpower:set output  
Query Syntax | SENSe<cnum>:IMS:TPOWer:SET?  
Return Type | Character  
Default | INPUT  
  
* * *

## SENSe<cnum>:IMS:TRACking:CHANnel <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the IMD
channel number to which the IM Spectrum channel is coupled.  
---  
Parameters |   
<cnum> | IMS channel. If unspecified, value is set to 1.  
<num> | Existing IMD channel to which frequency and power settings are coupled.  
Examples | SENS:IMS:TRAC:CHAN 2 sense2:ims:tracking:channel 1  
Query Syntax | SENSe<cnum>:IMS:TRACking:CHANnel?  
Return Type | Numeric  
Default | First IMD channel  
  
* * *

## SENSe<cnum>:IMS:TRACking:MSENable <bool>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the step sweep
mode for the IM Spectrum channel.  
---  
Parameters |   
<cnum> | IMS channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0) - Automatic Step ON (or 1) \- Manual Step  
Examples | SENS:IMS:TRAC:MSEN 1 sense2:ims:tracking:msenable 0  
Query Syntax | SENSe<cnum>:IMS:TRACking:MSENable?  
Return Type | Boolean  
Default | 0 - Automatic  
  
* * *

## SENSe<cnum>:IMS:TRACking:SINDex <num>

Applicable Models: N522xB, N524xB (Read-Write) When [SENS:IMS:TRAC:MSEN =
Manual](IMS.htm#TrackMSenable), sets and returns the data point number at
which a sweep is performed.  
---  
Parameters |   
<cnum> | IMS channel. If unspecified, value is set to 1.  
<num> | Step index. Choose from 1 to the specified number of points.  
Examples | SENS:IMS:TRAC:SINDex 201 sense2:ims:tracking:sindex 1  
Query Syntax | SENSe<cnum>:IMS:TRACking:SINDex?  
Return Type | Numeric  
Default | 1  
  
* * *

## SENSe<cnum>:IMS:TRACking:STATe <bool>

Applicable Models: N522xB, N524xB (Read-Write) When an IMD channel exists,
allows the IM Spectrum frequency and power setting to track (couple with) the
IMD channel settings.  
---  
Parameters |   
<cnum> | IMS channel. If unspecified, value is set to 1.  
<bool> | Tracking state. Choose from: ON (or 1) \- IM Spectrum frequency and power settings track the IMD channel settings. OFF (or 0) \- IM Spectrum frequency and power settings are specified in the IMS channel.  
Examples | SENS:IMS:TRAC:STAT 0 sense2:ims:tracking:state ON  
Query Syntax | SENSe<cnum>:IMS:TRACking:STATe?  
Return Type | Boolean  
Default | OFF  
  
* * *

