# Sense:Segment Commands

* * *

Defines the segment sweep settings.

Enable segment sweep with [SENS:SWE:TYPE SEGMent.](Sweep_SCPI.md#ssty)

SENSe:Segment | [ADD](Segment.md#add) | [ARBitrary](Segment.md#arb) | BWIDth | PORT | [:RESolution] | CONTrol | [[RESolution]](Segment.md#bdwval) | [CONTrol](Segment.md#bdwON) | [COUNt](Segment.md#count) | [DELete](Segment.md#del) | [ALL](Segment.md#delall) | FREQuency | [CENTer](Segment.md#cent) | [SPAN](Segment.md#span) | [STARt](Segment.md#start) | [STOP](Segment.md#stop) | HANDler | A:CONTrol <bool> | A <num> | [LIST](Segment.md#list) | NFBW | CONTrol | POWer | ATTenuation | RECeiver | CONTrol | REFerence | TEST | [[LEVel]](Segment.md#pwrval) | [CONTrol](Segment.md#pwrON) | SA | DTHReshold | CONTrol | MTReference | CONTrol | MAX? | MIN? | VAVerage | CONTrol | VIDeobw | CONTrol | SHLO | CONTrol | SOURCE | [RECeiver:GAIN](Segment.md#SourRecGain)  
| [ALL](Segment.md#SouRecGainAll) | [CONTrol](Segment.md#SourRecGainCont) | [[STATe]](Segment.md#segON) | SWEep | DELay | CONTrol | DWELl | CONTrol | GENeration | CONTrol | [POINts](Segment.md#point) | TOTal? | [TIME](Segment.md#time) | [CONTrol](Segment.md#timeon) | TOTal? | X | [SPACing](Segment.md#X AXIS)  
---  
  
Click on a keyword to view the command details.

### See Also

  * Example: [Upload and Download a Segment List](../../GPIB_Example_Programs/Upload_and_Download_a_Segment_List.md)

  * [Learn about Segment Sweep](../../../S1_Settings/Sweep.md#segment)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:SEGMent<snum>:ADD

Applicable Models: All (Write-only) Adds a segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to add. If unspecified, value is set to 1. Segment numbers must be sequential. If a new number is added where one currently exists, the existing segment and those following are incremented by one.  
Examples | Two Segments exist (1 and 2). The following command will add a new segment (1). The existing (1 and 2) will become (2 and 3) respectively. SENS:SEGM1:ADD  
sense2:segment1:add  
Query Syntax | Not applicable. Use Sense:Segment:Count to determine the number of segments in a trace.  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent:ARBitrary <ON | OFF>

Applicable Models: All (Read-Write) Enables you to setup a segment sweep with
arbitrary frequencies. The start and stop frequencies of each segment can
overlap other segments. Also, each segment can have a start frequency that is
greater than its stop frequency which causes a reverse sweep over that
segment. Learn more about [Arbitrary Segment
Sweep](../../../S1_Settings/Sweep.htm#Arbitrary).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<ON | OFF> | ON (or 1) - Allows the setup of arbitrary segment sweep.  
OFF (or 0) - Prevents the setup of arbitrary segment sweep.  
Examples | SENS:SEGM:ARB ON  
sense2:segment:arbitrary off  
Query Syntax | SENSe<cnum>:SEGMent:ARBitrary?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:BWIDth:PORT<pnum>[:RESolution] <num>

Applicable Models: All (Read-Write) Specifies whether the IF Bandwidth
resolution can be set independently for each segment for the selected port and
channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<pnum> | Individual port number of the source: Port 1 to Port 2/Port 4. If unspecified, value is set to 1.  
<num> | IF Bandwidth of each segment in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [(Click to see the lists.)](../../../s2_opt/trce_noise.md#IFDiag) If an invalid number is specified, the analyzer will round up to the closest valid number. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../learning_about_gpib/the_rules_and_syntax_of_scpi_commands.md#min) for more information.  
Examples | SENS:SEGM:BWID:PORT1 1KHZ sense2:segment2:bandwidth:PORT2:resolution max  
Query Syntax | SENSe<cnum>:SEGMent<snum>:BWIDth \ BANDwidth:PORT<pnum>[:RESolution]?  
Return Type | Numeric  
Default | Varies with VNA model.  
  
* * *

## SENSe<cnum>:SEGMent:BANDwidth | BWIDth:PORT[:RESolution]:CONTrol <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the individual (Port 1 to
Port n) IF Bandwidth control in the segment sweep table. This command can be
turned ON when the [SENS:SEGM:BWID:CONT](Segment.md#bdwON) is OFF.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Specified the individual IFBW control, either ON or OFF. ON or 1 \- Turns ON the individual port IFBW control. OFF or 0 \- Turns OFF the individual port IFBW control.  
Examples | SENS:SEGM:BWID:PORT:CONT ON sense2:segment2:bandwidth:PORT:resolution:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:BWIDth | BANDwidth:PORT[:RESolution]:CONTrol?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:BWIDth[:RESolution] <num>

Applicable Models: All (Read-Write) Sets the IF Bandwidth for the specified
segment. First set [SENS:SEGM:BWIDth:CONTrol](Segment.md#bdwON) ON. All
subsequent segments that are added assume the new IF Bandwidth value.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [(Click to see the lists.)](../../../S2_Opt/Trce_Noise.md#IFDiag) If an invalid number is specified, the analyzer will round up to the closest valid number. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:BWID 1KHZ sense2:segment2:bwidth:resolution max  
Query Syntax | SENSe<cnum>:SEGMent<snum>:BWIDth[:RESolution]?  
Return Type | Numeric  
Default | Varies with VNA model.  
  
* * *

## SENSe<cnum>:SEGMent:BWIDth[:RESolution]:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether the IF Bandwidth
resolution can be set independently for each segment. This command can be
turned ON when the [SENS:SEGM:BWID:PORT:CONT](Segment.md#BwidthPortCtrl) is
OFF.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - turns Bandwidth control ON. Bandwidth can be independently set for each segment. OFF (or 0) - turns Bandwidth control OFF. Use the channel IF bandwidth setting [SENS:BWID](Sense_Bandwidth.md#res).  
Examples | SENS:SEGM:BWID:CONT ON sense2:segment:bwidth:control off  
Query Syntax | SENSe<cnum>:SEGMent:BWIDth[:RESolution]:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent:COUNt?

Applicable Models: All (Read-only) Queries the number of segments that exist
in the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:SEGM:COUNt?  
sense2:segment:count?  
Return Type | Numeric  
Default | 1 segment  
  
* * *

## SENSe<cnum>:SEGMent<snum>:DELete

Applicable Models: All (Write-only) Deletes the specified sweep segment. When
ALL segments are deleted, [SENS:SWE:TYPE](Sweep_SCPI.md#ssty) is
automatically set to Linear because there are no segments to sweep.  
---  
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Number of the segment to delete. If unspecified, value is set to 1  
Examples | SENS:SEGM:DEL  
sense2:segment2:delete  
Query Syntax | Not applicable  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent:DELete:ALL

Applicable Models: All (Write-only) Deletes all sweep segments. When this
command is executed, [SENS:SWE:TYPE](Sweep_SCPI.md#ssty) is automatically set
to Linear because there are no segments to sweep.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:SEGM:DEL:ALL  
sense2:segment:delete:all  
Query Syntax | Not applicable  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent<snum>:FREQuency:CENTer <num>

Applicable Models: All (Read-Write) Sets the Center Frequency for the
specified segment. The Frequency Span of the segment remains the same. The
Start and Stop Frequencies change accordingly. Note: All previous segment's
Start and Stop Frequencies that are larger than the new Start Frequency are
changed to the new Start Frequency. All following segment's start and stop
frequencies that are smaller than the new Stop Frequency are changed to the
new Stop Frequency.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Center Frequency in Hz. Choose any number between the minimum and maximum frequency of the analyzer. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:FREQ:CENT 1MHZ  
sense2:segment2:frequency:center 1e9  
Query Syntax | SENSe<cnum>:SEGMent<snum>:FREQuency:CENTer?  
Return Type | Numeric  
Default | Stop Frequency of the previous segment. If first segment, start frequency of the analyzer.  
  
* * *

## SENSe<cnum>:SEGMent<snum>:FREQuency:SPAN <num>

Applicable Models: All (Read-Write) Sets the Frequency Span for the specified
segment. The center frequency of the segment remains the same. The start and
stop frequencies change accordingly. Note: All previous segment's Start and
Stop Frequencies that are larger than the new Start Frequency are changed to
the new Start Frequency. All following segment's start and stop frequencies
that are smaller than the new Stop Frequency are changed to the new Stop
Frequency.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Frequency Span in Hz. Choose any number between the minimum and maximum frequency of the analyzer. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:FREQ:SPAN 1MHZ  
sense2:segment2:frequency:span max  
Query Syntax | SENSe<cnum>:SEGMent<snum>:FREQuency:SPAN?  
Return Type | Numeric  
Default | If first segment, frequency span of the analyzer. Otherwise 0.  
  
* * *

## SENSe<cnum>:SEGMent<snum>:FREQuency:START <num>

Applicable Models: All (Read-Write) Sets the Start Frequency for the specified
sweep segment. Notes All other segment Start and Stop Frequency values that
are larger than this frequency are changed to this frequency. To return the
start and stop frequency of the entire sweep (all segments), Use
[SENS:FREQ:STARt](Frequency.md#start) and
[SENS:FREQ:STOP](Frequency.md#stop)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Start Frequency in Hz. Choose any number between the minimum and maximum frequency of the analyzer. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:FREQ:STAR 1MHZ  
sense2:segment2:frequency:start minimum  
Query Syntax | SENSe<cnum>:SEGMent<snum>:FREQuency:STARt?  
Return Type | Numeric  
Default | Stop Frequency of the previous segment. If first segment, start frequency of the analyzer.  
  
* * *

## SENSe<cnum>:SEGMent<snum>:FREQuency:STOP <num>

Applicable Models: All (Read-Write) Sets the Stop Frequency for the specified
sweep segment. Notes All other segment Start and Stop Frequency values that
are larger than this frequency are changed to this frequency. To return the
start and stop frequency of the entire sweep (all segments), Use
[SENS:FREQ:STARt?](Frequency.md#start) and
[SENS:FREQ:STOP?](Frequency.md#stop)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Stop Frequency in Hz. Choose any number between the minimum and maximum frequency of the analyzer. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:FREQ:STOP 1MHZ  
sense2:segment2:frequency:stop maximum  
Query Syntax | SENSe<cnum>:SEGMent<snum>:FREQuency:STOP?  
Return Type | Numeric  
Default | If first segment, stop frequency of the analyzer. Otherwise, start frequency of the segment.  
  
* * *

## SENSe<cnum>:SEGMent<snum>:HANDler:A:CONTrol <bool>

Applicable Models: N522xB (Read-Write) Enable/disable Handler Port A by
segment. Note: By default, the Material Handler output uses negative logic.
Refer to [CONTrol:HANDler:LOGic](../ControlHandler.md#handlogic) for setting
it to positive logic.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<bool> | Specified the individual handler control, either ON or OFF. ON or 1 \- Turns ON the individual port handler control. OFF or 0 \- Turns OFF the individual port handler control.  
Examples | SENS:SEGM:HAND:A:CONT ON  
Query Syntax | SENSe<cnum>:SEGMent<snum>:HANDler:A:CONT?  
Return Type | Boolean (1 = ON, 0 = OFF)  
  
* * *

## SENSe<cnum>:SEGMent<snum>:HANDler:A <num>

Applicable Models: N522xB (Read-Write) Set an 8-bit value for the Handler A
segment. Note: By default, the Material Handler output uses negative logic.
Refer to [CONTrol:HANDler:LOGic](../ControlHandler.md#handlogic) for setting
it to positive logic.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | This is an 8-bit value (0-255). Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:HAND:A 4  
Query Syntax | SENSe<cnum>:SEGMent<snum>:HANDler:A?  
Return Type | Numeric (0-255)  
  
* * *

## SENSe<cnum>:SEGMent:LIST <char>,<numSegs>,<data>

Applicable Models: All (Read-Write) Reads or writes the entire list of values
in the segment sweep table.  Note: For binary data transfer, specify 64-bit
instead of 32-bit using [FORMat[:DATA]](../Format_SCPI.md#fd). This is
because higher frequencies used on VNA exceed the maximum value that can be
represented by a 32-bit floating point number. When sending/receiving this
data as binary (FORMat[:DATA] REAL,64), use
[FORMat:BORDer](../Format_SCPI.md#fb) to specify the correct 'endianness'
(byte ordering) corresponding to your programming environment / computer
platform.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Choose from: SSTOP \- Frequency values are Start and Stop for each segment.  CSPAN \- Frequency values are Center and Span for each segment.  
<numSegs> | Total number of sweep segments being input. This allows the VNA to determine how many values per-each-segment are in the input <data> block.  
<data> | A list of segments specified using either a comma-separated string of data, or an array of double (real,64) depending on the state of FORM:DATA. Each segment is specified with a minimum of 4 and maximum of 7 values consecutively. The set of values that specify each segment should be in the following order :

  1. Segment state (Boolean 1 for ON and 0 for OFF)
  2. Number of Points in the segment
  3. Start Freq (when <char> is SSTOP), or Center Freq (when <char> is CSPAN)
  4. Stop Freq (when <char> is SSTOP), or Freq Span (when <char> is CSPAN)
  5. IFBW (optional for the Write)
  6. Dwell Time (optional for the Write)
  7. Power (optional for the Write) - see below.

The first four data elements must always be supplied. After those values, data
must be supplied for successive optional elements. For example, to set dwell
time values, you must also supply IFBW values, because IFBW (#5) precedes
dwell time (#6) in the array order. The [IF Bandwidth](Segment.md#bdwON),
[Sweep Time](Segment.md#timeon) and [Source Power](Segment.md#pwrON) Control
settings do NOT affect the order in which elements are interpreted. The number
of elements to supply for Power depends on the following two settings:

  1. [Source Power Option](Segment.md#pwrON) \- ON allows segments to have independent power levels.
  2. [Couple Ports](../source.md#cplON) = Off allows different power levels for each test port.

| CouplePorts | SourcePowerOption | Number of Elements  
---|---|---  
False | False | Each port has its own channel-wide power setting, which is set using [SOURce:POWer[:LEVel]](../source.md#pwrval). Provide exactly 7 elements per segment. The last element (power) is ignored.  
False | True | Provide 6 elements + total number of ports. The first 7 elements are still interpreted the same. The remaining elements (in-order) are interpreted as the power levels to set on that segment for Ports 2 through N, where N is the total number of ports currently enabled for the VNA or for a VNA with multiport external test set.  
True | False | Provide exactly 7 elements per segment. The last element (power) is ignored.  
True | True | Provide exactly 7 elements per segment. The last element (power) is honored.  
  
Examples | SENS:SEGM:LIST SSTOP,1,1,201,10E6,26.5E9,1E3,0,-10 1 segment, state ON, 201 points, 10 MHz to 26.5 GHz, 1kHz IFBW, 0 dwell time, -10 dBm (port powers coupled) sense2:segment:list? cspan See [Upload and Download a Segment List](../../GPIB_Example_Programs/Upload_and_Download_a_Segment_List.md) example program  
Query Syntax | SENSe<cnum>:SEGMent:LIST? [char]. If unspecified, char is set to SSTOP. The number of data elements per segment returned will be 6 + total number of source ports, regardless of the [IF Bandwidth](Segment.md#bdwON), [Sweep Time](Segment.md#timeon) and [Source Power](Segment.md#pwrON) Control settings. For the N5264B, which has no source ports, the query will return just 6 values per segment. For all other VNA models, the last elements in each segment correspond to the power level for each port.  
Return Type | Returns block data in the format specified by [FORMat[:DATA]](../Format_SCPI.md#fd).  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent<snum>:NFBW <num>

Applicable Models: All with S93070xA/B or S95070A/B (Read-Write) Sets or
returns the noise figure bandwidth.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Noise figure bandwidth. Choose any number between the minimum and maximum IF bandwidth of the analyzer. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:NFBW MIN  
sense2:segment2:nfbw maximum  
Query Syntax | SENSe<cnum>:SEGMent<snum>:NFBW?  
Return Type | Numeric  
Default | If first segment, stop frequency of the analyzer. Otherwise, start frequency of the segment.  
  
* * *

## SENSe<cnum>:SEGMent<snum>:NFBW:CONTrol <bool>

Applicable Models: All with S93070xA/B or S95070A/B

(Read-Write) Turns ON or OFF the noise figure bandwidth setting specified
using SENSe:SEGMent:NFBW.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<snum> | Segment number to modify. Choose any existing segment number.  
<bool> | ON or 1 - Turns ON the noise figure bandwidth control. OFF or 0 - Turns OFF the noise figure bandwidth control  
Examples | SENS:SEGM:NFBW:CONT ON sense:segment:nfbw:control 1  
Query Syntax | SENSe<cnum>:SEGMent:NFBW:CONTrol?  
Return Type | Boolean.  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent:POWer:ATTenuation:RECeiver:CONTrol <bool>

Applicable Models: N522xB, N523xB, N524xB, M9485A

(Read-Write) Turns ON or OFF the individual receiver attenuator control in the
segment sweep table.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<bool> | ON or 1 - Turns ON the individual receiver attenuator control. OFF or 0 - Turns OFF the individual receiver attenuator control  
Examples | SENS:SEGM:POW:ATT:REC:REC:CONT ON sense:segment:power:attenuation:receiver:control 1  
Query Syntax | SENSe<cnum>:SEGMent:POWer:ATTenuation:RECeiver:CONTrol?  
Return Type | Boolean. If querying for the standard (M9376A) port, the return value is 0  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:POWer<port>:ATTenuation:RECeiver:REFerence <num>

Applicable Models: N522xB, N523xB, N524xB, M9485A

(Read-Write) Sets the attenuation level for the specified reference attenuator
for each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<snum> | Segment number to modify. Choose any existing segment number. If unspecified, value is set to 1.  
<port> | Port number of the VNA. If unspecified, value is set to 1.  
<num> | Attenuation value in dB. 0dB or 35dB. If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19dB is entered, then 0dB attenuation will be selected.  
Examples | SENS:SEGM:POW2:ATT:REC:REF 0 sense:segment:power:attenuation:receiver:reference 35  
Query Syntax | SENSe<cnum>:SEGMent<snum>:POWer<port>:ATTenuattion:RECeiver:REFerence?  
Return Type | Numeric. If querying for the standard (M9376A) port, the return value is 0  
Default | 35  
  
* * *

## SENSe<cnum>:SEGMent<snum>:POWer<port>:ATTenuation:RECeiver:TEST <num>

Applicable Models: N522xB, N523xB, N524xB, M9485A

(Read-Write) Sets the attenuation level for the specified test attenuator for
each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<snum> | Segment number to modify. Choose any existing segment number. If unspecified, value is set to 1.  
<port> | Port number of the VNA. If unspecified, value is set to 1.  
<num> | Attenuation value in dB. 0dB or 35dB. If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19dB is entered, then 0dB attenuation will be selected.  
Examples | SENS:SEGM:POW2:ATT:REC:TEST 0 sense:segment:power:attenuation:receiver:test 35  
Query Syntax | SENSe<cnum>:SEGMent<snum>:POWer<port>:ATTenuation:RECeiver:TEST?  
Return Type | Numeric. If querying for the standard (M9376A) port, the return value is 0  
Default | 35  
  
* * *

## SENSe<cnum>:SEGMent<snum>:POWer[<port>][:LEVel] <num>

Applicable Models: All (Read-Write) Sets the Port Power level for the
specified sweep segment. First set SENS:SEGM:POW:CONTrol ON. When [port power
is Coupled](../source.htm#cplON), setting port power for one port will apply
port power for all source ports. All subsequent segments that are added assume
the new Power Level value.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<port> | Port number of the source. If unspecified, value is set to 1.  
<num> | Power level. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, send SOUR:POW? MAX and SOUR:POW? MIN. ([SOUR:POW:ATT:AUTO](../source.md#attauto) must be set to ON). Actual achievable leveled power depends on frequency.  
Examples | SENS:SEGM:POW 0  
sense2:segment2:power1:level -10  
Query Syntax | SENSe<cnum>:SEGMent<snum>:POWer[<port>][:LEVel]?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:SEGMent:POWer[:LEVel]:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether Power Level can be set
independently for each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - turns Power Level control ON. Power level can be set for each segment.  
OFF (or 0) - turns Power Level control OFF. Use the channel power level
setting.  
Examples | SENS:SEGM:POW:CONT ON  
sense2:segment:power:level:control off  
Query Syntax | SENSe<cnum>:SEGMent:POWer[:LEVel]:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:DTHReshold <num>

Applicable Models: All (Read-Write) Sets or returns the SA data threshold for
the segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Data threshold (in dBm).  
Examples | SENS:SEGM:SA:DTHR -60  
sense2:segment2:sa:dthreshold -60  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:DTHReshold?  
Return Type | Numeric  
Default | -60 dBm  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:DTHReshold:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether SA Data Threshold can be
set independently for each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<ON | OFF> | ON (or 1) - turns SA Data Threshold control ON.   
OFF (or 0) - turns SA Data Threshold control OFF.  
Examples | SENS:SEGM:SA:DTHR:CONT ON  
sense2:segment:sa:dthreshold:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:DTHReshold:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:MTReference <num>

Applicable Models: All (Read-Write) Sets or returns the SA multitone reference
for the segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Multitone reference (in dBm).  
Examples | SENS:SEGM:SA:MTR 0  
sense2:segment2:sa:mtreference 0  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:MTReference?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:MTReference:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether SA Reference Tone can be
set independently for each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<ON | OFF> | ON (or 1) - turns SA Reference Tone control ON.   
OFF (or 0) - turns SA Reference Tone control OFF.  
Examples | SENS:SEGM:SA:MTR:CONT ON  
sense2:segment:sa:mtreference:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:MTReference:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:MTReference:MAX?

Applicable Models: All (Read-only) Queries the maximum value of the SA
Reference Tone, which is the maximum frequency.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
Examples | SENS:SEGM:SA:MTR:MAX?  
sense2:segment:sa:mtreference:max?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:MTReference:MIN?

Applicable Models: All (Read-only) Queries the minimum value of the SA
Reference Tone.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
Examples | SENS:SEGM:SA:MTR:MIN?  
sense2:segment:sa:mtreference:min?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:VAVerage <num>

Applicable Models: All (Read-Write) Sets or returns the SA vector averaging
points for the segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Vector average points.  
Examples | SENS:SEGM:SA:VAV 10  
sense2:segment2:sa:vaverage 10  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:VAVerage?  
Return Type | Numeric  
Default | 1  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:VAVerage:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether SA Vector Averaging can
be set independently for each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<ON | OFF> | ON (or 1) - turns SA Vector Averaging control ON.   
OFF (or 0) - turns SA Vector Averaging control OFF.  
Examples | SENS:SEGM:SA:VAV:CONT ON  
sense2:segment:sa:vaverage:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:VAVerage:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:VIDeobw <num>

Applicable Models: All (Read-Write) Sets or returns the SA video bandwidth for
the segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<num> | Video bandwidth (in Hz).  
Examples | SENS:SEGM:SA:VID 1E6  
sense2:segment2:sa:videobw 1e6  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:VIDeobw?  
Return Type | Numeric  
Default | 1E6 Hz  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SA:VIDeobw:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether SA Video Bandwidth can
be set independently for each segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number.  
<ON | OFF> | ON (or 1) - turns SA Video Bandwidth control ON.   
OFF (or 0) - turns SA Video Bandwidth control OFF.  
Examples | SENS:SEGM:SA:VID:CONT ON  
sense2:segment:sa:videobw:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SA:VIDeobw:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns the specified sweep segment ON or
OFF. At least ONE segment must be ON or [Sweep Mode](Sweep_SCPI.md#ssm) is
automatically set to Linear.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to be turned ON or OFF  
<ON | OFF> | ON (or 1) - turns segment ON.  
OFF (or 0) - turns segment OFF.  
Examples | SENS:SEGM ON  
sense2:segment2:state off  
Query Syntax | SENSe<cnum>:SEGMent<snum>[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SHLO

Applicable Models: N522xB, N523xB, N524xB, E5080A/B , E5081A, M98xxA

(Read-Write) Sets or returns the Shift LO state of each segment in the segment
sweep table for the selected channel. Notes: The SENS:SEGM:SHLO:CONT command
must first be set to ON before using this command.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
Examples | SENS:SEGM:SHLO  
sense2:segment2:shlo  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SHLO?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SHLO:CONTrol <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, E5081A, M98xxA

(Read-Write) Turns ON or OFF the individual Shift LO state control in the
segment sweep table.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<bool> | ON or 1 \- Turns ON the individual Shift LO state control.  
OFF or 0 \- Turns OFF the individual Shift LO state control.  
Examples | SENS:SEGM:SHLO:CONT ON  
sense2:segment2:shlo:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SHLO:CONTrol?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent:<snum>:SOURce<sport>:RECeiver<rport>:GAIN[:VALue]
<string>

Applicable Models: M98xxA, P50xxA/B, E5080B, E5081A (Read-Write) Sets the gain
settings to a specified port on the specified sweep segment.
SENS:SEGM:SOUR:REC:GAIN:CONT should be turned on when you us this. Use
[SENS:SOUR:REC:GAIN:CAT?](SenseSource.md#RecGainCat) to return a list of
available gain states for the specified port.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number. If unspecified, value is set to 1.  
<sport> | Source port number of the VNA. If unspecified, value is set to 1  
<rport> | Receiver port number of the VNA. If unspecified, value is set to 1  
<string> | Receiver gain state. Not case sensitive. For M980xA, P50xxA choose from:

  * Auto
  * Low
  * High

  
Examples | SENS:SEGM2:SOUR:REC:GAIN:CONT ON  
SENSe:SEGM2:SOUR1:REC2:GAIN "Low" ' Low for S21 measurement in segment 2
sense:segment:source:receiver:control on  
sense:segment:source2:receiver2:gain:value "High" ' High for S22 measurement
in Segment 1  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SOURce<sport>:RECeiver<rport>:GAIN[:VALue] ?  
Return Type | String  
Default | Auto  
  
* * *

## SENSe<cnum>:SEGMent:<snum>:SOURce<sport>:RECeiver<rport>:GAIN:ALL[:VALue]
<string>

Applicable Models: M98xxA, P50xxA/B, E5080B, E5081A (Read-Write) Sets the gain
settings to all ports on the specified sweep segment.
SENS:SEGM:SOUR:REC:GAIN:CONT should be turned on when you us this. Use
[SENS:SOUR:REC:GAIN:CAT?](SenseSource.md#RecGainCat) to return a list of
available gain states for the specified port.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Segment number to modify. Choose any existing segment number. If unspecified, value is set to 1.  
<sport> | This parameter is Ignored  
<rport> | This parameter is Ignored  
<string> | Receiver gain state. Not case sensitive. For M980xA, P50xxA choose from:

  * Auto
  * Low
  * High

  
Examples | SENS:SEGM2:SOUR:REC:GAIN:CONT ON  
SENSe:SEGM2:SOUR:REC:GAIN:ALL "Low" ' Low for all measurements in Segment 2
sense:segment:source:receiver:control on  
sense:segment:source2:receiver2:gain:all:value "High" ' High for all
measurements in Segment 1  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SOURce<sport>:RECeiver<rport>:GAIN:ALL[:VALue] ?  
Return Type | String, "MIXED" is returned when the settings are not the same.   
Default | Auto  
  
* * *

## SENSe<cnum>:SEGMent:<snum>:SOURce<sport>:RECeiver<rport>:GAIN:CONTrol
<bool>

Applicable Models: M98xxA, P50xxA/B, E5080B, E5081A (Read-Write) Sets and read
the status of the segment receiver gain setting function. This must be turned
ON when SENS:SEGM:SOUR:REC:GAIN or SENS:SEGM:SOUR:REC:GAIN:ALL is used.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | This parameter is Ignored.  
<sport> | This parameter is Ignored.  
<rport> | This parameter is Ignored.  
<bool> | ON or 1 - Turn the segment receiver gain setting function ON OFF or 0 - Turn the segment receiver gain setting function OFF  
Examples | SENS:SEGM2:SOUR:REC:GAIN:CONT ON  
sense:segment:source:receiver:control on  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SOURce<sport>:RECeiver<rport>:GAIN:CONTrol ?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:DELay <num>

Applicable Models: All (Read-Write) Sets or returns the sweep delay time of
the specified sweep segment. Notes: The
[SENS:SEGM:SWE:DEL:CONT](segment.md#DelayControl) command must first be set
to ON before using this command.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<num> | Range of sweep delay time is between 0 to 1 and the resolution is 0.001. Notes: If the specified variable is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set.  
<unit> | s (second)  
Examples | SENS:SEGM:SWE:DEL  
sense2:segment2:sweep:delay  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:DELay?  
Return Type | Numeric / Double precision floating point  
Default | 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:DELay:CONTrol <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the sweep delay time of
the specified sweep segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<bool> | ON or 1 \- Turns ON sweep delay time.  
OFF or 0 \- Turns OFF sweep delay time.  
Examples | SENS:SEGM:SWE:DEL:CONT ON  
sense2:segment2:sweep:delay:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:DELay:CONTrol?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:DWELl <num>

Applicable Models: All (Read-Write) Sets or returns the sweep dwell time of
the specified sweep segment. Notes: The SENS:SEGM:SWE:DWELl:CONT command must
first be set to ON before using this command.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<num> | Range of sweep dwell time Notes: If the specified variable is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set.  
<unit> | s (second)  
Examples | SENS:SEGM:SWE:DWEL  
sense2:segment2:sweep:dwell  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:DWELl?  
Return Type | Numeric / Double precision floating point  
Default | 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:DWELl:CONTrol <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the sweep dwell time of
the specified sweep segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<bool> | ON or 1 \- Turns ON sweep dwell time.  
OFF or 0 \- Turns OFF sweep dwell time.  
Examples | SENS:SEGM:SWE:DWEL:CONT ON  
sense2:segment2:sweep:dwell:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:DWELl:CONTrol?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:GENeration <char>

Applicable Models: All (Read-Write) Sets or returns the sweep mode of the
specified sweep segment. Notes: The
[SENS:SEGM:SWE:GEN:CONT](segment.md#GenControl) command must first be set to
ON before using this command.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<snum> | Any existing segment number.  
<char> | Select sweep mode from either of the following:

  * "ANALog": Sets the sweep mode to the auto mode.
  * "STEPped": Sets the sweep mode to the stepped mode.

  
Examples | SENS:SEGM:SWE:GEN ANAL  
sense2:segment2:sweep:generation stepped  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:GENeration?  
Return Type | Character  
Default | "ANAL"  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:GENeration:CONTrol <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the sweep mode of the
specified sweep segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<snum> | Any existing segment number.  
<bool> | ON or 1 \- Turn ON sweep mode.  
OFF or 0 \- Turn OFF sweep mode.  
Examples | SENS:SEGM:SWE:GEN:CONT ON  
sense2:segment2:sweep:generation:control off  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:GENeration:CONTrol?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:POINts <num>

Applicable Models: All (Read-Write) Sets the number of data points for the
specified sweep segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number. If unspecified, value is set to 1  
<num> | Number of points in the segment. The total number of points in all segments cannot exceed 20001. A segment can have as few as 1 point. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:SWE:POIN 51  
sense2:segment2:sweep:points maximum  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:POINts?  
Return Type | Numeric  
Default | 21  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:POINts:TOTal? <totalPoints>

Applicable Models: All (Read-only) Queries the total point count from the
active segments or from all segments.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<totalPoints> | Choose from: ACTive \- Returns the total point count of the active segments. ALL \- Returns the total point count of all segments.  
Examples | SENS:SEGM:SWE:POIN:TOT? ACT  
sense2:segment:sweep:points:total? all  
Return Type | Numeric  
Default | 21  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:TIME <num>

Applicable Models: All (Read-Write) Sets the time the analyzer takes to sweep
the specified sweep segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<num> | Sweep time in seconds. Choose a number between 0 and 100 Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SEGM:SWE:TIME 1ms  
sense2:segment2:sweep:time .001  
Query Syntax | SENSe<cnum>:SEGMent<snum>:SWEep:TIME?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:SEGMent:SWEep:TIME:CONTrol <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether Sweep Time can be set
independently for each sweep segment.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - turns Sweep Time control ON. Sweep Time can be set for each segment.  
OFF (or 0) - turns Sweep Time control OFF. Uses the channel Sweep Time
setting.  
Examples | SENS:SEGM:SWE:TIME:CONT ON  
sense2:segment:sweep:time:control off  
Query Syntax | SENSe<cnum>:SEGMent:SWEep:TIME:CONTrol?  
Return Type | Boolean (1 = ON, 0 = OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:SEGMent<snum>:SWEep:TIME:TOTal? <totalTime>

Applicable Models: All (Read-only) Queries the total sweep time of the active
segments or of all segments.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<snum> | Any existing segment number.  
<totalTime> | Choose from: ACTive \- Returns the total sweep time of the active segments. ALL \- Returns the total sweep time of all segments.  
Examples | SENS:SEGM:SWE:TIME:TOT? ACT  
sense2:segment:sweep:time:total? all  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:SEGMent:X:SPACing <char>

Applicable Models: All (Read-Write) Sets X-axis spacing ON or OFF  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | LINear \- turns X-axis point spacing OFF OBASe \- turns X-axis point spacing ON  
Examples | SENS:SEGM:X:SPACing LIN  
sense2:segment:spacing obase  
Query Syntax | SENSe<cnum>:SEGMent:X:SPACing?  
Return Type | Character  
Default | LINear  
  
* * *

