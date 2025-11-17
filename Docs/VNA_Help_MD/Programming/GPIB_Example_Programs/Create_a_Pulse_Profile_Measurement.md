# Create a Pulse Profile Measurement

* * *

The following SCPI example demonstrates how to create a Pulse Profile
measurement using the Integrated Pulse Application on the PNA-X and N522xB.

Four measurements are created:

  1. S11 (default)

  2. S21

  3. B receiver

  4. R1 receiver - used to verify pulse gen settings.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as PulseProfile.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

  * Integrated Pulse Application

  * [SCPI commands](../GP-IB_Command_Finder/Sense/SweepPulse.md) used in the program.

  * [SCPI commands](../GP-IB_Command_Finder/Sense/Pulse.md) to control the internal pulse generators

  * [Other Pulse SCPI examples](SCPI_Example_Programs.md#Pulsed)

' VNA application object Dim oPNA ' Channel 1 object Dim chan1 ' Create / Get
the VNA application. Set oPNA = CreateObject("AgilentPNA835x.Application") dim
scpi Set scpi = oPNA.ScpiStringParser scpi.parse "syst:preset" scpi.parse
"CALCulate:PARameter:DEFine:EXT 'MyMeas1',S21" scpi.parse
"DISPlay:WINDow1:TRACe2:FEED 'MyMeas1'" scpi.parse
"CALCulate:PARameter:DEFine:EXT 'MyMeas2',R_1" scpi.parse
"DISPlay:WINDow1:TRACe3:FEED 'MyMeas2'" scpi.parse
"CALCulate:PARameter:DEFine:EXT 'MyMeas3',B_1" scpi.parse
"DISPlay:WINDow1:TRACe4:FEED 'MyMeas3'" 'Pulse settings scpi.parse
"SENSe:SWEep:PULSe:MODE PROFILE" scpi.parse "SENSe:SWEep:PULSe:DRIVe 1"
scpi.parse "SENSe:SWEep:PULSe:PRF 1" scpi.parse "SENSe:SWEep:PULSe:TIMing 1"
scpi.parse "SENSe:SWEep:PULSe:DETectmode 1" scpi.parse "SENSe:SWEep:PULSe:IFBW
1" scpi.parse "SENSe:SWEep:PULSe:MASTer:WIDth 10e-6" scpi.parse
"SENSe:SWEep:PULSe:MASTer:PERiod 1e-3"  
---  
  
* * *

