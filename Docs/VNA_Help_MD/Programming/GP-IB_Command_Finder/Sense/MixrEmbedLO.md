# Sense:Mixer:ELO Commands

* * *

Allows measurements of a Mixer with an Embedded LO.

SENSe:MIXer:ELO [LO:DELTa](MixrEmbedLO.md#delta) [LO:RESet](MixrEmbedLO.md#reset) [NORMalize:POINt](MixrEmbedLO.md#point) RESet [STATe](MixrEmbedLO.md#state) TUNing | [IFBW](MixrEmbedLO.md#ifbw) | [INTerval](MixrEmbedLO.md#interval) | [ITERations](MixrEmbedLO.md#iteration) | [MODE](MixrEmbedLO.md#mode) | NBW | [RESet](MixrEmbedLO.md#tuningReset) | [SPAN](MixrEmbedLO.md#span) | [TOLerance](MixrEmbedLO.md#tolerance) DIAGnostic | [CLEar](MixrEmbedLO.md#diagClear) | [STATus](MixrEmbedLO.md#diagStatus) | SWEep | [COUNt?](MixrEmbedLO.md#DiagCount) | [LO:DELTa?](MixrEmbedLO.md#diagLoDelta) | MARKer | [ANNotation?](MixrEmbedLO.md#diagMarkAnn) | [POSition?](MixrEmbedLO.md#diagMarkerPos) | [STATe?](MixrEmbedLO.md#diagMarkState) | [PARameter?](MixrEmbedLO.md#diagParam) | X | [ANNotation?](MixrEmbedLO.md#diagXann) | [STARt?](MixrEmbedLO.md#diagXstart) | [STOP?](MixrEmbedLO.md#diagXstop) | Y | [ANNotation?](MixrEmbedLO.md#diagYann)  
---  
  
Click on a keyword to view the command details.

Note: The Find Now feature on the Embedded LO dialog is performed remotely by
doing a 'Single Sweep" with ELO enabled. [See example
program](../../GPIB_Example_Programs/Create_SMC_Embedded_LO_Measurement.htm).

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Embedded LO Settings](../../../Applications/Embedded_LO.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Note: The Embedded LO DIAGnostic commands read data from the various broadband
and precise tuning sweeps, similar to the textual and graphical data that are
available in the user interface.

* * *

## SENSe<ch>:MIXer:ELO:LO:DELTa <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns LO
Frequency Delta. There is usually no need to set this value. Read this value
to determine the difference between the LO Frequency that is stated in the
Mixer dialog box and the last measured LO Frequency.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | LO Frequency delta in Hertz.  
Examples | SENS:MIX:ELO:LO:DELT 10.3  
Query Syntax | SENSe<ch>:MIXer:ELO:LO:DELTa?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:LO:RESet

Applicable Models: N522xB, N524xB, M983xA (Write-only) Resets the LO Delta
Frequency to 0 (zero).  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:ELO:LO:RES sense2:mixer:elo:lo:reset  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:NORMalize:POINt <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the
sweep data point around which to perform broadband and precise tuning.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | Mixer Sweep data point. Choose a data point number, between1 and the max number of data points in the sweep, that has the least amount of expected noise.  
Examples | SENS:MIX:ELO:LO:NORM:POIN 200 sense2:mixer:elo:normalize:point 101  
Query Syntax | SENSe<ch>:MIXer:ELO:NORMalize:POINt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Center point in the sweep span  
  
* * *

## SENSe<ch>:MIXer:ELO:RESet

Applicable Models: N522xB, N524xB, M983xA (Write-only) Resets the LO Frequency
Delta and Tuning parameters to their default settings.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:ELO:RES sense2:mixer:elo:reset  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:STATe <bool>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the ON
|OFF state of Embedded LO.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<bool> | ON | OFF state. Choose from 0 - Embedded LO OFF 1 - Embedded LO ON  
Examples | SENS:MIX:ELO:STAT 1 sense2:mixer:elo:state 0  
Query Syntax | SENSe<ch>:MIXer:ELO:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:IFBW <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the IF
Bandwidth for Broadband and Precise tuning sweeps.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | IF Bandwidth  
Examples | SENS:MIX:ELO:TUN:IFBW 10kHz sense2:mixer:elo:tuning:ifbw 20e3  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:IFBW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 30kHz  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:INTerval <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns how
often a tuning sweep is performed.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | Tuning sweep interval  
Examples | SENS:MIX:ELO:TUN:INT 2 sense2:mixer:elo:tuning:interval 1  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:INTerval?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:ITERations <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the
maximum number of tuning iterations to achieve the precise tolerance.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | Number of tuning iterations. Choose a number between 1 and 100.  
Examples | SENS:MIX:ELO:TUN:ITER 5 sense2:mixer:elo:tuning:iterations 3  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:ITERations?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 5  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:MODE <char>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the
method used to determine the embedded LO Frequency.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<char> | Tuning mode. Choose from: BROadband Both broadband and precise tuning PRECise Precise tuning only NONe No tuning; just apply the LO Frequency Delta value.  
Examples | SENS:MIX:ELO:TUN:MODE BRO sense2:mixer:elo:tuning:mode precise  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | BROadband  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:NBW <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the
Noise Bandwidth for Broadband and Precise tuning sweeps.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | Noise Bandwidth  
Examples | SENS:MIX:ELO:TUN:NBW 3.2kHz sense2:mixer:elo:tuning:nbw 3.2e3  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:NBW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3.2 kHz  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:RESet

Applicable Models: N522xB, N524xB, M983xA (Write-only) Resets the tuning
parameters to their default values.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:ELO:TUN:RES sense2:mixer:elo:tuning:reset  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:SPAN <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the
frequency span for the broadband tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | Broadband frequency span in Hz.  
Examples | SENS:MIX:ELO:TUN:SPAN 1e6 sense2:mixer:elo:tuning:span 1mhz  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:SPAN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3 MHz  
  
* * *

## SENSe<ch>:MIXer:ELO:TUNing:TOLerance <num>

Applicable Models: N522xB, N524xB, M983xA (Read-Write) Sets and returns the
tuning tolerance for precise tuning.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<num> | Tuning tolerance in Hz. Choose a number between .001 and 1e3.  
Examples | SENS:MIX:ELO:TUN:TOL .5 sense2:mixer:elo:tuning:tolerance 1  
Query Syntax | SENSe<ch>:MIXer:ELO:TUNing:TOLerance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 Hz  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:CLEar

Applicable Models: N522xB, N524xB, M983xA (Write-only) Clears current
diagnostic information.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:ELO:DIAG:CLEar sense2:mixer:elo:diagnostic:clear  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:STATus?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns a string that
describes the result of the last tuning sweeps.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:ELO:DIAG:STAT? sense2:mixer:elo:diagnostic:status  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep:COUNt?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the number of
tuning sweeps used for the latest embedded LO measurement.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:ELO:DIAG:SWEep:COUNt sense2:mixer:elo:diagnostic:sweep:count?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:LO:DELTa?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the LO frequency
delta from the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:LO:DELT? sense2:mixer:elo:diagnostic:sweep1:lo:delta?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:MARKer:ANNotation?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the Y-axis
marker value from the specified tuning sweep. This command assumes that a
marker was used. Use SENS:MIX:ELO:DIAG:SWE:MARK:STATe? to confirm if a marker
was used for the tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:MARKer:ANN? sense2:mixer:elo:diagnostic:sweep1:marker:annotation?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:MARKer:POSition?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the X-axis
marker position from the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:MARK:POS? sense2:mixer:elo:diagnostic:sweep1:marker:position?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:MARKer:STATe?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns whether or not a
marker was used for the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:MARK:POS? sense2:mixer:elo:diagnostic:sweep1:marker:position?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:PARameter?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the name of the
parameter of the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:PAR? sense2:mixer:elo:diagnostic:sweep1:parameter?  
Return Type | String \- either "VC21" or "B,1"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:TITLe?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the title of the
specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:TITL? sense2:mixer:elo:diagnostic:sweep1:title?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:X:ANNotation?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the X-Axis
annotation of the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:X:ANN? sense2:mixer:elo:diagnostic:sweep1:x:annotation?  
Return Type | String \- either "Hz" or "s"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:X:STARt?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the start value
of the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:X:STAR? sense2:mixer:elo:diagnostic:sweep1:x:start?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:X:STOP?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns the stop value
of the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:X:STOP? sense2:mixer:elo:diagnostic:sweep1:x:stop?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:ELO:DIAGnostic:SWEep<n>:Y:ANNotation?

Applicable Models: N522xB, N524xB, M983xA (Read-only) Returns Y-axis
annotation value of the specified tuning sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<n> | Tuning sweep number. Use [SENS:MIX:ELO:DIAG:SWE:COUNt?](MixrEmbedLO.md#DiagCount) to find the number of sweeps taken.  
Examples | SENS:MIX:ELO:DIAG:SWE2:Y:ANN? sense2:mixer:elo:diagnostic:sweep1:y:annotation?  
Return Type | String \- either "U" or "Phase"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

