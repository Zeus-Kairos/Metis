# Uploading a Source Power Cal using SCPI

* * *

Programming the VNA using COM or using SICL/VISA over LAN (as in this example)
leaves the VNA free to control GPIB devices as needed. This Visual Basic
program demonstrates:

  * Uploading a source power calibration of Port 2 for Channel 1.

  * Reading the calibration data.

Learn more about [Power Calibrations](../../S3_Cals/PwrCalibration.md)

[Other SCPI Example Programs](SCPI_Example_Programs.md)

To run this program, you need:

  * Your PC and VNA both connected to a LAN (if using VISA LAN server / client).

  * The SICL and VISA components of Keysight I/O Libraries software installed on your PC (both are included when you install the software, unless you already have another vendor's VISA installed. Then specify Full SICL and VISA installation to overwrite the other vendor's VISA.

  * The module visa32.bas added to your VB project.

  * A form with two buttons: cmdRun and cmdQuit.

  * A VISA interface configured on your remote PC to control the VNA. This could be GPIB interface or a [VISA LAN Client](../Learning_about_GPIB/Configure_for_VISA_and_SICL.md).

'Session to VISA Default Resource Manager  
Private defRM As Long  
'Session to VNA  
Private viPNA As Long  
'VISA function status return code  
Private status As Long  
Private Sub Form_Load()  
defRM = 0  
End Sub  
Private Sub cmdRun_Click()  
  
' String to receive data from the VNA.  
' Dimensioned large enough to receive scalar comma-delimited values  
' for 21 frequency points (20 ASCII characters per point)  
Dim strReply As String * 420  
Dim strPower As String, strCalPower As String  
Dim strStimulus, strCalValue  
Dim strResult As String  
  
' Open the VISA default resource manager  
status = viOpenDefaultRM(defRM)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Open a session (viPNA) to the VNA at "address 16" on the VISA  
' interface configured as "GPIB0" on this PC.  
status = viOpen(defRM, "GPIB0::16::INSTR", 0, 0, viPNA)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Set the number of sweep points to 2 on Channel 1.  
status = myGPIBWrite(viPNA, "SENS1:SWE:POIN 2")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Ensure there's currently no source power cal on for this channel and port.  
status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR OFF")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Specify if the cal power level is offset (positive value for a gain,
negative  
' value for a loss) from the VNA port power setting on the channel when no
source  
' power cal is active. This is to account for components between the VNA test  
' port and cal reference plane. In this example, let's set up our calibration  
' at the output of an amplifier with 15 dB gain.  
status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:OFFS 15 DB")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Prepare for doing data transfer in ASCII format.  
status = myGPIBWrite(viPNA, "FORM:DATA ASCII")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Send our source power correction data to the VNA. For purpose of simplicity  
' in this example, we'll set up for no correction (0) at our start stimulus
and  
' 0.5 dB at our stop stimulus (recall that our sweep currently has just 2
points).  
status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:DATA 0,0.5")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Set the number of sweep points to 21 on Channel 1.  
status = myGPIBWrite(viPNA, "SENS1:SWE:POIN 21")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Read the fixed power level for this port on Channel 1.  
status = myGPIBWrite(viPNA, "SOUR1:POW2:LEV?")  
If (status < VI_SUCCESS) Then HandleVISAError  
status = myGPIBRead(viPNA, strReply)  
If (status < VI_SUCCESS) Then HandleVISAError  
strPower = strReply  
  
' Turn the source power cal on.  
status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR ON")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Again read the fixed power level for this port on Channel 1  
' (with our calibration turned on, this should now include the 15 dB offset  
' we indicated our power amplifier provides).  
status = myGPIBWrite(viPNA, "SOUR1:POW2:LEV?")  
If (status < VI_SUCCESS) Then HandleVISAError  
status = myGPIBRead(viPNA, strReply)  
If (status < VI_SUCCESS) Then HandleVISAError  
strCalPower = strReply  
  
' Read the stimulus values from Channel 1.  
status = myGPIBWrite(viPNA, "SENS1:X?")  
If (status < VI_SUCCESS) Then HandleVISAError  
status = myGPIBRead(viPNA, strReply)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Tokenize the reply string into an array containing the values  
strStimulus = Split(strReply, ",")  
  
' Read back the source power correction data, now interpolated for 21 points  
status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:DATA?")  
If (status < VI_SUCCESS) Then HandleVISAError  
status = myGPIBRead(viPNA, strReply)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Tokenize the reply string into an array containing the values  
strCalValue = Split(strReply, ",")  
  
' Print the data using a message box (here, Chr returns the ASCII characters  
' for Tab (9) and Linefeed (10)).  
strResult = "PNA port power = " & Val(strPower) & Chr(10)  
strResult = strResult & "Power at reference plane = " & Val(strCalPower) &
Chr(10) Chr(10)  
strResult = strResult & "Stimulus" & Chr(9) & Chr(9) & "Cal Value" & Chr(10)  
For i = 0 To UBound(strStimulus)  
strResult = strResult & Val(strStimulus(i)) & Chr(9) & Val(strCalValue(i)) &
Chr(10)  
Next  
MsgBox strResult  
End Sub  
Private Sub cmdQuit_Click()  
  
' Close the resource manager session (which also closes  
' the session to the VNA).  
If defRM <> 0 Then Call viClose(defRM)  
  
' End the program  
End  
End Sub  
Private Function myGPIBWrite(ByVal viHandle As Long, ByVal strOut As String)
As Long  
  
' The "\+ Chr$(10)" appends an ASCII linefeed character to the  
' output, for terminating the write transaction.  
myGPIBWrite = viVPrintf(viHandle, strOut + Chr$(10), 0)  
End Function  
Private Function myGPIBRead(ByVal viHandle As Long, strIn As String) As Long  
myGPIBRead = viVScanf(viHandle, "%t", strIn)  
  
' Remove trailing linefeed character  
If Right(strIn, 1) = Chr(10) Then strIn = Left(strIn, Len(strIn) - 1)  
End Function  
Sub HandleVISAError()  
Dim strVisaErr As String * 200  
Call viStatusDesc(defRM, status, strVisaErr)  
MsgBox "*** Error : " \+ strVisaErr, vbExclamation  
  
' Close the resource manager session (which also closes  
' the session to the VNA).  
If defRM <> 0 Then Call viClose(defRM)  
End  
End Sub  

