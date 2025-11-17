# Sense:IMD Commands

* * *

Controls an IMD or IMDx measurement configuration.

SENSe:IMD: [SWEep:TYPE](IMD.md#SweepType) CSO: | [NDPRoducts](IMD.md#CSONumProducts) | [NORMalized:POWer](IMD.md#CSONormPower) | [OFFSet](IMD.md#csoOffset) CTB | [NCARriers](IMD.md#CTBNumCarriers) | [NORMalized:POWer](IMD.md#CTBNormPower) | [OFFSet](IMD.md#ctbOffset) FREQuency | DFRequency | [[:CW]](IMD.md#DFRCW) | [STARt](IMD.md#DFRStart) | [STOP](IMD.md#DFRStop) | [F1[:CW]](IMD.md#FreqF1) | [F2[:CW]](IMD.md#FreqF2) | FCENter | [[:CW]](IMD.md#FCentCW) | [STARt](IMD.md#FCentStart) | [STOP](IMD.md#FCentStop) | [CENTer](IMD.md#FcentCenter) | [SPAN](IMD.md#FCentSpan) [HOPRoduct?](IMD.md#HOproduct) HOPRoduct | ACTive? IFBWidth | [MAIN](IMD.md#ifbwMain) | [IMTone](IMD.md#ifbwTone) NORMalized | [MODE](IMD.md#NormMode) [PMAP](IMD.md#PMap) | [INPut](IMD.md#pmapIn) | LO1 | LO1:CATalog? | LO2 | LO2:CATalog? | [OUTPut](IMD.md#pmapOut) | RF2 | RF2:CATalog? RECeiver | CONFig | COMBiner | PATH | REFerence |  SORDer | ACTive? TPOWer | [COUPle[:STATe]](IMD.md#TPowCoupState) | [EQUalize:STATe](IMD.md#Equal) | [F1](IMD.md#TPowf1) | [F2](IMD.md#TPowF2) | [F1:START](IMD.md#TpowF1Start) | [F1:STOP](IMD.md#TpowF1Stop) | [F2:START](IMD.md#TpowF2Start) | [F2:STOP](IMD.md#TpowF2Stop) | [LEVel](IMD.md#tpowLev) | [SET](IMD.md#TpowerSet)  
---  
  
Click on a keyword to view the command details.

Blue commands are superseded.

### Other Swept IMD commands

  * [CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine) \- creates a Swept IMD measurement.

  * [Swept IMD Calibration](Corr_IMD.md) \- these are supplemental to the [Guided Cal](CorrGuided.md) commands.

  * Use std channel commands to set [Source](../source.md#attval) and [Receiver Attenuation](Power.md).

  * [SENS:ROLE:DEVice RF2](Role.md#Device) \- use an external source for f2.

See Also

  * Example [Create and Cal an IMD Measurement](../../GPIB_Example_Programs/Create_and_Cal_an_IMD_Measurement.md)

  * [IM Spectrum commands](IMS.md)

  * [Learn about Swept IMD](../../../Applications/Swept_IMD.md)

  * [Learn about Measurement Class](../../../S1_Settings/Measurement_Classes.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:IMD:SWEep:TYPE <char>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the sweep type
for the IMD measurement.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<char> |  Sweep type. Choose from:

  * FCENter \- (Center Frequency) Maintaining a constant tone spacing (DeltaF) and tone powers (P1 and P2), the center frequency (FC) is swept from Start to Stop.
  * DFRequency \- (Delta Frequency) The center frequency (FC) is held constant. The tone spacing is increased from StartDeltaF to StopDeltaF.
  * POWer \- The main tone frequencies are specified as either F1 and F2, or as FC and DeltaF. These frequencies are held constant while the power of each tone is stepped from the Start Power to the Stop Power.
  * CW \- The main tone frequencies (F1 and F2) and power levels (P1 and P2) are held constant. Measurements are taken for the specified Number of Points.
  * SEGMent \- Not available for IMDx. Same as FCenter sweep, except that the center frequencies for the sweep are constructed using the standard [segment sweep commands](Segment.md).
  * LOPower \- All frequencies are fixed while the LO power is swept from Start to Stop power.

For each sweep type, use the commands that follow: FCENTer:

  * [SENS:IMD:FREQ:FCEN:STAR](IMD.md#FCentStart)
  * [SENS:IMD:FREQ:FCEN:STOP](IMD.md#FCentStop)
  * [SENS:IMD:FREQ:FCEN:CEN](IMD.md#FcentCenter)T
  * [SENS:IMD:FREQ:FCEN:SPAN](IMD.md#FCentSpan)
  * [SENS:IMD:FREQ:DFR:[CW]](IMD.md#DFRCW)
  * [SENS:IMD:TPOW:F1](IMD.md#TPowf1)
  * [SENS:IMD:TPOW:F2](IMD.md#TPowF2)

DFRequency

  * [SENS:IMD:FREQ:DFR:STAR](IMD.md#DFRStart)
  * [SENS:IMD:FREQ:DFR:STOP](IMD.md#DFRStop)
  * [SENS:IMD:FREQ:FCEN:[CW]](IMD.md#FCentCW)
  * [SENS:IMD:TPOW:F1](IMD.md#TPowf1)
  * [SENS:IMD:TPOW:F2](IMD.md#TPowF2)

POWer

  * [SENS:IMD:FREQ:F1:[CW]](IMD.md#FreqF1)
  * [SENS:IMD:FREQ:F2:[CW]](IMD.md#FreqF2)
  * [SENS:IMD:FREQ:FCEN:[CW]](IMD.md#FCentCW)
  * [SENS:IMD:FREQ:DFR:[CW]](IMD.md#DFRCW)
  * [SENS:IMD:TPOW:F1:STAR](IMD.md#TpowF1Start)
  * [SENS:IMD:TPOW:F1:STOP](IMD.md#TpowF1Stop)
  * [SENS:IMD:TPOW:F2:STAR](IMD.md#TpowF2Start)
  * [SENS:IMD:TPOW:F2:STOP](IMD.md#TpowF2Stop)

CW

  * [SENS:IMD:FREQ:F1:[CW]](IMD.md#FreqF1)
  * [SENS:IMD:FREQ:F2:[CW]](IMD.md#FreqF2)
  * [SENS:IMD:FREQ:FCEN:[CW]](IMD.md#FCentCW)
  * [SENS:IMD:FREQ:DFR:[CW]](IMD.md#DFRCW)
  * [SENS:IMD:TPOW:F1](IMD.md#TPowf1)
  * [SENS:IMD:TPOW:F2](IMD.md#TPowF2)

SEGMent - Not available for IMDx.

  * [SENS:IMD:FREQ:DFR:[CW]](IMD.md#DFRCW)
  * [SENS:IMD:TPOW:F1](IMD.md#TPowf1)
  * [SENS:IMD:TPOW:F2](IMD.md#TPowF2)
  * Use the standard [segment sweep commands](Segment.md) to set freq start and stop

LOPower - IMDx ONLY

  * [SENS:MIX:LO:POW:STAR](MIXerSCPI.md#LOPowerStart)
  * [SENS:MIX:LO:POW:STOP](MIXerSCPI.md#LOPowerStop)
  * [SENS:IMD:FREQ:F1:[CW]](IMD.md#FreqF1)
  * [SENS:IMD:FREQ:F2:[CW]](IMD.md#FreqF2)
  * [SENS:IMD:FREQ:FCEN:[CW]](IMD.md#FCentCW)
  * [SENS:IMD:FREQ:DFR:[CW]](IMD.md#DFRCW)
  * [SENS:IMD:TPOW:F1](IMD.md#TPowf1)
  * [SENS:IMD:TPOW:F2](IMD.md#TPowF2)

  
Examples |  SENS:IMD:SWEep:TYPE CW sense2:imd:sweep:type power  
Query Syntax |  SENSe<cnum>:IMD:SWEep:TYPE?  
Return Type |  Character  
Default |  FCENTer  
  
* * *

## SENSe<cnum>:IMD:CSO:NDPRoducts <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the N =
number of distortion products value for the calculation of the CSO parameter.
[Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CSO)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Number of distortion products.  
Examples |  SENS:IMD:CSO:NDPR 30 sense2:imd:cso:ndproducts 7  
Query Syntax |  SENSe<cnum>:IMD:CSO:NDPRoducts?  
Return Type |  Numeric  
Default |  40  
  
* * *

## SENSe<cnum>:IMD:CSO:NORMalized:POWer <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the CSO Power
for POWER normalization mode. Valid only with measurement parameters: CSO2Lo
and CSO2Hi and for Normalization Modes dBm and dBmV. [Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CTB)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Power level. The units are determined by [Sens:IMD:Norm:Mode](IMD.md#NormMode), which must be set first.  
Examples |  SENS:IMD:CSO:NORM:POW 0 sense2:imd:cso:normalized:power -5  
Query Syntax |  SENSe<cnum>:IMD:CSO:NORMalized:POWer?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SENSe<cnum>:IMD:CSO:OFFSet <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the offset
that is applied to CSO measurements. Valid only with measurement parameters:
CSO2Lo and CSO2Hi. [Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CSO)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Offset value in dBm  
Examples |  SENS:IMD:CSO:OFFS 3 sense2:imd:cso:offset 7  
Query Syntax |  SENSe<cnum>:IMD:CSO:OFFSet?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SENSe<cnum>:IMD:CTB:NCARriers <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the N = Total
number of carriers value used in the calculation of the XMOD parameter.
[Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CTB)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Number of carriers.  
Examples |  SENS:IMD:CTB:NCAR 10 sense2:imd:ctb:ncarriers 50  
Query Syntax |  SENSe<cnum>:IMD:CTB:NCARriers?  
Return Type |  Numeric  
Default |  40  
  
* * *

## SENSe<cnum>:IMD:CTB:NORMalized:POWer <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the CTB Power.
Valid only with measurement parameters: CTBLo and CTBHi and for Normalization
Modes dBm and dBmV. [Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CTB)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Power level. The units are determined by [Sens:IMD:Norm:Mode](IMD.md#NormMode), which must be set first.  
Examples |  SENS:IMD:CTB:NORM:POW 0 sense2:imd:ctb:normalized:power -5  
Query Syntax |  SENSe<cnum>:IMD:CTB:NORMalized:POWer?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SENSe<cnum>:IMD:CTB:OFFSet <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the offset
that is applied to CTB measurements. Valid only with measurement parameters:
CTB, CTBLo, CTBHi, CTBE, CTBELo, and CTBEHi. [Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CTB)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Offset value in dBm  
Examples |  SENS:IMD:CTB:OFFS 3 sense2:imd:ctb:offset 7  
Query Syntax |  SENSe<cnum>:IMD:CTB:OFFSet?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SENSe<cnum>:IMD:FREQuency:DFRequency[:CW] <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns fixed tone
spacing.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Tone spacing frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:DFR 1e6 sense2:imd:frequency:dfrequency:cw 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:DFRequency[:CW]?  
Return Type |  Numeric  
Default |  1 MHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:DFRequency:STARt <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the starting
main tone separation for sweep type = DFRequency (delta frequency).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Starting tone separation between F1 and F2 in Hz. Both F1 and F2 tones MUST be within the frequency range of the VNA where: F1 (start) = FREQ:FCEN  DFR:Start / 2 F2 (start) = FREQ:FCEN + DFR:Start / 2  
Examples |  SENS:IMD:FREQ:DFR:STAR 1e6 sense2:imd:frequency:dfrequency:start 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:DFRequency:STARt?  
Return Type |  Numeric  
Default |  1 MHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:DFRequency:STOP <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the stopping
main tone separation for sweep type = DFRequency (delta frequency).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Stopping tone separation between F1 and F2 in Hz. Both F1 and F2 tones MUST be within the frequency range of the VNA where: F1 (stop) = FREQ:FCEN  DFR:Stop / 2 F2 (stop) = FREQ:FCEN + DFR:Stop / 2  
Examples |  SENS:IMD:FREQ:DFR:STOP 1e6 sense2:imd:frequency:dfrequency:stop 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:DFRequency:STOP?  
Return Type |  Numeric  
Default |  10 MHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:F1[:CW] <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the frequency
of the F1 tone.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  F1 tone frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:F1 1e9 sense2:imd:frequency:F1:cw 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:F1[:CW]?  
Return Type |  Numeric  
Default |  .9995 GHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:F2[:CW] <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the frequency
of the F2 tone.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  F2 tone frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:F2 1e9 sense2:imd:frequency:F2:cw 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:F2[:CW]?  
Return Type |  Numeric  
Default |  1.0005 GHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:FCENter[:CW] <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the center
frequency of the main tones.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Tone center frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:FCEN 1e9 sense2:imd:frequency:fcenter:cw 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:FCENter[:CW]?  
Return Type |  Numeric  
Default |  1.0 GHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:FCENter:CENTer <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the sweep
center frequency when sweeping the main tones.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Center frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:FCEN:CENT 1e9 sense2:imd:frequency:fcenter:center 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:FCENter:CENTer?  
Return Type |  Numeric  
Default |  13.255 GHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:FCENter:SPAN <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the frequency
span when sweeping the main tones.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Frequency span in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:FCEN:SPAN 1e9 sense2:imd:frequency:fcenter:span 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:FCENter:SPAN?  
Return Type |  Numeric  
Default |  26.489 GHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:FCENter:STARt <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the start
frequency when sweeping the main tones.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Start frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:FCEN:STAR 1e9 sense2:imd:frequency:fcenter:start 2e7  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:FCENter:STARt?  
Return Type |  Numeric  
Default |  10.5 MHz  
  
* * *

## SENSe<cnum>:IMD:FREQuency:FCENter:STOP <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the stop
frequency when sweeping the main tones.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Stop frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
Examples |  SENS:IMD:FREQ:FCEN:STOP 1e9 sense2:imd:frequency:fcenter:stop 2e9  
Query Syntax |  SENSe<cnum>:IMD:FREQuency:FCENter:STOP?  
Return Type |  Numeric  
Default |  26.4995 GHz  
  
* * *

## SENSe:IMD:HOPRoduct?

Applicable Models: N522xB, N524xB (Read-only) Returns the highest order
product that can be measured by SweptIMD.  
---  
Parameters |  None  
Examples |  SENS:IMD:HOPR? 'always returns 9  
Return Type |  Numeric  
Default |  9  
  
* * *

## SENSe<cnum>:IMD:HOPRoduct:ACTive?

(Read-only) Returns the highest order product measured by SweptIMD.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
Examples |  SENS:IMD:HOPR:ACT?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:IFBWidth:MAIN <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the IF
Bandwidth for measurement of the main F1 and F2 tones. [Learn more about
setting IFBW for IMD.](../../../Applications/Swept_IMD.htm#IFBW)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Choose from: 1 | 2 | 3 | 5 | 7 | 10 | 15 | 20 | 30 | 50 | 70 | 100 | 150 | 200 | 300 | 500 | 700 | 1k | 1.5k | 2k | 3k | 5k | 7k | 10k | 15k | 20k | 30k | 50k | 70k | 100k | 150k| 200k | 280k | 360k | 600k If an invalid number is specified, the analyzer will round up to the closest valid number.  
Examples |  SENS:IMD:IFBW:MAIN 280e3 sense2:imd:ifbwidth:main 150K  
Query Syntax |  SENSe<cnum>:IMD:IFBWidth:MAIN?  
Return Type |  Numeric  
Default |  1 kHz  
  
* * *

## SENSe<cnum>:IMD:IFBWidth:IMTone <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the IF
Bandwidth for measurement of the intermodulation products. [Learn more about
setting IFBW for IMD.](../../../Applications/Swept_IMD.htm#IFBW)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Choose from: 1 | 2 | 3 | 5 | 7 | 10 | 15 | 20 | 30 | 50 | 70 | 100 | 150 | 200 | 300 | 500 | 700 | 1k | 1.5k | 2k | 3k | 5k | 7k | 10k | 15k | 20k | 30k | 50k | 70k | 100k | 150k| 200k | 280k | 360k | 600k If an invalid number is specified, the analyzer will round up to the closest valid number.  
Examples |  SENS:IMD:IFBW:IMT 50 sense2:imd:ifbwidth:imtone 200  
Query Syntax |  SENSe<cnum>:IMD:IFBWidth:IMTone?  
Return Type |  Numeric  
Default |  1 kHz  
  
* * *

## SENSe<cnum>:IMD:NORMalized:MODE <char>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the method by
which CTB and CSO calculations are performed.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<char> |  Normalization mode. Choose from: NONE \- the normalized power is not used in calculation NCARrier \- CTB and CSO is corrected by subtracting 10*log(N/2), where

  * N = # of carriers for CTB
  * N = # of distortion products for CSO

DBM \- the composited normalized power for CTB or CSO is treated as a dBm
value DBMV \- the composited normalized power for CTB or CSO is treated as a
dBmV value. Note: Power values are stored using the currently-set units.
Therefore, first set units with this command, then set power values using:
[SENS:IMD:CSO:NORM:POW](IMD.md#CSONormPower) or
[SENS:IMD:CTB:NORM:POW](IMD.md#CTBNormPower)  
Examples |  SENS:IMD:NORM:MODE NCAR sense2:imd:normalized:mode none  
Query Syntax |  SENSe<cnum>:IMD:NORMalized:MODE?  
Return Type |  Character  
Default |  NCARrier  
  
* * *

## SENSe<cnum>:IMD:PMAP <input>,<output>

Applicable Models: N522xB, N524xB (Write-only) Sets the input port and output
port of an IMD or IMDx channel. This setting is necessary only when using the
limited port mapping feature. [Learn
more.](../../../Applications/SweptIMDLimitedPortMapping.htm)  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<input> |  VNA port connected to the DUT Input. Choose from 1 or 3. When input is 3, an external combiner must be used.  
<output> |  VNA port connected to the DUT Output. When input is 1, output must be 2. When input is 3, output must be 4.  
Examples |  SENS:IMD:PMAP 3,4 sense2:imd:pmap 3,4  
Query Syntax |  Not Applicable  
Default |  1,2  
  
* * *

## SENSe<cnum>:IMD:PMAP:INPut?

Applicable Models: N522xB, N524xB (Read-only) Returns the VNA test port to be
connected to the DUT input for an IMD or IMDx channel. Set the VNA port to DUT
mapping using [SENS:IMD:PMAP](IMD.md#PMap)  
---  
Parameters |   
<cnum> |  IMD channel number. If unspecified, value is set to 1.  
Examples |  SENS:IMD:PMAP:INP? sense2:imd:pmap:input?  
Default |  1  
  
* * *

## SENSe<cnum>:IMD:PMAP:LO1 <string>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the source
used as the LO1 tone for a Swept IMDX channel.  
---  
Parameters |   
<cnum> |  IMD channel number. If unspecified, value is set to 1.  
<string> |  Name of source.  
Example |  SENS:IMD:PMAP:LO1 "MyMXG"  
Query Syntax |  SENSe<cnum>:IMD:PMAP:LO1?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:PMAP:LO1:CATalog?

Applicable Models: N522xB, N524xB (Read-only) Returns the available sources
that can be used as the LO1 tone for a Swept IMDX channel.  
---  
Parameters |   
<cnum> |  IMD channel number. If unspecified, value is set to 1.  
Example |  SENS:IMD:PMAP:LO1:CAT?  
Query Syntax |  SENSe<cnum>:IMD:PMAP:LO1:CATalog?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:PMAP:LO2 <string>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the source
used as the LO2 tone for a Swept IMDX channel.  
---  
Parameters |   
<cnum> |  IMD channel number. If unspecified, value is set to 1.  
<string> |  Name of source.  
Example |  SENS:IMD:PMAP:LO2 "MyMXG"  
Query Syntax |  SENSe<cnum>:IMD:PMAP:LO2?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:PMAP:LO2:CATalog?

Applicable Models: N522xB, N524xB (Read-only) Returns the available sources
that can be used as the LO2 tone for a Swept IMDX channel.  
---  
Parameters |   
<cnum> |  IMD channel number. If unspecified, value is set to 1.  
Example |  SENS:IMD:PMAP:LO2:CAT?  
Query Syntax |  SENSe<cnum>:IMD:PMAP:LO2:CATalog?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:PMAP:OUTPut?

Applicable Models: N522xB, N524xB (Read-only) Returns the VNA test port to be
connected to the DUT output for an IMD or IMDx channel. Set the VNA port to
DUT mapping using [SENS:IMD:PMAP](IMD.md#PMap)  
---  
Parameters |   
<cnum> |  IMD channel number. If unspecified, value is set to 1.  
Examples |  SENS:IMD:PMAP:OUTP? sense2:imd:pmap:output?  
Default |  2  
  
* * *

## SENSe<cnum>:IMD:PMAP:RF2 <string>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the source
used as the RF2 tone for a Swept IMD or IMDX channel.  
---  
Parameters |   
<cnum> |  IMD or IMDX channel number. If unspecified, value is set to 1.  
<string> |  Name of source.  
Example |  SENS:IMD:PMAP:RF2 "MyMXG"  
Query Syntax |  SENSe<cnum>:IMD:PMAP:RF2?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:PMAP:RF2:CATalog?

Applicable Models: N522xB, N524xB (Read-only) Returns the available sources
that can be used as the RF2 tone for a Swept IMD or IMDX channel.  
---  
Parameters |   
<cnum> |  IMD or IMDX channel number. If unspecified, value is set to 1.  
Example |  SENS:IMD:PMAP:RF2:CAT?  
Query Syntax |  SENSe<cnum>:IMD:PMAP:RF2:CATalog?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:RECeiver:CONFig:COMBiner:PATH <enum>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the receiver
configuration. The number of reference receivers is set using the
SENSe:IMD:RECeiver:CONFig:REFerence:COUNt command.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<enum> |  Receiver configuration. Choose from: INT \- (default) this configuration is one reference receiver + internal combiner mode. EXT \- this configuration is an external combiner + one reference receiver or two reference receivers. For two reference receivers, each port uses its own reference receiver.  DUT \- this configuration uses two reference receivers for two input tones applied to a combiner inside the DUT. Each port uses its own reference receiver.   
Examples |  SENSe:IMD:RECeiver:CONFig:COMBiner:PATH EXT  
Query Syntax |  SENSe<cnum>:IMD:RECeiver:CONFig:COMBiner:PATH?  
Return Type |  Enumerator  
Default |  INT  
  
* * *

## SENSe<cnum>:IMD:RECeiver:CONFig:REFerence:COUNt <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the number of
receivers to use in the receiver configuration. The receiver configuration is
set using the SENSe:IMD:RECeiver:CONFig:COMBiner:PATH command.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Sets the number of receivers to use in the receiver configuration.  
Examples |  SENSe:IMD:RECeiver:CONFig:COMBiner:PATH EXT SENSe:IMD:RECeiver:CONFig:REFerence:COUNt 2  
Query Syntax |  SENSe<cnum>:IMD:RECeiver:CONFig:REFerence:COUNt?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SENSe<cnum>:IMD:SORDer:ACTive?

Applicable Models: N522xB, N524xB (Read-only) Returns the state of whether or
not 2nd order parameters are measured. A "1" or "ON" indicates 2nd order
parameters are measured.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
Examples |  SENS:IMD:SORD:ACT?  
Return Type |  Boolean  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:IMD:TPOWer:COUPle[:STATe] <bool>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the state of
power coupling for F1 and F2. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<bool> |  Tone power level coupling state. Choose from: ON (or 1) \- F1 and F2 power is coupled. OFF (or 0) \- F1 and F2 power is NOT coupled. Set power levels individually.  
Examples |  SENS:IMD:TPOW:COUP 0 sense2:imd:tpower:couple:state ON  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:COUPle[:STATe]?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## SENSe<cnum>:IMD:TPOWer:EQUalize:STATe <bool> \- Superseded

Applicable Models: N522xB, N524xB (Read-Write) This command is replaced with
[SENS:IMD:TPOW:LEV](IMD.md#tpowLev) Sets and returns the state of Equal Tone
Power setting. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<bool> |  Equal Tone Power state. Choose from: ON (or 1) \- Equalize f1 and f2 power. OFF (or 0) \- Do NOT equalize f1 and f2 power. Use source power cal.  
Examples |  SENS:IMD:TPOW:EQU 0 sense2:imd:tpower:equalize:state ON  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:EQUalize:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SENSe<cnum>:IMD:TPOWer:F1 <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the power
level of the F1 tone. When [SENS:IMD:TPOW:COUP ON](IMD.md#TPowCoupState)
(tone power is coupled), setting either F1 or F2 power sets both. [Learn more
about tone power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Tone power level in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples |  SENS:IMD:TPOW:F1 0 sense2:imd:tpower:F1 -10  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:F1?  
Return Type |  Numeric  
Default |  -24 dBm  
  
* * *

## SENSe<cnum>:IMD:TPOWer:F2 <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the power
level of the F2 tone. When [SENS:IMD:TPOW:COUP ON](IMD.md#TPowCoupState)
(tone power is coupled), setting either F1 or F2 power sets both. [Learn more
about tone power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Tone power level in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples |  SENS:IMD:TPOW:F2 0 sense2:imd:tpower:F2 -10  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:F2?  
Return Type |  Numeric  
Default |  -24 dBm  
  
* * *

## SENSe<cnum>:IMD:TPOWer:F1:STARt <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the start
power level of the F1 tone. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Start power in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples |  SENS:IMD:TPOW:F1:STAR 0 sense2:imd:tpower:F1:start -10  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:F1:STARt?  
Return Type |  Numeric  
Default |  -24 dBm  
  
* * *

## SENSe<cnum>:IMD:TPOWer:F1:STOP <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the stop power
level of the F1 tone. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Stop power in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples |  SENS:IMD:TPOW:F1:STOP 0 sense2:imd:tpower:F1:stop 10  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:F1:STOP?  
Return Type |  Numeric  
Default |  -10 dBm  
  
* * *

## SENSe<cnum>:IMD:TPOWer:F2:STARt <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the start
power level of the F2 tone. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Start power in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples |  SENS:IMD:TPOW:F2:STAR 0 sense2:imd:tpower:F2:start -10  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:F2:STARt?  
Return Type |  Numeric  
Default |  -24 dBm  
  
* * *

## SENSe<cnum>:IMD:TPOWer:F2:STOP <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the stop power
level of the F2 tone. [Learn more about tone
power](../../../Applications/Swept_IMD.htm#PowerTabDiag).  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<num> |  Stop power in dBm. Choose a value between +30 dBm and -30 dBm.  
Examples |  SENS:IMD:TPOW:F2:STOP 0 sense2:imd:tpower:F2:stop 10  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:F2:STOP?  
Return Type |  Numeric  
Default |  -10 dBm  
  
* * *

## SENSe<cnum>:IMD:TPOWer:LEVel <char>

Applicable Models: N522xB, N524xB (Read-Write) This command replaces
SENS:IMD:TPOW:EQU and SENS:IMD:TPOW:SET Sets and returns the tone power
leveling mode.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<char> |  Choose from: NONE \- (Set Input Power) The specified f1 and f2 power levels are set at the DUT input. INPut \- (Set Input Power, receiver leveling) The specified f1 and f2 power levels are set at the DUT input using receiver leveling at the input reference receiver. EQUal \- (Set Input Power, equal tones at output) The specified f1 and f2 power levels are set at the DUT input and a measurement is made at the output. OUTPut \- (Set Output Power, receiver leveling) The specified f1 and f2 power levels are set at the DUT output. [Learn more about these choices](../../../Applications/Swept_IMD.md#PowerTabDiag).  
Examples |  SENS:IMD:TPOW:LEV INP sense2:imd:tpower:level output  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:LEV?  
Return Type |  Character  
Default |  NONE  
  
* * *

## SENSe<cnum>:IMD:TPOWer:SET <char> \- Superseded

Applicable Models: N522xB, N524xB (Read-Write) This command is replaced with
[SENS:IMD:TPOW:LEV](IMD.md#tpowLev) Sets and returns whether tone power is
specified at the DUT input or output.  
---  
Parameters |   
<cnum> |  Channel number of the IMD measurement. If unspecified, value is set to 1.  
<char> |  Choose from: INPUT - Specified power level is set at the DUT input. OUTPUT - Specified power level is set at the DUT output.  
Examples |  SENS:IMD:TPOW:SET INPUT sense2:imd:tpower:set output  
Query Syntax |  SENSe<cnum>:IMD:TPOWer:SET?  
Return Type |  Character  
Default |  INPUT  
  
* * *

