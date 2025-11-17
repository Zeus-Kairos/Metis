# Calculate:Equation Commands

* * *

Controls Equation Editor capabilities.

CALCulate:EQUation: LIBRary | [FUNCtions](Equation.md#LibraryFunctions) | [IMPort?](Equation.md#LibraryImport) | PYTHon | [:STATe]? | MODules? | VERsion? | [REMove](Equation.md#LibraryRemove) [STATe](Equation.md#state) [TEXT](Equation.md#text) [VALid?](Equation.md#valid)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Equation Editor](../../../S4_Collect/Equation_Editor.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

CALCulate:EQUation:LIBRary:FUNCtions <string>

Applicable Models: All (Read-only) Returns the functions in the specified DLL.  
---  
Parameters |   
<string> |  Full path and filename of the *.dll to be read.  
Examples |  functions = CALC:EQU:LIBR:FUNC C:\Program Files(x86)\Keysight\Network Analyzer\UserFunctions\Expansion.dll  
Query Syntax |  CALCulate:EQUation:LIBRary:FUNCtions?  
Return Type |  Comma delimited string of function names.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate:EQUation:LIBRary:IMPort <string>

Applicable Models: All (Read-Write) Imports the functions in the specified DLL
and returns whether the functions have been imported into the VNA.  
---  
Parameters |   
<string> |  Full path and filename of the *.dll.  
Examples |  'Command - Imports functions CALC:EQU:LIBR:IMPort C:\Program Files(x86)\Keysight\Network Analyzer\UserFunctions\Expansion.dll  'Query if Imported successfully success = CALC:EQU:LIBR:IMPort? C:\Program Files(x86)\Keysight\Network Analyzer\UserFunctions\Expansion.dll 1 'Returns 1 if successfully imported  
Query Syntax |  CALCulate:EQUation:LIBRary:IMPort? Returns the following: 1 \- Imported 0 \- NOT imported  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate:EQUation:LIBRary:PYTHon[:STATe]?

Applicable Models: All (Read-only) Returns a boolean value to indicate if
Python is installed.  
---  
Parameters |   
<Boolean> |  1  Python is installed 0  Python is NOT installed  
Examples |  CALC:EQU:LIBR:PYTH?   
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate:EQUation:LIBRary:PYTHon:MODules?

Applicable Models: All (Read-only) Returns all importable Python packages and
their version numbers as provided by sys.path.  
---  
Parameters |   
<string> |  Comma delimited list of Python packages and their version numbers  
Examples |  CALC:EQU:LIBR:PYTH:MOD? Returns "setuptools 65.5.0,pip 23.1.2,packaging 23.1,Pillow 9.5.0,fonttools 4.40.0,matplotlib 3.7.1,networkx 3.1,pyparsing 3.1.0,python-dateutil 2.8.2,soupsieve 2.4.1,numpy 1.25.2,six 1.16.0,scipy 1.11.1,kiwisolver 1.4.4,contourpy 1.1.0,importlib 1.0.4,cycler 0.11.0"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate:EQUation:LIBRary:PYTHon:VERsion?

Applicable Models: All (Read-only) Returns a string containing the Python
version number if Python is installed, else returns an empty string.  
---  
Parameters |   
<string> |  Python version number  
Examples |  CALC:EQU:LIBR:PYTH:VER? Returns "Python 3.11.4"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate:EQUation:LIBRary:REMove <string>

Applicable Models: All (Write-only) Removes an imported an Equation Editor DLL
from the VNA.  
---  
Parameters |   
<string> |  Full path and filename of the *.dll.  
Examples |  CALC:EQU:LIBR:REM C:\Program Files(x86)\Keysight\Network Analyzer\UserFunctions\Expansion.dll   
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate<cnum>:EQUation[:STATe] <bool>

Applicable Models: All (Read-Write) Turns ON and OFF the equation on selected
measurement for the specified channel. If the equation is not valid, then
processing is not performed. Use [CALC:EQUation:VALid?](Equation.md#valid) to
ensure that the equation is valid.  See Critical Note  
---  
Parameters |   
<cnum> |  Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> |  **ON** (or 1) - turns equation ON. **OFF** (or 0) - turns equation OFF.  
Examples |  CALC:EQU 1 calculate2:equation:state 0  
Query Syntax |  CALCulate<cnum>:EQUation[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

CALCulate<cnum>:EQUation:TEXT <string>

Applicable Models: All (Read-Write) Specifies an equation or expression to be
used on the selected measurement for the specified channel.  See Critical Note  
---  
Parameters |   
<cnum> |  Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<string> |  Any valid equation or expression. [See Equation Editor.](../../../S4_Collect/Equation_Editor.md)  
Examples |  'Equation (includes '=') CALC:EQU:TEXT "foo=S11/S21" 'Expression  
calculate2:equation:text "S11/S21"  
Query Syntax |  CALCulate<cnum>:EQUation:TEXT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

CALCulate<cnum>:EQUation:VALid?

Applicable Models: All (Read-Only) Returns a boolean value to indicate if the
current equation on the selected measurement for the specified channel is
valid. For equation processing to occur, the equation must be valid and ON
([CALC:EQU:STAT 1](Equation.md#state)).  See Critical Note  
---  
Parameters |   
<cnum> |  Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples |  CALC:EQU:VAL? calculate2:equation:valid?  
Return Type |  Boolean 1 - equation is valid 0 - equation is NOT valid  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

