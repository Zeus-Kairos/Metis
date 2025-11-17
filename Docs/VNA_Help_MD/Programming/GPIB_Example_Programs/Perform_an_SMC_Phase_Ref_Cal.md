# Perform an SMC Phase Reference Calibration

* * *

This example sets Phase Reference Cal properties, then performs a Phase
Reference calibration.

It is NOT necessary to create an SMC measurement before performing a remote
Phase Reference Cal. It is necessary when performed from the user interface.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Phase Reference Cal SCPI commands](../GP-
IB_Command_Finder/SystCalPhase.htm)

[Learn about SMC with Phase Ref
Cal](../../FreqOffset/Phase_Reference_Calibration.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Set app = CreateObject("agilentpna835x.application") SET s =
app.scpistringparser s.parse "SYST:PRES" s.parse "SENS:SWE:MODE HOLD" 'Set cal
params s.parse "SYST:CAL:PHAS:RESet" s.parse "SYST:CAL:PHAS:FREQ:STAR 1e9"
s.parse "SYST:CAL:PHAS:FREQ:STOP 10E9" ' Read then set the phase ref ID '
Change this to your phase ref name s.parse "SYST:CAL:PHAS:REF 'MYPILOT44'"
s.parse "SYST:CAL:PHAS:POW:ATT 10" s.parse "SYST:CAL:PHAS:CONN 'APC 3.5
female'" s.Parse "SYST:CAL:PHAS:CKIT '85052D'" ' turn on port 4 as well. Port
1 and Port 2 are always on s.parse "SYST:CAL:PHAS:PORT4 on" ' Uncomment the
following line to use ' an unknown mixer to measure below 55 Mhz. ' If the
unknown mixer cal is ON, then the start frequency of the ' entire calibration
is always 10 Mhz ' s.parse "SYST:CAL:PHAS:UNKN:INCLude ON" ' Read chan num
then begin guided cal chan = s.parse("SYST:CAL:PHAS:GUID:CHAN?") header =
"SENS" & CInt(chan) & ":CORR:COLL:GUID:" S.parse header & "INIT" steps =
s.parse(header & "STEPS?") wscript.echo steps ' Acquire stds for i = 1 to
steps Msgbox s.parse(header & "DESC? " & i) s.parse header & "ACQ STAN" & i
next s.parse header & "SAVE:CSET 'scpi_phase_reference'" msgbox "done"  
---  
  
* * *

