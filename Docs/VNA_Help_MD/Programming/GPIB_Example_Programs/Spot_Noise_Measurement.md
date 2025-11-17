# Spot Noise Measurement

This example program creates a Spot Noise measurement.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
PN_Spot_Noise.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also

  * [Setting Up a Phase Noise Measurement](Setting_Up_a_Phase_Noise_Measurement.md)

  * [Setting Up a Source](Setting_Up_a_Source.md)

  * [Spurious Measurement](Spurious_Measurement.md)

  * [Integrated Noise Measurement](Integrated_Noise_Measurement.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' Phase Noise - Spot Noise ' Dim app Dim scpi ' Create / Get the VNA
application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser ' Enable spot noise analysis scpi.parse
"CALCulate:MEASure:PN:SNOise:STATe ON" ' Enable spot noise of decade frequency
scpi.parse "CALCulate:MEASure:PN:SNOise:DEC:STAT ON" ' Enable spot noise of
120 kHz and 3 MHz offset frequency scpi.parse
"CALCulate:MEASure:PN:SNOise:USER1:STATe ON" scpi.parse
"CALCulate:MEASure:PN:SNOise:USER2:STATe ON" scpi.parse
"CALCulate:MEASure:PN:SNOise:USER1:X 120e3" scpi.parse
"CALCulate:MEASure:PN:SNOise:USER2:X 3e6" ' Show spot noise table scpi.parse
"DISPlay:WINDow:TABle:SNOise:ENABle ON" ' Query spot noise data s1 =
scpi.parse("CALCulate:MEASure:PN:SNO:USER1:X?") s2 =
scpi.parse("CALCulate:MEASure:PN:SNO:USER1:Y?") s3 =
scpi.parse("CALCulate:MEASure:PN:SNO:USER2:X?") s4 =
scpi.parse("CALCulate:MEASure:PN:SNO:USER2:Y?") s5 =
scpi.parse("CALCulate:MEASure:PN:SNO:DEC:X?") s6 =
scpi.parse("CALCulate:MEASure:PN:SNO:DEC:Y?") Wscript.Echo "User1" & vbCrLf &
_ " X = " & s1 & " Y = " & s2 & vbCrLf & _ "User2" & vbCrLf & _ " X = " & s3 &
" Y = " & s4 & vbCrLf & _ "Decades Edges" & vbCrLf & _ " X = " & s5 & " Y = "
& s6  
---

