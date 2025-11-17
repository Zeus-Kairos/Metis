# Calculate:RData? Command

This command is Superseded by the
[CALCulate:MEASure:RDATa](Measure.md#CALCulate:MEASure:RDATA) command.

* * *

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

## CALCulate<cnum>:RDATA? <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
receiver data for the selected measurement. To query measurement data, see
[CALC:DATA?](Data.md)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from any physical receiver in the VNA. For example: "A" Also, REF - returns data for either R1 or R2 data depending on the source port of the selected measurement. See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. Note: Logical receiver notation is NOT allowed with this command. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation)  
Example | GPIB.Write "INITiate:CONTinuous OFF"  
GPIB.Write "INITiate:IMMediate;*wai"  
GPIB.Write "CALCulate:RDATA? A" GPIB.Write "CALCulate:RDATA? REF"  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd) \- Two numbers per data point  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
Notes:

Generally when you query the analyzer for data, you expect that the number of
data values returned will be consistent with the number of points in the
sweep.

However, if you query receiver data while the instrument is sweeping, the
returned values may contain zeros. For example, if your request for receiver
data is handled on the 45th point of a 201 point sweep, the first 45 values
will be valid data, and the remainder will contain complex zero.

This can be avoided by synchronizing this request with the end of a sweep or
putting the channel in hold mode.

[Learn about Unratioed
Measurements](../../../S1_Settings/Measurement_Parameters.htm#Unratioed_Power)

