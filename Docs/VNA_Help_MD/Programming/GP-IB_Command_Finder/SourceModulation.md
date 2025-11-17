# Source Modulation Commands

* * *

These commands control an external source to set up and calibrate I/Q
modulation.

SOURce: CORRection | SELect MODulation | ARB | CLOCk:SRATe | DATA:I | DATA:Q | AUTO | ACPR | GBANd | [:STATe] | IMMediate | NPR | GBANd | [:STATe] | SA | [:STATe] | CORRection | COLLection | ACP | ENABle | ITERations | LOWer | ENABle | GBANd | ITERations | RECeiver | SPAN | TOLerance | RECeiver | SPAN | TOLerance | UPPer | ENABle | GBANd | ITERations | RECeiver | SPAN | TOLerance | ACQuire | DETails? | STATus? | APPend | DISTortion | ENABle | ITERations | RECeiver | SPAN | TOLerance | EQUalization | ENABle | ITERations | RECeiver | SPAN | TOLerance | FAST | ENABle | FLATness | ENABle | ITERations | RECeiver | SPAN | TOLerance | FREQuency | [:FIXed] | POINts | STARt | STOP | TYPE | LO | FTHRu | ENABle | ITERations | RECeiver | SPAN | TOLerance | NOTch | ENABle | ITERations | RECeiver | SPAN | TOLerance | POWer | ENABle | [:FIXed] | ITERations | POINts | RECeiver | SPAN | STARt | STOP | TOLerance | TYPE | UPDate | ENABle | [:STATe] | FILE? | FILE | CORRection | CATalog? | DELete | FREQuency? | POWer? | INITialize | LOAD | SAVE | SIGNal | CARRier | OFFSet | COMPact | FILE | NUMBer | SELect | OFILe | SRATe | PAVG? | CALCulated? | PRIority | SUBCarrier | NUMBer | OFFSet | SPAN | TIME | STARt | CALCulated? | PRIority | DAC | SCALing | DIGital | CARRier:NUMBer | CARRier:SPACing:CALCulated | CARRier:SPACing | CFILe | FILTer:ALPHa | FILTer:TYPE | FORMat | QUADrature:ERRor | RANDom:SEED | SYMBol:NUMBer:CALCulated | SYMBol:NUMBer | SYMBol:RATE:CALCulated | SYMBol:RATE | NPR | NOTCh | LOCation | NUMBer | OFFSet | SPAN | OPTimize | BURSt:PREServe:ENABle | ENABle | FILTer | ENABle | TAPS | FREQuency | LIMit | DDIGits | ENABle | TOLerance | HREJect | MAX | TONE | SPACing | MIN | TONE | NUMBer | WAVeform | PERiod | NYQReject | ENABle | TYPE | PAVG | CALCulated? | PHASe | FIXed | RANDom | SEED | TYPE | SPAN | CALCulated? | PRIority | SRATe | AUTO | CALCulated? | TONE | NUMBer | CALCulated? | PRIority | ROUNd | SPACing | CALCulated? | PRIority | TONE | ALL | [:STATe] | COUNt? | FREQuency? | LOAD | PHASe | POWer | SAVE | [:STATe] | TYPE | LOAD | SAVE | [STATe]  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

  * [Remotely Specifying a Source Port](../Remotely_Specifying_a_Source_Port.md)

* * *

## SOURce<cnum>:CORRection<Port>:SELect<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B. (Read-Write) Sets and
reads the source correction type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: OFF - Do not include power or modulation calibration in source correction MODulation - Include modulation calibration in source correction. This includes the LO Feedthru correction. POWer - Include the power calibration in the source correction MODPwr - Include power and modulation calibration in source correction. This includes the LO Feedthru correction.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:CORR:SEL MOD  
Query Syntax |  SOURce<cnum>:CORRection<port>:SELect? [srcPort]  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:ARB:CLOCk:SRATe <value> [,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Sets and reads
the sample clock rate of the arbitrary waveform generator.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1. To make settings for ports that are not simple numbers, use the [srcPort] argument.  
<value> |  Clock frequency in units of Hertz (Hz-MHz).  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:ARB:CLOC:SRAT 1E8  
source2:modulation:arb:clock:srate 1E8  
Query Syntax |  SOURce<cnum>:MODulation<port>:ARB:CLOCk:SRATe? [srcPort]  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:ARB:DATA:I <propName> [,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Sets and reads
the I data for I/Q modulation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1. To make settings for ports that are not simple numbers, use the [srcPort] argument.  
<propName> |  Array for I data  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Query Syntax |  SOURce<cnum>:MODulation<port>:DARB:DATA:I? [srcPort]  
Return Type |  Array  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:ARB:DATA:Q <propName> [,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Sets and reads
the Q data for I/Q modulation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1. To make settings for ports that are not simple numbers, use the [srcPort] argument.  
<propName> |  Array for Q data  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Query Syntax |  SOURce<cnum>:MODulation<port>:DARB:DATA:Q? [srcPort]  
Return Type |  Array  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:AUTO:ACPR:GBANd <num>[,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Sets and reads
the guard band between the end of the modulation signal and where ACPR is
measured (SA channel only).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Guard band for ACP measurement.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:AUTO:ACPR:GBAN 0 Hz  
source2:modulation:auto:acpr:gband 0 Hz  
Query Syntax |  SOURce<cnum>:MODulation<port>:AUTO:ACPR:GBANd?  
Return Type |  Numeric  
**Default** |  0 Hz  
  
* * *

## SOURce<cnum>:MODulation<port>:AUTO:ACPR[:STATe] <bool>[,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Enable or
disable Autoset ACPR markers (SA channel only).  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable ACPR markers. **1 - ON** \- Enable ACPR markers.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:AUTO:ACPR:STAT 1 source:modulation:auto:acpr:state on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:AUTO:ACPR[:STATe]?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:AUTO:IMMediate [,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Write-only) Adjusts
frequencies and markers immediately if modulation settings are changed (SA
channel only). This command depends on the status of the SA, NPR, and ACPR
autoset booleans.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:AUTO:IMM  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:AUTO:NPR:GBANd <num>[,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Sets and reads
the guard band on each side of the notch in an NPR measurement (SA channel
only).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Guard band for NPR measurement.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:AUTO:NPR:GBAN 0 Hz  
source2:modulation:auto:npr:gband 0 Hz  
Query Syntax |  SOURce<cnum>:MODulation<port>:AUTO:NPR:GBANd?  
Return Type |  Numeric  
**Default** |  0 Hz  
  
* * *

## SOURce<cnum>:MODulation<port>:AUTO:NPR[:STATe] <bool>[,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Enable or
disable Autoset NPR markers (SA channel only).  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable NPR markers. **1 - ON** \- Enable NPR markers.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:AUTO:NPR:STAT 1 source:modulation:auto:npr:state on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:AUTO:NPR[:STATe]?  
**Return Type** |  Boolean  
**Default** |  ON  
  
* * *

## SOURce<cnum>:MODulation<port>:AUTO:SA[:STATe] <bool>[,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Enable or
disable automatic updating of SA sweep settings and coherence settings if the
modulation settings are changed (SA channel only).  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable automatic updating. **1 - ON** \- Enable automatic updating.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:AUTO:SA:STAT 1 source:modulation:auto:sa:state on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:AUTO:SA[:STATe]?  
**Return Type** |  Boolean  
**Default** |  ON  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:ENABle
<bool>[,srcPort]

Applicable Models: All with S93070xB or S9x070A/B (Read-Write) Set and read
the ACP modulation calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable ACP calibration. **1 - ON** \- Enable ACP calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:ACP:ENAB 1 source2:modulation:correction:collection:acp:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:ITER 2  
source2:modulation:correction:collection:acp:iterations 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:ITERations?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  2  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Enables or disables the lower ACP (ACPLo)
modulation calibration. ![](../../assets/images/ModDistortion_CenterFreq.png)  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable lower ACP calibration. **1 - ON** \- Enable lower ACP calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:ACP:LOW:ENAB 1 source2:modulation:correction:collection:acp:lower:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:GBANd
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the ACP lower frequency
delta from the edge of the carrier to the beginning of the calibration span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Guard band for lower ACP.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:LOW:GBAN 0 Hz  
source2:modulation:correction:collection:acp:lower:gband 0 Hz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:GBANd?  
Return Type |  Numeric  
**Default** |  0 Hz  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:LOW:ITER 2  
source2:modulation:correction:collection:acp:lower:iterations 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:ITERations?  
Return Type |  Numeric  
**Default** |  2  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the receiver for the lower
ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:LOW:REC "R1"  
source2:modulation:correction:collection:acp:lower:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:RECeiver?  
Return Type |  String  
**Default** |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the calibration span for a
lower ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span for lower ACP.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:LOW:SPAN 100 MHz  
source2:modulation:correction:collection:acp:lower:span 100 MHz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:SPAN?  
Return Type |  Numeric  
**Default** |  Signal Span  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the desired ACP calibration
tolerance for the lower ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:LOW:TOL -40dBc  
source2:modulation:correction:collection:acp:lower:tolerance -40dBc  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:LOWer:TOLerance?  
Return Type |  Numeric  
**Default** |  -40  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for the ACP
modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:REC "R1"  
source2:modulation:correction:collection:acp:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:RECeiver?  
Return Type |  String  
**Default** |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for an
ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:SPAN 100 MHz  
source2:modulation:correction:collection:acp:span 100 MHz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:SPAN?  
Return Type |  Numeric  
**Default** |  Signal Span  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired ACP calibration
tolerance for the ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:TOL -40dBc  
source2:modulation:correction:collection:acp:tolerance -40dBc  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:TOLerance?  
Return Type |  Numeric  
**Default** |  -40  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enables or disables the upper ACP (ACPUp)
modulation calibration. ![](../../assets/images/ModDistortion_CenterFreq.png)  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable upper ACP calibration. **1 - ON** \- Enable upper ACP calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:ACP:UPP:ENAB 1 source2:modulation:correction:collection:acp:upper:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:GBANd
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the ACP upper frequency delta
from the edge of the carrier to the beginning of the calibration span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Guard band for upper ACP.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:UPP:GBAN 0 Hz  
source2:modulation:correction:collection:acp:upper:gband 0 Hz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:GBANd?  
Return Type |  Numeric  
**Default** |  0 Hz  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:UPP:ITER 2  
source2:modulation:correction:collection:acp:upper:iterations 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:ITERations?  
Return Type |  Numeric  
**Default** |  2  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for the upper
ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:UPP:REC "R1"  
source2:modulation:correction:collection:acp:upper:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:RECeiver?  
Return Type |  String  
**Default** |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for an
upper ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span for upper ACP.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:UPP:SPAN 100 MHz  
source2:modulation:correction:collection:acp:upper:span 100 Mhz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:SPAN?  
Return Type |  Numeric  
Default |  Signal Span  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:TOLerance
<num>[,srcPort]

Applicable Models:All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired ACP calibration
tolerance for the upper ACP modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:ACP:UPP:TOL -40dBc  
source2:modulation:correction:collection:acp:upper:tolerance -40dBc  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACP:UPPer:TOLerance?  
Return Type |  Numeric  
Default |  -40  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACQuire
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Sets the collection acquire.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: SYNChronous ASYNchronous  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:CORR:COLL:ACQ SYNC  
Query Syntax |  Not applicable  
Default |  SYNChronous  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACQuire:DETails?
[,srcPort]

Applicable Models: N522xB, N523xB, N524xB, All with S9x070A/B (Read-only)
Returns the detailed messages generated by modulation correction.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:CORR:COLL:ACQ:DET? "Calibration frequency and power: 1.500000 GHz, -10.000000 dBm at a1 \-------------------------------------------------------------------------------- Calibrating: Power Cal Iteration #1... Power error = -3.395dB Calibrating: Power Cal Iteration #2... Power error = 0.032dB, Succeeded Calibrating: Equalization Iteration #1... Equalization error = 0.331dB Calibrating: Equalization Iteration #2... Equalization error = 0.019dB, Succeeded Calibrating: Measuring corrected modulation... \---------------------------------------------------------------------------------------------------- Calibration finished. Summary: \- Power Cal succeeded \- Equalization succeeded \---------------------------------------------------------------------------------------------------- "  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:ACQuire:STATus?
[,srcPort]

Applicable Models: N522xB, N523xB, N524xB, All with S9x070A/B (Read-only)
Returns a message indicating if the calibration was successful or not.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:CORR:COLL:ACQ:STAT? "Calibration succeeded."  
Return Type |  Comma-separated list of strings.  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:APPend <bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enable appending source modulation
calibration data to the stored *.mdx file. If disabled, old calibration data
in the *.mdx file will be overwritten.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** \- Disable appending calibration data. Old calibration data in the *.mdx file will be overwritten. **1 - ON** \- Enable appending calibration data.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD6:LOAD 'D:\ModulationFile\npr.csv' ... SOUR:MOD6:CORR:COLL:APP 1 SOUR:MOD6:CORR:COLL:ACQ  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:APPend?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enable or disable the distortion calibration
state. The distortion calibration minimizes the vector error of the modulation
signal over the Cal Span.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable distortion calibration. **1 - ON** \- Enable distortion calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:DIST:ENAB 1 source2:modulation:correction:collection:distortion:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
distortion correction iterations used by the calibration routine. The
calibration routine uses successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of distortion correction iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:DIST:ITER 3  
source2:modulation:correction:collection:distortion:iterations 3  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:ITERations?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for distortion
calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:DIST:REC "R1"  
source2:modulation:correction:collection:distortion:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:RECeiver?  
Return Type |  String  
Default |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for a
distortion calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:DIST:SPAN 1.5GHz  
source2:modulation:correction:collection:distortion:span 1.5ghz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:SPAN?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired distortion
calibration tolerance.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Desired tolerance is the un-equalized EVM in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:DIST:TOL -50 dBc  
source2:modulation:correction:collection:distortion:tolerance -50 dBc  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:DISTortion:TOLerance?  
Return Type |  Numeric  
Default |  -40  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enable or disable the equalization
calibration state. Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:FLATness:ENABle command.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable equalization calibration. **1 - ON** \- Enable equalization calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:EQU:ENAB 1 source2:modulation:correction:collection:equalization:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:FLATness:ITERations command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:EQU:ITER 3  
source2:modulation:correction:collection:equalization:iterations 3  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:ITERations?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for equalization
calibration.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:FLATness:RECeiver command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:EQU:REC "R1"  
source2:modulation:correction:collection:equalization:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:RECeiver?  
Return Type |  String  
Default |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for a
equalization calibration.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:FLATness:SPAN command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:EQU:SPAN 1.5GHz  
source2:modulation:correction:collection:equalization:span 1.5ghz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:SPAN?  
Return Type |  Numeric  
Default |  Signal Span  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired equalization
calibration tolerance.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:FLATness:TOLerance command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration equalization tolerance in dB-pk.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:EQU:TOL 0.100  
source2:modulation:correction:collection:equalization:tolerance 0.100  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:EQUalization:TOLerance?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FAST:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enable or disable a fast calibration with
reduced accuracy.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable fast calibration. **1 - ON** \- Enable fast calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:FAST:ENAB 1 source2:modulation:correction:collection:fast:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FAST:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enable or disable the flatness calibration
state. Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:EQUalization:ENABle command.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable flatness calibration. **1 - ON** \- Enable flatness calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:FLAT:ENAB 1 source2:modulation:correction:collection:flatness:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:EQUalization:ITERations command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FLAT:ITER 3  
source2:modulation:correction:collection:flatness:iterations 3  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:ITERations?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for flatness
modulation calibration.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:EQUalization:RECeiver command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FLAT:REC "R1"  
source2:modulation:correction:collection:flatness:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:RECeiver?  
Return Type |  String  
Default |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for a
flatness modulation calibration.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:EQUalization:SPAN command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FLAT:SPAN 1.5GHz  
source2:modulation:correction:collection:flatness:span 1.5ghz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:SPAN?  
Return Type |  Numeric  
Default |  Signal Span  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired flatness
modulation calibration tolerance.  Note: This command is the same as the
SOURce:MODulation:CORRection:COLLection:EQUalization:TOLerance command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration flatness tolerance in dB-pk.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FLAT:TOL 0.100  
source2:modulation:correction:collection:flatness:tolerance 0.100  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FLATness:TOLerance?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency[:FIXed]
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads a fixed frequency to use for
the source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Fixed frequency to perform calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FREQ:FIX 10E9  
source2:modulation:correction:collection:frequency:fixed 10E9  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency[:FIXed]?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:POINts
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of frequency
measurement points to use for a swept frequency source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of frequency points.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FREQ:POIN 5  
source2:modulation:correction:collection:frequency:points 5  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:POINts?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:STARt
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the start frequency to use
for a swept frequency source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Start frequency.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FREQ:STAR 10E9  
source2:modulation:correction:collection:frequency:start 10E9  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:STARt?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:STOP
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the stop frequency to use for
a swept frequency source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Stop frequency.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:FREQ:STOP 11E9  
source2:modulation:correction:collection:frequency:stop 11E9  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:STOP?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:TYPE
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration frequency
type to fixed or swept.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: FIXed SWEpt  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:CORR:COLL:FREQ:TYPE FIX  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:FREQuency:TYPE?  
Return Type |  Enumeration  
Default |  FIX  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enable or disable the LO feedthru
calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable LO feedthru calibration. **1 - ON** \- Enable LO feedthru calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:LO:FTHR:ENAB 1 source2:modulation:correction:collection:lo:fthru:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:LO:FTHR:ITER 3  
source2:modulation:correction:collection:lo:fthru:iterations 3  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:ITERations?  
Return Type |  Numeric  
Default |  6  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for LO feedthru
modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:LO:FTHR:REC "R1"  
source2:modulation:correction:collection:lo:fthru:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:RECeiver?  
Return Type |  String  
Default |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for a LO
feedthru modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:LO:FTHR:SPAN 1.5GHz  
source2:modulation:correction:collection:lo:fthru:span 1.5ghz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:SPAN?  
Return Type |  Numeric  
Default |  0 Hz  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired LO feedthru
modulation calibration tolerance.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration LO feedthru tolerance in dBc  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:LO:FTHR:TOL -40.00  
source2:modulation:correction:collection:lo:fthru:tolerance -40.00  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:LO:FTHRu:TOLerance?  
Return Type |  Numeric  
Default |  -40.00 dBc  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Set and read the notch modulation
calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable Notch calibration. **1 - ON** \- Enable Notch calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:NOT:ENAB 1 source2:modulation:correction:collection:notch:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:NOT:ITER 2  
source2:modulation:correction:collection:notch:iterations 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:ITERations?  
Return Type |  Numeric  
Default |  2  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for an notch
modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:NOT:REC "R1"  
source2:modulation:correction:collection:notch:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:RECeiver?  
Return Type |  String  
Default |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for a
notch modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:NOT:SPAN 100MHz  
source2:modulation:correction:collection:notch:span 100MHz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:SPAN?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired notch calibration
tolerance for the notch modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:NOT:TOL -40dBc  
source2:modulation:correction:collection:notch:tolerance -40dBc  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:NOTch:TOLerance?  
Return Type |  Numeric  
Default |  -40  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Set and read the power modulation
calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable Power calibration. **1 - ON** \- Enable Power calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:POW:ENAB 1 source2:modulation:correction:collection:power:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer[:FIXed]
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads a fixed power level to use
for the source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Fixed power level to perform calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:FIX 0  
source2:modulation:correction:collection:power:fixed 0  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer[:FIXed]?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the maximum number of
iterations used by the calibration routine. The calibration routine uses
successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:ITER 3  
source2:modulation:correction:collection:power:iterations 3  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:ITERations?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:POINts
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of power
measurement points to use for a swept power source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of power points.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:POIN 5  
source2:modulation:correction:collection:power:points 5  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:POINts?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:RECeiver
<rcvr>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the receiver for a power
modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S9x09xxA/B, S9x090A/B choose from: A, B, C, D, R1, R2, R3, R4, a1, a2, a3, a4, b1, b2, b3, b4. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:REC "R1"  
source2:modulation:correction:collection:power:receiver "R1"  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:RECeiver?  
Return Type |  String  
Default |  a1 (options S9x09xxA/B, S9x090A/B) DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration span for a
power modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:SPAN 1.5GHz  
source2:modulation:correction:collection:power:span 1.5ghz  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:SPAN?  
Return Type |  Numeric  
Default |  Signal Span  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:STARt
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the start power level to use
for a swept power source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Start power level.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:STAR -20 dBm  
source2:modulation:correction:collection:power:start -20 dBm  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:STARt?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:STOP
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the stop power level to use
for a swept power source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Stop power level.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:STOP 10 dBm  
source2:modulation:correction:collection:power:stop 10 dBm  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:STOP?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the desired power calibration
tolerance for the power modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dB.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:CORR:COLL:POW:TOL 0.100 dB  
source2:modulation:correction:collection:power:tolerance 0.100 dB  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:TOLerance?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:TYPE
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the calibration power type to
fixed or swept.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: FIXed SWEpt  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:CORR:COLL:POW:TYPE FIX  
Query Syntax |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:POWer:TYPE?  
Return Type |  Enumeration  
Default |  FIX  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection:COLLection:UPDate:ENABle
<bool>[,srcPort]

Applicable Models: N522xB, N523xB, N524xB, All with S9x070A/B (Read-Write)
Enable or disable the option that new Cal will update the currently active
correction.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable the option that new Cal will update the currently active correction. **1 - ON** \- Enable the option that new Cal will update the currently active correction.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:COLL:UPD:ENAB 1 source2:modulation:correction:collection:update:enable on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection:COLLection:UPDate:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:CORRection[:STATe] <bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Set and read the modulation correction
state.  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable modulation correction. **1 - ON** \- Enable modulation correction.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:CORR:STAT 1 source:modulation:correction:state on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:CORRection[:STATe]?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the most recently used filename. For
example, if a new file is loaded, then this file is returned.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE? source:modulation1:file?  
Return Type |  Comma-separated list of strings.  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:CORRection:CATalog? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns a list of the calibrations stored in
the .mdx file. Each calibration displayed in the list is for one power level.
Calibrations may have been performed on multiple power levels during a single
calibration. In this case, multiple calibrations will be saved in the .mdx
file. Delete any of these calibrations using the
SOURce:MODulation:FILE:CORRection:DELete command.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:CORR:CAT? "ModCal_1,ModCal_2,ModCal_3,ModCal_4"  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:CORRection:DELete <calName>

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Deletes any of the calibration files stored
in the .mdx file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<calName> |  String. Name of the source modulation calibration file.  
Examples |  SOUR1:MOD1:FILE:CORR:DEL "ModCal_1"  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:CORRection:FREQuency? <string>

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the frequency of the specified source
modulation calibration file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<String> |  String. Source modulation calibration file name.  
Examples |  SOUR:MOD:FILE:CORR:FREQ? "ModCal_1"  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:CORRection:POWer? <string>

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the power level of the specified
source modulation calibration file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<String> |  String. Source modulation calibration file name.  
Examples |  SOUR:MOD:FILE:CORR:POW? "ModCal_1"  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:INITialize [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Resets the modulation file to default
values.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:INIT  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:LOAD <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Specifies the file path to recall a previous
modulation file. This command allows you to edit an existing modulation file
but does not load the file into the source. You must save the file using the
SOURce:MODulation:FILE:SAVE command then load it into the source using the
SOURce:MODulation:LOAD command. Current settings are overwritten with those in
the file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Modulation file name to be edited.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:LOAD "C:/modulation/MyModFile.mdx" 'open modulation file for editing SOUR1:MOD1:FILE:SAVE "C:/modulation/MyModFile.mdx" 'save modulation file SOUR1:MOD1:LOAD "C:/modulation/MyModFile.mdx","Source3" 'load modulation file into Source3  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SAVE <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Specifies the file path and file name to
save a modulation file. If the file exists, it is overwritten.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Modulation file name.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:SAVE "C:/modulation/MyModFile.mdx"  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:CARRier:OFFSet <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the Carrier offset value.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Carrier offset value.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:CARR:OFFS 1e6  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:CARRier:OFFSet?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:FILE:NUMBer
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of compact
modulation files to create. This function is useful to create several signals,
compare them, then save the best signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of compact modulation files.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:FILE:NUMB 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:FILE:NUMBer?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:FILE:SELect
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the compact modulation file
selection. This function is useful to compare several signals, then save the
best signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Compact modulation file selection.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:FILE:SEL 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:FILE:SELect?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:OFILe
<fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Specifies the file path of the original
signal from which to create a compact signal.  Note: The original signal can
be created from Signal Studio, Matlab, SystemVue, etc.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<fileName> |  File name of original signal.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:OFIL "C:/modulation/MyModFile.mdx"  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:OFILe?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:OFILe:SRATe
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the sample rate of the
compact modulation file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Compact modulation file sample rate.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:OFIL:SRAT 0  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:OFILe:SRATe?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:PAVG? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the peak-to-average value of the
original signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:COMP:PAVG?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:PAVG:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the peak-to-average value of the
signal created from the original signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:COMP:PAVG:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:PAVG:PRIority
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the Peak-to-Avg priority for
Compact signals.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable priority. **1 - ON** \- Enable priority  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:PAVG:PRI ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:PAVG:PRIority?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:SUBCarrier<nnum>:NUMBer
<num>[,srcPort]

Applicable Models: N524xB models with Option S93070xB, and/or N522xB, N523xB,
N524xB with Option S9x09xxA/B, S9x090A/B (Read-Write) Allows setup of multiple
carriers when defining a multicarrier signal. Select 0 for none, or 1 - 9.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<nnum> |  Subcarrier index (1 - 9).  
<num> |  Subcarrier number.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:SUBC:NUMB 1  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:SUBCarrier<nnum>:NUMBer?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:SUBCarrier<nnum>:OFFSet
<num>[,srcPort]

Applicable Models: N524xB models with Option S93070xB, and/or N522xB, N523xB,
N524xB with Option S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the
offset of the selected subcarrier.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<nnum> |  Subcarrier index (1 - 9).  
<num> |  Subcarrier offset.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:SUBC:NUMB 10E6  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:SUBCarrier<nnum>:OFFSet?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:SUBCarrier<nnum>:SPAN
<num>[,srcPort]

Applicable Models: N524xB models with Option S93070xB, and/or N522xB, N523xB,
N524xB with Option S9x09xxA/B, S9x090A/B (Read-Write) Sets and reads the span
of the selected subcarrier.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<nnum> |  Subcarrier index (1 - 9).  
<num> |  Subcarrier span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:SUBC:NUMB 100E6  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:SUBCarrier<nnum>:SPAN?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:TIME:STARt
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads where to start the compact
signal within the original signal. The compact signal is a slice of the
original signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Compact signal start time.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:TIME:STAR 0  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:TIME:STARt?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:TIME:STARt:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the calculated start time of the
signal created from the original signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:COMP:TIME:STAR:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:TIME:STARt:PRIority
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the start time priority for
Compact signals.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable priority. **1 - ON** \- Enable priority  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:COMP:TIME:STAR:PRI ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:COMPact:TIME:STARt:PRIority?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DAC:SCALing <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the scaling factor used for
the waveform (full scale = 100%). This ensures that the DAC filter does not
output a signal that is larger than the DAC's maximum output level, which can
cause distortion in the system. Setting the scaling factor to 100% will
usually cause excessive distortion.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  DAC scale as a percentage of full scale.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DAC:SCAL 70  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DAC:SCALing?  
Return Type |  Numeric  
Default |  70%  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CARRier:NUMBer
<int>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Allows selection of multiple carriers for
multi-carrier modulated signals.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<int> |  (Integer) Number of carriers.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:CARR 1  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CARRier?  
Return Type |  String  
Default |  1  
  
* * *

##
SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CARRier:SPACing:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read) Returns the carrier spacing setting that was used
to create the modulated signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:CARR:SPAC:CALC?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CARRier:SPACing[:VALue]
<real>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Specifies the space between carriers when
setting up multi-carrier signals.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<real> |  Carrier spacing value in Hz.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:CARR:SPAC 50 MHz  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CARRier:SPACing?  
Return Type |  String  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CFILe <string>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Specifies the IQ file name. If Modulation
Type is set to IQ File, then this file defines the IQ constellation. The
symbols will be pseudo-randomly chosen from these constellation values. The
file is a *.csv with the following format:  I_1,Q_1 I_2,Q_2 I_3,Q_3 ...
I_N,Q_N.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<string> |  IQ file name or constellation file name.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:CFIL "MyConstellation.csv"  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:CFILe?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:FILTer:ALPHa
<real>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets the Alpha/BT characteristics of the
selected filter.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<real> |  Set the Alpha/BT filter value.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:FILT:ALPH 0.25  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:FILTer:ALPHa?  
Return Type |  String  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:FILTer:TYPE
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets the filter to apply to the time data.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<enum> |  Choose from: RRC RC  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:FILT:TYPE RC  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:FILTer:TYPE?  
Return Type |  String  
Default |  RRC  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:FORMat <string>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Selects a modulation type:  QPSK 8-PSK
16-QAM 64-QAM 256-QAM 1024-QAM BPSK 8-APSK 16-APSK CR 9/10 32-APSK CR 9/10 IQ
File - If selected, enter a filename of an existing IQ file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<string> |  Modulation type or file name.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:FORM "BPSK"  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:FORMat?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:QUADrature:ERRor
<real>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Indicates the orthogonal error between the I
and Q signals. The ideal orthogonal between I and Q signals is 90 degrees. An
error of 3 degrees indicates that the I and Q are 93 degrees apart.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<real> |  Error in degrees.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:QUAD:ERR 3  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:QUADrature:ERRor?  
Return Type |  String  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:RANDom:SEED
<int>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) The waveform is created using a pseudo-
random number generator. The number generator starts at a value determined by
the Random Seed. For a given Random Seed, the number generator will always
create the same pseudo-random sequence of values. Changing the Random Seed
will change the pseudo-random sequence. The Random Seed may be set to an
integer between 1 and 1,000,000.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<int> |  (Integer) Random seed value, 1 to 1,000,000.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:RAND:SEED 512  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:RANDom:SEED?  
Return Type |  String  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:SYMBol:NUMBer:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read) Returns the number of symbols used to create the
modulated signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:SYMB:NUMB:CALC?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:SYMBol:NUMBer[:VALue]
<int>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Specifies the number of symbols in the
waveform.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<int> |  (Integer) Number of symbols, 1 to 1,000,000.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:SYMB:NUMB 512  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:SYMBol:NUMBer?  
Return Type |  String  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:SYMBol:RATE:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read) Returns the rate, or frequency, at which symbols
occur to create the modulated signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:SYMB:RATE:CALC?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:SYMBol:RATE[:VALue]
<int>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Specifies the rate, or frequency, at which
symbols occur.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<int> |  (Integer) Symbol rate in Hz.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:DIG:SYMB:RATE 512  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:DIGital:SYMBol:NUMBer?  
Return Type |  String  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh[1-20]:LOCation
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Sets the NPR notch location type for the
selected NPR Notch modulation type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: SYMMetric - Symmetric locates the notch in the center of the signal span. ACARrier - Avoid Carrier locates the notch near the center of the signal span but will be shifted to avoid the LO carrier feedthrough. CUSTom Allows the user to define the offset of the notch.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:SIGN:NPR:NOTC1:LOC CUST  
Query Syntax |  Not applicable  
Default |  SYMMetric  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh[1-20]:NUMBer
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of NPR notches in
the modulated signal. A notch can be up to 10% of the Signal Span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of notches (1 - 20)  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:NPR:NOTC1:NUMB 1  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh:NUMBer?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh[1-20]:OFFSet
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the NPR notch offset
frequency of the selected notch. This offset is the center frequency of the
selected notch relative to the LO carrier frequency. Typically, the notch will
have a 0 Hz offset, meaning it is centered on the LO carrier. If you have more
than one notch, you can offset some of the notches from the carrier. For
example, if you have three notches 1 MHz wide, you might set their offsets to
-10 MHz, 0 MHz and +10 MHz so that they are spaced across the wideband
carrier.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  NPR notch offset.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:NPR:NOTC:OFFS 0  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh:OFFSet?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh[1-20]:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the span of the selected
notch.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  NPR notch offset.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:NPR:NOTC1:SPAN 10e6  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:NPR:NOTCh:SPAN?  
Return Type |  Numeric  
Default |  10 MHz  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:BURSt:PREServe:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enables or disables burst preservation. This
is only applied to Compact Signals. If turned ON, then the code will determine
if the Original Signal is a Burst Signal and ensure that the Compact Signal
will be a burst with the same duty cycle. If OFF, no changes will be made to
the Compact Signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Do not ensure Compact Signal will be a burst with the same duty cycle. **1 - ON** \- Ensure Compact Signal will be a burst with the same duty cycle.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:BURst:PRES:ENAB 1  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:BURSt:PREServe:ENABle [srcPort]?  
Return Type |  Boolean  
Default |  False  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:ENABle <bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enables or disables signal optimization
settings. When enabled, the calculated modulated signal will be optimized
according to the constraints defined in this group box. If disabled, then the
signal will not be optimized.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable signal optimization for NPR Notch modulation type. **1 - ON** \- Enable signal optimization for other modulation types (Compact, Flat Tones).  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:ENAB ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:ENABle?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FILTer:ENABle
<bool>[,srcPort]

Applicable Models: N524xB models with Option S93070xB, and/or N522xB, N523xB,
N524xB with Option S9x09xxA/B, S9x090A/B (Read-Write) Enables or disables a
brick-wall filter for spectral leakage (for Compact signals only). The brick-
wall filter is applied to the band-power span calculated for the signal. The
brick-wall filter cuts off signals outside this span. Disable filter to retain
signals outside the calculated band power span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable brick-wall filter. **1 - ON** \- Enable brick-wall filter.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:FILT:ENAB ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FILTer:ENABle?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FILTer:TAPS
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number the number of taps
used for the tapering window. The Compact Signal is generated from a time
slice of the Original Signal. This time slice is repeated. The Tapering Window
is used to smooth the ends of the time slice to minimize spectral splatter
caused by a sharp transition at the boundary.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of taps.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:FILT:TAPS 40  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FILTer:TAPS?  
Return Type |  Numeric  
Default |  30  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FREQuency:LIMit:DDIGits
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of decimal digits
limit for calculated frequencies.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of decimal digits.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:FREQ:LIM:DDIG 2  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FREQuency:LIMit:DDIGits?  
Return Type |  Numeric  
Default |  2  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FREQuency:LIMit:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enables or disables the number of decimal
digits limit for calculated frequencies.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable decimal digit limit setting. **1 - ON** \- Enable decimal digit limit setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:FREQ:LIM:ENAB ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FREQuency:LIMit:ENABle?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FREQuency:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the frequency tolerance value
(in percent).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Tolerance value.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:FREQ:TOL 1  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:FREQuency:TOLerance?  
Return Type |  Numeric  
Default |  1%  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:HREJect <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of test signal
harmonics you want to be protected against. This adds constraints to the list
of LOs used to cover the span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of test signal harmonics to reject.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:HREJ 5  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:HREJect?  
Return Type |  Numeric  
Default |  5  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:MAX:TONE:SPACing
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the tone spacing less than or
equal to the value (Hz).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Distance between each tone.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:MAX:TONE:SPAC 100 kHz  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:MAX:TONE:SPACing?  
Return Type |  Numeric  
Default |  100 kHz  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:MIN:TONE:NUMBer
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the minimum number of tones.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of tones.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:MIN:TONE:NUMB 1001  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:MIN:TONE:NUMBer?  
Return Type |  Numeric  
Default |  1001  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:MIN:WAVeform:PERiod
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the minimum waveform period.
This command minimizes the period of the waveform greater than or equal to the
value (seconds).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Waveform period value.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:MIN:TONE:NUMB 1e-5  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:MIN:WAVeform:PERiod?  
Return Type |  Numeric  
Default |  10 usec  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:NYQReject:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Enables or disables the rejection of Nyquist
frequencies. This ensures that Nyquist images of the signal tones in the IF
bandwidth are not falling back on top of real signal frequencies.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable Nyquist frequency rejection. **1 - ON** \- Enable Nyquist frequency rejection.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:OPT:NYQR:ENAB ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:NYQReject:ENABle?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:OPTimize:TYPE <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Sets the optimize signal type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: MIWPeriod - (Min Waveform Period) Minimizes the period of the waveform greater than or equal to the value (seconds). MITNumber- (Min Number of Tones) Minimizes the number of tones greater than or equal to the value. This will ignore the Number of Tones selection. MATSpacing - (Max Tone Spacing) Maximizes the tone spacing greater than or equal to the value (Hz). This will ignore the Tone Spacing selection. FTOLerance - (Frequency Tolerance) Set frequency tolerance value (in percent).  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:SIGN:OPT:TYPE FTOL  
Query Syntax |  Not applicable  
Default |  FTOLerance  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:PAVG:CALCulated? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the calculated peak-to-average value.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:PAVG:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:PHASe:FIXed <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the phase when Fixed phase is
the Phase Type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Phase setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:PHAS:FIX 0  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:PHASe:FIXed?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:PHASe:RANDom:SEED <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the phase seed when Random
phase is the Phase Type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Phase setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:PHAS:RAND:SEED 1  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:PHASe:RANDom:SEED?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:PHASe:TYPE <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Sets the phase type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: RANDom FIXed PARabolic  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:SIGN:PHAS:TYPE RAND  
Query Syntax |  Not applicable  
Default |  RANDom  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:SPAN <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the signal span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Signal span setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:SPAN 100e6  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:SPAN?  
Return Type |  Numeric  
Default |  100 MHz  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:SPAN:CALCulated? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the calculated signal span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:SPAN:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:SPAN:PRIority <bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the signal span priority.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable priority. **1 - ON** \- Enable priority  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:SPAN:PRI ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:SPAN:PRIority?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:SRATe <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the source sample rate.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Source sample rate setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:SRAT 200e6  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:SRATe?  
Return Type |  Numeric  
Default |  200 MHz  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:SRATe:AUTO <bool> [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Set and read the auto sample rate.  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable auto sample rate. **1 - ON** \- Enable auto sample rate.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:FILE:SIGN:SRAT:AUTO 1  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:SRATe:AUTO?  
**Return Type** |  Boolean  
**Default** |  ON (Not applicable for Compact modulation type)  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:SRATe:CALCulated? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the calculated sampling rate of the
signal created from the original signal.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:SRAT:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the number of tones. This
setting is related to the span and tone spacing: (Number of Tones) = (Signal
Span)/(Tone Specing) +1.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of tones setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:TONE:NUMB 1001  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer?  
Return Type |  Numeric  
Default |  1001  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the calculated number of tones.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:TONE:NUMB:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer:PRIority
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the tone number priority.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable priority for Compact modulation type. **1 - ON** \- Enable priority for NPR Notch and Flat Tone modulation types.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:TONE:NUMB:PRI ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer:PRIority?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer:ROUNd
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Specifies whether firmware should round the
user-input number of tones to an odd or even number.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<enum> |  Choose from: ODD EVEN  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:TONE:NUMB:ROUN EVEN  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:NUMBer:ROUNd?  
Default |  ODD  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:SPACing <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the tone spacing.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Tone spacing setting.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:TONE:SPACing 100e3  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:SPACing?  
Return Type |  Numeric  
Default |  100 kHz  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:SPACing:CALCulated?
[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the calculated spacing between the
tones.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:SIGN:TONE:SPAC:CALC?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:SPACing:PRIority
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the tone spacing priority.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable priority for NPR Notch and Flat Tone modulation types. **1 - ON** \- Enable priority for Compact modulation type.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:SIGN:TONE:SPAC:PRI ON  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:SIGNal:TONE:SPACing:PRIority?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:ALL[:STATe] <bool> [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Set all tone states to on or off.  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable all tones. **1 - ON** \- Enable all tones.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:FILE:TONE:ALL:STAT 1 source:modulation:file:tone:all:state on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:FILE:TONE:ALL[:STATe]? [srcPort]  
**Return Type** |  Boolean  
**Default** |  ON  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:COUNt? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the number of tones.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:TONE:COUN?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:FREQuency? <toneNum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-only) Returns the tone frequency in Hz relative to
the carrier.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<toneNum> |  Tone number.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD:FILE:TONE:FREQ? 118  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:LOAD <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Loads the specified multitone file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Name of the file to be loaded (csv).  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:TONE:LOAD "C:/modulation/MyToneFile.csv"  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:PHASe
<toneNum>,<phaseVal>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the phase in degrees of the
specified tone number.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<toneNum> |  Tone number.  
<phaseVal> |  Phase value in degrees.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:TONE:PHAS 10,45  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:TONE:PHASe? <toneNum>  
Return Type |  Numeric  
Default |  0 - toneNum 0 - phaseVal  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:POWer
<toneNum>,<powerVal>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Sets and reads the power in dBm of the
specified tone number.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<toneNum> |  Tone number.  
<powerVal> |  Power value in dBm.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:MOD1:FILE:TONE:POW 10,-30  
Query Syntax |  SOURce<cnum>:MODulation<port>:FILE:TONE:POWer? <toneNum>  
Return Type |  Numeric  
Default |  0 - toneNum 0 - powerVal  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE:SAVE <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Saves the specified multitone file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Name of the file to be saved (csv).  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:TONE:SAVE "C:/modulation/MyToneFile.csv"  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TONE[:STATe] <toneNum>,<bool> [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Read-Write) Set specified tone state to on or off.  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable tone. **1 - ON** \- Enable tone.  
<toneNum> |  Tone number.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:FILE:TONE:STAT 10,1 source:modulation:file:tone:state 10,on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>:FILE:TONE[:STATe]? <toneNum>  
**Return Type** |  Boolean  
**Default** |  0 - toneNum 1 - bool  
  
* * *

## SOURce<cnum>:MODulation<port>:FILE:TYPE <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B, and/or All with Option
S9x09xxA/B/S9x090A/B (Write-only) Sets the modulation type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: COMPact - (Compact) Shortened version of any type of modulation. Compact signals cut a slice of the IQ data from an original waveform. Note: A Spectrum Analyzer channel does not support the COMPact modulation type. FLATtones - (Flat Tones) This signal is a set of constant amplitude tones over a defined signal span. NPRNotch - (NPR Notch) This signal is a set of constant amplitude tones over a defined signal span where a subset of those tones are set to zero over a notch span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:FILE:TYPE COMP  
Query Syntax |  Not applicable  
Default |  NPRNotch  
  
* * *

## SOURce<cnum>:MODulation<port>:LOAD <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Write-only) Loads the
specified modulation file into the source.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Name of the file to be loaded into the source.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:LOAD "C:/modulation/MyModFile.mdx","Source3" 'load modulation file into Source3  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>:SAVE <file>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Write-only) Saves the
specified modulation file.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<file> |  String. Name of the file to be saved.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:MOD1:SAVE "C:/modulation/MyModFile.mdx"  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:MODulation<port>[:STATe] <bool> [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Set and read
the modulation state.  
---  
**Parameters** |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable I/Q modulation. **1 - ON** \- Enable I/Q modulation.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:MOD1:STAT 1 source:modulation:state on  
**Query Syntax** |  SOURce<cnum>:MODulation<port>[:STATe]? [srcPort]  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

