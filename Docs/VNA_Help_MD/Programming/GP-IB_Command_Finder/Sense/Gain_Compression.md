# SENSe:GCSetup Commands

* * *

Controls the Gain Compression configuration.

SENSe:GCSetup: [AMODe <enum>](Gain_Compression.md#Amode) COMPression: | [ALGorithm <enum>](Gain_Compression.md#CompAlgorithm) | [BACKoff:LEVel <num>](Gain_Compression.md#backoff) | [DELTa:X <num>](Gain_Compression.md#deltaX) | [DELTa:Y <num>](Gain_Compression.md#deltaY) | INTerpolate | [[:STATe]](Gain_Compression.md#comInterp) | [LEVel <num>](Gain_Compression.md#compLevel) | PHASe | LEVel | MODE | [SATuration:LEVel](Gain_Compression.md#SatLevel) [EOSoperation <string>](Gain_Compression.md#eos) MIXer | REFerence [PMAP](Gain_Compression.md#portMap) | [INPut](Gain_Compression.md#PortIN)? | [OUTPut?](Gain_Compression.md#PortOutput) | SOURce | OVERride POWer: | LINear:INPut:COMPute:APERture | [LINear:INPut:LEVel <num>](Gain_Compression.md#InpPwer) | [REVerse:LEVel <num>](Gain_Compression.md#REVpower) | [STARt:LEVel <num>](Gain_Compression.md#startPower) | [STOP:LEVel <num>](Gain_Compression.md#stopPower) SAFE: | [CPADjustment <num>](Gain_Compression.md#SafeCourse) | DC | MLimit <num> | PARameter <value> | [ENABle <bool>](Gain_Compression.md#SafeEnable) | [FPADjustment <num>](Gain_Compression.md#SafeFine) | [FTHReshold <num>](Gain_Compression.md#safeThresh) | [MLIMit <num>](Gain_Compression.md#SaveMaxPwr) [SFA?](Gain_Compression.md#SFA) SMARt: | CDC | [MITerations <num>](Gain_Compression.md#smartMiter) | [SITerations <bool>](Gain_Compression.md#Siterations) | [STIMe <num>](Gain_Compression.md#Settling) | [TOLerance <num>](Gain_Compression.md#smartToler) SWEep: | [FREQuency:POINts <num>](Gain_Compression.md#FreqPoints) | POWer: | [POINts <num>](Gain_Compression.md#powerPoints) | SMOoth | APERture  
---  
  
Click on a keyword to view the command details.

### See Also

### Other Gain Compression commands

  * [CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine) \- creates a gain compression measurement.

  * [CALC:MEAS:GCMeas:ANAL](../Calculate/MeasureGCMeas.md) \- Gain Compression Analysis settings

  * GCA Calibration uses the [Guided Calibration commands](../../COM_Reference/Objects/GuidedCalibration_Object.md), except for the following:

  *     * [Sens:Corr:GCS:Power](Sense_Correction.md#GCSPower) \- sets power level for Source Power Cal

GCX

  * Setup Mixer using [Sense:Mixer commands](MIXerSCPI.md)

  * Calibrate using [SMC commands](CorrCollGuidSMC.md) and [Guided commands](CorrGuided.md)

  * Example Programs

  *     * [Create and Cal a Gain Compression Measurement](../../GPIB_Example_Programs/Create_and_Cal_a_GCA_Measurement.md)

    * [Create and Cal a GCX Measurement](../../GPIB_Example_Programs/Create_and_Cal_a_GCX_Measurement.md)

  * [Learn about Gain Compression Application](../../../Applications/Gain_Compression_Application.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:GCSetup:AMODe <enum>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the method by which gain compression data is acquired.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<enum> | Choose from:

  * PFREQuency - 2D Power Per Frequency
  * FPOWer - 2D Frequency Per Power
  * SMARtsweep - Smart Sweep

  
Examples | SENS:GCS:AMOD SMAR sense:gcsetup:amode pfrequency  
Query Syntax | SENSe<ch>:GCSetup:AMODe ?  
Return Type | Enumeration  
Default | SMARtsweep  
  
* * *

## SENSe<ch>:GCSetup:COMPression:ALGorithm <enum>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the algorithm method used to compute gain compression.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<enum> | Algorithm method. Choose from:

  * CFLG \- compression from linear gain
  * CFMG \- compression from maximum gain
  * BACKoff \- compression from BackOff
  * XYCOM \- X/Y Compression
  * SAT \- compression from saturation

  
Examples | SENS:GCS:COMP:ALG BACK sense:gcsetup:compression:algorithm XYcom  
Query Syntax | SENSe<ch>:GCSetup:COMPression:ALGorithm?  
Return Type | Enumeration  
Default | CFLG  
  
* * *

## SENSe<ch>:GCSetup:COMPression:BACKoff:LEVel <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
value for the BackOff compression algorithm.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Backoff value in dB. Choose a value between 1 and 99.  
Examples | SENS:GCS:COMP:BACK:LEV 10 sense:gcsetup:compression:backoff:level 5  
Query Syntax | SENSe<ch>:GCSetup:COMPression:BACKoff:LEVel?  
Return Type | Numeric  
Default | 10  
  
* * *

## SENSe<ch>:GCSetup:COMPression:DELTa:X <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the 'X" value in the delta X/Y compression algorithm.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | X value in dB. Choose a value from .01 to 10.  
Examples | SENS:GCS:COMP:DELT:X 9 sense:gcsetup:compression:delta:X 8  
Query Syntax | SENSe<ch>:GCSetup:COMPression:DELTa:X?  
Return Type | Numeric  
Default | 10  
  
* * *

## SENSe<ch>:GCSetup:COMPression:DELTa:Y <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the 'Y" value in the delta X/Y compression algorithm.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Y value in dB. Choose a value from .01 to 10.  
Examples | SENS:GCS:COMP:DELT:Y 9 sense:gcsetup:compression:delta:Y 8  
Query Syntax | SENSe<ch>:GCSetup:COMPression:DELTa:Y?  
Return Type | Numeric  
Default | 9  
  
* * *

## SENSe<ch>:GCSetup:COMPression:INTerpolate[:STATe] <bool>

Applicable Models: All with Gain Compression Option  (Read-Write) Sets whether
or not interpolation should be performed on 2D measured compression data.
Applies ONLY to [2D acquisition modes](Gain_Compression.md#Amode).  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Interpolate the results OFF or (0) Do NOT interpolate the results but return the value closest to compression.  
Examples | SENS:GCS:COMP:INT 1 sense:gcsetup:compression:interpolate off  
Query Syntax | SENSe<ch>:GCSetup:COMPression:INTerpolation?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<ch>:GCSetup:COMPression:LEVel <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the desired gain reduction (from reference gain). This value is used for
Compression from Linear Gain and Compression from Maximum Gain. Use
[SENS:GCS:COMP:ALG CFLG](Gain_Compression.md#CompAlgorithm) to set this
compression algorithm.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Compression level in dB. Choose a value between .01 and 100.  
Examples | SENS:GCS:COMP:LEV 1 sense:gcsetup:compression:level 3  
Query Syntax | SENSe<ch>:GCSetup:COMPression:LEVel?  
Return Type | Numeric  
Default | 1  
  
* * *

## SENSe<ch>:GCSetup:COMPression:PHASe:LEVel <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the desired phase to measure compression. This is only used when
SENSe:GCSetup:COMPression:PHASe:MODE is set to PHASe or BOTH.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Phase level in degrees. Choose a value between .01 and 360.  
Examples | SENS:GCS:COMP:PHAS:LEV 0.01 sense:gcsetup:compression:phase:level 0.01  
Query Syntax | SENSe<ch>:GCSetup:COMPression:PHASe:LEVel?  
Return Type | Numeric  
Default | 2  
  
* * *

## SENSe<ch>:GCSetup:COMPression:PHASe:MODE <enum>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
compression format to be either magnitude, phase, or magnitude and phase. This
option is only available with the 2D type of compression sweeps.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<enum> | Choose from:

  * MAGNitude \- compression against magnitude
  * PHASe \- compression against phase
  * BOTH \- compression against magnitude and phase

  
Examples | SENS:GCS:COMP:PHAS:MODE PHAS sense:gcsetup:compression:phase:mode both  
Query Syntax | SENSe<ch>:GCSetup:COMPression:PHASe:MODE?  
Return Type | Enumeration  
Default | MAGNitude  
  
## SENSe<ch>:GCSetup:COMPression:SATuration:LEVel <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the deviation dB from the maximum Pout. This is the point of saturation. Use
[SENS:GCS:COMP:ALG CFLG](Gain_Compression.md#CompAlgorithm) to set this
compression algorithm.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Saturation level in dB. Choose a value between .01 and 10.  
Examples | SENS:GCS:COMP:SAT:LEV 1 sense:gcsetup:compression:saturation:level 3  
Query Syntax | SENSe<ch>:GCSetup:COMPressionSATuration:LEVel?  
Return Type | Numeric  
Default | .1 dB  
  
* * *

## SENSe<ch>:GCSetup:EOSoperation <enum>

Applicable Models: All with Gain Compression Option  (Read-Write) This setting
is used to protect a sensitive device from too much power during the sweep
retrace. Other instrument settings or channels may over-ride this setting.
[Learn more.](../../../Applications/Gain_Compression_Application.md#End)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<enum> | End Of Sweep operation. Choose from:

  * STANdard Use the default VNA method. [Learn more.](../../../S1_Settings/Power_Level.md#PowerONOFF)
  * POFF Always turn power OFF while waiting.
  * PSTArt Sweep Start power
  * PSTOp Sweep Stop power.

  
Examples | SENS:GCS:EOS PSTA sense:gcsetup:eosoperation standard  
Query Syntax | SENSe<ch>:GCSetup:EOSoperation?  
Return Type | Enumeration  
Default | STANdard  
  
* * *

## SENSe<ch>:GCSetup:MIXer:REFerence <bool>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the state of the mixer reference. This option is only available in Gain
Compression for Converters (GCX), and is only used when
SENSe:GCSetup:COMPression:PHASe:MODE is set to PHASe or BOTH. To improve the
noise of the phase measurements in GCX, an optional user supplied external
reference can be added to the R1 loop. The LO for the reference mixer should
be common with the LO for the DUT mixer. After this hardware is added, and
this command is set to ON, the GCX application will use the reference mixer to
improve the phase measurements.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Enable mixer reference. OFF or (0) Disable mixer reference.  
Examples | SENS:GCS:MIX:REF 1 sense:gcsetup:mixer:reference off  
Query Syntax | SENSe<ch>:GCSetup:MIXer:REFerence?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<ch>:GCSetup:PMAP <in>,<out>

Applicable Models: All with Gain Compression Option  (Write-only) Set the DUT-
to-VNA port mapping for the Gain Compression measurement.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<in> | VNA port which is connected to the DUT input.  
<out> | VNA port which is connected to the DUT output.  
Examples | SENS:GCS:PMAP 1,2 sense:gcsetup:pmap 2,1  
Query Syntax | Not Applicable  
Default | 1,2  
  
* * *

## SENSe<ch>:GCSetup:PMAP:INPut?

Applicable Models: All with Gain Compression Option  (Read-only) Read the VNA
port number to be connected to the DUT Input. Use
[SENS:GCS:PORTMap](Gain_Compression.md#portMap) to set the port mapping.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
Examples | SENS:GCS:PMAP:INP? sense:gcsetup:pmap:input?  
Return Type | Numeric  
Default | 1  
  
* * *

## SENSe<ch>:GCSetup:PMAP:OUTPut?

Applicable Models: All with Gain Compression Option  (Read-only) Read the VNA
port number to be connected to the DUT Output.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
Examples | SENS:GCS:PMAP:OUTP? sense:gcsetup:pmap:output?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 2  
  
* * *

## SENSe<ch>:GCSetup:PMAP:SOURce:OVERride <bool>

Applicable Models: All with Gain Compression Option  (Read-Write) This
function is used when GCX channels with a reference mixer and one GCA channel
without a reference mixer are set up simultaneously and you want to use the
same path configuration for all channels. This remaps the source port to Port
1. This is only used when SENSe:GCSetup:COMPression:PHASe:MODE is set to PHASe
or BOTH.  
---  
Parameters |   
<ch> | Any existing GCA/GCX channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Use same path configuration for all channels. OFF or (0) Do not use the same path configuration for all channels.  
Examples | SENS:GCS:PMAP:SOUR:OVER 1 sense:gcsetup:pmap:source:override off  
Query Syntax | SENSe<ch>:GCSetup:PMAP:SOURce:OVERride?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<ch>:GCSetup:POWer:LINear:INPut:COMPute:APERture <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the aperture to use when computing the linear input power. This is only used
when SENSe:GCSetup:COMPression:PHASe:MODE is set to PHASe or BOTH. In that
mode, the linear input power is computed using a least squares fit of the
linear region. This command sets the width, or aperture, of the linear input
region. The default is 5%.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Input percentage. Choose a value from 0 to 25.  
Examples | SENS:GCS:POW:LIN:INP:COMP:APER 5 sense:gcsetup:power:linear:input:compute:aperture 5  
Query Syntax | SENSe<ch>:GCSetup:POWer:LINear:INPut:COMPute:APERture?  
Return Type | Numeric  
Default | 5  
  
* * *

## SENSe<ch>:GCSetup:POWer:LINear:INPut:LEVel <num>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the input power at which Linear Gain and all S-parameters are measured.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Input power level in dBm. Choose a value from +30 to (-30).  
Examples | SENS:GCS:POW:LIN:INP:LEV 0 sense:gcsetup:power:linear:input:level -10  
Query Syntax | SENSe<ch>:GCSetup:POWer:LINear:INPut:LEVel?  
Return Type | Numeric  
Default | -25 dBm  
  
* * *

## SENSe<ch>:GCSetup:POWer:REVerse:LEVel <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the reverse power level to the DUT. This is applied to the DUT output port
when making reverse measurements like S22.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Reverse power level in dBm. Choose a value from +30 to (-30).  
Examples | SENS:GCS:POW:REV:LEV 0 sense:gcsetup:power:reverse:level -5  
Query Syntax | SENSe<ch>:GCSetup:POWer:REVerse:LEVel?  
Return Type | Numeric  
Default | -5  
  
* * *

## SENSe<ch>:GCSetup:POWer:STARt:LEVel <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the start power level.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Start power level in dBm. Choose a value from +30 to (-30).  
Examples | SENS:GCS:POW:STAR:LEV 0 sense:gcsetup:power:start:level -5  
Query Syntax | SENSe<ch>:GCSetup:POWer:STARt:LEVel?  
Return Type | Numeric  
Default | -25  
  
* * *

## SENSe<ch>:GCSetup:POWer:STOP:LEVel <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the stop power level.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Stop power level in dBm. Choose a value from +30 to (-30).  
Examples | SENS:GCS:POW:STOP:LEV 0 sense:gcsetup:power:stop:level -5  
Query Syntax | SENSe<ch>:GCSetup:POWer:STOP:LEVel?  
Return Type | Numeric  
Default | -5  
  
* * *

## SENSe<ch>:GCSetup:SAFE:CPADjustment <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the Safe Sweep COARSE power adjustment. [Learn
more](../../../Applications/Gain_Compression_Application.htm#Safe).  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Coarse power adjustment setting in dBm. Choose a value between 0 and 6.  
Examples | SENS:GCS:SAFE:CPAD 2 sense:gcsetup:safe:cpadjustment 3.5  
Query Syntax | SENSe<ch>:GCSetup:SAFE:CPADjustment?  
Return Type | Numeric  
Default | 3.0  
  
* * *

## SENSe<ch>:GCSetup:SAFE:DC:MLimit <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the maximum limit of the external DC device.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Maximum DC level.  
Examples | SENS:GCS:SAFE:DC:MLIM -5 sense:gcsetup:safe:dc:mlimit -5  
Query Syntax | SENSe<ch>:GCSetup:SAFE:DC:MLIMit?  
Return Type | Numeric  
Default | -5  
  
* * *

## SENSe<ch>:GCSetup:SAFE:DC:PARameter <value>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the name of the external DC device.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<value> | (String) Name of the external DC device.  
Examples | SENS:GCS:SAFE:DC:PAR "MyDCDevice" sense:gcsetup:safe:dc:parameter "MYDCDevice"  
Query Syntax | SENSe<ch>:GCSetup:SAFE:DC:PARameter?  
Return Type | String  
Default | Not Applicable  
  
* * *

## SENSe<ch>:GCSetup:SAFE:ENABle <bool>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read the (ON | OFF) state of Safe Sweep mode. [Learn more](../../../Applications/Gain_Compression_Application.md#Safe)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | (Boolean) - Safe Sweep state. Choose from: OFF (or 0) \- Disable Safe Sweep ON (or 1) - Enable Safe Sweep  
Examples | SENS:GCS:SAFE:ENAB 0 sense:gcsetup:safe:enable 1  
Query Syntax | SENSe<ch>:GCSetup:SAFE:ENABle?  
Return Type | Boolean  
Default | 0  
  
* * *

## SENSe<ch>:GCSetup:SAFE:FPADjustment <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the Safe Sweep FINE power adjustment. [Learn
more](../../../Applications/Gain_Compression_Application.htm#Safe)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Fine power adjustment setting in dBm. Choose a value between 0 and 3.  
Examples | SENS:GCS:SAFE:FPAD 2 sense:gcsetup:safe:fpadjustment .5  
Query Syntax | SENSe<ch>:GCSetup:SAFE:FPADjustment?  
Return Type | Numeric  
Default | 1.0 dBm  
  
* * *

## SENSe<ch>:GCSetup:SAFE:FTHReshold <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the compression level in which Safe Sweep changes from the COARSE power
adjustment to the FINE power adjustment. [Learn
more](../../../Applications/Gain_Compression_Application.htm#Safe)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Threshold setting in dB. Choose a value between 0 and 3.  
Examples | SENS:GCS:SAFE:FTHR .1 sense:gcsetup:safe:fthreshold .75  
Query Syntax | SENSe<ch>:GCSetup:SAFE:FTHReshold?  
Return Type | Numeric  
Default | 0.5 dB  
  
* * *

## SENSe<ch>:GCSetup:SAFE:MLimit <num>

Applicable Models: All with Gain Compression Option (Read-Write) When the VNA
port that is connected to the DUT Output measures this value, the input power
to the DUT is no longer incremented at that frequency. Safe Mode must be
enabled with [SENS:GCS:SAFE:ENAB ON](Gain_Compression.md#SafeEnable) [Learn
more](../../../Applications/Gain_Compression_Application.htm#Safe)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Maximum power limit in dBm. Choose a value from -100 to +100  
Examples | SENS:GCS:SAFE:MLIM 20 sense:gcsetup:safe:mlimit 30  
Query Syntax | SENSe<ch>:GCSetup:SAFE:MLIMit?  
Return Type | Numeric  
Default | 30  
  
* * *

## SENSe<ch>:GCSetup:SFAilures?

Applicable Models: All with Gain Compression Option (Read-only) Returns a
comma-separated list of the frequency indexes that were out of tolerance for
SMART Sweep mode, or at the power limit for 2D acquisition modes. Zero (0) is
the first frequency data point.  Must be Single triggered. Invalid results
occur if the GCA channel is continuously sweeping.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
Examples | SENS:GCS:SFA? sense:gcsetup:sfailures?  
Return Type | Comma-separated list of frequency indexes.  
Default | Not Applicable  
  
* * *

## SENSe<ch>:GCSetup:SMARt:CDC <bool>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the DC readings at the compression point in the last iteration of a smart
sweep. Taking only these DC readings improves measurement speed.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Enable reading DC value at compression point in the last iteration of a smart sweep. OFF or (0) Disable reading DC value at compression point in the last iteration of a smart sweep.  
Examples | SENS:GCS:SMAR:CDC 1 sense:gcsetup:smart:cdc off  
Query Syntax | SENSe<ch>:GCSetup:SMARt:CDC?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<ch>:GCSetup:SMARt:MITerations <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the maximum permitted number of iterations which SMART Sweep may utilize to
find the desired compression level, to within the specified tolerance.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Maximum number of iterations. Choose a value between 1 and 500  
Examples | SENS:GCS:SMAR:MIT 5 sense:gcsetup:smart:miterations 3  
Query Syntax | SENSe<ch>:GCSetup:SMARt:MITerations?  
Return Type | Numeric  
Default | 20  
  
* * *

## SENSe<ch>:GCSetup:SMARt:SITerations <bool>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
enable for showing intermediate results for each iteration of SMART Sweep  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Compression traces are updated after each iteration. OFF or (0) Compression traces are updated after ALL iterations are complete.  
Examples | SENS:GCS:SMAR:SIT 1 sense:gcsetup:smart:siterations off  
Query Syntax | SENSe<ch>:GCSetup:SMARt:SITerations?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<ch>:GCSetup:SMARt:STIMe <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the amount of time SMART Sweep will dwell at the first point where the input
power changes by the Backoff or X level. Applies only to SMART Sweep when
Backoff or XY compression methods are selected. [Learn
more.](../../../Applications/Gain_Compression_Application.htm#SmartBO)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Settling time in seconds. Choose any positive value.  
Examples | SENS:GCS:SMAR:STIM 1 sense:gcsetup:smart:stime .1  
Query Syntax | SENSe<ch>:GCSetup:SMARt:STIMe?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<ch>:GCSetup:SMARt:TOLerance <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the acceptable range SMART Sweep will allow for the measured compression
level.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Tolerance level in dBm. Choose a value between .01 and 10  
Examples | SENS:GCS:SMAR:TOL .1 sense:gcsetup:smart:tolerance .05  
Query Syntax | SENSe<ch>:GCSetup:SMARt:TOLerance?  
Return Type | Numeric  
Default | .05  
  
* * *

## SENSe<ch>:GCSetup:SWEep:FREQuency:POINts <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the number of data points in each frequency sweep. [Learn
more](../../../Applications/Gain_Compression_Application.htm#FreqTabDiag)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Frequency points. Do not exceed the max number of data points. [See Data Points Limit](../../../Applications/Gain_Compression_Application.md#PointsLimit)  
Examples | SENS:GCS:SWE:FREQ:POIN 201 sense:gcsetup:sweep:frequency:points 101  
Query Syntax | SENSe<ch>:GCSetup:SWEep:FREQuency:POINts?  
Return Type | Numeric  
Default | 201  
  
* * *

## SENSe<ch>:GCSetup:SWEep:POWer:POINts <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the number of data points in each power sweep. Applies ONLY to 2D [acquisition
modes.](../../../Applications/Gain_Compression_Application.htm#Acquisition)  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Power points. Do not exceed the max number of data points. [See Data Points Limit](../../../Applications/Gain_Compression_Application.md#PointsLimit)  
Examples | SENS:GCS:SWE:POW:POIN 50 sense:gcsetup:sweep:power:points 21  
Query Syntax | SENSe<ch>:GCSetup:SWEep:POWer:POINts?  
Return Type | Numeric  
Default | 21  
  
* * *

## SENSe<ch>:GCSetup:SWEep:POWer:SMOoth <bool>

Applicable Models: All with Gain Compression Option  (Read-Write) Set and read
the state of the power smoothing. This is only available in Gain Compression
for Converters (GCX). This is only used when
SENSe:GCSetup:COMPression:PHASe:MODE is set to PHASe or BOTH. This enables an
optional smoothing procedure of the power sweep.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Enable power smoothing. OFF or (0) Disable power smoothing.  
Examples | SENS:GCS:SWE:POW:SMO 1 sense:gcsetup:sweep:power:smooth off  
Query Syntax | SENSe<ch>:GCSetup:SWEep:POWer:SMOoth?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<ch>:GCSetup:SWEep:POWer:SMOoth:APERture <num>

Applicable Models: All with Gain Compression Option (Read-Write) Set and read
the power smoothing aperture in percent. This is only available in Gain
Compression for Converters (GCX). This is only used when
SENSe:GCSetup:COMPression:PHASe:MODE is set to PHASe or BOTH. It is only
applied when smoothing has been enabled. This SCPI command configures the
smoothing aperture used. The default is 25%.  
---  
Parameters |   
<ch> | Any existing GCA channel. If unspecified, value is set to 1.  
<num> | Power smoothing aperture.  
Examples | SENS:GCS:SWE:POW:SMO:APER 10 sense:gcsetup:sweep:power:smooth:aperture 10  
Query Syntax | SENSe<ch>:GCSetup:SWEep:POWer:SMOoth:APERture?  
Return Type | Numeric  
Default | 25  
  
* * *

  

