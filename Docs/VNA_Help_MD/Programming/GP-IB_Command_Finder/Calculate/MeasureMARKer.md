# CALCulate:MEASure:MARKer Commands

Controls the marker settings used to remotely output specific data to the
computer.

CALCulate:MEASure:MARKer: AOFF BUCKet BWIDth | DATA? | REF | [:STATe] | THReshold COUPling | METHod | [STATe] DELTa DISCrete DISTance FORMat FUNCtion | APEak:POLarity | COMPression | LEVel | PIN? | POUT? | [:STATe] | DOMain | USER | [:RANGe] | STARt | STOP | EXECute | MULTI | EXECute | PEAK | EXCursion | POLarity | THReshold | SELect | TARGet | TRANsition | [:VALue] | TRACking | PEAK | EXCursion | POLarity | THReshold | [:SELect] |[ :SEL:EXTended](MeasureMARKer.md#FuncSelExt) | TARGet | TRANsition | [:VALue] | TRACking NOTCh | DATA? | REF | [:STATe] | THReshold PNOP | BACKoff | GAIN | PIN | POUT | COMPression | MAXimum | GAIN | MAXimum | PIN | MAXimum | POFFset | POUT | MAXimum | [:STATe] PSATuration | BACKoff | COMPression | MAXimum | SATuration | GAIN | LINear | MAXimum | PIN | MAXimum | POUT | MAXimum | [:STATe] REFerence | [:STATe] | X | Y SET [:STATe] TYPE X Y  
---  
  
Click a keyword to view the command details.

See Also

  * Marker Readout [number](../Display.md#single) and [size](../Display.md#size) commands.

  * [Learn about Markers](../../../S4_Collect/Markers.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:AOFF

Applicable Models: All (Write-only) Turns all markers off for selected
measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:AOFF  
calculate2:measure2:marker:aoff  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<n>:BUCKet <num>

Applicable Models: All (Read-Write) Sets and reads the data point (bucket)
number of the trace on which the marker resides. When the markers are
[interpolated (non-discrete](../../../S4_Collect/Markers.md#discrete)), the
returned value is the nearest marker bucket position.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number to move or query. The marker must already exist. If unspecified, <n> is set to 1.  
<num> | Data point (bucket) number. Choose any data point between: 0 and the number of data points minus 1.  
Examples | CALC:MEAS:MARK:BUCK 5 calculate2:measure2:marker2:bucket 200  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<n>:BUCKet?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The first marker is set to the middle of the span. Subsequent markers are set to the bucket number of the previously active marker.  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:BWIDth:DATA?

Applicable Models: All (Read-only) Read the bandwidth search result of marker
1 to 15 and reference marker (Mkr:16), for the active trace of selected
channel. If the bandwidth search is impossible, an error occurs when executed
and the object is ignored.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; If unspecified, value is set to 1.  
| Four Character values separated by commas => {numeric 1}, {numeric 2},
{numeric 3}, {numeric 4}

  * {numeric 1} : Bandwidth
  * {numeric 2} : Center point frequency of the 2 cutoff frequency points
  * {numeric 3} : Q value
  * {numeric 4} : Insertion loss

  
Examples | CALC:MEAS:MARK:BWID:DATA?  
calculate2:measure1:marker:bwidth:data?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:BWIDth:DATA?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:BWIDth:REF <string>

Applicable Models: All (Read-Write) Set the bandwidth marker function
reference to either MARKer or PEAK. If the reference is set to MARKer, the
active marker is not moved; the bandwidth search is computed at the marker's
current location. If the reference is PEAK, the active marker is moved to the
maximum or minimum peak on the trace and then bandwidth search is computed.

  * If the bandwidth level is negative, the active marker is moved to the maximum peak.
  * If the bandwidth level is positive, the active marker is moved to the minimum peak.

  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<string> | PEAK _MARKer_  
Examples | CALC:MEAS:MARK:BWID:REF MARK  
calculate2:measure1:marker:bwidth:ref peak  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:BWIDth:REF?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MARKer  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:BWIDth[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the bandwidth search
result display, for the active trace of selected channel .  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | Bandwidth search result display: ON or 1 \- Turns ON the bandwidth search result display. OFF or 0 \- Turns OFF the bandwidth search result display.  
Examples | CALC:MEAS:MARK:BWID ON  
calculate2:measure1:marker:bwidth:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:BWIDth[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:BWIDth:THReshold <value><unit>

Applicable Models: All (Read-Write) Sets or returns the bandwidth definition
value (the value to define the pass-band of the filter) of marker 1 to 15 and
reference marker (Mk:16), for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<value> | Bandwidth definition value (the value to define the pass band of the filter) is between -5E8 to 5E8.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:BWID:THR -3  
calculate2:measure1:marker:bwidth:threshold -3  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:BWIDth:THReshold?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -3  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:COUPling:METHod <char>

Applicable Models: All (Read-Write) Sets and reads the scope of Coupled
Markers. This is a global setting that affects all markers. [Learn
more.](../../../S4_Collect/Markers.htm#Coupled_Markers) Note: This command
will not take effect until Coupled Markers is turned on using
CALC:MEAS:MARK:COUP:STATe ON. Note: The preset behavior of Coupled Markers
depends on the setting of
[SYSTem:PREFerences:ITEM:MCControl](../System_Preferences.md#markerCouplControl),
[SYSTem:PREFerences:ITEM:MCMethod](../System_Preferences.md#markerCoupleMethod),
and
[SYSTem:PREFerences:ITEM:MCPRest](../System_Preferences.md#MarkerCouplPreset).
Note: If any or all <cnum>, <mnum>, or <mkr> arguments are omitted, they are
assumed to have the value 1.  
---  
Parameters |   
<cnum> | Must be a valid channel number (unless a measurement number is provided), but marker coupling is not set per channel.  
<mnum> | Must be a valid measurement number and must be displayed on the screen. Marker coupling is not set per measurement.  
<mkr> | Not used. The marker number must still be in the range of 1-16, but marker coupling is not set per marker.  
<char> | CHANnel \- Coupling is limited to traces in the same channel. ALL \- Coupling occurs across all channels.  
Examples | CALC:MEAS:MARK:COUP:METH CHAN calculate:measure:marker:coupling all  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:COUPling:METHod?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ALL  
  
* * *

## CALCulate:MEASure<mnum>:MARKer<mkr>:COUPling[:STATe]<ON|OFF>

Applicable Models: All (Read-Write) Sets and reads the state of Coupled
Markers (ON and OFF). The scope of coupled markers can be changed with
CALC:MEAS:MARK:COUP:METH. Note: If the <mnum> or <mkr> argument is omitted,
they are assumed to have the value 1.  
---  
Parameters |   
<mnum> | Must be a valid measurement number and must be displayed on the screen.  
<mkr> | Not used. The marker number must still be in the range of 1-16.  
<ON|OFF> | OFF (0) - Turns Coupled Markers OFF ON (1) \- Turns Coupled Markers ON  
Examples | CALC:MEAS:MARK:COUP ON  
calculate:measure1:marker:coupling off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:COUPling:[STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:DELTa <ON|OFF>

Applicable Models: All (Read-Write) Specifies whether marker is relative to
the Reference marker or absolute. Note: The reference marker must already be
turned ON with [CALC:MARK:REF:STATE](Marker.md#rstate).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - Specified marker is a Delta marker OFF (or 0) - Specified marker is an ABSOLUTE marker  
Examples | CALC:MEAS:MARK:DELT ON calculate2:measure1:marker8:delta off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:DELTa?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:DISCrete <ON|OFF>

Applicable Models: All (Read-Write) Makes the specified marker display either
a calculated value between data points (interpolated data) or the actual data
points (discrete data).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - Specified marker displays the actual data points  
OFF (or 0) - Specified marker displays calculated data between the actual data
points.  
Examples | CALC:MEAS:MARK:DISC ON  
calculate2:measure2:marker8:discrete off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:DISCrete?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:DISTance <num>

Applicable Models: All (Read-Write) Set or query marker distance on a time
domain trace. The Write command moves the marker to the specified distance
value. Once moved, you can [read the Y axis](Marker.md#Y) value or [read the
X-axis time](Marker.htm#X) value. (Distance is calculated from the X-axis time
value.) The Read command reads the distance of the marker. If the marker is
set as delta, the WRITE and READ data is relative to the reference marker.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Marker distance in the unit of measure specified with [CALC:TRAN:TIME:MARK:UNIT](Transform_Calc.md#MarkerUnit)  
Examples | CALC:MEAS:MARK:DIST .1  
calculate2:measure1:marker8:distance 5  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:DISTance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FORMat <char>

Applicable Models: All (Read-Write) Sets the format of the data that will be
returned in a marker data query CALC:MARK:Y? and the displayed value of the
marker readout. The selection does not have to be the same as the
measurement's display format.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<char> | Choose from:  
DEFault \- The format of the selected measurement MLINear \- Linear magnitude
MLOGarithmic \- Logarithmic magnitude IMPedance \- (R+jX) ADMittance \- (G+jB)
PHASe \- Phase IMAGinary \- Imaginary part (Im) REAL \- Real part (Re) POLar
\- (Re, Im) GDELay \- Group Delay LINPhase - Linear Magnitude and Phase
LOGPhase - Log Magnitude and Phase KELVin - temperature FAHRenheit -
temperature CELSius - - temperature NOISe \- Noise (available ONLY in [IM
Spectrum](../../../Applications/IMSpectrum.htm) and
[SA](../../../Applications/Spectrum_Analyzer.md) measurement classes).  
Examples | CALC:MEAS:MARK:FORMat MLIN  
calculate2:measure:marker8:format Character  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FORMat?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | DEFault  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:APEak:POLarity <char>

Applicable Models: All (Read-Write) Sets or returns polarity of the peak
search with marker 1 to 15 and reference marker (Mk:16), for the active trace
of selected channel. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Polarity for peak search function to be performed. Choose from:

  * "NEGative" : Specifies the negative peak.
  * "POSitive" : Specifies the positive peak.
  * "BOTH" : Specifies both the positive peak and the negative peak.

  
Examples | CALC:MEAS:MARK:FUNC:APE:POL NEG  
calculate2:measure1:marker6:function:apeak:polarity both  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:APEak:POLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "POSitive"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:COMPression:LEVel <num>

Applicable Models: All (Read-Write) Sets and read the marker compression
level. A compression marker must already exist. Use [CALC:MARK
ON](Marker.htm#state) and [CALC:MEAS:MARK:FUNC COMP](Marker.md#fselect) to
create compression markers.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Compression level. Choose any number between: -500 dB to 500 dB Standard gain compression values are positive.  
Examples | CALC:MEAS:MARK:FUNC:COMP:LEV 1  
calculate2:measure1:marker:function:compression:level 1.5  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:COMPression:LEVel?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | +1 dB  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:COMPression:PIN?

Applicable Models: All (Read-only) Read the input power at the marker
compression level. First send [CALC:MEAS:MARK:FUNC:EXEC COMP](Marker.md#fexe)
or [CALC:MEAS:MARK:FUNC:TRAC ON](Marker.md#track).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
Examples | CALC:MEAS:MARK:FUNC:COMP:PIN?  
calculate2:measure1:marker:function:compression:pin?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:COMPression:POUT?

Applicable Models: All (Read-only) Read the output power at the marker
compression level. First send [CALC:MEAS:MARK:FUNC:EXEC COMP](Marker.md#fexe)
or [CALC:MEAS:MARK:FUNC:TRAC ON](Marker.md#track)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
Examples | CALC:MEAS:MARK:FUNC:COMP:POUT?  
calculate2:measure1:marker:function:compression:pout?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:COMPression[:STATe]
<bool>

Applicable Models: All (Read-Write) Turns ON or OFF the compression state.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | Bandwidth search result display: ON or 1 \- Turns ON the compression. OFF or 0 \- Turns OFF the compression.  
Examples | CALC:MEAS:MARK:FUNC:COMP:STAT ON  
calculate2:measure1:marker:function:compression:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:FUNCtion:COMPression[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:DOMain:USER[:RANGe]
<range>

Applicable Models: All (Read-Write) Assigns the specified marker to a range
number. The x-axis travel of the marker is constrained to the range's span.
The span is specified with the
[CALC:MEAS:MARK:FUNC:DOM:USER:START](Marker.md#ustart) and
[STOP](Marker.md#ustop) commands, unless range 0 is specified which is the
full span of the analyzer. Each channel has 16 user ranges. (Trace statistics
use the same ranges.) More than one marker can use a domain range.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<range> | User span. Choose any Integer from 0 to 16. 0 is Full Span of the analyzer. 1 to 16 are available for user-defined x-axis span.  
Examples | CALC:MEAS:MARK:FUNC:DOM:USER:RANG 1  
calculate2:measure1:marker8:function:domain:user:range 1  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:DOMain:USER:RANGe?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 \- Full Span  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STARt
<start>

Applicable Models: All (Read-Write) Sets the start of the span that the
specified marker's x-axis span will be constrained to. Use
[CALC:MEAS:MARK:FUNC:DOM:USER<range>](Marker.md#rang) to set range number.
Use [CALC:MEAS:MARK:FUNC:DOM:USER:STOP](Marker.md#ustop) to set the stop
value. Note: If the marker is assigned to range 0 (full span), the USER:STARt
and STOP commands generate an error. You cannot set the STARt and STOP values
for "Full Span". Note: This command does the same as
[CALC:FUNC:DOM:USER:STAR](Function.md#start)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<start> | The analyzer's Minimum x-axis value  
Examples | CALC:MEAS:MARK:FUNC:DOM:USER:START 500E6  
calculate2:measure1:marker8:function:domain:user:start 1e12  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The analyzer's Minimum x-axis value  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STOP <stop>

Applicable Models: All (Read-Write) Sets the stop of the span that the
marker's x-axis travel will be constrained to. Use
[CALC:MEAS:MARK:FUNC:DOM:USER<range>](Marker.md#rang) to set range number.
Use [CALC:MEAS:MARK:FUNC:DOM:USER:STARt](Marker.md#ustart) to set the stop
value. Note: If the marker is assigned to range 0 (full span), the USER:STARt
and STOP commands generate an error. You cannot set the STARt and STOP values
for "Full Span". Note: This command does the same as
[CALC:FUNC:DOM:USER:STOP](Function.md#stop)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<stop> | Stop value of x-axis span; Choose any number between the analyzer's MINimum and MAXimum x-axis value.  
Examples | CALC:MEAS:MARK:FUNC:DOM:USER:STOP 500e6  
calculate2:measure1:marker8:function:domain1:user:stop 1e12  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:DOMain:USER:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The analyzer's MAXimum x-axis value.  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:EXECute <func>

Applicable Models: All (Write-only) Immediately executes (performs) the
specified search function. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<func> | The function to be performed. Choose from:

  * MAXimum \- finds the highest value.
  * MINimum \- finds the lowest value.
  * RPEak \- finds the next valid peak to the right.
  * LPEak - finds the next valid peak to the left.
  * NPEak \- finds the next highest value among the valid peaks.
  * TARGet \- finds the target value to the right, wraps around to the left.
  * LTARget \- finds the next target value to the left of the marker.
  * RTARget \- finds the next target value to the right of the marker.
  * PEAK - finds the peak value.
  * COMPression \- finds the compression level on a Power Swept S21 trace.
  * SPURious - finds spurious signals based on [spurious settings](../../../Applications/Phase_Noise/Configuring_Phase_Noise.md#Spurious_Tab).
  * LSPurious - finds the next spurious signal to the left.
  * RSPurious - finds the next spurious signal to the right.

  
Examples | CALC:MEAS:MARK:FUNC:EXEC MAX  
calculate2:measure1:marker2:function:execute maximum  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:EXECute <func>

Applicable Models: All (Write-only) Immediately executes (performs) the
specified multi search function.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<func> | The function to be performed. Choose from:

  * OFF\- function is disabled.
  * PEAK\- finds the peak value of a multi-peak search.
  * TARGet \- finds the target value to the right, wraps around to the left.
  * SPURious \- finds spurious signals based on [spurious settings](../../../Applications/Phase_Noise/Configuring_Phase_Noise.md#Spurious_Tab).

  
Examples | CALC:MEAS:MARK:FUNC:MULT:EXEC PEAK  
calculate2:measure1:marker2:function:multi:execute target  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:PEAK:EXCursion
<num><unit>

Applicable Models: All (Read-Write) Sets or returns the lower limit of peak
excursion value of multi peak search, for the selected channel and selected
trace. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Excursion value. Choose any number between -500 and 500. Notes: If the specified variable is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:FUNC:MULT:PEAK:EXC 10  
calculate2:measure2:marker8:function:multi:peak:excursion maximum  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:PEAK:EXCursion?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:PEAK:POLarity
<func>

Applicable Models: All (Read-Write) Sets or returns the peak polarity of the
multi peak search, for the selected channel and selected trace. [Learn more
about Marker Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<func> | Polarity for multi peak search function to be performed. Choose from:

  * "NEGative : Specifies the negative peak.
  * "POSitive" : Specifies the positive peak.
  * "BOTH" : Specifies both the positive peak and the negative peak.

  
Examples | CALC:MEAS:MARK:FUNC:MULT:PEAK:POL NEG  
calculate2:measure1:marker6:function:multi:peak:polarity both  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:PEAK:POLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "POSitive"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:PEAK:THReshold
<num><unit>

Applicable Models: All (Read-Write) Sets peak threshold for the specified
marker. If a peak (using the criteria set with :EXCursion) is below this
reference value, it will not be considered when searching for peaks. This
command applies to marker peak searches (Next peak, Peak Right, Peak Left).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Excursion value. Choose any number between -500 and 500. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:FUNC:MULT:PEAK:THR -40  
calculate2:measure1:marker8:function:multi:peak:threshold -55  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:PEAK:THReshold?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -100  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:SELect<char>

Applicable Models: All (Read-Write) Sets or returns the search type of the
multi search, for the selected channel and selected trace. [Learn more about
Marker Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Select from the following:

  * "OFF": Turn OFF the multi search function.
  * "PEAK": Sets the search type to the multi peak search.
  * "TARGet": Sets the search type to the multi target search.

  
Examples | CALC:MEAS:MARK:FUNC:MULT:SEL BOTH  
calculate2:measure1:marker6:function:multi:select both  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:SELect?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "OFF"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:TARGet:TRANsition
<char>

Applicable Models: All (Read-Write) Sets the transition type of the multi
target search. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Transition type of multi target search function to be performed. Choose from:

  * "NEGative" : Specifies the negative transition.
  * "POSitive" : Specifies the positive transition.
  * "BOTH" : Specifies both the positive transition and the negative transition.

  
Examples | CALC:MEAS:MARK:FUNC:MULT:TARG:TRAN BOTH  
calculate2:measure1:marker6:function:multi:target:transition both  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:TARGet:TRansition?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "BOTH"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:TARGet[:VALue]
<num><unit>

Applicable Models: All (Read-Write) Sets or returns the target value for the
specified marker when doing Multi Target Search, for the selected channel and
selected trace. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Target value for multi target search to search for. The range of target value is -5E8 to 5E8. Notes: If the specified variable is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:FUNC:MULT:TARG 2.5  
calculate2:measure2:marker5:function:multi:target:value -10.3  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:TARGet[:VALue]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:TRACking <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the search tracking
capability (function to repeat search for each sweep) of the multi search, for
the selected channel and selected trace. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | **ON or 1** \- Turns ON the marker search tracking. The specified multi marker will "Track" (find) the selected function every sweep. **OFF or 0** \- Turns OFF the marker search tracking. The specified multi marker will find the selected function **only** when the CALC:MEAS:MARK:FUNC:EXECute command is sent.  
Examples | CALC:MEAS:MARK:FUNC:MULT:TRAC ON  
calculate2:measure2:marker8:function:multi:tracking off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:MULTi:TRACking?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:PEAK:EXCursion
<num><unit>

Applicable Models: All (Read-Write) Sets amplitude peak excursion for the
specified marker. The Excursion value determines what is considered a "peak".
This command applies to marker peak searches (Next peak, Peak Right, Peak
Left).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any existing marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Excursion value. Choose any number between -500 and 500. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:FUNC:PEAK:EXC 10  
calculate2:measure2:marker8:function:peak:excursion maximum  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:PEAK:EXCursion?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:PEAK:POLarity <char>

Applicable Models: All (Read-Write) Sets or returns polarity of the peak
search with marker 1 to 15 and reference marker (Mk:16), for the active trace
of selected channel. [Learn more about Marker
Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Polarity for peak search function to be performed. Choose from:

  * "NEGative" : Specifies the negative peak.
  * "POSitive" : Specifies the positive peak.
  * "BOTH" : Specifies both the positive peak and the negative peak.

  
Examples | CALC:MEAS:MARK:FUNC:APE:POL NEG  
calculate2:measure1:marker6:function:apeak:polarity both  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:APEak:POLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "POSitive"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:PEAK:THReshold
<num><unit>

Applicable Models: All (Read-Write) Sets peak threshold for the specified
marker. If a peak (using the criteria set with :EXCursion) is below this
reference value, it will not be considered when searching for peaks. This
command applies to marker peak searches (Next peak, Peak Right, Peak Left).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<num> | Excursion value. Choose any number between -500 and 500. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:FUNC:APE:THR -40  
calculate2:measure:marker8:function:apeak:threshold -55  
Query Syntax | CALCulate<cnum>:MARKer<mkr>:FUNCtion:APEak:THReshold?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -100  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion[:SELect] <char>

Applicable Models: All (Read-Write) Sets the search function that the
specified marker will perform when executed. Use [CALC:MEAS:MARK:FUNC:TRAC
ON](Marker.htm#track) to automatically execute the search every sweep. [Learn
more about Marker Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Marker function. Choose from:

  * MAXimum \- finds the highest value
  * MINimum \- finds the lowest value
  * TARGet \- finds the target value to the right, wraps around to the left
  * LTARget \- finds the next target value to the left of the marker
  * RTARget \- finds the next target value to the right of the markerRPEak \- finds the next valid peak to the right
  * PEAK - finds the highest value among the valid peaks
  * NPEak \- finds the next highest value among the valid peaks
  * LPEak - finds the next valid peak to the left
  * RPEak - finds the next valid peak to the right
  * COMPression \- finds the compression level on a power-swept S21 trace
  * SPURious - finds spurious signals based on [spurious settings](../../../Applications/Phase_Noise/Configuring_Phase_Noise.md#Spurious_Tab)
  * LSPurious - finds the next spurious signal to the left
  * RSPurious - finds the next spurious signal to the right
  * NONE

  
Examples | CALC:MEAS:MARK:FUNC MAX  
calculate2:measure1:marker8:function:select ltarget  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion[:SELect]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TRACking:EXTended <char>

Applicable Models: All (Read-Write) Set marker tracking function and activate
the tracking. This commands execute both
[CALC:MEAS:MARK:FUNC](MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:SELect)
and [CALC:MEAS:MARK:FUNC:TRAC ON](Marker.md#track) at the same time. [Learn
more about Marker Search](../../../S4_Collect/Markers.htm#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Marker function. Choose from:

  * MAXimum \- finds the highest value
  * MINimum \- finds the lowest value
  * TARGet \- finds the target value to the right, wraps around to the left
  * LTARget \- finds the next target value to the left of the marker
  * RTARget \- finds the next target value to the right of the markerRPEak \- finds the next valid peak to the right
  * PEAK - finds the highest value among the valid peaks
  * NPEak \- finds the next highest value among the valid peaks
  * LPEak - finds the next valid peak to the left
  * RPEak - finds the next valid peak to the right
  * COMPression \- finds the compression level on a power-swept S21 trace
  * SPURious - finds spurious signals based on [spurious settings](../../../Applications/Phase_Noise/Configuring_Phase_Noise.md#Spurious_Tab)
  * LSPurious - finds the next spurious signal to the left
  * RSPurious - finds the next spurious signal to the right
  * NONE

  
Examples | CALC:MEAS:MARK:FUNC:TRAC:EXT MAX  
calculate2:measure1:marker8:funcion:tracking:exteded ltarget  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TRACking:EXTended?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

##
CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TARGet[:VALue]:TRANsition
<char>

Applicable Models: All (Read-Write) Selects the transition type of the target
search for specified marker (marker 1 to 15 and reference marker (Mk:16)) of
the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<char> | Transition type for search function to be performed. Choose from:

  * "NEGative" : Specifies the negative transition.
  * "POSitive" : Specifies the positive transition.
  * "BOTH" : Specifies both the positive transition and the negative transition.

  
Examples | CALC:MEAS:MARK:FUNC:TARG:TRAN POS  
calculate2:measure1:marker8:function:target:value:transition both  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TARGet[:VALue]:TRANsition?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "BOTH"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TARGet[:VALue]
<num><unit>

Applicable Models: All (Read-Write) Sets the target value for the specified marker when doing Target Searches with [CALC:MEAS:MARK:FUNC:SEL](Marker.md#fselect) <TARGet | RTARget | LTARget>  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Target value to search for. The range of value is between -5E8 to 5E8. Notes: If the specified variable is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set.  
<unit> | Varies depending on the data format.

  * Log magnitude (MLOG): dB (decibel)
  * Phase (PHAS), Expanded phase (UPH) or Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:FUNC:TARG 2.5  
calculate2:measure1:marker8:function:target:value -10.3  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:TARGet[:VALue]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TRACking <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the tracking search
capability for the specified marker. The tracking function finds the selected
search function every sweep. In effect, turning Tracking ON is the same as
doing a [CALC:MEAS:MARK:FUNC:EXECute](Marker.md#fexe) command every sweep.
[Learn more about Marker Search](../../../S4_Collect/Markers.md#Searching)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | ON or 1 \- Turns ON the search tracking. The specified marker will "Track" (find) the selected function every sweep. OFF or 0 \- Turns OFF the search tracking. The specified marker will find the selected function only when the CALC:MEAS:MARK:FUNC:EXECute command is sent.  
Examples | CALC:MEAS:MARK:FUNC:TRAC ON  
calculate2:measure1:marker8:function:tracking off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:FUNCtion:TRACking?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh:DATA?

Applicable Models: All (Read-only) Reads the notch search result of marker 1
to 15 and reference marker (Mk:16), for the active trace of selected channel.
If the notch search is impossible, an error occurs and the command is ignored.
In this case, no query response is obtained.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
| Indicates 4-element array data (notch bandwidth search result). Four
Character values separated by commas => {Data 1}, {Data 2}, {Data 3}, {Data 4}

  * Data(0) :The bandwidth.
  * Data(1) :Center point frequency of the 2 cutoff frequency points.
  * Data(2) :The Q value.
  * Data(3) :Insertion loss

The index of the array starts from 0.  
Examples | CALC:MEAS:MARK:NOTC:DATA?  
calculate2:measure1:marker:notch:data?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh:DATA?  
Return Type | Variant  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh:REF <string>

Applicable Models: All (Read-Write) Set the notch marker reference to either
MARKer or PEAK. If the reference is set to MARKer, the active marker is not
moved; the notch search is computed at the marker's current location. If the
reference is set to PEAK, the active marker is moved to the maximum or minimum
peak on the trace and then notch search is computed.

  * If the notch level is negative, the active marker is moved to the maximum peak.
  * If the notch level is positive, the active marker is moved to minimum peak.

  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<string> | PEAK MARKer  
Examples | CALC:MEAS:MARK:NOTCh:REF  
calculate2:measure1:marker:notch:ref  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh:REF?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MARKer  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the notch search result
display, for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | Notch search result display. Choose from: ON or 1 \- Turns ON the notch search result display. OFF or 0 \- Turns OFF the notch search result display.  
Examples | CALC:MEAS:MARK:NOTC ON  
calculate2:measure1:marker:notch:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh:THReshold <num><unit>

Applicable Models: All (Read-Write) Sets or returns the notch definition value
of marker 1 to 15 and reference marker (Mk:16), for the active trace of
selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | The notch definition value range is between -5E8 to 5E8. Notes: If the specified parameter is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set.  
<unit> | Varies depending on the data format as follows:

  * Amplitude (MLOG):dB (decibel)
  * Phase (PHAS), Expanded phase (UPH),Positive phase (PPH): deg (degree)
  * Group delay (GDEL): s (second)
  * Others: No unit

  
Examples | CALC:MEAS:MARK:NOTC:THR -3  
calculate2:measure1:marker:notch:threshold -3  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:NOTCh:THReshold?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -3  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:BACKoff <num>

Applicable Models: All (Read-Write) Turns on and sets markers 1, 2, 3, and 4
to calculate various PNOP parameters. Either this command, or the
[POFFset](MarkerPNOP.md#Poffset) command, will initiate the PNOP search
markers. To turn off the PNOP markers, either turn them off individually or
turn them [All Off](Marker.md#aoff). To search a User Range with the PNOP
search, first activate marker 1 and set the desired [User
Range](Marker.htm#rang). Then send CALC:MARK:PNOP:BACK. The user range used
with the PNOP search only applies to marker 1 searching for the linear gain
value. The other markers may fall outside the user range.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Backoff value. Choose any number between :-500 and 500  
Examples | CALC:MEAS:MARK:PNOP:BACK? calculate2:measure1:marker:pnop:backoff 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:BACKoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:BACKoff:GAIN?

Applicable Models: All (Read-only) Reads the power backoff gain value from a
PNOP marker search. PBO Gain = PBO Out - PBO In Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS1:MARK:PNOP:BACK:GAIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:BACKoff:PIN?

Applicable Models: All (Read-only) Reads the power backoff input value from a
PNOP marker search. PBO In = Marker 2 X-axis Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS1:MARK:PNOP:BACK:PIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:BACKoff:POUT?

Applicable Models: All (Read-only) Reads the power backoff output value from a
PNOP marker search. PBO Out = Marker 2 Y-axis Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS1:MARK:PNOP:BACK:POUT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:COMPression?

Applicable Models: All (Read-only) Reads the PNOP compression value from a
PNOP marker search. Pnop Comp = Pnop Gain - Linear Gain (not shown on marker
readout). Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS1:MARK:PNOP:COMP?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:COMPression:MAXimum?

Applicable Models: All (Read-only) Reads the max compression value from a PNOP
marker search. Comp Max = Gain Max - Linear Gain (not shown on marker
readout). Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS1:MARK:PNOP:COMP:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:GAIN?

Applicable Models: All (Read-only) Reads the PNOP gain value from a PNOP
marker search. Pnop Gain = Pnop Out - Pnop In. Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:MARK:PNOP:GAIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:GAIN:MAXimum?

Applicable Models: All (Read-only) Reads the max gain from a PNOP marker
search. Gain Max = PMax Out - PMax In Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:MARK:PNOP:GAIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:PIN?

Applicable Models: All (Read-only) Reads the PNOP input value from a PNOP
marker search. Pnop In = Marker 4 X-axis value Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:MARK:PNOP:PIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:PIN:MAXimum?

Applicable Models: All (Read-only) Reads the max input power from a PNOP
marker search. PMax In = Marker 3 X-axis value Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:MARK:PNOP:PIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:POFFset <num>

Applicable Models: All (Read-Write) Turns on and sets markers 1, 2, 3, and 4
to calculate various PNOP parameters. Either this command, or the
[Backoff](MarkerPNOP.md#backoff) command, will initiate the PNOP search
markers. To turn off the PNOP markers, either turn them off individually or
turn them [All Off](Marker.md#aoff). To search a User Range with the PNOP
search, first activate marker 1 and set the desired [User
Range](Marker.htm#rang). Then send the CALC:MARK:PNOP:POFF command. The user
range used with the PNOP search only applies to marker 1 searching for the
linear gain value. The other markers may fall outside the user range.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Power Offset value in dB. Choose any number between :-500 and 500  
Examples | CALC:MEAS1:MARK:PNOP:POFF 3 calculate2:measure2:marker:pnop:poffset 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:POFFset?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:POUT?

Applicable Models: All (Read-only) Reads the output power value of the offset
marker from a PNOP marker search. Pnop Out = Marker 4 Y-axis value Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PNOP:POUT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PNOP:POUT:MAXimum?

Applicable Models: All (Read-only) Reads the max output power from a PNOP
marker search. PMax Out = Marker 3 Y-axis value Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PNOP:POUT:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:PNOP[:STATe] <ON|OFF>

Applicable Models: All (Read-Write) Turns the PNOP marker search ON and OFF.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - turns marker ON. OFF (or 0) - turns marker OFF.  
Examples | CALC:MEAS1:MARK:PNOP ON  
calculate2:measure2:marker8:pnop on  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:PNOP:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Off  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:BACKoff <num>

Applicable Models: All (Read-Write) Turns on and sets markers 1, 2, and 3 to
calculate various Power Saturation parameters. The <num> parameter sets and
reads the back-off value for a Power Saturation marker search. To turn off the
Power Saturation markers, either turn them off individually or turn them [All
Off](Marker.htm#aoff). To search a User Range with the PSAT search, first
activate marker 1 and set the desired [User Range](Marker.md#rang). Then send
the CALC:MARK:PSAT:BACK command. The user range used with the PSAT search only
applies to marker 1 searching for the linear gain value. The other markers may
fall outside the user range.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Backoff value. Choose any number between :-500 and 500  
Examples | CALC:MEAS2:MARK:PSAT:BACK 3  
calculate2:measure2:marker:psaturation:backoff 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:BACKoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:COMPression:MAXimum?

Applicable Models: All (Read-only) Reads the compression maximum value from a
PSAT marker search. Comp Max = Gain Max - Gain Linear Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:COMP:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:COMPression:SATuration?

Applicable Models: All (Read-only) Reads the compression saturation value from
a PSAT marker search. Comp Sat = Gain Sat - Gain Linear Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:COMP:SAT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:GAIN?

Applicable Models: All (Read-only) Reads the saturation gain value from a PSAT
marker search. Gain Sat = Psat Out - Psat In Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:GAIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:GAIN:LINear?

Applicable Models: All (Read-only) Reads the linear gain value from a PSAT
marker search. Gain Linear = Marker 1 - Y-axis value MINUS X-axis value. Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:GAIN:LIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:GAIN:MAXimum?

Applicable Models: All (Read-only) Reads the maximum gain value from a PSAT
marker search. Gain Max = PMax Out - PMax In Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:GAIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:PIN?

Applicable Models: All (Read-only) Reads the power saturation input value from
a PSAT marker search. Psat In = Marker 2 X-axis value Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:PIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:PIN:MAXimum?

Applicable Models: All (Read-only) Reads the maximum input power from a PSAT
marker search. PMax In = Marker 3 X-axis value Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:PIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:POUT?

Applicable Models: All (Read-only) Reads the back-off output power from a PSAT
marker search. PSat Out = Marker 2 Y-axis value Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:POUT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer:PSATuration:POUT:MAXimum?

Applicable Models: All (Read-only) Reads the back-off output power from a PSAT
marker search. PMaxOut = Marker 3 Y-axis value Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:MARK:PSAT:POUT:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:PSATuration[:STATe] <ON|OFF>

Applicable Models: All (Read-Write) Turns the PSAT marker search ON and OFF.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> | ON (or 1) - turns marker ON. OFF (or 0) - turns marker OFF.  
Examples | CALC:MEAS1:MARK:PSAT ON  
calculate2:measure2:marker8:psaturation on  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:PSATuration:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Off  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:REFerence[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the reference marker mode,
for the active trace of selected channel. When turned OFF, existing Delta
markers revert to absolute markers.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | ON or 1 \- Turns reference marker mode ON. OFF or 0 \- Turns reference marker mode OFF.  
Examples | CALC:MEAS:MARK:REF ON  
calculate2:measure1:marker:reference:state OFF  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:REFerence[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:REFerence:X <num>

Applicable Models: All (Read-Write) Sets and returns the absolute x-axis value
of the reference marker.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | X-axis value. Choose any number within the operating domain of the reference marker.  
Examples | CALC:MEAS:MARK:REF:X 1e9 calculate2:measure1:marker:reference:x 1e6  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:REFerence:X?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | If the first Marker, turns ON in the middle of the X-axis span. If not, turns ON at the position of the active marker.  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:REFerence:Y <num>

Applicable Models: All (Read-Write) Sets and returns the absolute Y-axis value
of the reference marker (Set the reference marker Y position only when the
marker is a fixed marker type).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Y-axis value. Choose any number within the operating domain of the reference marker.  
Examples | CALC:MEAS:MARK:REF:Y 1e6 calculate2:measure1:marker:reference:y 1e9  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:SET <char>

Applicable Models: All (Write-only) Sets the selected instrument setting to
assume the value of the specified marker. Marker Functions CENT, SPAN, STARt,
and STOP do not work with channels that are in
[CW](../../../S1_Settings/Sweep.md#SweepTypeDiag) or [Segment
Sweep](../../../S1_Settings/Sweep.htm#segment) mode.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<char> | Choose from:

  * CENTer - changes center frequency to the value of the marker.
  * SPAN \- changes the sweep span to the span that is defined by the delta marker and the marker that it references. Unavailable if there is no delta marker.
  * STARt - changes the start frequency to the value of the marker.
  * STOP - changes the stop frequency to the value of the marker.
  * RLEVel \- changes the reference level to the value of the marker.
  * DELay \- changes the line length at the receiver input to the phase slope at the active marker stimulus position.
  * CWFReq \- Sets the CW frequency to the frequency of the active marker. Does NOT change sweep type. NOT available in CW or Power Sweep. Use this argument to first set the CW Frequency to a value that is known to be within the current calibrated range, THEN set [Sweep:Type](../Sense/Sweep_SCPI.md#ssty) to POWer or CW.
  * SA \- creates an SA channel with a marker at the same CW frequency. [Learn more](../../../Applications/Spectrum_Analyzer.md#MarkerToSA).

  
Examples | CALC:MEAS:MARK:SET CENT  
calculate2:measure1:marker8:set span  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the specified marker.
Marker 16 is the Reference Marker. To turn all markers OFF, use
[CALC:MEAS:MARK:AOFF](Marker.md#aoff).
Note:[SYSTem:PREFerences:ITEM:REFMarker](../System_Preferences.md#REFMarker)
must be set to OFF (0) for marker 16 to be used as the reference marker. If
[SYSTem:PREFerences:ITEM:REFMarker](../System_Preferences.md#REFMarker) is
set to ON (1) for legacy behavior, marker 10 is the reference marker.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<bool> | ON or 1 \- Turns marker ON.  
OFF or 0 \- Turns marker OFF.  
Examples | SYST:PREF:ITEM:REFM 0 'disable marker 10 as the reference marker  
CALC:MEAS:MARK ON  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:TYPE <char>

Applicable Models: All (Read-Write) Sets the type of the specified marker.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1  
<char> | Choose from:

  * NORMal \- a marker that stays on the assigned X-axis position unless moved or searching.
  * FIXed \- a marker that will not leave the assigned X or current Y-axis position.

  
Examples | CALC:MEAS:MARK:TYPE NORM  
calculate2:measure1:marker2:type fixed  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NORMal  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:X <num>

Applicable Models: All (Read-Write) Sets the marker's X-axis value (frequency,
power, or time). If the marker is set as delta, the SET and QUERY data is
relative to the reference marker.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
<num> | Any X-axis position within the measurement span of the marker. (When the span value of the sweep range is 0, the range is from 0 to sweep time value.) Notes: If the specified variable is out of the allowable setup range, the minimum value (if the lower limit of the range is not reached) or the maximum value (if the upper limit of the range is exceeded) is set. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
<unit> | Hz (hertz), dBm or s (second)  
Examples | CALC:MEAS:MARK:X 100Mhz  
calculate2:measure1:marker8:x maximum  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:X?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | First Marker turns ON in the middle of the X-axis span. Subsequent markers turn ON at the position of the active marker. (When the span value of the sweep range is 0, the preset value is 0.)  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:Y?

Applicable Models: All (Read-only) Reads the marker's Y-axis value. The format
of the value depends on the current [CALC:MEAS:MARK:FORMAT](Marker.md#form)
setting. If the marker is set as delta, the data is relative to the reference
marker. The query always returns two numbers:

  * Smith and Polar formats - (Real, Imaginary)
  * LINPhase and LOGPhase - (Real, Imaginary)
  * All other formats \- (Value,0)

Note: To accurately read the marker Y-axis value with [trace
smoothing](../../../S2_Opt/Trce_Noise.htm#Smoothing) applied, the requested
format must match the [displayed
format](../../../S1_Settings/Data_Format.htm#FormatDiag). Otherwise, the
returned value is un-smoothed data. For example, to read the smoothed marker
value when measuring group delay, both the display format and the marker
format must be set to (Group) Delay.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<mkr> | Any marker number from 1 to 15; if unspecified, value is set to 1.  
Examples | CALC:MEAS:MARK:Y?  
calculate2:measure1:marker3:y?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:MARKer<mkr>:Y?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

