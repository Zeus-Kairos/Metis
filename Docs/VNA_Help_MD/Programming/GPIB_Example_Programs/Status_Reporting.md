##### [ See Other SCPI Example Programs](SCPI_Example_Programs.md)

## Status Reporting using SCPI

* * *

This Visual Basic program demonstrates two methods of reading the analyzer's
status registers:

  * Polled Bit Method - reads the Limit1 register continuously.

  * SRQ Method - enables an interrupt of the program when bit 6 of the status byte is set to 1. The program then queries registers to determine if the limit line failed.

To run this program, you need:

  * An established [GPIB interface connection](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

  * A form with two buttons: Poll and SRQ Method

  * A means of causing the limit line to fail, assuming it passes initially.

* * *

Private Sub Poll_Click()  
' POLL THE BIT METHOD  
' Clear status registers  
GPIB.Write "*CLS"  
  
'Loop FOREVER  
Do  
DoEvents  
GPIB.Write "STATus:QUEStionable:LIMit1:EVENt?"  
onn = GPIB.Read  
Loop Until onn = 2  
  
MsgBox "Limit 1 Failed "  
End Sub  
  
  
Private Sub SRQMethod_Click()  
'SRQ METHOD  
GPIB.Write "SYSTem:PRESet"  
GPIB.Write "CALCulate:PARameter:SELect 'CH1_S11_1'"  
'slow down the trace  
GPIB.Write "SENS:BWID 150"  
  
'Setup limit line  
GPIB.Write "CALC:LIM:DATA 2,3e9,6e9,-2,-2"  
GPIB.Write "CALC:LIMit:DISP ON"  
GPIB.Write "CALC:LIMit:STATe ON"  
  
' Clear status registers.  
GPIB.Write "*CLS;*wai"  
' Clear the Service Request Enable register.  
GPIB.Write "*SRE 0"  
' Clear the Standard Event Status Enable register.  
GPIB.Write "*ESE 0"  
  
' Enable questionable register, bit(10) to report to the status byte.  
GPIB.Write "STATus:QUEStionable:ENABle 1024"  
  
' Enable the status byte register bit3 (weight 8) to notify controller  
GPIB.Write "*SRE 8"  
  
' Enable the onGPIBNotify event  
GPIB.NotifyMask = cwGPIBRQS  
GPIB.Notify  
End Sub  
  
\----------------------------------------------------  
Private Sub GPIB_OnGPIBNotify(ByVal mask As Integer)  
' check to see what failed  
' was it the analyzer?  
GPIB.Write "*STB?"  
onn = GPIB.Read  
If onn <> 0 Then  
' If yes, then was it the questionable register?  
GPIB.Write "STATus:QUEStionable:EVENt?"  
onn = GPIB.Read  
' Determine if the limit1 register, bit 8 is set.  
If onn = 1024 Then  
'if yes, then was it trace 1?  
GPIB.Write "STAT:QUES:LIMIT1:EVEN?"  
onn = GPIB.Read  
If onn = 2 Then MsgBox ("Limit Line1 Failed")  
End If  
End If  
End Sub

