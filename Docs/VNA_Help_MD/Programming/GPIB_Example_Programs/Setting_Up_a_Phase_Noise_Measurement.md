# Setting Up a Phase Noise Measurement

This example program creates a Phase Noise measurement setup.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
PN_Setup.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also

  * [Setting Up a Source](Setting_Up_a_Source.md)

  * [Spurious Measurement](Spurious_Measurement.md)

  * [Integrated Noise Measurement](Integrated_Noise_Measurement.md)

  * [Spot Noise Measurement](Spot_Noise_Measurement.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' ' Phase Noise - basic measurement ' Dim app Dim scpi ' Create / Get the VNA
application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser scpi.parse "SYST:PRES" ' Create a Phase Noise channel
scpi.parse "CALC:PAR:DEL:ALL" scpi.parse "CALC:MEAS1:DEF 'PN:Phase Noise'"
scpi.parse "DISP:MEAS1:FEED 1" ' Set Carrier frequency to 3 GHz scpi.parse
"SENS:PN:SWEep:CARRier:FREQuency 3.0e9" ' Set Start/Stop Offset to 1 kHz and
10 MHz scpi.parse "SENS:FREQuency:STARt 1e3" scpi.parse "SENS:FREQuency:STOP
10e6" ' Set RBW Ratio to 5 % scpi.parse "SENS:PN:BWIDth:RESolution:RATio 5" '
Set FFT Avg Factor to 2 scpi.parse "SENSe:PN:FAVerage:FACTor 2" ' Select Noise
Mode to Normal scpi.parse "SENS:PN:SWEep:NOISe:MODE NORMal" ' Select VNA Input
to use for the measurement scpi.parse "SENS:PN:RECeiver 'b2'"  
---

