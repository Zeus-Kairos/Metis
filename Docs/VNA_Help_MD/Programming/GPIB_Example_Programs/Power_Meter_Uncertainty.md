# Power Meter Uncertainty

This VBScript program is an example of setting up power uncertainty on a power
meter.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Guided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

' ' Keysight Technologies 2018 ' ' Uncertainty on power meter example with
SCPI ' ' This script executes and prints the results of all the ' commands
related to the uncertainty on power meter '
''''''''''''''''''''''''''''''''''''''''' ' Create the Application and parser
objects  option explicit dim app, scpi set app =
CreateObject("AgilentPNA835x.Application") set scpi = app.ScpiStringParser
''''''''''''''''''''''''''''''''''''''''' ' query for the ID to verify the
communication is established wscript.echo scpi.execute("*IDN?") ' ' In the
following 'Device2' is name of the used external device ' ''''''''''''''''
QUERY COMMANDS ''''''''''''''''''' ' Query for the available power meter
models ' dim catalog catalog=scpi.Execute ("SYST:CONF:EDEV:PMAR:UNC:CAT?
'Device2' ") wscript.echo catalog ' the return is a csv value ' ' Query for
the file path. If the model is NOT Custom Model this function will return '
"Undefined" ' wscript.echo scpi.Execute ("SYST:CONF:EDEV:PMAR:UNC:FILE?
'Device2' ") ' ' Query for the pwr mtr model used. wscript.echo scpi.Execute
("SYST:CONF:EDEV:PMAR:UNC:MOD? 'Device2' ") ' ' Query for the uncertainty of
the pwr meter at 0.GHz and with 10dBm power level wscript.echo scpi.Execute
("SYST:CONF:EDEV:PMAR:UNC:READ? 'Device2',0.1GHz,10.0 ") ' ' Query for the
optimum power level (minimum uncertainty) for for the selected  ' power meter
wscript.echo scpi.Execute ("SYST:CONF:EDEV:PMAR:UNC:PLEV? 'Device2' ") '
'''''''''''''''' SETTING COMMANDS ''''''''''''''''''' ' ' Setting a specific
model:  scpi.Execute ("SYST:CONF:EDEV:PMAR:UNC:MOD 'Device2','N8482A' ") ' '
Setting a custom file scpi.Execute ("SYST:CONF:EDEV:PMAR:UNC:FILE
'Device2','C:\Users\Public\Documents\Network Analyzer\UncSensorExample.dat' ")
' '  
---

