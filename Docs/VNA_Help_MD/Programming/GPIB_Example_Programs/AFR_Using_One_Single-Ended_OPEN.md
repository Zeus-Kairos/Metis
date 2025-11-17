# AFR Using One Single-Ended OPEN

* * *

This VBScript program performs AFR using one single-ended OPEN, saves the
fixture data to a file, then performs deembedding.

Each VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the code into a text editor file, such as Notepad, and save it on the PNA
hard drive as *.vbs.

### See Also:

[Learn how to setup and run the macro](../Using_Macros.md#HowToSetup)

[SCPI Example Programs](SCPI_Example_Programs.md)

Dim app  
Dim scpi  
Set app = CreateObject("AgilentPNA835x.Application")  
Set scpi = app.ScpiStringParser  
  
'The AOPen data file should alreay exist  
aopenFile = "S:\case_05\AOpen.s1p"  
'Fixture data file will be created or overwritten  
fixaFile = "S:\case_05\\_demo_fix_a.s2p"  
  
'AFR extracts fixture files  
scpi.Execute("AFR:INITialize")  
scpi.Execute("AFR:FIXTure:MEASurement 1")  
scpi.Execute("AFR:STANdard:USE AOPen")  
scpi.Execute("AFR:STANdard:LOAD AOPen," & Q(aopenFile))  
scpi.Execute("AFR:SAVE:PORTs VNA")  
scpi.Execute("AFR:SAVE:FILename " & Q(fixaFile))  
opc = scpi.Execute("*OPC?")  
  
' deembedding  
scpi.Execute("CALC:FSIM:SEND:DEEM:PORT1:USER:FILename " & Q(fixaFile))  
scpi.Execute("CALC:FSIM:SEND:DEEM:PORT1:TYPE USER")  
scpi.Execute("CALC:FSIM:SEND:DEEM:STATe ON")  
scpi.Execute("CALC:FSIM:STATe ON")  
opc = scpi.Execute("*OPC?")  
  
Set scpi = Nothing  
Set app = Nothing  
  
'Add double quotation marks to a string  
Function Q(s)  
Q = Chr(34) & s & Chr(34)  
End Function

