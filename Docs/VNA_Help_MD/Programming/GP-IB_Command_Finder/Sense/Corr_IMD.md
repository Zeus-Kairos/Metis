# Sense:Correction:IMD Commands

* * *

Controls an IMD and IMDx calibration. These commands supplement the [Guided
Cal commands](CorrGuided.htm).

SENSe:CORRection:IMD | CALibration | [FREQuencies](Corr_IMD.md#calFreq) | [METHod](Corr_IMD.md#calMethod) | LO | [PCAL](Corr_IMD.md#LOCal) | [MPRoduct](Corr_IMD.md#Mproduct) | [POWer](Corr_IMD.md#Power) | SENSor | [CKIT](Corr_IMD.md#sensCKIT) | [CONNector](Corr_IMD.md#sensCONN) | [SORDer:INCLude](Corr_IMD.md#SordInclude)  
---  
  
Click on a keyword to view the command details.

### Other IMD (Opt S93087A/B) commands

  * [CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine) \- creates an IMD measurement.

  * [Swept IMD](IMD.md)

  * [IMSpectrum](IMS.md)

See Also

  * Example \- [Create and Cal an IMD measurement](../../GPIB_Example_Programs/Create_and_Cal_an_IMD_Measurement.md)

  * [Learn about IMD Calibration](../../../Applications/Swept_IMD.md#CalOverview)

  * [Learn about Measurement Class](../../../S1_Settings/Measurement_Classes.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:CORRection:IMD:CALibration:FREQuencies <char>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the
frequencies at which an IMD source power cal is performed.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<char> | Choose from: CENTer \- Perform source power calibration at only the center frequencies, midway between the main tones. ALL \- Perform source power calibration at all main tone frequencies.  
Examples | SENS:CORR:IMD:CAL:FREQ ALL sense2:correction:imd:calibration:frequencies center  
Query Syntax | SENSe<cnum>:CORRection:IMD:CALibration:FREQuencies?  
Return Type | Character  
Default | CENTer  
  
* * *

## SENSe<cnum>:CORRection:IMD:CALibration:METHod <char>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the method by
which the match-correction portion of an IMD calibration is performed. [Learn
more.](../../../Applications/Swept_IMD.htm#CalSelectTones)  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<char> | Choose from: MATCh \- Performs a full 2-port cal for full match-correction. RESPonse \- Performs only a response (normalization) cal instead of a full 2-port cal.  
Examples | SENS:CORR:IMD:CAL:METH MATC sense2:correction:imd:calibration:method response  
Query Syntax | SENSe<cnum>:CORRection:IMD:CALibration:METHod?  
Return Type | Character  
Default | MATCh  
  
* * *

## SENSe<cnum>:CORRection:IMD:LO<n>:PCAL[:STATe] <bool>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns whether or not
the LO power cal step is included in the cal steps when an IMDX cal is
performed. [Learn more.](../../../Applications/Swept_IMD.md#CalSelectTones)  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | LO Stage. Choose 1.  
<char> | LO Power Cal state. Choose from: O or OFF \- Skips over the LO Power Cal when calibrating. 1 or ON \- Includes a step for LO Power Cal when calibrating  
Examples | SENS:CORR:IMD:LO1:PCAL 0 sense2:correction:imd:lo1:pcal:state on  
Query Syntax | SENSe<cnum>:CORRection:IMD:LO<n>:PCAL[:STATe]?  
Return Type | Boolean  
Default | 0 or OFF  
  
* * *

## SENSe<cnum>:CORRection:IMD:MPRoduct <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the maximum
intermod product frequencies to be calibrated. All lower product frequencies
are also calibrated.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<char> | Maximum IM products to calibrate. Choose from: 2 \- second order products 3 \- third order products 5 \- fifth order products 7 \- seventh order products 9 \- ninth order products  
Examples | SENS:CORR:IMD:MPR 5 sense2:correction:imd:mproduct 9  
Query Syntax | SENSe<cnum>::CORRection:IMD:MPRoduct?  
Return Type | Numeric  
Default | 3  
  
* * *

## SENSe<cnum>:CORRection:IMD:POWer <num>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the power
level at which to perform the source power calibration using a power sensor.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<num> | Power level. Choose a value between the min and max power level of the VNA.  
Examples | SENS:CORR:IMD:POW -5 sense2:correction:imd:power 5  
Query Syntax | SENSe<cnum>::CORRection:IMD:POWer?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:CORRection:IMD:SENSor:CKIT <string>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the cal kit to
be used for calibrating at the port 1 reference plane when the power sensor
connector is different from the DUT port 1. This effectively removes the
effects of an adapter that is used to connect the power sensor.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<string> | Cal Kit enclosed in quotes. First set the DUT connector for port 1 and the connector of the power sensor. Then use [SENS:CORR:COLL:GUID:CKIT:PORT1:CAT?](CorrGuided.md#gKitCat) to return a list of valid cal kits.  
Examples | SENS:CORR:IMD:SENS:CKIT "85052B"  
Query Syntax | SENSe<cnum>::CORRection:IMD:SENSor:CKIT?  
Return Type | String  
Default | Depends on the specified connectors  
  
* * *

## SENSe<cnum>:CORRection:IMD:SENSor:CONNector <string>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns the power
sensor connector type which is used to perform the Source Power Cal portion of
an IMD calibration.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<string> | Power sensor connector type. Use [SENS:CORR:COLL:GUID:CONN:CAT?](CorrGuided.md#gConnCat) to return a list of valid connector types. Select "Ignored" to NOT compensate for the adapter.  
Examples | SENS:CORR:IMD:SENS:CONN "APC 3.5 male" sense2:correction:imd:sensor:connector "Ignored"  
Query Syntax | SENSe<cnum>::CORRection:IMD:SENSor:CONNector?  
Return Type | String  
Default | "Ignored"  
  
* * *

## SENSe<cnum>:CORRection:IMD:SORDer:INCLude <bool>

Applicable Models: N522xB, N524xB (Read-Write) Sets and returns whether to
include the second order products in the calibration. These frequencies of
these products can be far from the main tones.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<bool> | Choose from: ON (or 1) \- Include 2nd order products OFF (or 0) \- Do NOT include 2nd order products  
Examples | SENS:CORR:IMD:SORD:INCL ON  
Query Syntax | SENSe<cnum>::CORRection:IMD:SORDer:INCLude?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

