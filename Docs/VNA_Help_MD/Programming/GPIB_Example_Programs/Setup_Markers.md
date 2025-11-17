## Set Up Markers using SCPI

* * *

This VBScript program does the following:

  * Preset the VNA

  * Return active channel number and measurement string

  * Create a marker

  * Set X-axis value

  * Read X, Y-axis values

  * Set marker to trace Min

  * Read X, Y-axis values

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Markers.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See all Marker SCPI commands.](../GP-IB_Command_Finder/Calculate/Marker.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim na, vi, ret Set na = CreateObject("AgilentPNA835x.Application") Set vi =
na.ScpiStringParser 'Get Identification String from Analyzer
ret=vi.Parse("*IDN?") msgbox ret 'Preset VNA ret=vi.Parse("SYST:PRES; *OPC?")
'Get Active Channel and Measurement chan = vi.Parse("SYST:ACT:CHAN?") meas =
vi.Parse("SYST:ACT:MEAS?") 'Convert chan to a single number
chan=CStr(CInt(chan)) 'Select Active Measurement vi.Parse "CALC" \+ chan +
":PAR:SEL " \+ meas 'Turn Marker 1 on and set X value to 1 GHz vi.Parse "CALC"
\+ chan + ":MARK1:STAT ON" vi.Parse "CALC" \+ chan + ":MARK1:X 1e9" 'Get X and
Y marker values x_val = vi.Parse("CALC" \+ chan + ":MARK1:X?") y_val =
vi.Parse("CALC" \+ chan + ":MARK1:Y?") 'Display Marker Values msgbox "X Value
= " \+ x_val + Chr(10) \+ "Y Value = " \+ y_val 'Use Marker 1 as a minimum
search vi.Parse "CALC" \+ chan + ":MARK1:FUNC:EXEC MIN" 'Get X and Y marker
values x_val = vi.Parse("CALC" \+ chan + ":MARK1:X?") y_val = vi.Parse("CALC"
\+ chan + ":MARK1:Y?") 'Display Marker Values msgbox "X Value = " \+ x_val +
Chr(10) \+ "Y Value = " \+ y_val  
---  
  
* * *

