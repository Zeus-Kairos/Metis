# Display Commands

* * *

Controls the settings of the front panel screen.

DISPlay: ANNotation | [FREQuency[:STATE]](Display.md#fstate) | [MESSage:STATe](Display.md#message) | [:[STATus](Display.md#annstatus)] [ARRange](Display.md#arrange) [CATalog?](Display.md#cat) DISP:CHANnel: | [NEW](Display.md#ChanNew) | [STATe](Display.md#ChanStat) [COLor More Commands](Display_Colors.md) [ENABle](Display.md#enable) [FSIGn](Display.md#fsign) GUI | POWer | SPIN | RESolution MEASure | DELete | FEED | MEMory | [:STATe] | MOVE | SELect | [:STATe] | TITLe | DATA | [:STATe] | [TYPe](Display.md#MeasType) | Y[:SCALe] | AUTO | PDIVision | RLEVel | RPOSition SHEet | ARRange | CATalog | LIST | [NEW](Display.md#SheNew) | STATe | TITle:DATA SIZE SPLit STATus | LOG | CLEar | [SCPI](Display.md#StatSCPI) [TDR More Commands](TDR_Display.md) [TMAX](Display.md#TMax) [TILE](Display.md#tile) TOOLbar | CSET[:STATe] | [ENTRy[:STATe]](Display.md#toolEntry) | [EXTensions[:STATe]](Display.md#extensions) | [KEYS[:STATe]](Display.md#keys) | [MARKer[:STATe](Display.md#toolMarker)] | [MEAS[:STATe]](Display.md#toolMeas) | [STIMulus](Display.md#toolStim)[[:STATe]](Display.md#toolMarker) | [SWEep[:STATe]](Display.md#toolSweep) | [TRANsform[:STATe]](Display.md#transform) [TRACe](Display.md#TracStat) | [NEW](Display.md#TracNew) | [STATe](Display.md#TracStat) UPDate | IMMediate | [:STATe] [VISible](Display.md#visible) WINDow | ANNotation | LIMit | [XPOSition](Display.md#limitX) | [YPOSition](Display.md#limitY) | MARKer | COUPle | NUMBer | MEASre | [XPOSition](display.md#MarkMeasXpox) | [YPOSition](display.md#MarkMeasYpos) | [NUMBer](Display.md#MarkerNumber) | RESolution | [RESPonse](Display.md#MarkerResolResponse) | [STIMulus](Display.md#MarkerResoStimulus) | [SINGle[:STATe]](Display.md#single) | [SIZE](Display.md#size) | [STATe](Display.md#mstatus) | [SYMBol](Display.md#MarkerSymbol) | [ABOVe[:STATe]](Display.md#MarkerSymbolAbove) | [VISible](Display.md#DISPlayWINDowANNotationMARKerVISible) | [XPOSition](Display.md#MarkerXposition) | [YPOSition](Display.md#MarkerYposition) | [:STATe] | [[TRACe]](Display.md#trstatus) | SCOPe | [[:STATe]](Display.md#trstatus) | X[:STATe] | [XAXis:SCOPe](Display.md#AnnXaxScop) | Y[:STATe] | [CATalog?](Display.md#dwc) | [ENABle](Display.md#wenable) | FEED | NEXT[:NUMBer]? [ | NEW](Display.md#WindNew) | [SIZE](Display.md#WinSize) | [[STATe]](Display.md#dwstat) | [TABLe](Display.md#tabl) | INOise | ENABle | SNOise | ENABle | SPURious | ENABle | TITLe | [DATA](Display.md#titdata) | [[STATe]](Display.md#titstate) | TRACe | [DELete](Display.md#tdel) | [FEED](Display.md#dwtf) | MNUMber | [GRATicule:GRID:LTYPe](Display.md#GridLtype) | [MEMory[:STATe]](Display.md#memstate) | [MOVE](Display.md#traceMove) | NEW | NEXT[:NUMBer]? | [SELect](Display.md#tselect) | [[STATe]](Display.md#tstat) | TITLe | [DATA](Display.md#TraceTitleData) | [[:STATe]](Display.md#TraceTitleState) | X[:SCALe] | RLEVel | RPOSition | Y[:SCALe] | [AUTO](Display.md#yauto) | BOTTom | COUPle | [METHod](Display.md#scaleCouplMethod) | [[STATe]](Display.md#scaleCouplState) | [PDIVision](Display.md#pdiv) | [RLEVel](Display.md#rlev) | [RPOSition](Display.md#rpos) | TOP | Y:SPACing | [Y:AUTO](Display.md#AutoscaleAll) | Y[:SCALe] | DIVisions  
---  
  
Click on a keyword to view the command details.

Blue keywords are [superseded.](../Replacement_Commands.md)

See Also

  * [Referring to Traces Channels Windows and Meas Using SCPI](../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.md)

  * See an [example](../GPIB_Example_Programs/Catalog_Measurements_using_SCPI.md) using some of these commands

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [Learn about Screen Setup](../../S1_Settings/Customize_Your_Analyzer_Screen.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## DISPlay:ANNotation:FREQuency[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns frequency information on the display
title bar ON or OFF for all windows.  
---  
Parameters |   
<ON | OFF> |  ON (or 1) - turns frequency annotation ON.  
OFF (or 0) - turns frequency annotation OFF.  
Examples |  DISP:ANN:FREQ ON  
display:annotation:frequency:state off  
Query Syntax |  DISPlay:ANNotation:FREQuency[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON (1)  
  
* * *

## DISPlay:ANNotation:MESSage:STATe <ON | OFF>

Applicable Models: All (Read-Write) Enables and disables error pop-up messages
on the display.  
---  
Parameters |   
<ON | OFF> |  ON (or 1) - enables error pop-up messages  
OFF (or 0) - disables error pop-up messages  
Examples |  DISP:ANN:MESS:STAT ON  
display:annotation:message:state off  
Query Syntax |  DISPlay:ANNotation:MESSage:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON (1)  
  
* * *

## DISPlay:ANNotation[:STATus] <ON | OFF>

Applicable Models: All (Read-Write) Turns the status bar at the bottom of the
screen ON or OFF. The status bar displays information for the active window.  
---  
Parameters |   
<ON | OFF> |  ON (or 1) - turns status bar ON.  
OFF (or 0) - turns status bar OFF.  
Examples |  DISP:ANN ON  
display:annotation:status off  
Query Syntax |  DISPlay:ANNotation[:STATus]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Last state that was set  
  
* * *

## DISPlay:ARRange <char>

Applicable Models: All (Write-only) Places EXISTING measurements into pre-
configured window arrangements. Overlay, Stack(2), Split(3), and Quad(4)
creates new windows. To learn more, see [Window
Layout](../../S0_Start/Traces_Channels_and_Windows.htm#Window_Layout).  
---  
Parameters |   
<char> |  Window arrangement. Choose from:

  * TILE - tiles existing windows
  * CASCade - overlaps existing windows
  * OVERlay - all traces placed in 1 window
  * STACk - 2 windows
  * SPLit - 3 windows
  * QUAD - 4 windows
  * MEASure - 1 measurement per window
  * CHANnel - 1 channel per window
  * LTOR - Arrange existing windows as a single row of side-by-side windows.

  
Examples |  DISP:ARR CASC  
display:arrange cascade  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  TILE  
  
* * *

## DISPlay:CATalog?

Applicable Models: All (Read-only) Returns the existing Window numbers.  Note:
If there are no traces in the window, this query returns the "EMPTY" string.
To read the window number of the selected trace, use
[Calc:Par:WNUM](Calculate/Parameter.md#wnum).  
---  
Return Type |  String of Character values, separated by commas  
Example |  Two windows with numbers 1 and 2 returns:  
"1,2"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## DISPlay:CHANnel:NEW [<int>]

Applicable Models: All  (Write-only) Add a new channel according to the <int>
parameter.  
---  
Parameters |   
<int> |  Add Type (optional) - 0: Trace + Channel (default), 1: Trace + Channel + Window  
Examples |  DISP:CHAN:NEW 1  
display:channel:new  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:CHANnel:<ch>STATe <ON | OFF>

Applicable Models: All (Read-Write) Create or delete the specified channel. If
set ON to an existing channel, just activate the channel.  
---  
Parameters |   
<ch> |  Channel Number. Default is 1.  
<ON | OFF> |  ON (or 1) - creates the channel OFF (or 0) - deletes the channel  
Examples |  DISP:CHAN2:STAT 1 display:channel3:state on  
Query Syntax |  DISPlay:CHANnel:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON (1) for Channel 1, OFF(0) for other channels  
  
* * *

## DISPlay:ENABle <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether to disable or enable all
analyzer display information in all windows in the analyzer application.
Marker data is not updated. More CPU time is spent making measurements instead
of updating the display.  
---  
Parameters |   
<ON | OFF> |  ON (or 1) - turns the display ON.  
OFF (or 0) - turns the display OFF.  
Examples |  DISP:ENAB ON  
display:enable off  
Query Syntax |  DISPlay:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:FSIGn <ON | OFF>

Applicable Models: All (Read-Write) Shows or hides the window which displays
global pass/fail results.  
---  
Parameters |   
<ON | OFF> |  ON (or 1) - displays the pass/fail dialog OFF (or 0) - hides the pass/fail dialog  
Examples |  DISP:FSIG ON  
display:fsign off  
Query Syntax |  DISPlay:FSIGn?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:GUI:POWer:SPIN:RESolution <real>

Applicable Models: All (Read-Write) Sets and returns the resolution of the
front panel knob when it is used to adjust Source Power manually.  
---  
Parameters |   
<real> |  Spin resolution value (Real value). The range of acceptable values is 0.01 to 100.  
Examples |  DISP:GUI:POW:SPIN:RES 0.01 'Write - Every tick of the front panel knob will change the Power Level by 0.01 dBm.  
display:gui:power:spin:resolution 0.01  
Query Syntax |  DISPlay:GUI:POWer:SPIN:RESolution?  
Return Type |  Real  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0.1  
  
* * *

## DISPlay:MEASure<mnum>:DELete

Applicable Models: All  (Write-only) Deletes the trace associated with the
specified measurement number.  Note: The measurement is not deleted. This
command does the reverse of [DISP:MEAS:FEED](Display.md#MeasFeed).  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
Examples |  DISP:MEAS:DEL  
display:measure2:delete  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:MEASure<mnum>:FEED <wnum>

Applicable Models: All (Write-only) This command creates a new trace in the
specified window and connects the trace to measurement which results in the
trace displaying the data from measurement.  
---  
Parameters |   
<mnum> |  Measurement number for the measurement. If unspecified, <mnum> is set to 1.  
<wnum> |  Display the measurement in a specified Window number. The window must be turned on. In addition, a window number must be specified. The range is 1 to 500.  
Examples |  DISP:MEAS2:FEED 10  
display:measure:feed 90  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:MEASure<mnum>:MEMory[:STATe] <bool>

Applicable Models: All (Read-Write) Turns the memory trace ON or OFF for the
specified measurement. Note: [DISP:MEAS:FEED](Display.md#MeasFeed) must first
be done to feed the measurement to a trace. This command behaves the same as
[DISP:WIND:TRAC:MEM[:STAT]](Display.md#memstate) except that it only requires
the measurement number.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<bool> |  ON or 1 \- Turns the memory trace ON.  
OFF or 0 \- Turns the memory trace OFF.  
Examples |  DISP:MEAS:MEM ON  
display:measure:memory:state off  
Query Syntax |  DISPlay:MEASure<mnum>:MEMory[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:MEASure<mnum>:MOVE <toWin>

Applicable Models: All (Write-only) Moves a trace associated with measurement
number to the specified window. If the window is OFF, it will be turn ON.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<toWin> |  Number of the window to which the specified measurement is moved. If the window does not exist, it will be created.  
Examples |  DISP:MEAS:MOVE 2  
display:measure:move 1  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:MEASure<mnum>:SELect

Applicable Models: All (Write-only) Activates the specified measurement to be
selected.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
Examples |  DISP:MEAS:SEL  
display:measure:select  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:MEASure<mnum>[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the display of a trace
associated with the specified measurement. When OFF, the measurement behind
the trace is still active.  Note: A trace must first be created (via FEED),
then the visibility of the trace can be affected with this command. If the
trace has not been created, an error is generated: 107,Requested trace not
found.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<bool> |  ON or 1 \- Turns the trace ON.  
OFF or 0 \- Turns the trace OFF.  
Examples |  DISP:MEAS:STAT ON  
display:measure off  
Query Syntax |  DISPlay:MEASure<mnum>[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON or 1  
  
* * *

## DISPlay:MEASure<mnum>:TITLe:DATA <string>

Applicable Models: All (Read-Write) Sets or gets the title for the specified
measurement. The trace title is embedded in the trace status field. [Learn
more about Trace
Titles](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle).
Newer entries replace (not append) older entries. The title is turned ON and
OFF with [DISP:WIND:TRAC:TITL:STAT](Display.md#TraceTitleState).  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<string> |  Used as the title to be displayed for the measurement. Any characters (not spaces) enclosed with quotes.  
Examples |  DISP:MEAS:TITL:DATA 'MyNewMeas'  
display:measure:title:data 'hello'  
Query Syntax |  DISPlay:MEASure<mnum>:TITLe:DATA?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:MEASure<mnum>:TITLe[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the measurement title.
Note: The measurement and trace need to exist. When turned OFF, the previous
trace title returns. Set a new trace title using
[DISP:WIND:TRAC:TITL:DATA](Display.md#TraceTitleData) [Learn more about Trace
Titles](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle)  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<bool> |  ON or 1 \- turns the title ON. OFF or 0 \- turns the title OFF.  
Examples |  DISP:MEAS:TITL ON  
Display:measure:title:state off  
Query Syntax |  DISPlay:MEAS<mnum>:TITLe[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF or 0  
  
* * *

## DISPlay:MEASure<mnum>:TYPE <char>

Applicable Models: All (Read-Write) Set and get the display type for the
specified measurement trace.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<char> |  Choose from:

  * OFF - Both Data and Memory traces off
  * DATA - Data Trace only
  * MEMory - Memory Trace only
  * DMEMory - Both Data and Memory traces on

  
Examples |  DISP:MEAS:TYPE MEM display:measure:type dmemory  
Query Syntax |  :DISPlay:MEASure:TYPE?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  DATA  
  
* * *

## DISPlay:MEASure<mnum>:Y[:SCALe]:AUTO

Applicable Models: All (Write-only) Performs an Autoscale on the specified
trace in the specified measurement, providing the best fit display.  Autoscale
is performed only when the command is sent; it does NOT keep the trace
autoscaled indefinitely. Autoscale behaves differently when [scale
coupling](Display.htm#scaleCouplState) is enabled. How it behaves depends on
the scale coupling method. [Learn
more.](../../S1_Settings/Scale.htm#ScaleCoupling) See Also,
[DISPlay:WINDow:Y:AUTO](Display.md#AutoscaleAll) which performs an Autoscale
All.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
Examples |  DISP:MEAS:Y:AUTO  
display:measure:y:scale:auto  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:MEASure<mnum>:Y[:SCALe]:PDIVision <num>

Applicable Models: All (Read-Write) Sets the Y axis Scale Per Division value
of the specified trace associated with the specified measurement.  Note: The
measurement and trace need to exist.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<num> |  Units / division value (Real value). The range of acceptable values is dependent on format and domain. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:MEAS:Y:PDIV 1  
display:measure:y:scale:pdivision maximum  
Query Syntax |  DISPlay:MEASure<mnum>:Y[:SCALe]:PDIVision?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

## DISPlay:MEASure<mnum>:Y[:SCALe]:RLEVel <num>

Applicable Models: All (Read-Write) Sets the Y axis Reference Level of the
specified trace associated with the specified measurement.  Note: The
measurement and trace need to exist.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<num> |  Reference level value (Real value). The range of acceptable values is dependent on format and domain. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:MEAS:Y:RLEV 0  
display:measure:y:scale:rlevel minimum  
Query Syntax |  DISPlay:MEASure<mnum>:Y[:SCALe]:RLEVel?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## DISPlay:MEASure<mnum>:Y[:SCALe]:RPOSition <num>

Applicable Models: All (Read-Write) Sets the Reference Position of the
specified trace associated with the specified measurement.  Note: The
measurement and trace need to exist.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<num> |  Reference position on the screen measured in horizontal graticules from the bottom (Real value). The range of acceptable values is dependent on format and domain. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:MEAS:Y:RPOS 0  
display:measure:y:rposition maximum  
Query Syntax |  DISPlay:MEASure<mnum>:Y[:SCALe]:RPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  5  
  
* * *

## DISPlay:SHEet<num>:ARRange <char>

Applicable Models: All (Write-only) This command arranges existing windows to
sheets.  
---  
Parameters |   
<num> |  Sheet number  
<char> |  Sheet arrangement. Choose from: WINDow: one sheet per window CHANnel: one sheet per channel TRACe: one channel per sheet ONE: merge all windows into one sheet  
Examples |  DISP:SHE:ARR CHAN  
display:sheet:arrange channel  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  One sheet per window  
  
* * *

## DISPlay:SHEet<num>:CATalog?

Applicable Models: All (Read-only) This command reads and displays comma
separated list of window numbers which the sheet contains.  
---  
Parameters |   
<num> |  Sheet number  
Examples |  DISP:SHE:CAT?  
display:sheet:catalog?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## DISPlay:SHEet<num>:LIST?

Applicable Models: All (Read-only) This command reads and displays a comma
separated list of the sheet numbers in use in the order they appear in the
GUI.  Note: This is not returning sheet names, just their number as you would
use in related commands like DISPlay:SHEet<num>:STATe?. Deleting and adding
sheets can cause them to be unordered.  
---  
Parameters |   
<num> |  Sheet number  
Examples |  DISP:SHE:LIST?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## DISPlay:SHEet: NEW [<int>]

Applicable Models: All  (Write-only) Add a new sheet according to the <int>
parameter.  
---  
Parameters |   
<int> |  Add Type (optional) - 0: Sheet (default), 1: Trace + Sheet, 2: Trace + Channel + Sheet  
Examples |  DISP:SHE:NEW 1 display:sheet:new  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:SHEet<num>:STATe

Applicable Models: All (Write-only) Sets the sheet visible and invisible:  ON:
If OFF, sets the sheet visible with a new window. OFF: If ON, sets the sheet
invisible with all the containing window state OFF (DISPlay:WINDow:STATe OFF)  
---  
Parameters |   
<num> |  Sheet number  
Examples |  DISP:SHE:STAT ON display:sheet:state off  
Query Syntax |  DISPlay:SHEet:STATe?  
Return Type |  Bool  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF except for Sheet 1  
  
* * *

## DISPlay:SHEet<num>:TITLe:DATA <char>

Applicable Models: All (Read-Write) This command sets or gets the sheet label.  
---  
Parameters |   
<num> |  Sheet number  
<char> |  The label of the sheets. Default and present value is "Sheet 1"  
Examples |  DISP:SHE:TITL:DATA "Sheet 1"  
display:sheet:title:data "Sheet 1"  
Query Syntax |  DISPlay:SHEet:TITLe:DATA?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "Sheet 1"  
  
* * *

## DISPlay:SIZE <enum>

Applicable Models: All (Read-Write) Set and read the display size. The
settings are minimum (minimizes the display), maximum, and normal.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<enum> |  Choose from: MIN - Minimizes the display. MAX - Maximizes display to the full size of the display. NORMal - Default size.  
Examples |  DISP:SIZE MAX  
Query Syntax |  DISPlay:SIZE?  
Return Type |  Enumeration  
Default |  NORM  
  
* * *

## DISPlay:SPLit <num>

Applicable Models: All (Write-only) Destroys all existing traces, channels and
windows, then creates N windows. No channels are created.  
---  
Parameters |   
<num> |  N is 1 or greater.  
Examples |  DISP:SPL  
display:split  
Query Syntax |  DISPlay:SPLit?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:STATus:LOG:CLEar

Applicable Models: All (Write-only) Clears the message region in the status
bar.  
---  
Parameters |   
Examples |  DISP:STAT:LOG:CLE  
display:status:log:clear  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:STATus:SCPI

Applicable Models: All (Read-Write) Turn on or off the Display SCPI feature in
[SCPI recorder](../SCPI_Recorder.md).  
---  
Parameters |   
<bool> |  ON (or 1) - Turn on the Display SCPI OFF (or 0) - Turn off the Display SCPI  
Examples |  DISP:STAT:SCPI ON  
Query Syntax |  DISPlay:STATus:SCPI?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:TMAX <bool>

Applicable Models: All (Read-Write) Maximizes (isolates) or restores the
active trace in the active window. When turned ON, the active trace is the
ONLY trace on the display. All other traces are hidden. [Learn
more.](../../Front_Panel/XScreen.htm#Traces)  
---  
Parameters |   
<bool> |  ON (or 1) - Maximize / isolates the active trace. OFF (or 0) - Restores other traces to the normal window setting.  
Examples |  DISP:TMAX ON  
display:tmax 0  
Query Syntax |  DISPlay:TMAX?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay[:TILE] - Superseded

This command is replaced by [DISP:ARRange](Display.md#arrange)

(Write-only) Tiles the windows on the screen.  
---  
Examples |  DISP  
display:tile  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:TOOLbar:CSET[:STATe] <bool>

Applicable Models: All (Read-Write) Show or hide the calset toolbar.  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:CSET ON display:toolbar:cset:state off  
Query Syntax |  DISPlay:TOOLbar:CSET:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:TOOLbar:ENTRy[:STATe] <bool>

Applicable Models: All (Read-Write) Specifies whether to show or hide the
active entry toolbar. [See this
toolbar](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#act_ent_tb).  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:ENTR ON display:toolbar:entry:state off  
Query Syntax |  DISPlay:TOOLbar:ENTRy:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:TOOLbar:EXTensions[:STATe] <bool>

Applicable Models: All (Read-Write) Specifies whether to show or hide the port
extensions toolbar. [See this
toolbar](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#PortExt).  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:EXT ON display:toolbar:extensions:state off  
Query Syntax |  DISPlay:TOOLbar:EXTensions:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:TOOLbar:KEYS[:STATe] <bool>

Applicable Models: All (Read-Write) Specifies whether to show or hide the
virtual hardkeys on the VNA display. These are primarily used when the VNA is
accessed remotely using [VNC](../../S0_Start/VNC.md) or Windows Remote
Desktop.  
---  
Parameters |   
<bool> |  ON (or 1) - Keys ON. OFF (or 0) - Keys OFF.  
Examples |  DISP:TOOL:KEYS ON display:toolbar:keys:state off  
Query Syntax |  DISPlay:TOOLbar:KEYS:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:TOOLbar:MARKer[:STATe] <bool>

Applicable Models: All (Read-Write) Specifies whether to show or hide the
marker toolbar. [See this
toolbar](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#markers_tb).  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:MARK ON display:toolbar:marker:state off  
Query Syntax |  DISPlay:TOOLbar:MARKer:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:TOOLbar:MEASurement[:STATe] <bool> OBSOLETE

This toolbar was eliminated with A.10.00 (Read-Write) Specifies whether to
show or hide the measurement toolbar.  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:MEAS ON display:toolbar:measurement:state off  
Query Syntax |  DISPlay:TOOLbar:MEASurement[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:TOOLbar:STIMulus[:STATe] <bool> OBSOLETE

This toolbar was eliminated with A.10.00 (Read-Write) Specifies whether to
show or hide the stimulus toolbar.  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:STIM ON display:toolbar:stimulus:state off  
Query Syntax |  DISPlay:TOOLbar:STIMulus[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:TOOLbar:SWEep[:STATe] <bool> OBSOLETE

This toolbar was eliminated with A.10.00 (Read-Write) Specifies whether to
show or hide the sweep control toolbar.  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:SWE ON display:toolbar:sweep:state off  
Query Syntax |  DISPlay:TOOLbar:SWEep[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:TOOLbar:TRANsform[:STATe] <bool>

Applicable Models: All (Read-Write) Specifies whether to show or hide the Time
Domain toolbar. [See this
toolbar](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#Time).  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:TOOL:TRAN ON display:toolbar:transform:state off  
Query Syntax |  DISPlay:TOOLbar:TRANsform:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:TRACe:NEW [<int>]

Applicable Models: All  (Write-only) Add a new trace according to the <int>
parameter.  
---  
Parameters |   
<int> |  Optional. Add Type -0: Trace (default), 1: Trace + Channel, 2: Trace + Window, 3: Trace + Channel + Window  
Examples |  DISP:TRAC:NEW 2  
display:trace:new 3  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:TRACe:<tr>STATe <ON | OFF>

Applicable Models: All (Read-Write) Add or delete the specified trace. If set
ON to an existing channel, just activate the trace.  
---  
Parameters |   
<ch> |  Trace Number. Default is 1.  
<ON | OFF> |  ON (or 1) - adds the trace OFF (or 0) - deletes the trace  
Examples |  DISP:TRAC2:STAT 1 display:trace3:state on  
Query Syntax |  DISPlay:TRACe:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON (1) for Trace 1, OFF(0) for other traces  
  
* * *

## DISPlay:UPDate[:STATe] <bool>

Applicable Models: All (Read-Write) Enables or disables display updates.
Disabling display updates improves measurement performance. When disabled, the
display windows (traces, markers, etc.) are frozen.  
---  
Parameters |   
<bool> |  ON (or 1) - Toolbar ON. OFF (or 0) - Toolbar OFF.  
Examples |  DISP:UPD ON display:update:state off  
Query Syntax |  DISPlay:UPDate[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:UPDate:IMMediate

Applicable Models: All (Write-only) Executes the display update once when the
display update of the LCD screen is set to OFF (specifying False with the
[DISPlay:ENABle](Display.md#enable) object).  
---  
Parameters |   
Examples |  DISP:UPD:IMM  
display:update:immediate  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:VISible <ON | OFF>

Applicable Models: All (Read-Write) Makes the VNA application visible or not
visible. In the Not Visible state, the analyzer cycle time for making
measurements, and especially data transfer, can be significantly faster
because the display does not process data.  
---  
Parameters |   
<ON | OFF> |  ON (or 1) - VNA app is visible  
OFF (or 0) - VNA app is NOT visible  
Examples |  DISP:VIS ON  
display:visible off  
Query Syntax |  DISPlay:VISible?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:LIMit:XPOSition <num>

Applicable Models: All (Read-Write) Sets and returns the X-axis position of
the Limit Line Pass/Fail indicator on the VNA screen. The lower-left corner of
the Pass/Fail indicator is the point of reference for positioning.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  X-axis position. Choose a value between 0 (far left) and 10 (far right).  
Examples |  DISP:WIND:ANN:LIM:XPOS 1.5 display:window:annotation:limit:xposition 5  
Query Syntax |  DISPlay:WINDow:ANNotation:LIMit:XPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  7  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:LIMit:YPOSition <num>

Applicable Models: All (Read-Write) Sets and returns the Y-axis position of
the Limit Line Pass/Fail indicator on the VNA screen. The lower-left corner of
the Pass/Fail indicator is the point of reference for positioning.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  Y-axis position. The maximum position is limited to the current Y-axis division value. Choose a value between 2 (bottom) and 30 (top).  
Examples |  DISP:WIND:ANN:LIM:YPOS 1.5 display:window:annotation:limit:yposition 5  
Query Syntax |  DISPlay:WINDow:ANNotation:LIMit:YPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:COUPle[:STATe] <bool>

Applicable Models: All

(Read-Write) Sets the marker readouts to coupled (one combination annotation)
or not coupled (one annotation per trace). This setting is per Window scope.
See other SCPI [Marker](../../GUI_Reference/Marker.md) commands. Learn more
about [Marker readout.](../../S4_Collect/Markers.md#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<bool> |  ON (or 1) - Marker readouts are coupled  
OFF (or 0) - Marker readouts are not coupled  
Examples |  DISP:WIND:ANN:MARK:COUP ON  
display:window:annotation:marker:couple on  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:COUPle?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
## DISPlay:WINDow<wnum>:ANNotation:MARKer:NUMBer <num>

Applicable Models: All This command replaces
[DISP:WIND:ANN:MARK:SINGle](Display.md#single) (Read-Write) Sets the number
of marker readouts to display per trace. Display up to 20 marker readouts per
window.  See other SCPI [Marker](Calculate/Marker.md) commands. Learn more
about [Marker readout.](../../S4_Collect/Markers.md#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  Number of marker readouts to display. Choose a value between 1 and 16.  
Examples |  DISP:WIND:ANN:MARK:NUMB 7  
display:window:annotation:marker:number 2  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:NUMBer?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  5  
  
* * *

## DISPlay:WINDow:ANNotation:MARKer:MEASure<mnum>:XPOSition <num>

Applicable Models: All

(Read-Write) Sets the X-axis position of marker readouts. Readouts are right-
justified at the specified position. This function is used when
:DISP:WIND:ANN:MARK:COUP:STAT is off. Use :DISP:WIND:ANN:MARK:XPOS is used
when :DISP:WIND:ANN:MARK:COUP:STAT is on.  See other SCPI
[Marker](../../GUI_Reference/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<mnum> |  Measurement. If unspecified, value is set to 1.  
<num> |  X-axis position. Choose a value between 1 (far left) and 10 (far right).  
Examples |  DISP:WIND:ANN:MARK:MEAS:XPOS 1.5  
display:window:annotation:marker:measure:xposition 5  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:MEASure:XPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

## DISPlay:WINDow:ANNotation:MARKer:MEASure<mnum>:YPOSition <num>

Applicable Models: All

(Read-Write) Sets the Y-axis position of marker readouts. Readouts are top-
justified at the specified position. This function is used when
:DISP:WIND:ANN:MARK:COUP:STAT is off. Use :DISP:WIND:ANN:MARK:YPOS is used
when :DISP:WIND:ANN:MARK:COUP:STAT is on.  See other SCPI
[Marker](../../GUI_Reference/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<mnum> |  Measurement. If unspecified, value is set to 1.  
<num> |  Y-axis position. Choose a value between 1 (bottom) and 10 (top).  
Examples |  DISP:WIND:ANN:MARK:MEAS:YPOS 1.5  
display:window:annotation:marker:measure:yposition 5  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:MEASure:YPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:RESolution:STIMulus <num>

Applicable Models: All (Read-Write) For the X-axis (stimulus), sets the number
digits to display after the decimal point in marker readouts.  See other SCPI
[Marker](Calculate/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  Number of digits to display. Choose a value between 2 and 6.  
Examples |  DISP:WIND:ANN:MARK:RES:STIM 2  
display:window:annotation:marker:resolution:stimulus 4  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:RESolution:STIMulus?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  3  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:RESolution:RESPonse <num>

Applicable Models: All (Read-Write) For the Y-axis (response), sets the number
digits to display after the decimal point in marker readouts.  See other SCPI
[Marker](Calculate/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  Number of digits to display. Choose a value between 1 and 4.  
Examples |  DISP:WIND:ANN:MARK:RES:RESP 1  
display:window:annotation:marker:resolution:stimulus 2  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:RESolution:RESPonse?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  2  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:SINGle[:STATe] <bool> \- Superseded

Applicable Models: All Note: This command is replaced by
[DISP:WIND:ANN:MARK:NUMB](Display.md#MarkerNumber) (Read-Write) Either shows
marker readout of only the active trace or other traces simultaneously.  See
other SCPI [Marker](Calculate/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<bool> |  ON (or 1) - Shows the readout of only the active marker for each trace. OFF (or 0) - Shows up to 5 marker readouts per trace, up to 20 total readouts.  
Examples |  DISP:WIND:ANN:MARK:SING ON  
display:window:annotation:marker:single off  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:SINGle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:SIZE <char>

Applicable Models: All (Read-Write) Specifies the size of the marker readout
text. See other SCPI [Marker](Calculate/Marker.md) commands. Learn more about
[Marker readout.](../../S4_Collect/Markers.md#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<char> |  Readout text size. Choose from:NORMal | LARGe  
Examples |  DISP:WIND:ANN:MARK:SIZE LARG  
display:window:annotation:marker:size normal  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:SIZE?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NORMal  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether to show or hide the
Marker readout (when markers are ON) on the selected window. See other SCPI
[Marker](Calculate/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns marker readout ON. OFF (or 0) - turns marker readout OFF.  
Examples |  DISP:WIND:ANN:MARK ON  
display:window:annotation:marker:state off  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:SYMBol <char>

Applicable Models: All (Read-Write) Sets the symbol to display for marker
position.  See other SCPI [Marker](Calculate/Marker.md) commands.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<char> |  Marker symbol. Choose from: TRIangle FLAG LINE [See pictures of each](../../S4_Collect/Markers.md#DisplayDiag)  
Examples |  DISP:WIND:ANN:MARK:SYMB TRI display:window:annotation:marker:symbol line  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:SYMBol?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  TRIangle  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:VISible <char>

Applicable Models: All

(Read-Write) Shows the marker readouts only for active trace or for all
traces. This setting is per Window scope. [See this
toolbars](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#markers_tb)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<char> |  ACTive \- readout is turned on for active trace only. ALL \- readout is turned on for all traces.  
Examples |  DISP:WIND:ANN:MARK:VIS ACT display:windows:annotation:marker:visible all  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:VISible?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ALL  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:SYMBol:ABOVe[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether or not to force marker
symbols to be displayed above the trace. When ON, all marker symbols will be
displayed above the trace and the active marker will be filled solid. See
other SCPI [Marker](Calculate/Marker.md) commands.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) \- ALL marker symbols are displayed above the trace. Only the active marker is filled solid. OFF (or 0) \- ONLY the active marker is displayed above the trace. The active marker is not filled solid.  
Examples |  DISP:WIND:ANN:MARK:SYMB:ABOV ON  
display:window:annotation:marker:symbol:above:state off  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:SYMBol:ABOVe:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF - ON in IM Spectrum and SA measurement classes  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MARKer:XPOSition <num>

Applicable Models: All (Read-Write) Sets the X-axis position of marker
readouts. Readouts are right-justified at the specified position.  See other
SCPI [Marker](Calculate/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  X-axis position. Choose a value between 1 (far left) and 10 (far right).  
Examples |  DISP:WIND:ANN:MARK:XPOS 1.5  
display:window:annotation:marker:xposition 5  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:XPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:MAR Ker:YPOSition <num>

Applicable Models: All (Read-Write) Sets the Y-axis position of marker
readouts. Readouts are top-justified at the specified position.  See other
SCPI [Marker](Calculate/Marker.md) commands. Learn more about [Marker
readout.](../../S4_Collect/Markers.htm#DisplayDiag)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<num> |  Y-axis position. Choose a value between 1 (bottom) and 10 (top).  
Examples |  DISP:WIND:ANN:MARK:YPOS 1.5  
display:window:annotation:marker:yposition 5  
Query Syntax |  DISPlay:WINDow:ANNotation:MARKer:YPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation[:TRACe]:SCOPe <enum>

Applicable Models: All (Read-Write) Set and read the scope for trace
annotation. Either display trace annotation for all traces or just the active
trace.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<enum> |  Choose from: ALL ACTive  
Examples |  DISP:WIND:ANN:SCOP ACT  
Query Syntax |  DISPlay:WINDow:ANNotation[:TRACe]:SCOPe?  
Return Type |  Enumeration  
Default |  ALL  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation[:TRACe][:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether to show or hide the
Trace Status at the top of the window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns the buttons ON.  
OFF (or 0) - turns the buttons OFF.  
Examples |  DISP:WIND:ANN ON  
display:window:annotation:trace:state off  
Query Syntax |  DISPlay:WINDow:ANNotation[:TRACe]:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation: X[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the X-axis scale label in
display window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<bool> |  ON or 1 \- Turns ON the X-axis scale.   
OFF or 0 \- Turns OFF the X-axis scale.  
Examples |  DISP:WIND:ANN:X ON  
display:window:annotation:x off  
Query Syntax |  DISPlay:WINDow:ANNotation:X?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON or 1  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation:XAXis:SCOPe <enum>

Applicable Models: All (Read-Write) Set and read the scope for the stimulus
information on the display title bar. Either display the stimulus information
for all traces or just the active trace.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<enum> |  Choose from: ALL ACTive  
Examples |  DISP:WIND:ANN:XAX:SCOP ACT  
Query Syntax |  DISPlay:WINDow:ANNotation:XAXis:SCOPe?  
Return Type |  Enumeration  
Default |  ALL  
  
* * *

## DISPlay:WINDow<wnum>:ANNotation: Y[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON or OFF the Y-axis scale label in
display window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<bool> |  ON or 1 \- Turns ON the Y-axis scale.   
OFF or 0 \- Turns OFF the Y-axis scale.  
Examples |  DISP:WIND:ANN:Y ON  
display:window:annotation:y off  
Query Syntax |  DISPlay:WINDow:ANNotation:Y?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON or 1  
  
* * *

## DISPlay:WINDow<wnum>:CATalog?

Applicable Models: All (Read-only) Returns the trace numbers for the specified
window.  Note: If there are no traces in the window, this query returns the
"EMPTY" string.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
Example |  Window 1 with four traces:  
DISPlay:WINDow1:CATalog?  
Returns:  
"1,2,3,4"  
Return Type |  String of Character values separated by commas  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## DISPlay:WINDow<wnum>:ENABle <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether to disable or enable all
analyzer display information in the specified window. Marker data is not
updated. More CPU time is spent making measurements instead of updating the
display.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns the display ON.  
OFF (or 0) - turns the display OFF.  
Examples |  DISP:WIND:ENABle ON  
display:window1:enable off  
Query Syntax |  DISPlay:WINDow<wnum>:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:FEED <snum>

Applicable Models: All (Write-only) This command feeds a specified window to
the sheet. If there is a window in the sheet, the sheet is visible. If there
is no window in the sheet, the sheet is not visible. If no windows exists in
the system, one empty sheet is visible.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<snum> |  Sheet number  
Examples |  DISP:WIND:FEED 5  
display:window:feed 5  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow:NEW [<int>]

Applicable Models: All  (Write-only) Add a new window according to the <int>
parameter.  
---  
Parameters |   
<int> |  Add Type (optional) - 0: Window (default), 1: Trace + Window, 2: Trace + Channel + Window  
Examples |  DISP:WINDS:NEW 1  
display:window:new  
Query Syntax |  Not Applicable  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:NEXT[:NUMBer]?

Applicable Models: All (Read-only) Returns the lowest window number which has
less than the maximum number of traces. Basically, returns the first window
which has room for another trace. Note that the window may need to be turned
on first (i.e. disp:wind:stat ON may be needed).  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
Examples |  DISP:WIND:NEXT  
display:window1:NEXT  
Query Syntax |  DISPlay:WINDow<wnum>:NEXT?  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:SIZE <char>

Applicable Models: All (Read-Write) Sets or returns the window setting of
Maximized or Normal. To arrange all of the windows, use DISP:ARR.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1  
<char> |  Window size. Choose from: MAX | NORM  
Examples |  DISP:WIND:SIZE MAX  
display:window:size norm  
Query Syntax |  DISPlay:WINDow:SIZE?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Write to create or delete a window on the
screen or Read whether a window is present.  
---  
Parameters |   
<wnum> |  Window number to create; choose any integer between 1 and the [maximum number of windows allowed in the VNA](../../S0_Start/Traces_Channels_and_Windows.md#window).  
<ON | OFF> |  ON (or 1) - The window <wnum> is created.  
OFF (or 0) - The window <wnum> is deleted.  
Examples |  DISP:WIND ON  
display:window2:state off  
Query Syntax |  DISPlay:WINDow<wnum>:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Window number "1" ON  
  
* * *

## DISPlay:WINDow<wnum>:TABLe <char>

Applicable Models: All (Read-Write) Write to show the specified table at the
bottom of the analyzer screen or Read to determine what table is visible.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1  
<char> |  Table to show. Choose from:  
OFF | MARKer | LIMit | SEGMent | RLIMit | DISTortion  
Examples |  DISP:WIND:TABLe SEGM  
display:window:table off  
Query Syntax |  DISPlay:WINDow<wnum>:TABLe?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<wnum>:TABLe:INOise:ENABle <ON | OFF>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enable or disable displaying the integrated noise table.  
---  
Parameters |   
<wnum> |  Window number to create; choose any integer between 1 and the [maximum number of windows allowed in the VNA](../../S0_Start/Traces_Channels_and_Windows.md#window).  
<ON | OFF> |  ON (or 1) - Display the integrated noise table.  
OFF (or 0) - Do not display the integrated noise table.  
Examples |  DISP:WIND:TABL:INO:ENAB ON  
display:window2:table:inoise:enable off  
Query Syntax |  DISPlay:WINDow<wnum>:TABLe:INOise:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<wnum>:TABLe:SNOise:ENABle <ON | OFF>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enable or disable displaying the spot noise table.  
---  
Parameters |   
<wnum> |  Window number to create; choose any integer between 1 and the [maximum number of windows allowed in the VNA](../../S0_Start/Traces_Channels_and_Windows.md#window).  
<ON | OFF> |  ON (or 1) - Display the spot noise table.  
OFF (or 0) - Do not display the spot noise table.  
Examples |  DISP:WIND:TABL:SNO:ENAB ON  
display:window2:table:snoise:enable off  
Query Syntax |  DISPlay:WINDow<wnum>:TABLe:SNOise:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<wnum>:TABLe:SPURious:ENABle <ON | OFF>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enable or disable displaying the spurious table.  
---  
Parameters |   
<wnum> |  Window number to create; choose any integer between 1 and the [maximum number of windows allowed in the VNA](../../S0_Start/Traces_Channels_and_Windows.md#window).  
<ON | OFF> |  ON (or 1) - Display the spurious table.  
OFF (or 0) - Do not display the spurious table.  
Examples |  DISP:WIND:TABL:SPUR:ENAB ON  
display:window2:table:spurious:enable off  
Query Syntax |  DISPlay:WINDow<wnum>:TABLe:SPURious:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<wnum>:TITLe:DATA <string>

Applicable Models: All (Read-Write) Sets data in the window title area. The
title is turned ON and OFF with [DISP:WIND:TITL:STAT
OFF](Display.htm#titstate).  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<string> |  Title to be displayed. Any characters, enclosed with quotes. If the title string exceeds 50 characters, an error will be generated and the title not accepted. Newer entries replace (not append) older entries.  
Examples |  DISP:WIND:TITL:DATA 'hello'  
display:window2:title:data 'hello'  
Query Syntax |  DISPlay:WINDow<wnum>:TITLe:DATA?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NA  
  
* * *

## DISPlay:WINDow<wnum>:TITLe[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns display of the title string ON or
OFF. When OFF, the string remains, ready to be redisplayed when turned back
ON.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns the title string ON.  
OFF (or 0) - turns the title string OFF.  
Examples |  DISP:WIND:TITL ON  
Display:window1:title:state off  
Query Syntax |  DISPlay:WINDow<wnum>:TITLe[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:DELete

Applicable Models: All (Write-only) Deletes the specified trace from the
specified window. The measurement parameter associated with the trace is not
deleted.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<tnum> |  The number of the trace to be deleted; if unspecified, value is set to 1. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
Examples |  DISP:WIND:TRAC:DEL  
display:window2:trace2:delete  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:FEED <name>

Applicable Models: All (Write-only) Creates a new trace <tnum> and associates
(feeds) a measurement <name> to the specified window<wnum>. This command
should be executed after creating a new measurement with
[CALCulate:MEASure:DEFine](Calculate/Measure.md#CALCulate:MEASure:DEFine).
Note: Window <wnum> must already be turned on before this command can be used.
Turn on the window state using DISPlay:WINDow:STATe. To feed the same
measurement to multiple traces, create another measurement with the same
<parameter>, but different <name>, using the CALC:PAR:DEF command. The
analyzer will collect the data only once.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<tnum> |  Trace number to be created. Choose any Integer between 1 and the VNA [maximum number of traces per window](../../S0_Start/Traces_Channels_and_Windows.md#Trace) allowed. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<name> |  Name of the measurement that was defined with CALC:PAR:DEF<name>,<parameter>  
Example |  CALCulate1:PARameter:DEFine 'CH1_S11',s11,1 CALCulate1:PARameter:SELect 'CH1_S11' DISPlay:WINDow1:STATe ON **DISPlay:WINDow1:TRACe1:FEED 'CH1_S11'**  
Query Syntax |  Not applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "CH1_S11"  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:FEED:MNUMber <int>

Applicable Models: All (Write-only) Creates a new trace <tnum> for an existing
measurement (MNUM) and associates (feeds) the measurement number to the
specified window<wnum>. A measurement is created using the
[CALC:MEAS:DEF](Calculate/Measure.md#CALCulate:MEASure:DEFine) command.
Measurements created in the system all have unique numbers. Similarly, every
window has a unique number and the numbers are displayed in the lower-left
corner of each window. Every window has the capacity to hold a finite number
of traces from 1 to N, where N is the maximum number of traces per window.
Each window uses the same range of trace numbers. For example, window 1 can
have a trace 1 and so can window 2.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<tnum> |  Trace number to be created. Choose any Integer between 1 and the VNA [maximum number of traces per window](../../S0_Start/Traces_Channels_and_Windows.md#Trace) allowed. Note: After executing the DISP:WIND:TRAC:FEED:MNUM command, a new trace is added to the specified window and the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display is the actual measurement number.  
<int> |  Number of an existing measurement. The range is 1 to 2000.  
Examples |  CALC:MEAS2:DEF "S22"  
DISP:WIND:TRAC4:FEED:MNUM 2  
Query Syntax |  Not applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## DISPlay:WINDow:TRACe:GRATicule:GRID:LTYPE <value>

Applicable Models: All (Read-Write) Sets and returns the grid line type (solid | dotted) for all open windows. Grid is returned to solid when the VNA is Preset. [Learn more.](../../S1_Settings/Customize_Your_Analyzer_Screen.md#GridLines)  
---  
Parameters |   
<value> |  Line type. Choose from: SOLid \- solid lines DOTTed \- dotted lines  
Examples |  DISP:WIND:TRAC:GREAT:GRID:LTYPE SOL  
display:window:trace:graticule:grid:ltype dotted  
Query Syntax |  DISPlay:WINDow:TRACe:GRATicule:GRID:LTYPE?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  SOLID  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:MEMory[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns the memory trace ON or OFF.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<ON | OFF> |  ON (or 1) - turns the memory trace ON.  
OFF (or 0) - turns the memory trace OFF.  
Examples |  DISP:WIND:TRAC:MEM ON  
display:window2:trace2:memory:state off  
Query Syntax |  DISPlay:WIND<wnum>:TRACe<tnum>:MEMory:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<fromWin>:TRACe<tnum>:MOVE <toWin>

Applicable Models: All (Write-only) Moves a trace from one window to another
window.  
---  
Parameters |   
<fromWin> |  Window number to move the trace from. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Trace number to be moved. If unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<toWin> |  Number of the window to move the trace to. If the window does not exist, it will be created.  
Examples |  DISP:WIND:TRAC2:MOVE 2  
display:window2:trace2:move 1  
Query Syntax |  Not applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## DISPlay:WINDow<wnum>:TRACe:NEXT[:NUMBer]?

Applicable Models: All (Read-only) Returns the next unused trace number. For
example, if trace #1, #2, and #3 are being used, then this command will return
4.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1.  
Examples |  DISP:WIND:TRAC:NEXT?  
display:window1:trace:NEXT?  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:SELect

Applicable Models: All (Write-only) Activates the specified trace in the
specified window for front panel use.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#Trace_Status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
Examples |  DISP:WIND:TRAC:SEL  
display:window2:trace2:select  
Query Syntax |  Not applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NA  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns the display of the specified trace
in the specified window ON or OFF. When OFF, the measurement behind the trace
is still active.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#Trace_Status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<ON | OFF> |  ON (or 1) - turns the trace ON.  
OFF (or 0) - turns the trace OFF.  
Examples |  DISP:WIND:TRAC ON  
display:window2:trace2:state off  
Query Syntax |  DISPlay:WIND<wnum>:TRACe<tnum>:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:TITLe:DATA <string>

Applicable Models: All (Read-Write) Writes and read data to the trace title
area. The trace title is embedded in the trace status field. [Learn more about
Trace
Titles](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle).
Newer entries replace (not append) older entries. The title is turned ON and
OFF with [DISP:WIND:TRAC:TITL:STAT](Display.md#TraceTitleState).  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Trace number of the specified window. If unspecified, value is set to 1. Use [Display:Cat?](Display.md#cat) to read the window numbers. Use [Disp:Window:Cat?](Display.md#dwc) to read the trace numbers of the specified window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<string> |  Title to be displayed. Any characters (not spaces) enclosed with quotes.  
Examples |  DISP:WIND:TRAC:TITL:DATA 'MyNewMeas'  
display:window2:trace3:title:data 'hello'  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>TITLe:DATA?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:TITLe[:STATe] <bool>

Applicable Models: All (Read-Write) Turns display of the Trace Title ON or
OFF. When turned OFF, the previous trace title returns. Set a new trace title
using [DISP:WIND:TRAC:TITL:DATA](Display.md#TraceTitleData) [Learn more about
Trace Titles](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle)  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1 Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Trace number of the specified window. If unspecified, value is set to 1. Use [Display:Cat?](Display.md#cat) to read the window numbers. Use [Disp:Window:Cat?](Display.md#dwc) to read the trace numbers of the specified window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<bool> |  ON (or 1) - turns the title ON. OFF (or 0) - turns the title OFF.  
Examples |  DISP:WIND:TRAC:TITL ON  
Display:window2:trace3:title:state off  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:TITLe[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:X[:SCALe]:RLEVel <num>

Applicable Models: All (Read-Write) Sets the X axis Reference Level of the
specified trace in the specified window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Reference level value.  
Examples |  DISP:WIND:TRAC:X:RLEV 0  
display:window2:trace2:x:scale:rlevel 0  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:X[:SCALe]:RLEVel?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:X[:SCALe]:RPOSition <num>

Applicable Models: All (Read-Write) Sets the Reference Position of the
specified trace in the specified window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Reference position on the screen measured in horizontal graticules from the bottom. Choose a value between 0 and 10.  
Examples |  DISP:WIND:TRAC:X:RPOS 0 display:window2:trace2:x:rposition 10  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:X[:SCALe]:RPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  5  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:AUTO

Applicable Models: All (Write-only) Performs an Autoscale on the specified
trace in the specified window, providing the best fit display.  Autoscale is
performed only when the command is sent; it does NOT keep the trace autoscaled
indefinitely. Autoscale behaves differently when [scale
coupling](Display.htm#scaleCouplState) is enabled. How it behaves depends on
the scale coupling method. [Learn
more.](../../S1_Settings/Scale.htm#ScaleCoupling) See Also,
[DISPlay:WINDow:Y:AUTO](Display.md#AutoscaleAll) which performs an Autoscale
All.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
Examples |  DISP:WIND:TRAC:Y:AUTO  
display:window2:trace2:y:scale:auto  
Query Syntax |  Not applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## DISPlay:WINDow:TRACe:Y[:SCALe]:COUPle:METHod <char>

Applicable Models: All (Read-Write) Sets and returns the method of scale
coupling. [Learn more](../../S1_Settings/Scale.md#CouplingDiag) about Scale
coupling.  
---  
Parameters |   
<char> |  OFF \- NO scale coupling for any windows. WINDow \- Scale settings are coupled for traces in each window. ALL \- Scale settings are coupled for traces in ALL selected windows. Enable the selected windows using [DISP:WIND:TRAC:Y:COUP ON](Display.md#scaleCouplState)  
Examples |  DISP:WIND:TRAC:Y:COUP:METH ALL Display:window2:trace:y:scale:method window  
Query Syntax |  DISPlay:WINDow:TRACe:Y[:SCALe]:COUPle:METHod?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## DISPlay:WINDow<wnum>:TRACe:Y[:SCALe]:COUPle[:STATe] <bool>

Applicable Models: All (Read-Write) Enables and disables scale coupling for
the specified window. [Learn more](../../S1_Settings/Scale.md#CouplingDiag)
about Scale coupling.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1 Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<bool> |  ON (or 1) - Scale coupling enabled for specified window. OFF (or 0) - Scale coupling disabled for specified window.  
Examples |  DISP:WIND:TRAC:Y:COUP ON Display:window2:trace:y:scale:couple:state off  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe:Y[:SCALe]:COUPle[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:PDIVision <num>

Applicable Models: All (Read-Write) Sets the Y axis Per Division value of the
specified trace in the specified window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Units / division value. The range of acceptable values is dependent on format and domain. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:WIND:TRAC:Y:PDIV 1  
display:window2:trace2:y:scale:pdivision maximum  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:PDIVision?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:RLEVel <num>

Applicable Models: All (Read-Write) Sets the Y axis Reference Level of the
specified trace in the specified window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Reference level value. The range of acceptable values is dependent on format and domain. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:WIND:TRAC:Y:RLEV 0  
display:window2:trace2:y:scale:rlevel minimum  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:RLEVel?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:RPOSition <num>

Applicable Models: All (Read-Write) Sets the Reference Position of the
specified trace in the specified window.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Reference position on the screen measured in horizontal graticules from the bottom. Choose a value between 0 and 10. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:WIND:TRAC:Y:RPOS 0 display:window2:trace2:y:rposition maximum  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:RPOSition?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  5  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:BOTTom <num>

Applicable Models: All (Read-Write) Sets the minimum scale value for the Log
Y-axis.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Minimum scale value. Range from 10f to 500P.  
Examples |  DISP:WIND:TRAC:Y:BOTT 0 display:window2:trace2:y:bottom 100  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:BOTTom?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:TOP <num>

Applicable Models: All (Read-Write) Sets the maximum scale value for the Log
Y-axis.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use [Disp:Wind:Cat?](Display.md#dwc) to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#trace_status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<num> |  Maximum scale value. Range from 20f to 1E.  
Examples |  DISP:WIND:TRAC:Y:TOP 0 display:window2:trace2:y:top 100  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:Y[:SCALe]:TOP?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1k  
  
* * *

## DISPlay:WINDow<wnum>:TRACe<tnum>:Y:SPACing<char>

Applicable Models: All (Read-Write) Sets or returns format type for Y axis
graph, either linear or logarithmic.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1 Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<tnum> |  Any existing trace number; if unspecified, value is set to 1. Use Disp:Wind:Cat? to read the trace numbers in an existing window. Note: This is NOT the trace number of the channel which appears as the [Tr annotation](../../S1_Settings/Customize_Your_Analyzer_Screen.md#Trace_Status) on the Trace Status display. This <tnum> is the trace number within the specified window, and is used ONLY for remote programs.  
<char> |  choose either LINear or LOGarithmic  
Examples |  DISP:WIND:TRACY:SPAC LOG Display:window2:trace2:y:spacing logarithmic  
Query Syntax |  DISPlay:WINDow<wnum>:TRACe<tnum>:Y:SPACing?  
Return Type |  char  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Lin  
  
* * *

## DISPlay:WINDow<wnum>:Y:AUTO

Applicable Models: All (Write-only) Scales ALL of the traces to fit in the
same window. This is equivalent to "Autoscale All" from the front panel.
Autoscale behaves differently when [scale
coupling](Display.htm#scaleCouplState) is enabled. How it behaves depends on
the scale coupling method. [Learn
more.](../../S1_Settings/Scale.htm#ScaleCoupling) Autoscale is performed only
when the command is sent; it does NOT keep the trace autoscaled indefinitely.
See Also, [DISPlay:WINDow:TRACe:Y:AUTO](Display.md#yauto) which Autoscales
only the specified trace.  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1. Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
Examples |  DISP:WIND:Y:AUTO  
display:window2:y:auto  
Query Syntax |  Not applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

##  DISPlay:WINDow<wnum>:Y[:SCALe]:DIVisions <num>

Applicable Models: All (Read-Write) Sets or returns the number of Y-axis
divisions in all the graphs, for the selected channel  
---  
Parameters |   
<wnum> |  Any existing window number. If unspecified, value is set to 1 Use [Disp:Cat?](Display.md#cat) to read the existing window numbers.  
<num> |  Number of divisions is from 2 to 30. Units / division value. The range of acceptable values is dependent on format and domain. Note: This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples |  DISP:WIND:Y:DIV 12 Display:window2:y:scale:divisions 12  
Query Syntax |  DISPlay:WINDow<wnum>:Y[:SCALe]:DIVisions?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10  
  
* * *

