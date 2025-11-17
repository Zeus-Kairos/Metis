# Simulated Eye Diagram

This example program demonstrates how to perform a simulated eye diagram
written in Excel VBA (VISA-COM).

[See the TDR
commands.](../../Applications/Enhanced_Time_Domain_Analysis/Enhanced_Time_Domain_Analysis.htm#TDR_Programming_Commands:)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim rm As VisaComLib.ResourceManager Dim vna As VisaComLib.FormattedIO488 Sub
Message(msg As String) Dim NumDmy As Integer 'Syncronize to VNA
vna.WriteString "*OPC?" NumDmy = vna.ReadNumber 'Write Message MsgBox msg,
vbOKOnly End Sub Sub SimEyeDiagram() On Error GoTo errorhandler Set rm = New
VisaComLib.ResourceManager Set vna = New VisaComLib.FormattedIO488 ' Set your
VNA address Set vna.IO = rm.Open("TCPIP0::K-N5232B-40046::hislip0::INSTR")
vna.IO.Timeout = 90000 ' Clear Excel Sheet Cells Range("A1:F22").ClearContents
With vna Dim i As Integer ' Set DUT Topology to Differential 2-Port
.WriteString ":CALC:TDR:DEV DIF2" ' Execute Deskew using TDR Setup Wizard
.WriteString ":DISP:TDR:MIN:STAT OFF" Message "[Deskew]" \+ vbCrLf + _ "1\.
Press 'TDR Setup Wizard' on TDR GUI." \+ vbCrLf + _ "2\. Select 'Deskew' and
complete the wizard with 'Finish' button." \+ vbCrLf + _ "3\. Confirm 'TDR
[Deskew]' indicator appears on VNA status line." \+ vbCrLf + _ "4\. Press OK
button to continue." ' Minimize TDR GUI .WriteString ":DISP:TDR:MIN:STAT ON" '
Set Rise Time .WriteString "CALC:PAR:COUN?" 'Get number of traces For i = 1 To
.ReadNumber .WriteString ":CALC:TDR:MEAS" \+ CStr(i) + ":TIME:STEP:RTIM:THR
T2_8" 'Threshold .WriteString ":CALC:TDR:MEAS" \+ CStr(i) + ":TIME:STEP:RTIM
50e-12" 'Rise Time Next i ' Set Bit Pattern Parameters .WriteString
":CALC:TDR:EYE:INP:BPAT:TYPE PRBS" 'Type .WriteString
":CALC:TDR:EYE:INP:BPAT:LENG 7" 'Length .WriteString ":CALC:TDR:EYE:INP:OLEV
200e-3" 'One Level .WriteString ":CALC:TDR:EYE:INP:DRAT 1e9" 'Data Rate ' Set
Rise Time/Threshold .WriteString ":CALC:TDR:EYE:INP:RTIM:DATA 50e-12"
.WriteString ":CALC:TDR:EYE:INP:RTIM:THR T2_8" ' Activate Trace 5 (Tdd21)
.WriteString ":CALC:PAR:MNUM:SEL 5" ' Execute Draw Eye Message "Connect DUT to
cables." \+ vbCrLf + "Press OK to draw Eye diagram." .WriteString
":CALC:TDR:EYE:STAT ON" .WriteString ":CALC:TDR:EYE:EXEC" ' Read Eye Results
Cells(3, 4) = "Eye Results" Dim Labels() As Variant Labels = Array("Min.
Value", "Max. Value", "Level Zero", "Level One", "Level Mean", "Amplitude",
"Height", "(Reserved)", "Width", "Opening Factor", _ "Signal/Noise", "Duty
Cycle Dist", "Duty Cycle Dist(%)", "Rise Time", "Fall Time", "Jitter p-p",
"Jitter RMS", "Crossing %") Dim EyeResult() As Double .WriteString
":CALC:TDR:EYE:RES:DATA?" EyeResult() = .ReadList(ASCIIType_R8, ",") For i = 0
To 17 'Number of results = 18 Cells(i \+ 5, 4) = Labels(i) Cells(i \+ 5, 6) =
EyeResult(i) Next i ' Restore TDR GUI .WriteString ":DISP:TDR:MIN:STAT OFF"
Message "Finished Simulated Eye Diagram." End With vna.IO.Close Exit Sub
errorhandler: MsgBox Err.Description, vbExclamation, "Error Occurred",
Err.HelpFile, Err.HelpContext End Sub  
---

