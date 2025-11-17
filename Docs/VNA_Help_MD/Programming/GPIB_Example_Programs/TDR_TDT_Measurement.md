# TDR/TDT Measurement

This example program demonstrates how to perform TDR/TDT setup written in
Excel VBA (VISA-COM).

[See the TDR
commands.](../../Applications/Enhanced_Time_Domain_Analysis/Enhanced_Time_Domain_Analysis.htm#TDR_Programming_Commands:)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim rm As VisaComLib.ResourceManager Dim vna As VisaComLib.FormattedIO488 Sub
Message(msg As String) Dim NumDmy As Integer 'Syncronize to VNA
vna.WriteString "*OPC?" NumDmy = vna.ReadNumber 'Write Message MsgBox msg,
vbOKOnly End Sub Sub TDRTDTMeasure() On Error GoTo errorhandler Set rm = New
VisaComLib.ResourceManager Set vna = New VisaComLib.FormattedIO488 ' Set VNA
Address Set vna.IO = rm.Open("TCPIP0::K-N5232B-40046::hislip0::INSTR")
vna.IO.Timeout = 90000 ' Clear Excel Sheet Cells Range("D5:F5").ClearContents
With vna Dim i As Integer ' Set DUT Topology to Differential 2-Port
.WriteString ":CALC:TDR:DEV DIF2" ' Desckew and Loss Compensation  
' ' Desckew .WriteString ":SENSe:CORR:TDR:EXTension:AUTO:IMMediate", True
.WriteString "*OPC?", True NumDmy = .ReadNumber '  
' Loss Compensation, thru MsgBox "Connect thru between ports 1 and 3.",
vbOKOnly .WriteString ":SENS:CORR:TDR:COLL:DLC:THRU 1,3", True .WriteString
"*OPC?", True NumDmy = .ReadNumber MsgBox "Connect thru between ports 2 and
4.", vbOKOnly .WriteString ":SENS:CORR:TDR:COLL:DLC:THRU 2,4", True
.WriteString "*OPC?", True NumDmy = .ReadNumber ' Loss Compensation, thru
MsgBox "Connect a Load to the ports 1,2,3,4.", vbOKOnly .WriteString
":SENS:CORR:TDR:COLL:DLC:LOAD 1", True .WriteString "*OPC?", True NumDmy =
.ReadNumbe .WriteString ":SENS:CORR:TDR:COLL:DLC:LOAD 2", True .WriteString
"*OPC?", True NumDmy = .ReadNumber .WriteString ":SENS:CORR:TDR:COLL:DLC:LOAD
3", True .WriteString "*OPC?", True NumDmy = .ReadNumber .WriteString
":SENS:CORR:TDR:COLL:DLC:LOAD 4", True .WriteString "*OPC?", True NumDmy =
.ReadNumber ' Save the data to finish the Deskew and Loss Compensation
.WriteString ":SENS:CORR:TDR:COLL:DLC:SAVE", True .WriteString "*OPC?", True
NumDmy = .ReadNumber ' Set Rise Time .WriteString "CALC:PAR:COUN?" 'Get number
of traces For i = 1 To .ReadNumber .WriteString ":CALC:TDR:MEAS" \+ CStr(i) +
":TIME:STEP:RTIM:THR T2_8" 'Threshold .WriteString ":CALC:TDR:MEAS" \+ CStr(i)
+ ":TIME:STEP:RTIM 50e-12" 'Rise Time Next i ' Measure Message "Connect DUT to
cables." \+ vbCrLf + "Press OK to execute measurement." .WriteString
":SENS:TDR:SWE:SING;*OPC?" NumDmy = .ReadNumber ' Auto Scale for all traces
.WriteString ":DISP:TDR:SCAL:AUTO" ' Read Rise Time of Tr 5 (Tdd21) Cells(5,
4) = "Rise Time" .WriteString ":CALC:TDR:MEAS5:TTIM:STAT ON" .WriteString
":CALC:TDR:MEAS5:TTIM:THR T2_8" .WriteString ":CALC:TDR:MEAS5:TTIM:DATA?"
Cells(5, 6) = .ReadNumber ' Restore TDR GUI .WriteString ":DISP:TDR:MIN:STAT
OFF" Message "Finished TDT/TDT Measurement." End With vna.IO.Close Exit Sub
errorhandler: MsgBox Err.Description, vbExclamation, "Error Occurred",
Err.HelpFile, Err.HelpContext End Sub  
---

