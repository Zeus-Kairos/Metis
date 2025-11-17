# Setting Up a Source

This example program sets up a source for a Phase Noise measurement.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
PN_Setup.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also

  * [Setting Up a Phase Noise Measurement](Setting_Up_a_Phase_Noise_Measurement.md)

  * [Spurious Measurement](Spurious_Measurement.md)

  * [Integrated Noise Measurement](Integrated_Noise_Measurement.md)

  * [Spot Noise Measurement](Spot_Noise_Measurement.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' ' Phase Noise - Set up the Source ' Dim app Dim scpi ' Create / Get the VNA
application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser ' Set source port1 to 3 GHz, -3 dBm scpi.parse
"SOURce:POWer1:MODE ON" scpi.parse "SOURce:FREQuency1:FIXed 3e9" scpi.parse
"SOURce:POWer1:LEVel:IMMediate:AMPlitude -3"  
---

