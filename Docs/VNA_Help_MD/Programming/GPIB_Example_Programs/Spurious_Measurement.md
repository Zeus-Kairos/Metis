# Spurious Measurement

This example program creates a Phase Noise Spurious measurement.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
PN_Spurious.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also

  * [Setting Up a Phase Noise Measurement](Setting_Up_a_Phase_Noise_Measurement.md)

  * [Setting Up a Source](Setting_Up_a_Source.md)

  * [Integrated Noise Measurement](Integrated_Noise_Measurement.md)

  * [Spot Noise Measurement](Spot_Noise_Measurement.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' Phase Noise - Spurious analysis ' Dim app Dim scpi ' Create / Get the VNA
application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser ' Set sort order of spurious list scpi.parse
"CALCulate:MEASure:PN:SPURious:SORT OFFSet" ' Enable spurious analysis
scpi.parse "CALCulate:MEASure:PN:SPURious:ANALysis:STATe ON" ' Disable
spurious omission scpi.parse "CALCulate:MEASure:PN:SPURious:OMISsion:STATe
OFF" ' Set sensibility of spurious detection to 2.5 scpi.parse
"CALCulate:MEASure:PN:SPURious:SENSibility 2.5" ' Set minimum level of
spurious to 140 dBc  scpi.parse
"CALCulate:MEASure:PN:SPURious:THReshold:LEVel:MINimum -140.0" ' Set threshold
table (***** but this feature is hidden at 1st release of MintP *****)
scpi.parse "CALCulate:MEASure:PN:SPURious:THReshold:TABle:DELete" scpi.parse
"CALCulate:MEASure:PN:SPURious:THReshold:TABle:DATA
1e3,-135.0,42.0,5e3,-145,56" ' Show spot noise table scpi.parse
"DISPlay:WINDow:TABle:SPURious:ENABle ON" ' Query analysis results s1 =
scpi.parse("CALCulate:MEASure:PN:SPUR:DATA?") Wscript.Echo "Spurs Result " &
s1  
---

