# CALCulate:X (Axis) Commands

* * *

Controls the display of X-axis for various measurements.

These commands are Superseded by the [CALCulate:MEASure:X](MeasureX.md)
commands.

CALCulate:X: [AXIS](Parameter.md#cpd) | :[DOMain](X_Values.md#domain) [[:VALues](X_Values.md#VALues)]  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<ch>:X:AXiS <string>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-Read) Sets
the X-axis of the selected measurement to a DC Source. This command does not
change the default setting for new traces.  
---  
Parameters |   
<ch> | Channel number of the selected measurement. If unspecified, value is set to 1.  
<string> | String \- (Not case-sensitive) For all channels EXCEPT DIQ, choose from the following: "Default" \- The default X-axis setting for the selected measurement. For Application measurements, the X-Axis domain is set with specific commands. "AO1" \- Internal DC source #1 "AO2" \- Internal DC source #2 Note: For DIQ channels, see [CALC:X:AXIS:DOMain](X_Values.md#domain)  
Examples | CALC:X:AXIS 'Default' calculate:x:axis "AO1"  
Query Syntax | CALCulate<ch>:X:AXIS?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "Default"  
  
* * *

## CALCulate<ch>:X:AXIS:DOMain <string>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
X-Axis domain of the selected DIQ measurement.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
|  | Choose one of these: | Then set X-Axis Source ([CALC:X:AXIS](X_Values.md#XAXis)) using one of these as the argument.  
---|---  
"Frequency" | "F1", "F2", etc.  
"Power" | Source port: "Port 1", "Port 2", etc.  
"Phase" | Source port: "Port 1", "Port 2", etc.  
"DC" | DC Source:"AO1", "AO2"  
"Points" | "Points"  
Example | 1\. CALC:X:AXIS:DOM "Power" 2\. CALC:X:AXIS "Port 1"  
Query Syntax | CALCulate<ch>:X:AXIS:DOMain?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | CALC:X:AXIS:DOMain: "Frequency" CALC:X:AXIS: "F1"  
  
* * *

## CALCulate<cnum>:X[:VALues]?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the stimulus values for the selected measurement in the current units. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).
This command can be used for all Measurement Classes. Note: To avoid frequency
rounding errors, specify [FORM:DATA](../Format_SCPI.md#fd) <Real,64> or
<ASCii, 0>  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
Examples | 1\. Calc:Par:Sel "MyGCATrace"  
2\. CALC:X?  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd) command  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

