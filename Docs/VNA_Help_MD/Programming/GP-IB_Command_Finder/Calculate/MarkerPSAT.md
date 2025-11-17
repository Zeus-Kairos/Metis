# Calculate:Marker:PSaturation Commands

* * *

Initiates a Power Saturation marker search and reads the results.

These commands are Superseded by the
[CALCulate:MEASure:MARKer:PSAT](MeasureMARKer.md) commands.

CALCulate:MARKer:PSATuration [BACKoff](MarkerPSAT.md#backoff) COMPression | [MAXimum](MarkerPSAT.md#compMax)? | [SATuration](MarkerPSAT.md#compSat)? [GAIN](MarkerPSAT.md#Gain)? | [LINear](MarkerPSAT.md#GainLinear)? | [MAXimum](MarkerPSAT.md#gainMax)? [PIN](MarkerPSAT.md#PSatIn)? | [MAXimum](MarkerPSAT.md#PinMax)? [POUT](MarkerPSAT.md#PSatOut)? | [MAXimum](MarkerPSAT.md#PMaxOut)?  
---  
  
Click on a keyword to view the command details.

See Also

  * [PSAT Example](../../GPIB_Example_Programs/Setup_PNOP_and_PSAT_Markers.md)

  * [Learn about PSAT Markers](../../../S4_Collect/Markers.md#PSat)

  * [Other SCPI Marker commands](Marker.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:MARKer:PSATuration:BACKoff <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
on and sets markers 1, 2, and 3 to calculate various Power Saturation
parameters. The <num> parameter sets and reads the back-off value for a Power
Saturation marker search. To turn off the Power Saturation markers, either
turn them off individually or turn them [All Off](Marker.md#aoff). To search
a User Range with the PSAT search, first activate marker 1 and set the desired
[User Range](Marker.md#rang). Then send the CALC:MARK:PSAT:BACK command. The
user range used with the PSAT search only applies to marker 1 searching for
the linear gain value. The other markers may fall outside the user range. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Backoff value. Choose any number between :-500 and 500  
Examples | CALC:MARK:PSAT:BACK 3  
calculate2:marker:psaturation:backoff 10  
Query Syntax | CALCulate<cnum>:MARKer:PSATuration:BACKoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:COMPression:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the compression maximum value from a PSAT marker search. Comp Max = Gain Max -
Gain Linear Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a
PSAT search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:COMP:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:COMPression:SATuration?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the compression saturation value from a PSAT marker search. Comp Sat = Gain
Sat - Gain Linear Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to
initiate a PSAT search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:COMP:SAT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:GAIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the saturation gain value from a PSAT marker search. Gain Sat = Psat Out -
Psat In Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT
search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:GAIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:GAIN:LINear?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the linear gain value from a PSAT marker search. Gain Linear = Marker 1 -
Y-axis value MINUS X-axis value. Use
[CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT search. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:GAIN:LIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:GAIN:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the maximum gain value from a PSAT marker search. Gain Max = PMax Out - PMax
In Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT
search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:GAIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:PIN?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the power saturation input value from a PSAT marker search. Psat In = Marker 2
X-axis value Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a
PSAT search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:PIN?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:PIN:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the maximum input power from a PSAT marker search. PMax In = Marker 3 X-axis
value Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT
search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:PIN:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:POUT?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the back-off output power from a PSAT marker search. PSat Out = Marker 2
Y-axis value Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a
PSAT search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:POUT?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MARKer:PSATuration:POUT:MAXimum?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Reads
the back-off output power from a PSAT marker search. PMaxOut = Marker 3 Y-axis
value Use [CALC:MARK:PSAT:BACK](MarkerPSAT.md#backoff) to initiate a PSAT
search. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MARK:PSAT:POUT:MAX?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

