# Sense:Average Commands

* * *

Sets sweep-to-sweep averaging parameters. Averaging is a noise reduction
technique that averages each data point over a user-specified number of
sweeps. Averaging affects all of the measurements in the channel.

SENSe:AVERage | [CLEar](Average_SCPI.md#cacl) | [COUNt](Average_SCPI.md#cac) | [MODE](Average_SCPI.md#mode) | [[STATe]](Average_SCPI.md#cas)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example](../../GPIB_Example_Programs/Setup_the_Display_using_GPIB.md) using some of these commands.

  * [Learn about Averaging](../../../S2_Opt/Trce_Noise.md#averaging)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

  * Keysight Support Article: [HOW TO ACQUIRE DATA USING AVERAGES ON A VNA WITH SCPI EXAMPLE IN PYTHON](https://support.keysight.com/KeysightdCX/s/knowledge-article-detail?language=en_US&keyid=How-to-acquire-data-using-averages-on-a-VNA-with-SCPI-example-in-Python)

* * *

## SENSe<cnum>:AVERage:CLEar

Applicable Models: All (Write-only) Clears and restarts averaging of the
measurement data. Does NOT apply to point averaging.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
Examples | SENS:AVER:CLE  
sense2:average:clear  
Query Syntax | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:AVERage:COUNt <num>

Applicable Models: All (Read-Write) Sets the number of measurements to combine
for an average. Must also set [SENS:AVER[:STATe] ON](Average_SCPI.md#cas)  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<num> | Number of measurements to average. Choose any number between 1 and 65536 (2^16).  
Examples | SENS:AVER:COUN 999  
sense2:average:count 73  
Query Syntax | SENSe<cnum>:AVERage:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<cnum>:AVERage:MODE <char>

Applicable Models: All (Read-Write) Sets the type of averaging to perform:
Point or Sweep.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<num> | Averaging Type. Choose from: POINt \- Averaging measurements are made on each data point before stepping to the next data point. SWEEP \- Averaging measurements are made on subsequent sweeps until the required number of averaging sweeps are performed.  
Examples | SENS:AVER:MODE POIN  
sense2:average:mode sweep  
Query Syntax | SENSe<cnum>:AVERage:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Sweep  
  
* * *

## SENSe<cnum>:AVERage[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns trace averaging ON or OFF.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<ON | OFF> | ON (or 1) - turns averaging ON.  
OFF (or 0) - turns averaging OFF.  
Examples | SENS:AVER ON  
sense2:average:state off  
Query Syntax | SENSe<cnum>:AVERage[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Off  
  
* * *

