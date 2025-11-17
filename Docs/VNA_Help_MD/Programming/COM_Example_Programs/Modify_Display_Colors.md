# Modify Display Colors

* * *

This VBScript example modifies display colors, modifies trace1 colors, then
saves and recalls the theme.

These programs can be run as a macro in the VNA. To do this, copy the code
into a text editor file such as Notepad and save on the VNA hard drive as
Colors.vbs. [Learn how to setup and run the macro.](../Using_Macros.md)

function RGB(R, G, B) RGB = R + G*(2^8) + B*(2^16) end Function
shell.AppActivate "PNA Series Network Analyzer" Set app =
CreateObject("AgilentPNA835X.Application") app.preset Set colors =
app.Preferences.DisplayColors ' Uncomment the following line to modify Print
colors ' Set colors = app.Preferences.PrintColors colors.ResetTheme( )
colors.background = RGB(64,0,64) ' purple  displaycolors.grid = RGB(0,255,128)
' greenish colors.activeLabels = RGB(0,0,255) ' blue colors.inactiveLabels =
RGB(255,0,0) ' red colors.failedTraces = RGB(255,128,64) ' orange dim Trace1
Set Trace1 = colors.Trace(1) Trace1.DataAndLimits = RGB(1,251,1) ' green
Trace1.Memory = RGB(251,1,1) ' red Trace1.Markers = RGB(251,251,251) ' white
Trace1.MemoryMarkers = RGB(1,251,251) ' green + blue
colors.StoreTheme("c:\Program Files(86)\Keysight\Network
Analyzer\Colors\Theme1.colors") colors.LoadTheme("c:\Program
Files(86)\Keysight\Network Analyzer\Colors\Theme1.colors")  
---  
  
* * *

