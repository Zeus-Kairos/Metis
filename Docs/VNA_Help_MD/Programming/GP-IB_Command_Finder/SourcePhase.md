# Source:Phase Commands

* * *

Makes phase control settings (Option S93088A)

SOURce:PHASe: | CONTrol | [COUPle[:STATe]](SourcePhase.md#coupleState) | [ITERation](SourcePhase.md#iteration) | [TOLerance](SourcePhase.md#tolerance) | CORRection | [DATA](SourcePhase.md#corrData) | [[STATe]](SourcePhase.md#corrState) | EXTernal | CATalog? | PORT | [[FIXed]](SourcePhase.md#fixed) | MODE | CATalog? | [:VALue] | [PARameter](SourcePhase.md#parameter) | CATalog? | [MODE](SourcePhase.md#parameterMode) | [CATalog?](SourcePhase.md#paramModeCat) | [PORT](SourcePhase.md#paramPort) | [:VALue] | POFFset | CORRection | [DATA](SourcePhase.md#poffCorrData) | [[STATe]](SourcePhase.md#poffCorrState) | [FIXed](SourcePhase.md#poffsetFixed) [|](SourcePhase.md#start) [STARt](SourcePhase.md#poffStart) | [STOP](SourcePhase.md#poffStop) | REFerence | CATalog? | PORT [| STARt](SourcePhase.md#start) | [STOP](SourcePhase.md#stop)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Learn about Phase Control](../../S1_Settings/Phase_Control.md)

  * [Example Program](../GPIB_Example_Programs/Setup_Phase_Control.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SOURce<ch>:PHASe<port>:CONTrol:COUPle[:STATe] <bool>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read whether to couple phase control settings (IFBW, Tolerance, Max
Iterations).  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Coupling state. Choose from: ON or 1 \- Couple phase control settings. The phase control settings from <port> are copied to the other phase-controlled ports. OFF or 0 \- Do NOT couple phase control settings. The phase control settings for each phase-controlled port are made independently.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:CONT:COUP 1 source2:phase:control:couple:state ON,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:CONTrol:COUPle[:STATe]? [src]  
Return Type | Boolean  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:PHASe<port>:CONTrol:ITERation <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the maximum number of background phase sweeps to perform.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Number of background sweep iterations. Choose a value between 1 and 25.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:CONT:ITER 3 source2:phase:control:iteration 4,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:CONTrol:ITERation? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10  
  
* * *

## SOURce<ch>:PHASe<port>:CONTrol:TOLerance <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the tolerance value to be used for background phase sweeps.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Tolerance for background sweeps in degrees. Choose a value between 1 and 5.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:CONT:TOL 3 source2:phase:control:tolerance 6,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:CONTrol:TOLerance? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 degree  
  
* * *

## SOURce<ch>:PHASe<port>:CORRection:DATA <data>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read an array of phase offsets.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<data> | Phase offset data array.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:CORR:DATA source2:phase:correction:data 10,15,20,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:CORRection:DATA? [src]  
Return Type | Depends on [FORMat:DATA](Format_SCPI.md#fd)  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:CORRection[:STATe] <bool>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read whether to use the phase correction offset array.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Phase correction array state. ON (1) Apply phase correction offset array. OFF(0) Do NOT apply phase correction offset array.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:CORR 1 source2:phase:correction:state OFF,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:CORRection[:STATe]? [src]  
Return Type | Boolean  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:PHASe<port>:EXTernal:CATalog?

Applicable Models: All with phase control option S9x088A/B (Read-only) Returns
the available internal ports that the external port can be set to. This
command is only intended to be executed for external sources. The command will
execute if the port is not an external source but does not do anything
meaningful.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | External port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:EXT:CAT? source2:phase:external:catalog?  
Return Type | String of comma-separated ports.  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:EXTernal:PORT <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Sets
and returns the internal port that the external port is routed through. This
command is only intended to be executed for external sources. The command will
execute if the port is not an external source but does not do anything
meaningful.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | External port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Internal port number.   
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | The following sets source port "Port 1 Src2" on channel 2 to use "Port 1" for the measurement SOUR2:PHAS:EXT:PORT 1,"PORT 1 Src2" The following sets source port 2 on channel 1 to use Port 1 for the measurement source:phas2:external:port 1  
Query Syntax | SOURce<ch>:PHASe<port>:EXTernal:PORT? [src]  
Return Type | Character  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## SOURce<ch>:PHASe<port>[:FIXed] <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the fixed phase value. Must not be in logarithmic sweep.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Phase value in degrees. Choose a value between -360 and 360.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2 60 source2:phase:fixed 120,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>[:FIXed]? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 degrees  
  
* * *

## SOURce<ch>:PHASe<port>:MODE:CATalog?

Applicable Models: All with phase control option S9x088A/B (Read-only) Returns
the available phase control modes for the specified port.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:MODE:CAT? source2:phase:mode:catalog?  
Return Type | String of comma-separated phase control modes. For example, OFF, OPENloop, PARameter, REFerence.  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:MODE[:VALue] <char>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Sets
and returns the Phase Control mode.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<char> | Choose from: OFF \- Turn phase control OFF OPENloop \- Sets a raw phase value for either swept phase or fixed phase, but no receivers are used to control the phase. PARameter \- Sets and controls the phase of the signal at <port>. REFerence (Read-only) \- Use [SOUR:PHAS:PARameter](SourcePhase.md#parameter) to set.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:MODE PAR source2:phase:mode:value off  
Query Syntax | SOURce<ch>:PHASe<port>:MODE[:VALue]? [src]  
Return Type | Character  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:PHASe<port>:PARameter <string>[,src]

Applicable Models:All with phase control option S9x088A/B (Read-Write) Write
and read the ratioed receivers (parameter) to use for phase control.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<string> | Ratioed parameter. Choose any two VNA physical receivers. Use either standard receiver notation ("R/R3") or [logical receiver notation](../../S1_Settings/Measurement_Parameters.md#RecNotation) ("a1/a3"). Separate the two receiver names by a forward slash '/'. For example: "a3/a1".  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:PAR: "a3/a1","Port 3" source2:phase:parameter "a3/a1","Port 3"  
Query Syntax | SOURce<ch>:PHASe<port>:PARameter? Returns the ratioed parameter name.  
Return Type | String  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "a1/b1"  
  
* * *

## SOURce<ch>:PHASe<port>:PARameter:CATalog?

Applicable Models: All with phase control option S9x088A/B (Read-only) Returns
the available parameters that are set using the SOURce:PHASe:PARameter
command. This command applies to phase control only. This command does not
apply to DIQ. DIQ does not restrict the parameters that can be set. It shows
an empty string if nothing is settable. Usually this means that the reference
port has not been set yet. SOUR:PHAS:REF:PORT <port> needs to be set first.
For an external source, SOURce:PHASe:EXTernal:PORT <port> should be set first,
then the reference port, then the control parameter. But I try to figure out
the relevant information, if the external port or reference is not set.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:REFCAT? source2:phase:reference:catalog?  
Return Type | String of comma-separated phase control parameters.  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:PARameter:MODE <char>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Sets
and returns the Phase Control mode.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<char> | Choose from: OFF \- Turn phase control OFF OPENloop \- Sets a raw phase value for either swept phase or fixed phase, but no receivers are used to control the phase. PARameter \- Sets and controls the phase of the signal at <port>. REFerence (Read-only) \- Use [SOUR:PHAS:PARameter](SourcePhase.md#parameter) to set.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:PAR:MODE PAR source2:phase:parameter:mode off  
Query Syntax | SOURce<ch>:PHASe<port>:PARameter:MODE? [src]  
Return Type | Character  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:PHASe<port>:PARameter:MODE:CATalog?

Applicable Models: All with phase control option S9x088A/B (Read-only) Returns
the available phase control modes for the specified port.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:PAR:MODE:CAT? source2:phase:parameter:mode:catalog?  
Return Type | String of comma-separated phase control modes. For example, OFF, OPENloop, PARameter, REFerence.  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:PARameter:PORT <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Sets
and returns the reference port for the Phase Control measurement.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Reference port number. ONLY specific ports are available to be a reference for each source port. [Learn more](../../S1_Settings/Phase_Control.md#PhaseSetupDiag).  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | The following sets source port "Port 1 Src2" on channel 2 to use "Port 1" as the phase reference SOUR2:PHAS:PAR:PORT 1,"PORT 1 Src2" The following sets source port 2 on channel 1 to use Port 1 as the phase reference source:phas2:PAR:PORT 1  
Query Syntax | SOURce<ch>:PHASe<port>:PARameter:PORT? [src]  
Return Type | Character  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## SOURce<ch>:PHASe<port>:PARameter[:VALue] <string>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Sets
and returns the ratioed receivers (parameter) to use for phase control.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<string> | Ratioed parameter. Choose any two VNA physical receivers. Use either standard receiver notation ("R/R3") or [logical receiver notation](../../S1_Settings/Measurement_Parameters.md#RecNotation) ("a1/a3"). Separate the two receiver names by a forward slash '/'. For example: "a3/a1". Note: Phase control does not allow any two VNA physical receivers. Can only choose from an option of ax/ay, ay/ax, or ax/bx, where x is the control port and y is the reference port. DIQ application allows any two VNA physical receivers.   
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:PAR: "a3/a1","Port 3" source2:phase:parameter:value "a3/a1","Port 3"  
Query Syntax | SOURce<ch>:PHASe<port>:PARameter[:VALue]? Returns the ratioed parameter name.  
Return Type | String  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "a1/b1"  
  
* * *

## SOURce<ch>:PHASe<port>:POFFset:CORRection:DATA <data>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read a ratio amplitude offset array. This allows the setting of arbitrary
impedance, which is used for active load applications.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Ratio amplitude offset data array.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:POFF:CORR:DATA source2:phase:poffset:correction:data ,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:POFFset:CORRection:DATA? [src]  
Return Type | Depends on [FORMat:DATA](Format_SCPI.md#fd)  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:POFFset:CORRection[:STATe] <bool>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read whether to use the ratio amplitude offset array.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Phase correction array state. ON (1) Apply ratio amplitude offset array. OFF(0) Do NOT apply ratio amplitude offset array.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:POFF:CORR 1 source2:phase:poffset:correction:state OFF,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:POFFset:CONTrol[:STATe]? [src]  
Return Type | Boolean  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:PHASe<port>:POFFset:FIXed <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the fixed power ratioed value. Must NOT be in power sweep to use this
value during phase control.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Fixed power ratio value within the allowable range of the VNA.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:POFF:FIX 1 source2:phase:poffset:fixed -5,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>::POFFset:FIXed? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 dBc  
  
* * *

## SOURce<ch>:PHASe<port>:POFFset:STARt <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the start power ratioed value. Must also send [SENS:SWE:TYPE
POWer](Sense/Sweep_SCPI.htm#sst) to put the analyzer into power sweep mode.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Start power ratio value in dBc. Must be within the allowable range of the VNA  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:POFF:STAR 0 source2:phase:poffset:start -5,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:POFFset:STARt? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 dBc  
  
* * *

## SOURce<ch>:PHASe<port>:POFFset:STOP <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the start power ratioed value. Must also send [SENS:SWE:TYPE
POWer](Sense/Sweep_SCPI.htm#sst) to put the analyzer into power sweep mode.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Stop power ratio value in dBc. Must be within the allowable range of the VNA  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:POFF:STOP 0 source2:phase:poffset:stop -5,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:POFFset:STOP? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 dBc  
  
* * *

## SOURce<ch>:PHASe<port>:REFerence:CATalog?

Applicable Models: All with phase control option S9x088A/B (Read-only) Returns
the available ports that can be used as phase control reference ports for the
phase controlled port.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:REF:CAT? source2:phase:reference:catalog?  
Return Type | String of comma-separated phase control reference ports.  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:PHASe<port>:REFerence:PORT <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Sets
and returns the reference port for the Phase Control measurement.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Reference port number. ONLY specific ports are available to be a reference for each source port. [Learn more](../../S1_Settings/Phase_Control.md#PhaseSetupDiag). Use the SOURce:PHASe:REFerence:CATalog? command to see which ports are available.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | The following sets source port "Port 1 Src2" on channel 2 to use "Port 1" as the phase reference SOUR2:PHAS:REF:PORT 1,"PORT 1 Src2" The following sets source port 2 on channel 1 to use Port 1 as the phase reference source:phas2:REF:PORT 1  
Query Syntax | SOURce<ch>:PHASe<port>:REFerence:PORT? [src]  
Return Type | Character  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## SOURce<ch>:PHASe<port>:STARt <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the start value of phase sweep. Must also send [SENS:SWE:TYPE
PHAS](Sense/Sweep_SCPI.htm#sst)e to put the analyzer into phase sweep mode.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Start phase value in degrees. Choose a value between -360 and 360.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:STAR 60 source2:phase:start 120,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:STARt? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 degrees  
  
* * *

## SOURce<ch>:PHASe<port>:STOP <num>[,src]

Applicable Models: All with phase control option S9x088A/B (Read-Write) Write
and read the stop value of phase sweep. Must also send [SENS:SWE:TYPE
PHAS](Sense/Sweep_SCPI.htm#sst)e to put the analyzer into phase sweep mode.  
---  
Parameters |   
<ch> | Channel number of phase control measurement. If unspecified, value is set to 1.  
<port> | Phase controlled port number. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> | Stop phase value in degrees. Choose a value between -360 and 360.  
[src] | String. (NOT case sensitive). Source port. Optional argument. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names.  
Examples | SOUR:PHAS2:STOP 60 source2:phase:stop 120,"Port 1 Src2"  
Query Syntax | SOURce<ch>:PHASe<port>:STOP? [src]  
Return Type | Numeric  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 degrees  
  
* * *

