# Integrated Noise Measurement

This example program creates a Integrated Phase Noise measurement.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
PN_Integ_Noise.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also

  * [Setting Up a Phase Noise Measurement](Setting_Up_a_Phase_Noise_Measurement.md)

  * [Setting Up a Source](Setting_Up_a_Source.md)

  * [Spurious Measurement](Spurious_Measurement.md)

  * [Spot Noise Measurement](Spot_Noise_Measurement.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' ' Phase Noise - Integrated Noise analysis ' Dim app Dim scpi ' Create / Get
the VNA application. Set app = CreateObject("AgilentPNA835x.Application") Set
scpi = app.ScpiStringParser ' Set analysis range ' Range1: Full span ' Range2:
Custom range from 1.2 MHz to 6 MHz  scpi.parse
"CALCulate:MEASure:PN:INTegral:RANGe1:TYPE FULL" scpi.parse
"CALCulate:MEASure:PN:INTegral:RANGe2:TYPE CUSTom" scpi.parse
"CALCulate:MEASure:PN:INTegral:RANGe2:STARt 1.2e6" scpi.parse
"CALCulate:MEASure:PN:INTegral:RANGe2:STOP 6.0e6" ' Show integrated noise
table scpi.parse "DISPlay:WINDow:TABle:INOise:ENABle ON" ' Query analysis
results s1 = scpi.parse("CALCulate:MEASure:PN:INT:RANGe1:DATA? IPN") s2 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe1:DATA? RPM") s3 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe1:DATA? RFM") s4 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe1:DATA? RMSJ") s5 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe2:DATA? IPN") s6 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe2:DATA? RPM") s7 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe2:DATA? RFM") s8 =
scpi.parse("CALCulate:MEASure:PN:INT:RANGe2:DATA? RMSJ") Wscript.Echo "
Range1" & vbCrLf & _ " Integ Noise " & s1 & _ " Residual PM " & s2 & _ "
Residual FM " & s3 & _ " Jitter " & s4 & vbCrLf & _ " Range2" & vbCrLf & _ "
Integ Noise " & s5 & _ " Residual PM " & s6 & _ " Residual FM " & s7 & _ "
Jitter " & s8 & vbCrLf  
---

