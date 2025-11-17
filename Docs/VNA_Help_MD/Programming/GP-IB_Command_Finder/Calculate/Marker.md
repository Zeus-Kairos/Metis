# Calculate:Marker Commands

* * *

Controls the marker settings used to remotely output specific data to the
computer.

These commands are Superseded by the
[CALCulate:MEASure:MARKer](MeasureMARKer.md) commands.

CALCulate:MARKer: [AOFF](Marker.md#aoff) [BUCKet](Marker.md#bucket) [BWIDth](Marker.md#band) COMPression | [LEVel](Marker.md#CompLevel) | [PIN?](Marker.md#pin) | [POUT?](Marker.md#pout) COUPling | [METHod](Marker.md#coupleMethod) | [[STATe]](Marker.md#couple) [DELTa](Marker.md#delta) [DISCrete](Marker.md#disc) [DISTance](Marker.md#distance) [FORMat](Marker.md#form) FUNCtion | APEak | [EXCursion](Marker.md#excr) | [THReshold](Marker.md#thres) | DOMain | [USER](Marker.md#rang) | [STARt](Marker.md#ustart) | [STOP](Marker.md#ustop) | [EXECute](Marker.md#fexe) | [[SELect]](Marker.md#fselect) | [TRACking](Marker.md#track) [PNOP more commands](MarkerPNOP.md) [PSATuration more commands](MarkerPSAT.md) REFerence | [[STATe]](Marker.md#rstate) | [X](Marker.md#rx) | [Y?](Marker.md#ry) [SET](Marker.md#set) [[STATe]](Marker.md#state) [TARGet](Marker.md#targval) [TYPE](Marker.md#type) [X](Marker.md#X) [Y?](Marker.md#Y)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Marker example program](../../GPIB_Example_Programs/Setup_Markers.md)

  * Marker Readout [number](../Display.md#single) and [size](../Display.md#size) commands.

  * [Learn about Markers](../../../S4_Collect/Markers.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

Important: Learn about [programming the reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers).

* * *

## CALCulate<cnum>:MARKer:AOFF

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Write-only) Turns all markers off for selected measurement. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:AOFF  
calculate2:marker:aoff  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer<n>:BUCKet <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets and reads the data point (bucket) number of the
trace on which the marker resides. When the markers are [interpolated (non-
discrete](../../../S4_Collect/Markers.htm#discrete)), the returned value is
the nearest marker bucket position. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Marker number to move or query. The marker must already exist. If unspecified, <n> is set to 1.  
<num> | Data point (bucket) number. Choose any data point between: 0 and the number of data points minus 1.  
Examples | CALC:MARK:BUCK 5 calculate2:marker2:bucket 200  
Query Syntax | CALCulate<cnum>:MARKer<n>:BUCKet?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The first marker is set to the middle of the span. Subsequent markers are set to the bucket number of the previously active marker.  
  
* * *

## CALCulate<cnum>:MARKer:BWIDth <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Turns on and sets markers 1 through 4 to calculate
filter bandwidth. The <num> parameter sets the value below the maximum
bandwidth peak that establishes the bandwidth of a filter. For example, if you
want to determine the filter bandwidth 3 db below the bandpass peak value, set
<num> to -3. To turn off the Bandwidth markers, either turn them off
individually or turn them [All Off](Marker.md#aoff). The analyzer screen will
show either Bandwidth statistics OR Trace statistics; not both. To search a
User Range with the bandwidth search, first activate marker 1 and set the
desired [User Range](Marker.md#rang). Then send the CALC:MARK:BWID command.
The user range used with bandwidth search only applies to marker 1 searching
for the max value. The other markers may fall outside the user range. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Target value below filter peak. Choose any number between :-500 and 500  
Examples | CALC:MARK:BWID -3  
calculate2:marker:bwidth -2.513  
Query Syntax | CALCulate<cnum>:MARKer:BWIDth?  
Returns the results of bandwith search:  
Return Type | Numeric - Four Character values separated by commas: bandwidth, center Frequency, Q, loss.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -3  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:COMPression:LEVel <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Set and read the marker compression level. A
compression marker must already exist. Use [CALC:MARK ON](Marker.md#state)
and [CALC:MARK:FUNC COMP](Marker.md#fselect) to create compression markers.
See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Compression level. Choose any number between: -500 dB to 500 dB Standard gain compression values are positive.  
Examples | CALC:MARK:COMP:LEV 1  
calculate2:marker:compression:level 1.5  
Query Syntax | CALCulate<cnum>:MARKer:COMPression:LEVel?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | +1  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:COMPression:PIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-only) Reads the input power at the marker compression level.
First send [CALC:MARK:FUNC:EXEC COMP](Marker.md#fexe) or [CALC:MARK:FUNC:TRAC
ON](Marker.htm#track) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
Examples | CALC:MARK:COMP:PIN?  
calculate2:marker:compression:pin?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:COMPression:POUT?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-only) Reads the output power at the marker compression level.
First send [CALC:MARK:FUNC:EXEC COMP](Marker.md#fexe) or [CALC:MARK:FUNC:TRAC
ON](Marker.htm#track) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
Examples | CALC:MARK:COMP:POUT?  
calculate2:marker2:compression:pout?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:COUPling:METHod <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets and reads the scope of Coupled Markers. This is a
global setting that affects all markers. [Learn
more.](../../../S4_Collect/Markers.htm#Coupled_Markers) Note: This command
will not take effect until Coupled Markers is turned on using
CALC:MARK:COUP:STATe ON. Note: The preset behavior of Coupled Markers depends
on the setting of
[SYSTem:PREFerences:ITEM:MCControl](../System_Preferences.md#markerCouplControl),
[SYSTem:PREFerences:ITEM:MCMethod](../System_Preferences.md#markerCoupleMethod),
and
[SYSTem:PREFerences:ITEM:MCPRest](../System_Preferences.md#MarkerCouplPreset).  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | CHANnel \- Coupling is limited to traces in the same channel. ALL \- Coupling occurs across all channels.  
Examples | CALC:MARK:COUP:METH CHAN calculate1:marker1:coupling:method all  
Query Syntax | CALCulate:MARKer:COUPling:METHod?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ALL  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:COUPling[:STATe]<ON|OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets and reads the state of Coupled Markers (ON and
OFF). The scope of coupled markers can be changed with
[CALC:MARK:COUP:METH](Marker.md#coupleMethod). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | OFF (0) - Turns Coupled Markers OFF ON (1) \- Turns Coupled Markers ON  
Examples | CALC:MARK:COUP ON  
calculate1:marker1:coupling off  
Query Syntax | CALCulate:MARKer:COUPling:[STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:DELTa <ON|OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Specifies whether marker is relative to the Reference
marker or absolute. Note: The reference marker must already be turned ON with
[CALC:MARK:REF:STATE](Marker.md#rstate). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - Specified marker is a Delta marker OFF (or 0) - Specified marker is an ABSOLUTE marker  
Examples | CALC:MARK:DELT ON calculate2:marker8:delta off  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:DELTa?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:DISCrete <ON|OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Makes the specified marker display either a calculated
value between data points (interpolated data) or the actual data points
(discrete data). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - Specified marker displays the actual data points  
OFF (or 0) - Specified marker displays calculated data between the actual data
points.  
Examples | CALC:MARK:DISC ON  
calculate2:marker8:discrete off  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:DISCrete?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:DISTance <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Set or
query marker distance on a time domain trace. CALCulate:MARKer commands are
Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md) commands. The
Write command moves the marker to the specified distance value. Once moved,
you can [read the Y axis](Marker.md#Y) value or [read the X-axis
time](Marker.htm#X) value. (Distance is calculated from the X-axis time
value.) The Read command reads the distance of the marker. If the marker is
set as delta, the WRITE and READ data is relative to the reference marker. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Marker distance in the unit of measure specified with [CALC:TRAN:TIME:MARK:UNIT](Transform_Calc.md#MarkerUnit)  
Examples | CALC:MARK:DIST .1  
calculate2:marker8:distance 5  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:DISTance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FORMat <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the format of the data that will be returned in a
marker data query CALC:MARK:Y? and the displayed value of the marker readout.
The selection does not have to be the same as the measurement's display
format. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<char> | Choose from:  
DEFault \- The format of the selected measurement MLINear \- Linear magnitude
MLOGarithmic \- Logarithmic magnitude IMPedance - (R+jX) ADMittance - (G+jB)
PHASe - Phase IMAGinary - Imaginary part (Im) REAL - Real part (Re) POLar \-
(Re, Im) GDELay \- Group Delay LINPhase - Linear Magnitude and Phase LOGPhase
- Log Magnitude and Phase KELVin - temperature FAHRenheit - temperature
CELSius - - temperature NOISe \- Noise (available ONLY in [IM
Spectrum](../../../Applications/IMSpectrum.htm) and
[SA](../../../Applications/Spectrum_Analyzer.md) measurement classes).  
Examples | CALC:MARK:FORMat MLIN  
calculate2:marker8:format Character  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FORMat?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | DEFault  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:APEak:EXCursion <num><unit>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets amplitude peak excursion for the specified marker.
The Excursion value determines what is considered a "peak". This command
applies to marker peak searches (Next peak, Peak Right, Peak Left). See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Excursion value. Choose any number between -500 and 500. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MARK:FUNC:APE:EXC 10  
calculate2:marker8:function:apeak:excursion maximum  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:APEak:EXCursion?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:APEak:THReshold <num><unit>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets peak threshold for the specified marker. If a peak
(using the criteria set with :EXCursion) is below this reference value, it
will not be considered when searching for peaks. This command applies to
marker peak searches (Next peak, Peak Right, Peak Left). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<num> | Threshold value.Choose any number between -500 and 500. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MARK:FUNC:APE:THR -40  
calculate2:marker8:function:apeak:threshold -55  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:APEak:THReshold?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -100  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:DOMain:USER[:RANGe] <range>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Assigns the specified marker to a range number. The
x-axis travel of the marker is constrained to the range's span. The span is
specified with the [CALC:MARK:FUNC:DOM:USER:START](Marker.md#ustart) and
[STOP](Marker.md#ustop) commands, unless range 0 is specified which is the
full span of the analyzer. Each channel has 16 user ranges. (Trace statistics
use the same ranges.) More than one marker can use a domain range. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<span> | User span. Choose any Integer from 0 to 16 0 is Full Span of the analyzer 1 to 16 are available for user-defined x-axis span  
Examples | CALC:MARK:FUNC:DOM:USER 1  
calculate2:marker8:function:domain:user:range 1  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:DOMain:USER[:RANGe]? Returns the user span number that the specified marker is assigned to.  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 - Full Span  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STARt <start>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the start of the span that the specified marker's
x-axis span will be constrained to. Use
[CALC:MARK:FUNC:DOM:USER<range>](Marker.md#rang) to set range number Use
[CALC:MARK:FUNC:DOM:USER:STOP](Marker.md#ustop) to set the stop value. Note:
If the marker is assigned to range 0 (full span), the USER:STARt and STOP
commands generate an error. You cannot set the STARt and STOP values for "Full
Span". Note: This command does the same as
[CALC:FUNC:DOM:USER:STAR](Function.md#start) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<start> | The analyzer's Minimum x-axis value  
Examples | CALC:MARK:FUNC:DOM:USER:START 500E6  
calculate2:marker8:function:domain:user:start 1e12  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The analyzer's Minimum x-axis value  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STOP <stop>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the stop of the span that the marker's x-axis
travel will be constrained to. Use
[CALC:MARK:FUNC:DOM:USER<range>](Marker.md#rang) to set range number Use
[CALC:MARK:FUNC:DOM:USER:STARt](Marker.md#ustart) to set the stop value.
Note: If the marker is assigned to range 0 (full span), the USER:STARt and
STOP commands generate an error. You cannot set the STARt and STOP values for
"Full Span". Note: This command does the same as
[CALC:FUNC:DOM:USER:STOP](Function.md#stop) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<stop> | Stop value of x-axis span; Choose any number between the analyzer's MINimum and MAXimum x-axis value.  
Examples | CALC:MARK:FUNC:DOM:USER:STOP 500e6  
calculate2:marker8:function:domain1:user:stop 1e12  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The analyzer's MAXimum x-axis value.  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:EXECute <func>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Write-only) Immediately executes (performs) the specified search
function. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<func> | The function to be performed. Choose from:

  * MAXimum \- finds the highest value
  * MINimum \- finds the lowest value
  * RPEak \- finds the next valid peak to the right
  * LPEak - finds the next valid peak to the left
  * NPEak \- finds the next highest value among the valid peaks
  * TARGet \- finds the target value to the right, wraps around to the left
  * LTARget \- finds the next target value to the left of the marker
  * RTARget \- finds the next target value to the right of the marker
  * COMPression \- finds the compression level on a Power Swept S21 trace.

  
Examples | CALC:MARK:FUNC:EXEC MAX  
calculate2:marker2:function:execute maximum  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion[:SELect] <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the search function that the specified marker will
perform when executed. Use [CALC:MARK:FUNC:TRAC ON](Marker.md#track) to
automatically execute the search every sweep. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Marker function. Choose from:

  * MAXimum \- finds the highest value
  * MINimum \- finds the lowest value
  * RPEak \- finds the next valid peak to the right
  * LPEak - finds the next valid peak to the left
  * NPEak \- finds the next highest value among the valid peaks
  * TARGet \- finds the target value to the right, wraps around to the left
  * LTARget \- finds the next target value to the left of the marker
  * RTARget \- finds the next target value to the right of the marker
  * COMPression \- finds the compression level on a power-swept S21 trace.

  
Examples | CALC:MARK:FUNC MAX  
calculate2:marker8:function:select ltarget  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion[:SELect]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MAX  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:TARGet[:VALue] <num><unit>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md) commands. (Read-Write) Sets the target value for the specified marker when doing Target Searches with [CALC:MARK:FUNC:SEL](Marker.md#fselect) <TARGet | RTARget | LTARget> See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Target value to search for; Units are NOT allowed.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MARK:TARG 2.5  
calculate2:marker8:target:value -10.3  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:TARGet[:VALue]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:FUNCtion:TRACking <ON | OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the tracking capability for the specified marker.
The tracking function finds the selected search function every sweep. In
effect, turning Tracking ON is the same as doing a
[CALC:MARK:FUNC:EXECute](Marker.md#fexe) command every sweep. [Learn more
about Marker Search](../../../S4_Collect/Markers.htm#Searching) See Critical
Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<ON | OFF> | ON (or 1) - The specified marker will "Track" (find) the selected function every sweep. OFF (or 0) - The specified marker will find the selected function only when the CALC:MARK:FUNC:EXECute command is sent.  
Examples | CALC:MARK:FUNC:TRAC ON  
calculate2:marker8:function:tracking off  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:TRACking?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MARKer:REFerence[:STATe] <ON | OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Turns the reference marker ON or OFF. When turned OFF,
existing Delta markers revert to general-purpose markers. Important: Learn
about [programming the reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> | ON (or 1) - turns reference marker ON OFF (or 0) - turns reference marker ON  
Examples | CALC:MARK:REF ON  
calculate2:marker:reference:state OFF  
Query Syntax | CALCulate<cnum>:MARKer:REFerence[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MARKer:REFerence:X <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets and returns the absolute x-axis value of the
reference marker. Important: Learn about [programming the reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers). See Critical Note  
---  
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | X-axis value. Choose any number within the operating domain of the reference marker.  
Examples | CALC:MARK:REF:X 1e9 calculate2:marker:reference:x 1e6  
Query Syntax | CALCulate<cnum>:MARKer:REFerence:X?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | If the first Marker, turns ON in the middle of the X-axis span. If not, turns ON at the position of the active marker.  
  
* * *

## CALCulate<cnum>:MARKer:REFerence:Y?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-only) Returns the absolute Y-axis value of the reference
marker. Important: Learn about [programming the reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:REF:Y? calculate2:marker:reference:y?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:SET <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Write-only) Sets the selected instrument setting to assume the
value of the specified marker. Marker Functions CENT, SPAN, STARt, and STOP do
not work with channels that are in
[CW](../../../S1_Settings/Sweep.md#SweepTypeDiag) or [Segment
Sweep](../../../S1_Settings/Sweep.htm#segment) mode. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<char> | Choose from:

  * CENTer - changes center frequency to the value of the marker
  * SA - creates an SA channel with a marker at the same CW frequency. [Learn more](../../../Applications/Spectrum_Analyzer.md#MarkerToSA).
  * SPAN - changes the sweep span to the span that is defined by the delta marker and the marker that it references. Unavailable if there is no delta marker.
  * STARt - changes the start frequency to the value of the marker
  * STOP - changes the stop frequency to the value of the marker
  * RLEVel \- changes the reference level to the value of the marker
  * DELay \- changes the line length at the receiver input to the phase slope at the active marker stimulus position.
  * CWFReq \- Sets the CW frequency to the frequency of the active marker. Does NOT change sweep type. NOT available in CW or Power Sweep. Use this argument to first set the CW Frequency to a value that is known to be within the current calibrated range, THEN set [Sweep:Type](../Sense/Sweep_SCPI.md#ssty) to POWer or CW.

  
Examples | CALC:MARK:SET CENT  
calculate2:marker8:set span  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MARKer<mkr>[:STATe] <ON|OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Turns the specified marker ON or OFF. To turn all
markers off, use CALC:MARK:AOFF. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - turns marker ON. OFF (or 0) - turns marker OFF.  
Examples | CALC:MARK ON  
calculate2:marker8 on  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Off  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:TYPE <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the type of the specified marker. See Critical
Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<char> | Choose from:

  * NORMal \- a marker that stays on the assigned X-axis position unless moved or searching.
  * FIXed \- a marker that will not leave the assigned X or current Y-axis position.

  
Examples | CALC:MARK:TYPE NORM  
calculate2:marker2:type fixed  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NORMal  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:X <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-Write) Sets the marker's X-axis value (frequency, power, or
time). If the marker is set as delta, the SET and QUERY data is relative to
the reference marker. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Any X-axis position within the measurement span of the marker. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | CALC:MARK:X 100Mhz  
calculate2:marker8:x maximum  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:X?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | First Marker turns ON in the middle of the X-axis span. Subsequent markers turn ON at the position of the active marker.  
  
* * *

## CALCulate<cnum>:MARKer<mkr>:Y?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA CALCulate:MARKer
commands are Superseded by the [CALCulate:MEASure:MARKer](MeasureMARKer.md)
commands. (Read-only) Reads the marker's Y-axis value. The format of the value
depends on the current CALC:MARKER:FORMAT setting. If the marker is set as
delta, the data is relative to the reference marker. The query always returns
two numbers:

  * Smith and Polar formats - (Real, Imaginary)
  * LINPhase and LOGPhase \- (Real, Imaginary)
  * All other formats - (Value,0)

Note: To accurately read the marker Y-axis value with [trace
smoothing](../../../S2_Opt/Trce_Noise.htm#Smoothing) applied, the requested
format must match the [displayed
format](../../../S1_Settings/Data_Format.htm#FormatDiag). Otherwise, the
returned value is un-smoothed data. For example, to read the smoothed marker
value when measuring group delay, both the display format and the marker
format must be set to (Group) Delay. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
Examples | CALC:MARK:Y?  
calculate2:marker3:y?  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:Y?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

