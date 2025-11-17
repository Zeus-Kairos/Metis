# VNA as Controller and Talker / Listener

* * *

This Visual Basic Program uses VISA to do the following:

  * Control the VNA using a VISA LAN Client interface on the VNA.

  * Control another instrument using the VNA as GPIB controller.

  * Queries both the analyzer and other instrument to identify themselves with *IDN?

Note: This program can be modified to work from a remote PC to control both
instruments. In that case, set up the VNA to be a talker/listener.

To run this program, you need to do the following:

  * Add module visa32.bas to the VB project.

  * [Configure the VNA for VISA / SICL](../Learning_about_GPIB/Configure_for_VISA_and_SICL.md)

  * Set up the VNA to be GPIB system controller.

  * Connect another instrument to the analyzer through a GPIB cable with Primary address of 13 on GPIB0 interface

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Sub main()

'This application run from onboard the VNA

'can control both the VNA and another GPIB instrument.

'

'To run this program the module visa32.bas must be added

'to the project.

'VISA function status return code

Dim status As Long

'Session to Default Resource Manager

Dim defRM As Long

'Session to instrument

Dim viPNA As Long

'Session to other GPIB instrument

Dim viInstrument As Long

'String to hold results

Dim strRes As String * 200

On Error GoTo ErrorHandler

status = viOpenDefaultRM(defRM)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Open the session to the VNA

status = viOpen(defRM, "GPIB1::16::INSTR", 0, 0, viPNA)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Ask for the VNA's ID.

status = viVPrintf(viPNA, "*IDN?" \+ Chr$(10), 0)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Read the ID as a string.

status = viVScanf(viPNA, "%t", strRes)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Display the results

MsgBox "PNA is: " \+ strRes

'Open the session to the other instrument

status = viOpen(defRM, "GPIB0::13::INSTR", 0, 0, viInstrument)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Ask for the instrument's ID.

status = viVPrintf(viInstrument, "*IDN?" \+ Chr$(10), 0)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Read the ID as a string.

status = viVScanf(viPNA, "%t", strRes)

If (status < VI_SUCCESS) Then GoTo VisaErrorHandler

'Display the results

MsgBox "Other instrument is: " \+ strRes

' Close the resource manager session (which closes everything)

Call viClose(defRM)

End

ErrorHandler:

'Display the error message

MsgBox "*** Error : " \+ Error$, MB_ICONEXCLAMATION

End

VisaErrorHandler:

Dim strVisaErr As String * 200

Call viStatusDesc(defRM, status, strVisaErr)

MsgBox "*** Error : " \+ strVisaErr

End

End Sub

