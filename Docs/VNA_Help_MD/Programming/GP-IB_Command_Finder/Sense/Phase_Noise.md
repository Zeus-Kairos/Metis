# Phase Noise Commands

Defines the settings for phase noise measurements. Option S93031xB is required
and applies ONLY to instruments with serial prefix 6021 and above.

SENSe:PN ADJust | CONFigure | FREQuency | CHECk | LIMit | HIGH | LOW | SEARch | [:STATe] | LEVel | THReshold BWIDth | [:RESolution] | RATio FAVerage | FACTor NTYPe RECeiver RESidual | INPut | OUTput SWEep | CARRier | FREQuency | NOISe | MODE  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:PN:ADJust:CONFigure:FREQuency:CHECk <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables check for carrier. This is a narrow band search
that expects the carrier to exist around the user-specified carrier frequency.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<bool> | Choose from: 0 - OFF \- Disable check for carrier. 1 - ON \- Enable check for carrier.  
Examples | SENS:PN:ADJ:CONF:FREQ:CHEC ON sense2:pn:adjust:configure:frequency:check ON  
Query Syntax | SENSe<ch>:PN:ADJust:CONFigure:FREQuency:CHECk?  
Return Type | Boolean  
Default | ON  
  
* * *

## SENSe<ch>:PN:ADJust:CONFigure:FREQuency:LIMit:HIGH <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the high frequency limit to use during a broadband
carrier search. The SENSe:PN:ADJust:CONFigure:FREQuency:SEARch[:STATe] command
enables/disables the carrier search.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<value> | Carrier search high frequency limit.  
Examples | SENS:PN:ADJ:CONF:FREQ:LIM:HIGH 1E9 sense2:pn:adjust:configure:frequency:limit:high 1e9  
Query Syntax | SENSe<ch>:PN:ADJust:CONFigure:FREQuency:LIMit:HIGH?  
Return Type | Numeric  
Default | 1 GHz  
  
* * *

## SENSe<ch>:PN:ADJust:CONFigure:FREQuency:LIMit:LOW <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the low frequency limit to use during a broadband
carrier search. The SENSe:PN:ADJust:CONFigure:FREQuency:SEARch[:STATe] command
enables/disables the carrier search.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<value> | Carrier search low frequency limit.  
Examples | SENS:PN:ADJ:CONF:FREQ:LIM:HIGH 1E6 sense2:pn:adjust:configure:frequency:limit:high 1e6  
Query Syntax | SENSe<ch>:PN:ADJust:CONFigure:FREQuency:LIMit:LOW?  
Return Type | Numeric  
Default | 1 MHz  
  
* * *

## SENSe<ch>:PN:ADJust:CONFigure:FREQuency:SEARch[:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables a broadband carrier search within the range
specified using the SENSe:PN:ADJust:CONFigure:FREQuency:LIMit:LOW and
SENSe:PN:ADJust:CONFigure:FREQuency:LIMit:HIGH commands.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<bool> | Choose from: 0 - OFF \- Disable search. 1 - ON \- Enable search.  
Examples | SENS:PN:ADJ:CONF:FREQ:SEAR ON sense2:pn:adjust:configure:frequency:search:state ON  
Query Syntax | SENSe<ch>:PN:ADJust:CONFigure:FREQuency:SEARch[:STATe]?  
Return Type | Boolean  
Default | ON  
  
* * *

## SENSe<ch>:PN:ADJust:CONFigure:LEVel:THReshold <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the threshold to use during a carrier search.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<value> | Carrier search threshold in dBm.  
Examples | SENS:PN:ADJ:CONF:LEV:THR -20 sense2:pn:adjust:configure:level:threshold -20  
Query Syntax | SENSe<ch>:PN:ADJust:CONFigure:LEVel:THReshold?  
Return Type | Numeric  
Default | -20 dBm  
  
* * *

## SENSe<ch>:PN:BWIDth[:RESolution]:RATio <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the resolution bandwidth ratio, which is the specified
resolution bandwidth percentage of every half decade offset frequency.
Example: Start Offset = 1 kHz Stop Offset = 100 kHz RBW Ratio = 10% 1 kHz - 3
kHz: RBW = 100 Hz (10% of 1 kHz) 3 kHz - 10 kHz: RBW = 300 Hz (10% of 3 kHz)
10 kHz - 30 kHz: RBW = 1 kHz (10% of 10 kHz) 30 kHz - 100 kHz: RBW = 3 kHz (10
% of 30 kHz)  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<value> | Resolution bandwidth ratio in %.  
Examples | SENS:PN:BWID:RAT 10 sense2:pn:bwidth:resolution:ratio 10  
Query Syntax | SENSe<ch>:PN:BWIDth[:RESolution]:RATio?  
Return Type | Numeric  
Default | 10%  
  
* * *

## SENSe<ch>:PN:FAVerage:FACTor <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the FFT average factor number. The average factor is
multiplied by the default average count for each frequency range. The default
average count of the lower frequency range is 1 and at the higher offset
frequency range is a larger count.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<value> | FFT average factor number from 1 to 10,000.  
Examples | SENS:PN:FAV:FACT 10 sense2:pn:faverage:factor 10  
Query Syntax | SENSe<ch>:PN:FAVerage:FACTor?  
Return Type | Numeric  
Default | 1  
  
* * *

## SENSe<ch>:PN:NTYPe <enum>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the noise type to phase or residual noise.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<enum> | (Enumeration) Choose from: PNOise \- Phase noise measurement. RESidual \- Residual (additive) noise measurement.  
Examples | SENS:PN:NTYP PNO sense2:pn:ntype residual  
Query Syntax | SENSe<ch>:PN:NTYPe?  
Return Type | Enumeration  
Default | PNOise  
  
* * *

## SENSe<ch>:PN:RECeiver <rcvr>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the receiver for the phase noise measurement or
receiver ratios for residual phase noise measurements.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<rcvr> | (String) Receiver string. Choose from: a1, a2, a3, a4, b1, b2, b3, b4, b2/a1, b1/a2. Note: The b2/a1 and b1/a2 ratios are for residual phase noise measurements. For example, b2/a1 measures the additive phase noise at b2 relative to a1.  
Examples | SENS:PN:REC "b2"  
sense:pn:receiver "b2"  
Query Syntax | SENSe<ch>:PN:RECeiver?  
Return Type | String  
**Default** | b2  
  
* * *

## SENSe<ch>:PN:RESidual:INPut <dutInput>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns receiver at the DUT input for residual phase noise
measurements.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<dutInput> | (String) Receiver string for DUT input. Choose from: a1, a2, a3, a4, b1, b2, b3, b4.  
Examples | SENS:PN:RES:INP "a1"  
sense:pn:residual:input "a1"  
Query Syntax | SENSe<ch>:PN:RESidual:INPut?  
Return Type | String  
**Default** | a1  
  
* * *

## SENSe<ch>:PN:RESidual:OUTput <dutOutput>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns receiver at the DUT output for residual phase noise
measurements.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<dutOutput> | (String) Receiver string for DUT output. Choose from: a1, a2, a3, a4, b1, b2, b3, b4.  
Examples | SENS:PN:RES:OUT "b2"  
sense:pn:residual:output "b2"  
Query Syntax | SENSe<ch>:PN:RESidual:OUTput?  
Return Type | String  
**Default** | b2  
  
* * *

## SENSe<ch>:PN:SWEep:CARRier:FREQuency <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the carrier frequency.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<value> | Carrier frequency. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../learning_about_gpib/the_rules_and_syntax_of_scpi_commands.md#min) for more information.  
Examples | SENS:PN:SWE:CARR:FREQ 1 GHz sense2:pn:sweep:carrier:frequency max  
Query Syntax | SENSe<ch>:PN:SWEep:CARRier:FREQuency?  
Return Type | Numeric  
Default | 1 GHz  
  
* * *

## SENSe<ch>:PN:SWEep:NOISe:MODE<enum>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the sweep noise mode.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<enum> | (Enumeration) Choose from: FAST \- Fastest measurement speed with lowest accuracy. NORMal \- Between fastest and slowest measurement speed and accuracy. BEST \- Slowest measurement speed with highest accuracy.  
Examples | SENS:PN:SWE:NOIS:MODE NORM sense2:pn:sweep:noise:mode fast  
Query Syntax | SENSe<ch>:PN:SWEep:NOISe:MODE?  
Return Type | Enumeration  
Default | NORMal  
  
* * *

