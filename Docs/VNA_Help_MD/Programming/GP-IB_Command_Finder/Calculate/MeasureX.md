# CALCulate:MEASure:X Commands

Controls the display of X-axis for various measurements.

CALCulate:MEASure:X AXIS | DOMain | FIXed | PARameter | VALue | UNIT? [:VALues]  
---  
  
Click a keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<ch>:MEASure<mnum>:X:AXIS <string>

Applicable Models: All (Write-Read) Sets the X-axis of the selected
measurement. This command does not change the default setting for new traces.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<string> | String \- (Not case-sensitive) For all channels EXCEPT DIQ, choose from the following: "Default" \- The default X-axis setting for the selected measurement. For Application measurements, the X-Axis domain is set with specific commands. "AO1" \- Internal DC source #1 "AO2" \- Internal DC source #2 Note: For DIQ channels, see CALC:MEAS:X:AXIS:DOMain For Modulation Distortion Channels (MOD), choose from: "SA Frequency" \- SA display showing the SA frequency settings. "Power In" \- Displays input power sweep. "Power Out" \- Displays output power sweep. "Measured Carrin" \- Measured input band power. "Measured CarrOut" \- Measured output band power. For Modulation Distortion Converters Channels (MODX), choose from: "SA Freq In" \- SA display showing mixer input range. "SA Freq Out" \- SA display showing mixer output range. "Power In" \- Displays input power sweep. "Power Out" \- Displays output power sweep. "Measured Carrin" \- Measured input band power. "Measured CarrOut" \- Measured output band power.  
Examples | CALC:MEAS2:X:AXIS 'Default' calculate:measure2:x:axis "AO1"  
Query Syntax | CALCulate<ch>:MEASure<mnum>:X:AXIS?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "Default"  
  
* * *

## CALCulate<ch>:MEASure<mnum>:X:AXIS:DOMain <string>

Applicable Models: All (Write-Read) Sets and returns the X-Axis domain of the
selected DIQ measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
|  | Choose one of these: | Then set X-Axis Source (CALC:MEAS:X:AXIS) using one of these as the argument.  
---|---  
"Frequency" | "F1", "F2", etc.  
"Power" | Source port: "Port 1", "Port 2", etc.  
"Phase" | Source port: "Port 1", "Port 2", etc.  
"DC" | DC Source:"AO1", "AO2"  
"Points" | "Points"  
Example | 1\. CALC:MEAS2:X:AXIS:DOM "Power" 2\. CALC:MEAS2:X:AXIS "Port 1"  
Query Syntax | CALCulate<ch>:MEASure<mnum>:X:AXIS:DOMain?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | CALC:MEAS:X:AXIS:DOMain: "Frequency" CALC:MEAS:X:AXIS: "F1"  
  
* * *

## CALCulate<ch>:MEASure<mnum>:X:AXIS:FIXed:PARameter <string>

Applicable Models: All with Option S93070xB or S9x070B (Write-Read) Sets the
X-axis fixed parameter for a power sweep measurement in a Modulation
Distortion channel.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<string> | String \- (Not case-sensitive) For Modulation Distortion Channels (MOD), choose from: "SA Frequency" \- SA display showing the SA frequency settings. For Modulation Distortion Converters Channels (MODX), choose from: "SA Freq In" \- SA display showing mixer input range. "SA Freq Out" \- SA display showing mixer output range.  
Examples | CALC:MEAS2:X:AXIS:FIX:PAR "SA Frequency" calculate:measure2:x:axis:fixed:parameter "SA Freq In"  
Query Syntax | CALCulate<ch>:MEASure<mnum>:X:AXIS:FIXed:PARameter?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ""  
  
* * *

## CALCulate<ch>:MEASure<mnum>:X:AXIS:FIXed:PARameter:VALue <num>

Applicable Models: All with Option S93070xB or S9x070B (Write-Read) Sets the
X-axis fixed parameter spectrum analyzer frequency value for a power sweep
measurement in a Modulation Distortion channel.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Fixed parameter value.  
Examples | CALC:MEAS2:X:AXIS:FIX:PAR:VAL 1.5e9 calculate:measure2:x:axis:fixed:parameter:value 1.5e9  
Query Syntax | CALCulate<ch>:MEASure<mnum>:X:AXIS:FIXed:PARameter:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:X:AXIS:UNIT?

Applicable Models: All (Read-only) Returns the current units of the X-axis (FREQuency | POWer | PHASe | DC | POINts | DEFault). This command can be used for all Measurement Classes.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:X:AXIS:UNIT?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | FREQuency  
  
* * *

## CALCulate<ch>:MEASure<mnum>:X[:VALues]?

Applicable Models: All (Read-only) Returns the stimulus values for the
selected measurement in the current units. This command can be used for all
Measurement Classes. Note: To avoid frequency rounding errors, specify
[FORM:DATA](../Format_SCPI.md#fd) <Real,64> or <ASCii, 0>  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | 1\. Calc:MEAS2:Par:Sel "MyGCATrace"  
2\. CALC:MEAS2:X?  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd) command  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable

