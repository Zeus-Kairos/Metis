# AFR Using One Differential 2X THRU

* * *

This VBScript program performs AFR using one differential 2X THRU, saves the
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
  
'The 2X THRU data file should alreay exist  
thruFile = "S:\case_02\AA.s4p"  
'Fixture A and B data file will be created or overwritten  
fixaFile = "S:\case_02\\_demo_fix_a.s4p"  
fixbFile = "S:\case_02\\_demo_fix_b.s4p"  
  
'AFR extracts fixture files  
scpi.Execute("AFR:INITialize")  
scpi.Execute("AFR:FIXTure:INPuts DIFFerential")  
scpi.Execute("AFR:FIXTure:MEASurement 4")  
scpi.Execute("AFR:STANdard:USE THRU,1")  
scpi.Execute("AFR:STANdard:LOAD THRU," & Q(thruFile))  
scpi.Execute("AFR:SAVE:PORTs VNA")  
scpi.Execute("AFR:SAVE:FILename " & Q(fixaFile) & "," & Q(fixbFile))  
opc = scpi.Execute("*OPC?")  
  
'Deembedding  
scpi.Execute("CALC:FSIM:EMB:TYPE C")  
scpi.Execute("CALC:FSIM:EMB:TOP:C:PORT 1,2,3,4")  
scpi.Execute("CALC:FSIM:EMBed:NETWork1:FILename " & Q(fixaFile))  
scpi.Execute("CALC:FSIM:EMBed:NETWork1:PMAP 1,2,3,4")  
scpi.Execute("CALC:FSIM:EMBed:NETWork1:TYPE DEEMbed")  
scpi.Execute("CALC:FSIM:EMBed:NETWork2:FILename " & Q(fixbFile))  
scpi.Execute("CALC:FSIM:EMBed:NETWork2:PMAP 1,2,3,4")  
scpi.Execute("CALC:FSIM:EMBed:NETWork2:TYPE DEEMbed")  
scpi.Execute("CALC:FSIM:EMBed:STATe ON")  
scpi.Execute("CALC:FSIM:STATe ON")  
opc = scpi.Execute("*OPC?")  
  
Set scpi = Nothing  
Set app = Nothing  
  
'Add double quotation marks to a string  
Function Q(s)  
Q = Chr(34) & s & Chr(34)  
End Function

