# SYSTem:CALibrate:CALupdate Commands

* * *

Contains the settings to recorrect S11 and S22 error between the VNA and the
DUT reference plane.

SYSTem:CALibrate:CALupdate AVERage | COUNt BWIDth | [:RESolution] CHANnels | [:SELect] GATE | AUTO | STARt | COUPle | [:STATe] | STOP | COUPle | [:STATe] INITialize PORTs | [:SELect] RECorrect REFerence SETTings | AUTO SOURce | POWer  
---  
  
Click on a red keyword to view the command details.

* * *

## SYSTem:CALibrate:CALupdate:AVERage:COUNt <value>

Applicable Models: All (Write-Read) Sets and returns the averaging used to
improve noise errors.  
---  
Parameters |   
<value> | Average factor value. The default value is 1.  
Examples | SYST:CAL:CAL:AVER:COUN 1  
Query Syntax | SYSTem:CALibrate:CALupdate:AVERage:COUNt?  
Return Type | Numeric  
Default | 1  
  
* * *

## SYSTem:CALibrate:CALupdate:BWIDth[:RESolution] <value>

Applicable Models: All (Write-Read) Manually sets and returns the IF bandwidth
used by the active measurement channel. [Learn
more](../../S2_Opt/Trce_Noise.htm#HowToIFBW).  
---  
Parameters |   
<value> | IF bandwidth value.   
Examples | SYST:CAL:CAL:BWID:RES 100 kHz  
Query Syntax | SYSTem:CALibrate:CALupdate:BWIDth[:RESolution]?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

## SYSTem:CALibrate:CALupdate:CHANnels[:SELect] <value>

Applicable Models: All (Write-Read) Selects the channel(s) to calibrate.  
---  
Parameters |   
<value> | Channel numbers to be calibrated. The range is 1 to 500. These channels must already exist.  
Examples | SYST:CAL:CAL:CHAN 1,2,3  
Query Syntax | SYSTem:CALibrate:CALupdate:CHANnels[:SELect]?  
Return Type | Comma separated list of channels  
Default | Not Applicable  
  
* * *

## SYSTem:CALibrate:CALupdate:GATE:AUTO <bool>

Applicable Models: All (Write-Read) When set to ON, calculates the gate values
automatically when the SYSTem:CALibrate:CALupdate:INITialize command is sent.
As a result, user-defined Gate Start and Gate Stop values are not used and
their Couple state is disabled.  
---  
Parameters |   
<bool> | ON (or 1) \- Couple all gate start times to the same value. OFF (or 0) \- Do not couple all gate start times to the same value.  
Examples | SYST:CAL:CAL:GATE:AUTO 1  
Query Syntax | SYSTem:CALibrate:CALupdate:GATE:AUTO?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SYSTem:CALibrate:CALupdate:GATE:STARt <value>

Applicable Models: All (Write-Read) Sets and returns the gate start value for
time domain gating.  
---  
Parameters |   
<value> | Gate start time.  
Examples | SYST:CAL:CAL:GATE:STAR -1ns  
Query Syntax | SYSTem:CALibrate:CALupdate:GATE:STARt?  
Return Type | Numeric  
Default | -1ns  
  
* * *

## SYSTem:CALibrate:CALupdate:GATE:STARt:COUPle[:STATe] <bool>

Applicable Models: All (Write-Read) Sets and returns the state of gate
coupling for gate start value. Enabling this function couples all gate start
times to the same value set using the SYSTem:CALibrate:CALupdate:GATE:STARt
command.  
---  
Parameters |   
<bool> | ON (or 1) \- Couple all gate start times to the same value. OFF (or 0) \- Do not couple all gate start times to the same value.  
Examples | SYST:CAL:CAL:GATE:STAR:COUP:STAT 1  
Query Syntax | SYSTem:CALibrate:CALupdate:GATE:STARt:COUPle[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SYSTem:CALibrate:CALupdate:GATE:STOP <value>

Applicable Models: All (Write-Read) Sets and returns the gate stop value for
time domain gating.  
---  
Parameters |   
<value> | Gate stop time.  
Examples | SYST:CAL:CAL:GATE:STop 1ns  
Query Syntax | SYSTem:CALibrate:CALupdate:GATE:STOP?  
Return Type | Numeric  
Default | +1ns  
  
* * *

## SYSTem:CALibrate:CALupdate:GATE:STOP:COUPle[:STATe] <bool>

Applicable Models: All (Write-Read) Sets and returns the state of gate
coupling for gate stop value. Enabling this function couples all gate stop
times to the same value set using the SYSTem:CALibrate:CALupdate:GATE:STOP
command.  
---  
Parameters |   
<bool> | ON (or 1) \- Couple all gate stop times to the same value. OFF (or 0) \- Do not couple all gate stop times to the same value.  
Examples | SYST:CAL:CAL:GATE:STOP:COUP:STAT 1  
Query Syntax | SYSTem:CALibrate:CALupdate:GATE:STOP:COUPle[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SYSTem:CALibrate:CALupdate:INITialize

Applicable Models: All (Write-only) Initializes the ports selected using the
SYSTem:CALibrate:CALupdate:PORTs[:SELect] command.  
---  
Parameters |   
Examples | SYST:CAL:CAL:INIT 1,2,3  
Query Syntax | SYSTem:CALibrate:CALupdate:INITialize?  
Default | Not Applicable  
  
* * *

## SYSTem:CALibrate:CALupdate:PORTs[:SELect] <value>

Applicable Models: All (Write-Read) Selects the port numbers to initialize.  
---  
Parameters |   
<value> | Ports numbers to be calibrated.  
Examples | SYST:CAL:CAL:PORT 1,2,3,4  
Query Syntax | SYSTem:CALibrate:CALupdate:PORTs[:SELect]?  
Return Type | Comma separated list of ports  
Default | Not Applicable  
  
* * *

## SYSTem:CALibrate:CALupdate:RECorrect

Applicable Models: All (Write-only) Recorrects the ports selected using the
SYSTem:CALibrate:CALupdate:PORTs[:SELect] command. A port must be initialized
using the SYSTem:CALibrate:CALupdate:INITialize command before it can be
recorrected.  
---  
Parameters |   
Examples | SYST:CAL:CAL:REC 1,2,3  
Query Syntax | SYSTem:CALibrate:CALupdate:RECorrect?  
Default | Not Applicable  
  
* * *

## SYSTem:CALibrate:CALupdate:REFerence <calsetName>

Applicable Models: All (Write-Read) Sets and returns the reference cal set
name.  
---  
Parameters |   
<calsetName> | Cal set name.  
Examples | SYST:CAL:CAL:REF "myCalSet"  
Query Syntax | SYSTem:CALibrate:CALupdate:REFerence?  
Return Type | String  
Default | Not Applicable  
  
* * *

## SYSTem:CALibrate:CALupdate:SETTings:AUTO <bool>

Applicable Models: All (Write-Read) Use a channel's existing IF BW, Averaging,
and Power value settings or enter the values manually.  
---  
Parameters |   
<bool> | ON (or 1) \- Use a channel's existing IF BW, Averaging, and Power value settings. OFF (or 0) \- Enter values for IF BW, Averaging, and Power manually.  
Examples | SYST:CAL:CAL:SETT:AUTO 1  
Query Syntax | SYSTem:CALibrate:CALupdate:SETTings:AUTO?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON or 1  
  
* * *

## SYSTem:CALibrate:CALupdate:SOURce:POWer <value>

Applicable Models: All (Write-Read) Manually sets and returns the source power
for the active measurement channel.  
---  
Parameters |   
<value> | Source power value.  
Examples | SYST:CAL:CAL:SOUR:POW -10 dBm  
Query Syntax | SYSTem:CALibrate:CALupdate:SOURce:POWer?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

