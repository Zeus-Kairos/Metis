## Set Up Receiver Leveling using SCPI

* * *

This VBScript program configures Receiver Leveling.

  * Preset the VNA

  * Make all receiver leveling settings

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as RxLev.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See all Recevier Leveling SCPI commands.](../GP-IB_Command_Finder/source.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Set pna = CreateObject("AgilentPNA835x.Application") Set SCPI =
pna.ScpiStringParser 'set source port dim srcP srcP = "1" 'Preset PNA
SCPI.Parse "SYST:PRES" SCPI.Parse "sour1:pow" \+ srcP + "-15" SCPI.Parse
"sour1:pow" \+ srcP + ":alc:mode:rec:ref 'R1'" SCPI.Parse "sour1:pow" \+ srcP
+ ":alc:mode:rec:tol 0.02" SCPI.Parse "sour1:pow" \+ srcP +
":alc:mode:rec:iter 10" SCPI.Parse "sour1:pow" \+ srcP + ":alc:mode:rec:fast
OFF" SCPI.Parse "sour1:pow" \+ srcP + ":alc:mode:rec:ifbw 100" SCPI.Parse
"sour1:pow" \+ srcP + ":alc:mode:rec:offs 0" SCPI.Parse "sour1:pow" \+ srcP +
":alc:mode:rec:safe:max 20" SCPI.Parse "sour1:pow" \+ srcP +
":alc:mode:rec:safe:min -100" SCPI.Parse "sour1:pow" \+ srcP +
":alc:mode:rec:safe ON" 'Last, enable receiver leveling SCPI.Parse "sour1:pow"
\+ srcP + ":alc:mode:rec ON"  
---  
  
* * *

