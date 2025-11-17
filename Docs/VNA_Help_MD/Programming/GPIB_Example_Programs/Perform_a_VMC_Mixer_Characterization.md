# Perform a VMC Mixer Characterization

* * *

This example performs a VMC Mixer Characterization ONLY.

To run this example program without error:

  * Replace the ECal module model and serial number with that of your own, or a mechanical cal kit model.

  * Store a 'default.csa' instrument state file on the VNA with the setup information for your mixer. Or add mixer setup information to this program. [See an example.](Create_and_Cal_a_VMC_Measurement.md)

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
scpi.Parse "MMEM:LOAD 'default.csa'" ' Perform Cal ' Define the connector and
calkit for port 1 of the VNA scpi.Parse "sens:corr:coll:guid:conn:port1 'APC
3.5 female'" scpi.Parse "sens:corr:coll:guid:ckit:port1 'N4691-60004 ECal
02593'" ' Define the connector and calkit for the mixer output port scpi.Parse
"sens:corr:coll:guid:conn:port3 'APC 3.5 female'" scpi.Parse
"sens:corr:coll:guid:ckit:port3 'N4691-60004 ECal 02593'" ' Select a
characterization only calibration. This produces an s2p ' file of the mixer -
so the mixer can be used as a calibration ' mixer for the VMC calibration '
The outcome of the calibration is an S2P file. scpi.Parse
"SENS:CORR:COLL:GUID:VMC:OPER 'CHAR'" scpi.Parse
"SENS:CORR:COLL:GUID:VMC:MIXer:CHAR:CAL:FIL 'C:\Program
Files(x86)\Keysight\Network Analyzer\Documents\MyMixer.s2p'" ' Set ECal Auto
orientation ON scpi.Parse "SENS:CORR:PREF:ECAL:ORI ON" ' For the mixer char
step ONLY, ' Auto orientation is turned OFF by the VNA. ' Otherwise it would
fail because of the loss of the mixer. ' Manually set the ECal orientation for
that step. scpi.Parse "SENS:CORR:COLL:GUID:VMC:MIXer:ECAL:PORTmap 1,'B1'" '
the main calibration loop ' a description for the connection instructions is
read ' and then the standard is acquired dim steps, strPrompt scpi.Parse
"sens:corr:coll:guid:init" steps=scpi.Parse ("sens:corr:coll:guid:steps?")
wscript.echo "Number of Steps = " \+ cstr(steps) if (steps > 0) then '
otherwise an error condition occurred for i = 1 to steps strPrompt =
scpi.Parse ("sens:corr:coll:guid:desc? " \+ CStr(i)) MsgBox strPrompt,
vbOKOnly, step scpi.Parse ("sens:corr:coll:guid:acq STAN" \+ CStr(i)) next
scpi.Parse "sens:corr:coll:guid:save" MsgBox ("Cal is done!") end if  
---  
  
* * *

