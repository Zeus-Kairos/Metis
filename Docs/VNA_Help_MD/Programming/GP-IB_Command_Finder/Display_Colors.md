# Display Color Commands

* * *

Controls the color settings of the VNA display.

DISPlay:COLor [ABACkground](Display_Colors.md#ActiveBack) [BACKground](Display_Colors.md#back) [GRAT1](Display_Colors.md#grat1) [GRAT2](Display_Colors.md#grat2) [ILABel](Display_Colors.md#inLabel) [LIM1](Display_Colors.md#limit) [LOAD](Display_Colors.md#load) [RESet](Display_Colors.md#reset) [STORe](Display_Colors.md#store) TRACe | [DATA](Display_Colors.md#traceData) | [MARKer](Display_Colors.md#marker) | [MEMory](Display_Colors.md#memory) | [MMARker](Display_Colors.md#mmarker)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [Learn about Display and Print Colors](Display_Colors.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## DISPlay:COLor<n>:ABACkground <num, num, num>

Applicable Models: All (Read-Write) Set and return the background color for
the active window on the VNA display or hardcopy print.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:ABAC 10,10,10 display:color1:abackground 80,80,80  
Query Syntax | DISPlay:COLor<n>:ABACkground?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Display = 0,0,24 (Black) Print = 255,255,255 (White)  
  
* * *

## DISPlay:COLor<n>:BACKground <num, num, num>

Applicable Models: All (Read-Write) Set and return the background color for
the inactive windows on the VNA display or hardcopy print.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:BACK 10,10,10 display:color1:background 80,80,80  
Query Syntax | DISPlay:COLor<n>:BACKground?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Display = 0,0,0 (Black) Print = 255,255,255 (White)  
  
* * *

## DISPlay:COLor<n>:GRAT1 <num, num, num>

Applicable Models: All (Read-Write) Set and return the labels and grid frame
colors in the active window for the VNA display or hardcopy print. (Active
labels, Grid frame)  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:GRAT1 10,10,10 display:color1:grat1 80,80,80  
Query Syntax | DISPlay:COLor<n>:GRAT1?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Display = 175,175,175 Print = 0,0,0 (Black)  
  
* * *

## DISPlay:COLor<n>:GRAT2 <num, num, num>

Applicable Models: All (Read-Write) Set and return the inner lines of all grid
in all windows, and the grid frame in inactive windows for the VNA display or
hardcopy print. (GRID)  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:GRAT2 10,10,10 display:color1:grat2 80,80,80  
Query Syntax | DISPlay:COLor<n>:GRAT2?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Display = 100,100,100 Print = 50,50,50  
  
* * *

## DISPlay:COLor<n>:ILABel <num, num, num>

Applicable Models: All (Read-Write) Set and return the Inactive (not selected)
Window Labels for the VNA display or hardcopy print.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:ILAB 10,10,10 display:color1:ilabel 80,80,80  
Query Syntax | DISPlay:COLor<n>:ILABel?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Display = 160,160,160 Print = 0,0,0 (Black)  
  
* * *

## DISPlay:COLor<n>:LIM1 <num, num, num>

Applicable Models: All (Read-Write) Set and return the limit line color of
failed traces or failure indicators (dots) and the word Fail.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:LIM1 10,10,10 display:color1:lim1 80,80,80  
Query Syntax | DISPlay:COLor<n>:LIM1?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Display = 255,20,20 Print = 255,20,20  
  
* * *

## DISPlay:COLor<n>:LOAD <value>

Applicable Models: All (Write-only) Load a color theme from a disc file.  
---  
Parameters |   
<n> | Colors to load. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<value> | String. Filename of the stored theme. The .colors suffix is automatically appended. By default, files are stored in C:\Program Files(x86)\Keysight\Network Analyzer\Colors\\. To store and load files from a different folder, specify the full path and filename.  
Examples | DISP:COL:LOAD "myDisplayTheme" display:color2:load "myPrintTheme"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## DISPlay:COLor<n>:RESet

Applicable Models: All (Write-only) Resets the current theme to the default
VNA colors.  
---  
Parameters |   
<n> | Colors to reset. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
Examples | DISP:COL:RES display:color2:reset  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## DISPlay:COLor<n>:STORe <value>

Applicable Models: All (Write-only) Saves the current color theme to a disc
file.  
---  
Parameters |   
<n> | Colors to store. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<value> | String. Filename. The .colors suffix is automatically appended. By default, files are stored in C:\Program Files(x86)\Keysight\Network Analyzer\Colors\\. To store and load files from a different folder, specify the full path and filename.  
Examples | DISP:COL:STOR "myDisplayTheme" display:color2:store "myPrintTheme"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## DISPlay:COLor<n>:TRACe<nth>:DATA <num, num, num>

Applicable Models: All (Read-Write) Set and return the color of Data and Limit
Lines for nth trace in a window.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<nth> | Numeric. Relative trace number in the window for which colors are set. This is not necessarily the trace number. [Learn more](../../System/Display_Colors.md#AbtTracePens). Choose from 1 to 8. If unspecified, <nth> is set to 1 (first trace).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:TRAC2:DATA 10,10,10 display:color1:trace5:data 80,80,80  
Query Syntax | DISPlay:COLor<n>:TRACe<nth>:DATA?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Varies for each trace.  
  
* * *

## DISPlay:COLor<n>:TRACe<nth>:MARKer <num, num, num>

Applicable Models: All (Read-Write) Set and return the color of data trace
markers for nth trace in a window.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<nth> | Numeric. Relative trace number in the window for which colors are set. This is not necessarily the trace number. [Learn more](../../System/Display_Colors.md#AbtTracePens). Choose from 1 to 8. If unspecified, <nth> is set to 1 (first trace).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:TRAC2:MARK 10,10,10 display:color1:trace5:marker 80,80,80  
Query Syntax | DISPlay:COLor<n>:TRACe<nth>:MARKer?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Varies for each trace.  
  
* * *

## DISPlay:COLor<n>:TRACe<nth>:MEMory <num, num, num>

Applicable Models: All (Read-Write) Set and return the memory trace color for
nth trace in a window.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<nth> | Numeric. Relative trace number in the window for which colors are set. This is not necessarily the trace number. [Learn more](../../System/Display_Colors.md#AbtTracePens). Choose from 1 to 8. If unspecified, <nth> is set to 1 (first trace).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:TRAC2:MEM 10,10,10 display:color1:trace5:memory 80,80,80  
Query Syntax | DISPlay:COLor<n>:TRACe<nth>:MEMory?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Varies for each trace.  
  
* * *

## DISPlay:COLor<n>:TRACe<nth>:MMARker <num, num, num>

Applicable Models: All (Read-Write) Set and return the color of memory trace
markers for nth trace in a window.  
---  
Parameters |   
<n> | Colors to modify. Choose from: 1 \- Display colors 2 \- Print colors If unspecified, <n> is set to 1 (Display colors).  
<nth> | Numeric. Relative trace number in the window for which colors are set. This is not necessarily the trace number. [Learn more](../../System/Display_Colors.md#AbtTracePens). Choose from 1 to 8. If unspecified, <nth> is set to 1 (first trace).  
<num, num, num> | Numeric. Red, Green, and Blue (RGB values) that specify a color. To find RGB values: from the [Display Colors dialog](../../System/Display_Colors.md#dispColorDiag), click Change Color, then Define Custom Color.  
Examples | DISP:COL:TRAC2:MMAR 10,10,10 display:color1:trace5:mmarker 80,80,80  
Query Syntax | DISPlay:COLor<n>:TRACe<nth>:MMARker?  
Return Type | Numeric (n,n,n)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Varies for each trace.  
  
* * *

  

