# Calculate:Marker:PNOP Commands

* * *

Initiates a Power Normal Operating Point marker search and reads the results.

These commands are Superseded by the
[CALCulate:MEASure:MARKer:PNOP](MeasureMARKer.md) commands.

CALCulate:MARKer:PNOP [BACKoff](MarkerPNOP.md#backoff) | [GAIN?](MarkerPNOP.md#backGain) | [PIN?](MarkerPNOP.md#BackPin) | [POUT?](MarkerPNOP.md#BackPout) [COMPression?](MarkerPNOP.md#Comp) | [MAXimum?](MarkerPNOP.md#CompMax) [GAIN?](MarkerPNOP.md#Gain) | [MAXimum?](MarkerPNOP.md#GainMax) [PIN?](MarkerPNOP.md#PIN) | [MAXimum?](MarkerPNOP.md#PinMax) [POFFset](MarkerPNOP.md#Poffset) [POUT?](MarkerPNOP.md#pout) | [MAXimum?](MarkerPNOP.md#poutMax)  
---  
  
Click on a keyword to view the command details.

See Also

  * [PNOP Example](../../GPIB_Example_Programs/Setup_PNOP_and_PSAT_Markers.md)

  * [Learn about PNOP Markers](../../../S4_Collect/Markers.md#PNOP)

  * [Other SCPI Marker commands](Marker.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:MARKer:PNOP:BACKoff <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
on and sets markers 1, 2, 3, and 4 to calculate various PNOP parameters.
Either this command, or the [POFFset](MarkerPNOP.md#Poffset) command, will
initiate the PNOP search markers. To turn off the PNOP markers, either turn
them off individually or turn them [All Off](Marker.md#aoff). To search a
User Range with the PNOP search, first activate marker 1 and set the desired
[User Range](Marker.md#rang). Then send CALC:MARK:PNOP:BACK. The user range
used with the PNOP search only applies to marker 1 searching for the linear
gain value. The other markers may fall outside the user range. See Critical
Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Backoff value. Choose any number between :-500 and 500  
Examples | CALC:MARK:PNOP:BACK? calculate2:marker:pnop:backoff 10  
Query Syntax | CALCulate<cnum>:MARKer:PNOP:BACKoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |   
  
* * *

## CALCulate<cnum>:MARKer:PNOP:BACKoff:GAIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the power backoff gain value from a PNOP marker search. PBO Gain = PBO Out -
PBO In Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:BACK:GAIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:BACKoff:PIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the power backoff input value from a PNOP marker search. PBO In = Marker 2
X-axis Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:BACK:PIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:BACKoff:POUT?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the power backoff output value from a PNOP marker search. PBO Out = Marker 2
Y-axis Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:BACK:POUT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:COMPression?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the PNOP compression value from a PNOP marker search. Pnop Comp = Pnop Gain -
Linear Gain (not shown on marker readout). Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:COMP?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:COMPression:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the max compression value from a PNOP marker search. Comp Max = Gain Max -
Linear Gain (not shown on marker readout). Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:COMP:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:GAIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the PNOP gain value from a PNOP marker search. Pnop Gain = Pnop Out - Pnop In.
Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:GAIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:GAIN:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the max gain from a PNOP marker search. Gain Max = PMax Out - PMax In Use
[CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:GAIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:PIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the PNOP input value from a PNOP marker search. Pnop In = Marker 4 X-axis
value Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:PIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:PIN:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the max input power from a PNOP marker search. PMax In = Marker 3 X-axis value
Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:PIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:POFFset <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
on and sets markers 1, 2, 3, and 4 to calculate various PNOP parameters.
Either this command, or the [Backoff](MarkerPNOP.md#backoff) command, will
initiate the PNOP search markers. To turn off the PNOP markers, either turn
them off individually or turn them [All Off](Marker.md#aoff). To search a
User Range with the PNOP search, first activate marker 1 and set the desired
[User Range](Marker.md#rang). Then send the CALC:MARK:PNOP:POFF command. The
user range used with the PNOP search only applies to marker 1 searching for
the linear gain value. The other markers may fall outside the user range. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Power Offset value in dB. Choose any number between :-500 and 500  
Examples | CALC:MARK:PNOP:POFF 3 calculate2:marker:pnop:poffset 10  
Query Syntax | CALCulate<cnum>:MARKer:PNOP:POFFset?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ??  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:POUT?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the output power value of the offset marker from a PNOP marker search. Pnop
Out = Marker 4 Y-axis value Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff)
or [CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search.
See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:POUT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PNOP:POUT:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the max output power from a PNOP marker search. PMax Out = Marker 3 Y-axis
value Use [CALC:MARK:PNOP:BACK](MarkerPNOP.md#backoff) or
[CALC:MARK:PNOP:POFF](MarkerPNOP.md#Poffset) to initiate a PNOP search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PNOP:POUT:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

