# ECAL Confidence Check

* * *

This Visual Basic program:

  * Initializes the VNA objects.

  * Performs a complete ECAL confidence check

Before using this code:

  * The active channel must contain an S11 measurement with a 1-port or N-port calibration

  * Prepare a form with two buttons named cmdRun and cmdQuit

Note: A confidence check can NOT be performed remotely from User
Characterizations that are stored on the VNA disk.

* * *

Private oPNA As AgilentPNA835x.Application Private oChan As Channel Private
oCal As Calibrator Private oMeas As Measurement Private Sub cmdRun_Click() Dim
iMeasIndex As Integer Set oPNA = CreateObject("AgilentPNA835x.Application",
"MachineName") Set oChan = oPNA.ActiveChannel Set oCal = oChan.Calibrator
iMeasIndex = 1 ' Loop through measurements until an S11 on the active channel
' is found, or the end of the measurement collection is reached. Do Set oMeas
= oPNA.Measurements(iMeasIndex) If oMeas.Parameter = "S11" And _
oMeas.channelNumber = oChan.channelNumber Then Exit Do iMeasIndex = iMeasIndex
+ 1 If iMeasIndex > oPNA.Measurements.Count Then MsgBox "No S11 measurement
found on the active channel." _ & " Create an S11 measurement, then try
again." Exit Sub End If Loop ' Set up trace view so we are viewing only the
data trace. oMeas.View = naData ' Acquire the S11 confidence check data from
ECal Module A ' into the memory buffer. oCal.AcquireCalConfidenceCheckECALEx
"S11", 1 ' Turn on trace math so the trace shows data divided by memory. ' You
can be confident the S11 calibration is reasonably good if ' the displayed
trace varies no more than a few tenths of a dB ' from 0 dB across the entire
span. oMeas.TraceMath = naDataDivMemory End Sub Sub cmdQuit_Click() ' Turn off
trace math ' in case someone clicks Quit without having clicked Run If oMeas
<> Nothing Then oMeas.TraceMath = naDataNormal ' Conclude the confidence check
to set the ECal module ' back to it's idle state. If oCal <> Nothing Then
oCal.DoneCalConfidenceCheckECAL ' End the program End End Sub  
---

