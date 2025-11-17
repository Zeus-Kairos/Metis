# ECALConfidence Check using SCPI

* * *

This Visual Basic program performs a complete ECAL confidence check.

To run this program, you need:

  * An established GPIB interface connection

  * Keysight's VISA or National Instrument's VISA installed on your PC

  * The module visa32.bas added to your VB project.

  * A form with two buttons: cmdRun and cmdQuit

  * A calibrated S11 1-port or N-port measurement active on Channel 1

  * Window 1 is visible

Note: A confidence check can NOT be performed remotely from User
Characterizations that are stored on the VNA disk.

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

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

'String to receive data from the VNA

Dim strReply As String * 200

' Open the VISA default resource manager

status = viOpenDefaultRM(defRM)

If (status < VI_SUCCESS) Then HandleVISAError

' Open a VISA session (viPNA) to the VNA at GPIB address 16.

status = viOpen(defRM, "GPIB0::16::INSTR", 0, 0, viPNA)

If (status < VI_SUCCESS) Then HandleVISAError

' Need to set the VISA timeout value to give all our GPIB Reads

' sufficient time to complete before a timeout error occurs.

' For this example, let's try setting the limit to

' 10000 milliseconds (10 seconds).

status = viSetAttribute(viPNA, VI_ATTR_TMO_VALUE, 10000)

If (status < VI_SUCCESS) Then HandleVISAError

' Get the catalog of all the measurements currently on Channel 1.

status = myGPIBWrite(viPNA, "CALC1:PAR:CAT?")

If (status < VI_SUCCESS) Then HandleVISAError

status = myGPIBRead(viPNA, strReply)

If (status < VI_SUCCESS) Then HandleVISAError

' If an S11 measurement named "MY_S11" doesn't already exist,

' then create it.

If InStr(strReply, "MY_S11") = 0 Then

status = myGPIBWrite(viPNA, "CALC1:PAR:DEF:EXT MY_S11,S11")

If (status < VI_SUCCESS) Then HandleVISAError

End If

strReply = ""

' Get the catalog of all the trace numbers currently active

' in Window 1.

status = myGPIBWrite(viPNA, "DISP:WIND1:CAT?")

If (status < VI_SUCCESS) Then HandleVISAError  

status = myGPIBRead(viPNA, strReply)

If (status < VI_SUCCESS) Then HandleVISAError

' If a trace number 4 already exists in Window 1, then this

' will remove it.

If InStr(strReply, "4") > 0 Then

status = myGPIBWrite(viPNA, "DISP:WIND1:TRAC4:DEL")

If (status < VI_SUCCESS) Then HandleVISAError

End If

' Set trace number 4 to MY_S11.

status = myGPIBWrite(viPNA, "DISP:WIND1:TRAC4:FEED MY_S11")

If (status < VI_SUCCESS) Then HandleVISAError

' Set up trace view so we are viewing only the data trace.

status = myGPIBWrite(viPNA, "DISP:WIND1:TRAC4 ON")

If (status < VI_SUCCESS) Then HandleVISAError

status = myGPIBWrite(viPNA, "DISP:WIND1:TRAC4:MEM OFF")

If (status < VI_SUCCESS) Then HandleVISAError

' Select MY_S11 as the measurement to be used for the

' Confidence Check.

status = myGPIBWrite(viPNA, "SENS1:CORR:CCH:PAR MY_S11")

If (status < VI_SUCCESS) Then HandleVISAError

' Acquire the S11 confidence check data from ECal Module A

' into the memory buffer (asking for an OPC reply when it's done).

status = myGPIBWrite(viPNA, "SENS1:CORR:CCH:ACQ ECAL1;*OPC?")

If (status < VI_SUCCESS) Then HandleVISAError

' The VNA sends an OPC reply ("+1") when the confidence data

' acquisition into memory is complete, so this Read is waiting on

' the reply until it is received.

status = myGPIBRead(viPNA, strReply)

If (status < VI_SUCCESS) Then HandleVISAError

' Turn on trace math so the trace shows data divided by memory.

' You can be confident the S11 calibration is reasonably good if

' the displayed trace varies no more than a few tenths of a dB

' from 0 dB across the entire span.

status = myGPIBWrite(viPNA, "CALC1:PAR:SEL MY_S11")

If (status < VI_SUCCESS) Then HandleVISAError

status = myGPIBWrite(viPNA, "CALC1:MATH:FUNC DIV")

If (status < VI_SUCCESS) Then HandleVISAError

End Sub

Private Sub cmdQuit_Click()

' Turn off trace math

status = myGPIBWrite(viPNA, "CALC1:MATH:FUNC NORM")

If (status < VI_SUCCESS) Then HandleVISAError

' Conclude the confidence check to set the ECal module

' back to it's idle state.

status = myGPIBWrite(viPNA, "SENS1:CORR:CCH:DONE")

If (status < VI_SUCCESS) Then HandleVISAError

' Close the resource manager session (which also closes

' the session to the VNA).

If defRM <> 0 Then Call viClose(defRM)

' End the program

End

End Sub

Private Function myGPIBWrite(ByVal viHandle As Long, ByVal strOut As String)
As Long

' The "\+ Chr$(10)" appends an ASCII linefeed character to the output, for

' terminating the write transaction.

myGPIBWrite = viVPrintf(viHandle, strOut + Chr$(10), 0)

End Function

Private Function myGPIBRead(ByVal viHandle As Long, strIn As String) As Long

myGPIBRead = viVScanf(viHandle, "%t", strIn)

End Function

Sub HandleVISAError()

Dim strVisaErr As String * 200

Call viStatusDesc(defRM, status, strVisaErr)

MsgBox "*** Error : " \+ strVisaErr, vbExclamation

End

End Sub

