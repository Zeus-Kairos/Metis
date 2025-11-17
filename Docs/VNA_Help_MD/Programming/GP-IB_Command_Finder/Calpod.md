# CalPod Commands

* * *

The following commands are sent as a string argument from:

[CONTrol:CALPod:COMMand <string>](Control.md#Calpod)

CALPod AVERage [DISable](Calpod.md#disable) [ENABle](Calpod.md#enable) [HIDE](Calpod.md#hide) INITialize | [ACTive](Calpod.md#InitActive) | [ALL](Calpod.md#InitAll) [LAUNch](Calpod.md#launch) POWer RECorrect | [ACTive](Calpod.md#RecorrectActive) | [ALL](Calpod.md#recorrectAll) [SHOW](Calpod.md#show) [STATe](Calpod.md#State) [TEMP?](Calpod.md#Temp)  
---  
  
Click on a blue keyword to view the command details.

In addition to the above Calpod commands, the following IEE 488 Common
Commands can also be sent as a string argument:

  * *CLS \- Clears all errors and event data from the error/event queue.

  * *IDN? \- Returns the instrument identification information.

For 4 state CALPod support the following is required.

      * CCT (configurable command table) version 1.4

      * Controller FPGA version 8.4

  * *OPC? \- Operation complete query. This query immediately returns a value, independent of whether or not the operation is complete. A return value of 0 indicates the operation is not complete. A value of +1 indicates the operation is complete. Typically this command is used in a loop with a 0.25 second delay when waiting for an operation to complete.

  * *TST? \- Performs a communication test on all the currently enabled Calpods. 0 = Test failed on one or more enabled Calpods. 1 = All enabled Calpods working.

  * SYSTem:ERRor? \- Queries the Event/Error queue and returns the most recent error element.

### Important Notes

  * ALL commands on this page are sent as a string argument from: [CONTrol:CALPod:COMMand <string>](Control.md#Calpod)
  * Use single quotes ONLY (NOT double quotes) for the CONT:CALP:COMM string arguments.
  * Sending queries requires TWO question marks. See following note as example.
  * To read errors with the commands on this page, use the Calpod query:  
CONT:CALP:COMM? 'SYSTem:ERRor?'

  * ALL queries return strings.

  
---  
  
### See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## **CALPod:AVERage< num >**

**Applicable Models:** All (Read-Write) Sets the number of OSL averages used
during initialization and recorrect. [See important
notes.](Calpod.htm#Important)  
---  
**Parameters** |   
<num> | Number of OSL averages to apply. Use an integer between 1 and 100.  
**Examples** | CONT:CALP:COMM 'CALP:AVER 8'  
**Query Syntax** | CONT:CALP:COMM? 'CALP:AVER?'  
**Return Type** | Numeric  
[**Default**](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 4  
  
* * *

## CALPod:DISable <port>

Applicable Models: All (Write-only) Unassign Calpod serial number from the
specified VNA port. [See important notes.](Calpod.md#Important)  
---  
Parameters |   
<port> | VNA port number to un-assign.  
Examples | CONT:CALP:COMM 'CALP:DIS 2'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:ENABle <port>,<sn>

Applicable Models: All (Write-read) Assign or return the Calpod serial number
for the specified VNA port. If a Calpod module is already assigned to the
specified VNA port, this assignment will replace the existing assignment. [See
important notes.](Calpod.htm#Important)  
---  
Parameters |   
<port> | VNA port number to be assigned the Calpod serial number.  
<sn> | Calpod serial number.  
Examples | CONT:CALP:COMM 'CALP:ENAB 2, 0001234' 'WRITE CONT:CALP:COMM? 'CALP:ENAB? 2' 'READ  
Query Syntax | CONTrol:CALPod:COMMand? 'CALPod:ENABle? <port>'  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:HIDE

Applicable Models: All (Write-only) Hides the Calpod setup dialog. [See
important notes.](Calpod.htm#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:HIDE'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:INITialize:ACTive

Applicable Models: All (Write-only) Performs the initialize process for the
active (selected) channel. Select a channel using
[CALCulate:MEASure:PARameter](Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter).
[See important notes.](Calpod.md#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:INIT:ACT'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:INITialize:ALL

Applicable Models: All (Write-only) Performs the initialize ALL channels
process. [See important notes.](Calpod.md#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:INIT:ALL'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:LAUNch

Applicable Models: All (Write-only) Starts the Calpod software. The Calpod
software can be started using this (Launch) command or by activating the
Calpod user interface. Once the Calpod software is started it remains active
until the VNA application is terminated. Send this command first in your
program, then wait a couple seconds while the software starts before sending
the next command. [See important notes.](Calpod.md#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:LAUN' wait 3  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## **CALPod:POWer< 0 | 1 >**

**Applicable Models:** All (Read-Write) Enables or disables the Correct
Power setting in the Calpod setup dialog. [See important
notes.](Calpod.htm#Important)  
---  
**Parameters** | 0  disable power correction  
1  enable power correction  
Note that ON and OFF cannot be used as arguments to this command.  
**Examples** | CONT:CALP:COMM 'CALP:POW 1'  
**Query Syntax** | CONT:CALP:COMM? 'CALP:POW?'  
**Return Type** | Numeric  
[**Default**](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 (disabled)  
  
* * *

## CALPod:RECorrect:ACTive

Applicable Models: All (Write-only) Performs the recorrect process for the
active (selected) channel. Select a channel using
[CALCulate:MEASure:PARameter](Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter).
[See important notes.](Calpod.md#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:REC:ACT'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:RECorrect:ALL

Applicable Models: All (Write-only) Performs the recorrect process for ALL
channels. [See important notes.](Calpod.md#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:REC:ALL'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:SHOW

Applicable Models: All (Write-only) Shows the Calpod setup dialog. [See
important notes.](Calpod.htm#Important)  
---  
Parameters | None  
Examples | CONT:CALP:COMM 'CALP:SHOW'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALPod:STATe <sn>,<state>

Applicable Models: All (Write-only) Sets the specified Calpod module to
specified impedance state. [See important notes.](Calpod.md#Important)  
---  
Parameters |   
<sn> | Serial number of the Calpod module. When set to 1, all modules are set to the specified state.  
<state> | Impedance state. Not case sensitive. Choose from: Short, Open, Load, or Thru  
Examples | CONT:CALP:COMM 'CALPod:STATe 0001234,thru'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Thru  
  
* * *

## CALPod:TEMP? <sn>

Applicable Models: All (Read-only) Returns the temperature of the specified
Calpod module in degrees Celsius. [See important notes.](Calpod.md#Important)  
---  
Parameters |   
<sn> | Serial number of the Calpod module.  
Examples | CONT:CALP:COMM? 'CALPod:TEMP? 0001234'  
Query Syntax | Not Applicable  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

