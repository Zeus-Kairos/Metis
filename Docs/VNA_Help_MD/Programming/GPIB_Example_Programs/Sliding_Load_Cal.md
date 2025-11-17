# Perform a Sliding Load Calibration using GPIB

* * *

This Visual Basic program does a only the sliding load portion of a
Calibration.

To run this program, you need:

  * An established [GPIB interface connection](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

  * A measurement and calibration routine to call this sub-program

  * STAN3 set up as a sliding load standard

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Sub slide()  
'Measure the sliding load for at least 5 and no more than 7 slides  
'Note that "SLSET" and "SLDONE" must be executed before the actual acquisition
of a slide  
MsgBox "Connect Sliding Load; set to Position 1; then press OK"  
GPIB.Write "SENS:CORR:COLL SLSET"  
GPIB.Write "SENS:CORR:COLL STAN3;"  
  
MsgBox "Set Sliding Load to position 2; then press OK"  
GPIB.Write "SENS:CORR:COLL SLSET"  
GPIB.Write "SENS:CORR:COLL STAN3;"  
  
MsgBox "Set Sliding Load to position 3; then press OK"  
GPIB.Write "SENS:CORR:COLL SLDONE"  
GPIB.Write "SENS:CORR:COLL STAN3;"  
End Sub

