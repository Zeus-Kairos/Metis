# SENSe:BANDwidth | BWIDth Commands

* * *

SENSe:BANDwidth | BWIDth: [RESolution <num>](Sense_Bandwidth.md#res) TRACk:FORCe [TRACk[:STATe] <bool>](Sense_Bandwidth.md#track)  
---  
  
See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about IF Bandwidth](../../../S2_Opt/Trce_Noise.md#Variable_IF_Bandwidth)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:BANDwidth | BWIDth[:RESolution] <num>

Applicable Models: All (Read-Write) Sets the bandwidth of the digital IF
filter to be used in the measurement. (Use either Sense:Bandwidth or
Sense:Bwidth)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [(Click to see the lists.)](../../../S2_Opt/Trce_Noise.md#IFDiag) If an invalid number is specified, the analyzer will round up to the closest valid number. This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples | SENS:BWID 1KHZ  
sense2:bandwidth:resolution 1000  
Query Syntax | SENSe<cnum>:BANDwidth | BWIDth[:RESolution]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Varies with VNA model.  
  
* * *

SENSe<cnum>:BANDwidth | BWIDth:TRACk:FORCe <bool>

Applicable Models: N522xB, N5234B, N5235B, N524xB, E5080A/B (Read-Write)
Enables/disables the [Reduce IF BW at Low
Frequencies](../../../S2_Opt/Trce_Noise.htm#IFDiag) feature in segments with
IFBW arbitrary. (Use either Sense:Bandwidth:Track:Force or
Sense:Bwidth:Track:Force).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON or 1 \- Enable reduce IF BW at Low Frequencies in segments with IFBW arbitrary. OFF or 0 - Disable reduce IF BW at Low Frequencies in segments with IFBW arbitrary.  
Examples | SENS:BWID:TRAC:FORC OFF  
sense2:bandwidth:track:force 1  
Query Syntax | SENSe<cnum>:BANDwidth | BWIDth:TRACk:FORCe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

SENSe<cnum>:BANDwidth | BWIDth:TRACk[:STATe] <bool>

Applicable Models: N522xB, N5234B, N5235B, N524xB, E5080A/B, M983xA (Read-
Write) Sets and returns the state of the [Reduce IF BW at Low
Frequencies](../../../S2_Opt/Trce_Noise.htm#IFDiag) feature. (Use either
Sense:Bandwidth:Track or Sense:Bwidth:Track).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON or 1 \- Reduce IF BW at Low Frequencies is set ON OFF or 0 - Reduce IF BW at Low Frequencies is set OFF  
Examples | SENS:BWID:TRAC OFF  
sense2:bandwidth:track 1  
Query Syntax | SENSe<cnum>:BANDwidth | BWIDth:TRACk[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF: E5080A ON: other models  
  
* * *

