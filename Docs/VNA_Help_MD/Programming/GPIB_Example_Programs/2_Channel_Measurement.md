# 2 Channel Measurement

This example program demonstrates a 2 channel measurement that allows you to
make TDR measurement on channel 1 and a more customized S-parameter
measurement on channel 2. This is a program example of the [2 Channel
Measurement
Example](../../Applications/Enhanced_Time_Domain_Analysis/Measurement_Examples/TDR_-_2_Channel_Measurement_Example.htm).

This program example is written in Excel VBA (VISA-COM).

#### See Also:

[TDR Programming
Commands](../../Applications/Enhanced_Time_Domain_Analysis/Enhanced_Time_Domain_Analysis.htm#TDR_Programming_Commands:)

[SCPI Example Programs](SCPI_Example_Programs.md)

Dim rm As VisaComLib.ResourceManager Dim vna As VisaComLib.FormattedIO488
Private Sub Message(msg As String) Dim NumDmy As Integer ' Syncronize to VNA
vna.WriteString "*OPC?" NumDmy = vna.ReadNumber ' Write Message MsgBox msg,
vbOKOnly End Sub Private Sub SetupCh1Measurement() On Error GoTo errorhandler
With vna ' Execute ECal using TDR Setup Wizard .WriteString
":DISP:TDR:MIN:STAT OFF" Message "[Full Calibration (ECal)]" \+ vbCrLf + _
"1\. Press 'TDR Setup Wizard' on TDR GUI." \+ vbCrLf + _ "2\. Select 'Full
Calibration (ECal)' and complete the wizard." \+ vbCrLf + _ "3\. Confirm 'TDR
[Full]' indicator appears on VNA status line." \+ vbCrLf + _ "4\. Press OK
button to continue." ' Minimize TDR GUI .WriteString ":DISP:TDR:MIN:STAT ON" '
Set Rise Time/Threshold For i = 1 To 8 .WriteString ":CALC:TDR:MEAS" \+
CStr(i) + ":TIME:STEP:RTIM:THR T2_8" .WriteString ":CALC:TDR:MEAS" \+ CStr(i)
+ ":TIME:STEP:RTIM 50e-12" Next i ' Setup Target Trace .WriteString
":CALC:TDR:MEAS1:PAR TDD11" 'Parameter .WriteString ":CALC:TDR:MEAS1:FORM IMP"
'Format ' Setup limit line .WriteString ":CALC:MEAS1:LIM:DATA
1,0,1e-9,105,105,2,0,1e-9,75,75" .WriteString ":CALC:MEAS1:LIM ON"
.WriteString ":CALC:MEAS1:LIM:DISP ON" End With Exit Sub errorhandler: MsgBox
Err.Description, vbExclamation, "Error Occurred", Err.HelpFile,
Err.HelpContext End Sub Private Sub ExecCh1Measurement() On Error GoTo
errorhandler Dim TimeData() As Double, Impedance() As Double Dim Nop As
Integer, PassFail As Integer, i As Integer, k As Integer With vna ' Exec
Trigger and Synchronize .WriteString ":SENS:TDR:SWE:SING;*OPC?" NumDmy =
.ReadNumber ' Auto Scale .WriteString ":DISP:TDR:SCAL:AUTO" ' Get Number Of
Points .WriteString ":SENS1:SWE:POIN?" Nop = .ReadNumber ReDim TimeData(Nop -
1) ReDim Impedance(Nop - 1) ' Get X-axis data .WriteString
":CALC:MEAS1:X:VAL?" TimeData() = .ReadList(ASCIIType_R8, ",") ' Get
Y-axis(Impedance) data .WriteString ":CALC:MEAS1:DATA:FDAT?" Impedance() =
.ReadList(ASCIIType_R8, ",") ' Get limit line test result .WriteString
":CALC:MEAS1:LIM:FAIL?" PassFail = .ReadNumber ' Write Results Cells(4, 4) =
"CH1" Cells(6, 4) = "Time" Cells(6, 5) = "Data" For i = 0 To Nop - 1 Cells(i +
7, 4) = TimeData(i) Cells(i + 7, 5) = Impedance(i) Next i If PassFail = 1 Then
Cells(4, 5) = "FAILED" Else Cells(4, 5) = "PASSED" End If End With Exit Sub
errorhandler: MsgBox Err.Description, vbExclamation, "Error Occurred",
Err.HelpFile, Err.HelpContext End Sub Private Sub SetupCh2Measurement() On
Error GoTo errorhandler With vna ' Create new measurement in CH2 .WriteString
":CALC:PAR:MNUM:SEL 8" 'Activate the last trace .WriteString ":DISP:WIND5:STAT
ON" 'Create new window .WriteString ":CALC2:PAR:DEF:EXT 'ch2_meas','S11'"
.WriteString ":DISP:WIND5:TRAC9:FEED 'ch2_meas'" ' Setup stimulus .WriteString
":SENS2:FREQ:STAR 1e9" .WriteString ":SENS2:FREQ:STOP 3e9" .WriteString
":SENS2:SWE:POIN 201" .WriteString ":SENS2:BWID 1e3" ' Execute 4-port ECal
using 2-port ECal module Dim ecalCmd As String calCmd =
":SENS2:CORR:COLL:GUID:" For i = 1 To 4 .WriteString calCmd + "CONN:PORT" \+
CStr(i) + " 'APC 3.5 female'" .WriteString calCmd + "CKIT:PORT" \+ CStr(i) + "
'N4691-60006 ECal'" Next i .WriteString calCmd + "INIT" .WriteString calCmd +
"STEPS?" nSteps = .ReadNumber For i = 1 To nSteps .WriteString calCmd + "DESC?
" \+ CStr(i) Message "[ECal for Channel 2 (" \+ CStr(i) + "/" \+ CStr(nSteps)
+ ")]" \+ vbCrLf + .ReadString .WriteString calCmd + "ACQ STAN" \+ CStr(i)
Next i .WriteString calCmd + "SAVE" Message "Finished ECal for Channel 2" '
Set measurement parameter to Sdd21 .WriteString ":CALC2:DTOP 'BB',1,2,3,4"
'Bal-Bal .WriteString ":CALC2:MEAS9:PAR SDD21" ' Setup limit line .WriteString
":CALC2:MEAS9:LIM:DATA
2,100e6,1.25e9,-1.5,-5,2,1.25e9,2.5e9,-5,-7.5,2,2.5e9,7.5e9,-7.5,-25"
.WriteString ":CALC2:MEAS9:LIM ON" .WriteString ":CALC2:MEAS9:LIM:DISP ON" End
With Exit Sub errorhandler: MsgBox Err.Description, vbExclamation, "Error
Occurred", Err.HelpFile, Err.HelpContext End Sub Private Sub
ExecCh2Measurement() On Error GoTo errorhandler Dim FreqData() As Double,
InsersionLoss() As Double Dim Nop As Integer, PassFail As Integer, i As
Integer, k As Integer With vna ' Exec Trigger and Synchronize .WriteString
":SENS2:SWE:MODE SING;*OPC?" NumDmy = .ReadNumber ' Get Number of Points
.WriteString ":SENS2:SWE:POIN?" Nop = .ReadNumber ' Get X-axis data ReDim
FreqData(Nop - 1) .WriteString ":CALC2:MEAS9:X:VAL?" FreqData() =
.ReadList(ASCIIType_R8, ",") ' Get Y-axis (Sdd21) data ReDim InsersionLoss(Nop
- 1) .WriteString ":CALC2:MEAS9:DATA:FDATA?" InsersionLoss() =
.ReadList(ASCIIType_R8, ",") ' Get limit line test result .WriteString
":CALC2:MEAS9:LIM:FAIL?" PassFail = .ReadNumber ' Write Results Cells(4, 7) =
"CH2" Cells(6, 7) = "Freq." Cells(6, 8) = "Data" For i = 0 To Nop - 1 Cells(i
+ 7, 7) = FreqData(i) Cells(i + 7, 8) = InsersionLoss(i) Next i If PassFail =
1 Then Cells(4, 8) = "FAILED" Else Cells(4, 8) = "PASSED" End If End With Exit
Sub errorhandler: MsgBox Err.Description, vbExclamation, "Error Occurred",
Err.HelpFile, Err.HelpContext End Sub Sub TwoChannelsMeasurement() On Error
GoTo errorhandler Set rm = New VisaComLib.ResourceManager Set vna = New
VisaComLib.FormattedIO488 ' Set VNA Address Set vna.IO =
rm.Open("TCPIP0::K-N5232B-40046::hislip0::INSTR") vna.IO.Timeout = 90000 '
Clear Excel Sheet Cells Range("A1:H10010").ClearContents With vna 'Set DUT
Topology first .WriteString ":CALC:TDR:DEV DIF2" ' Setup Measurement Call
SetupCh1Measurement Call SetupCh2Measurement ' Exec Measurement Message
"Connect DUT to cables." \+ vbCrLf + "Press OK to execute measurement." Call
ExecCh1Measurement Call ExecCh2Measurement 'Restore TDR GUI .WriteString
":DISP:TDR:MIN:STAT OFF" Message "Finished 2 Channels Measurement." End With
vna.IO.Close Exit Sub errorhandler: MsgBox Err.Description, vbExclamation,
"Error Occurred", Err.HelpFile, Err.HelpContext End Sub  
---

