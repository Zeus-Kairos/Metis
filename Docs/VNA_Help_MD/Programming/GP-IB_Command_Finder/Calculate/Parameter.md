# Calculate:Parameter Commands

* * *

Lists, creates, selects, and deletes measurements.

For application measurements, use [Calc:Custom commands](Custom.md).

CALCulate:PARameter: [CATalog](Parameter.md#cpc) | [EXTended](Parameter.md#ParCatExtended) COUNt [DEFine](Parameter.md#cpd) | [EXTended](Parameter.md#DefineExtend) [DELete](Parameter.md#cpdel) | [ALL](Parameter.md#cpdelall) MNUMber | [[SELect]](Parameter.md#MnumSel) [MODify](Parameter.md#modify) | [EXTended](Parameter.md#ModExtend) [SELect](Parameter.md#cps) TAG | NEXT? [TNUMber?](Parameter.md#Tnum) [WNUMber?](Parameter.md#wnum)  
---  
  
Click on a keyword to view the command details.

Blue commands are [superseded](../../Replacement_Commands.md).

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Measurement Parameters](../../../S1_Settings/Measurement_Parameters.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:PARameter:CATalog? <enum> Superseded

Applicable Models: All Note: This command is replaced with
[CALC:PAR:CAT:EXTended?](Parameter.md#ParCatExtended) which lists parameters
with "_" instead of "," allowing the list to be parsed easily. This command
will continue to work. (Read-only) Returns the names and parameters of
existing measurements for the specified channel. Note: For Balanced
Measurements: CALC:PAR:CAT? may have an unexpected behavior. [Learn
more.](FSimulatorBalun.htm) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurements to be listed. If unspecified, <cnum> is set to 1.  
<enum> | Choose from: NORMal \- This is the default if no parameter is specified. If a trace title is defined in a standard channel, then the "name" returned is the same as the trace title. For non standard channels, the "name" returned is the underlying parameter name, regardless of whether the user has turned on a trace title or not. DISPlay \- If a trace title is defined, then the "name" returned is the same as the trace title. DEFine \- The "name" returned is always the same as the underlying parameter name, regardless of whether the trace title is turned on or not.  
Examples | CALC:PAR:CAT? DISP  
calculate2:parameter:catalog?  
Return Type | String \- "<measurement name>,<parameter>,[<measurement name>,<parameter>...]"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "CH1_S11_1,S11"  
  
* * *

## CALCulate<cnum>:PARameter:CATalog:EXTended? <enum>

Applicable Models: All (Read-only) Returns the names and parameters of
existing measurements for the specified channel. This command lists receiver
parameters with "_" such that R1,1 is reported as R1_1. This makes the
returned string a true "comma-delimited" list all the time. The returned
string of this command is easily parsed and used to create measurements using
the [CALC:PAR:EXT](Parameter.md#DefineExtend) command.  
---  
Parameters |   
<cnum> | Channel number of the measurements to be listed. If unspecified, <cnum> is set to 1.  
<enum> | Choose from: NORMal \- This is the default if no parameter is specified. If a trace title is defined in a standard channel, then the "name" returned is the same as the trace title. For non standard channels, the "name" returned is the underlying parameter name, regardless of whether the user has turned on a trace title or not. DISPlay \- If a trace title is defined, then the "name" returned is the same as the trace title. DEFine \- The "name" returned is always the same as the underlying parameter name, regardless of whether the trace title is turned on or not.  
Examples | CALC:PAR:CAT:EXT? DEF calculate2:parameter:catalog:extended?  
Return Type | String \- "<measurement name>,<parameter>,[<measurement name>,<parameter>...]"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "CH1_S11_1,S11"  
  
* * *

## CALCulate<cnum>:PARameter:COUNt <numOfTraces>,[<measClass>]

Applicable Models: All (Read-Write) Sets or gets the number of traces of
selected channel. Requirements:

  * Requires that window [n] exist. So to use the command properly you need to create window [n] before this command can succeed.
  * If window[n] exists but is already occupied by another channels measurement, an error is returned Duplicate trace number.
  * If window[n] does not exist, an error is returned: Window number not found.
  * If the command succeeds, it will always delete measurements.   
calc[n]:par:count <m> will delete existing measurements in channel [n] and
create <m> copies of S11 in window [n].

  
---  
Parameters |   
<cnum> | Channel number of the measurements to be listed. If unspecified, <cnum> is set to 1.  
<measClass> | Measurement class name.  
<numOfTraces> | Number of traces on the selected channel. Varies depending on the upper limit setting for the channel/trace number. **_Note: This command always deletes existing measurements and replaces them with S11._**  
Examples | 'Create a standard S-parameter channel with one trace  
disp:wind4:state on  
calc4:par:count 1  
  
'Create a Gain Compression channel with one trace  
disp:wind4:state on  
calc4:par:count 1,"Gain Compression"  
Query Syntax | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## CALCulate<cnum>:PARameter[:DEFine] <Mname>,<param>[,port]  Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
is replaced with [CALC:PAR:DEFine:EXTended](Parameter.md#DefineExtend). This
command will continue to work for up to 4-port parameters. (Write-only)
Creates a measurement but does NOT display it. There is no limit to the number
of measurements that can be created. However, there is a limit to the number
of measurements that can be displayed. See [Traces, Channels, and Windows on
the VNA](../../../S0_Start/Traces_Channels_and_Windows.htm#window).

  * Use [DISP:WIND:STATe](../Display.md#dwstat) to create a window if it doesn't already exist.
  * Use [DISP:WIND<wnum>:TRAC<tnum>:FEED <Mname>](../Display.md#dwtf) to display the measurement.

For Application Measurements see [CALC:CUST:DEF](Custom.md#CustDef) You must
select the measurement (CALC<cnum>:PAR:SEL <mname>) before making additional
settings. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the new measurement. If unspecified, value is set to 1.  
<Mname> | Name of the measurement. Any non-empty, unique string, enclosed in quotes.  
<param> | Parameter to be measured. Quotes are optional. For S-parameters: Any S-parameter available in the VNA For ratioed measurements: Any two receivers that are available in the VNA. (See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA.) For example: AR1 (this means A/R1) For non-ratioed measurements: Any receiver that is available in the VNA. (See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA.) For example: A For Balanced Measurements: First create an S-parameter measurement, then change the measurement using [CALC:FSIM:BAL](FSimulatorBalun.md) commands. [See an example](../../GPIB_Example_Programs/Create_a_Balanced_Measurement_using_SCPI.md). For [Applications](../../../Applications/Applications.md) see [CALC:CUST:DEF](Custom.md#CustDef).  
[port] | Optional argument; For multi-port reflection S-parameter measurements: specifies the VNA port which will provide the load for the calibration. This argument is ignored if a transmission S-parameter is specified. For all non S-parameter measurements: specifies the source port for the measurement.  
Examples | CALC4:PAR 'ch4_S33',S33,2 'Defines an S33 measurement with a load on port2 of the analyzer. calculate2:parameter:define 'ch1_a', a, 1 'unratioed meas calculate2:parameter:define 'ch1_a', ar1,1 'ratioed meas  
Query Syntax | Not Applicable; see [Calc:Par:Cat?](Parameter.md#cpc)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter[:DEFine]:EXTended <Mname>,<param>

Applicable Models: All Note: This command replaces
[CALC:PAR:DEF](Parameter.md#cpd) as it allows the creating of measurements
using [external multiport
testsets](../../../System/External_Testset_Control.htm). (Write-only) Creates
a measurement but does NOT display it. There is no limit to the number of
measurements that can be created. However, there is a limit to the number of
measurements that can be displayed. See [Traces, Channels, and Windows on the
VNA](../../../S0_Start/Traces_Channels_and_Windows.htm#window).

  * Use [DISP:WIND:STATe](../Display.md#dwstat) to create a window if it doesn't already exist.
  * Use [DISP:WIND<wnum>:TRAC<tnum>:FEED <Mname>](../Display.md#dwtf) to display the measurement.

Note: For Application Measurements see [CALC:CUST:DEF](Custom.md#CustDef) You
must select the measurement using [CALC:PAR:SELect](Parameter.md#cps) before
making additional settings. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the new measurement. If unspecified, value is set to 1.  
<Mname> | (String) Name of the measurement. Any non-empty, unique string, enclosed in quotes.  
<param> | (String ) Measurement Parameter to create. Case sensitive. For S-parameters: Any S-parameter available in the VNA Single-digit port numbers CAN be separated by "_" (underscore). For example: **" S21" or "S2_1"** Double-digit port numbers MUST be separated by underscore. For example: **" S10_1"** For ratioed measurements: Any two VNA physical receivers separated by forward slash '/' followed by comma and source port. For example: "A/R1, 3" [Learn more about ratioed measurements](../../../S1_Settings/Measurement_Parameters.md#arb_ratio) See a [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. For non-ratioed measurements: Any VNA physical receiver followed by comma and source port. For example: "A, 4" [Learn more about unratioed measurements.](../../../S1_Settings/Measurement_Parameters.md#Unratioed_Power) See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in YOUR VNA. Ratioed and Unratioed measurements can also use logical receiver notation to refer to receivers. This notation makes it easy to refer to receivers with an [external test set](../../../System/External_Testset_Control.md) connected to the VNA. You do not need to know which physical receiver is used for each test port. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation) For ADC measurements: Any ADC receiver in the VNA followed by a comma, then the source port. For example: "AI1,2" indicates the Analog Input1 with source port of 2. [Learn more about ADC receiver measurements.](../../../S1_Settings/ADC_Measurements.md) For Balanced Measurements: First create an S-parameter measurement, then change the measurement using [CALC:FSIM:BAL](FSimulatorBalun.md) "define" commands. [See an example](../../GPIB_Example_Programs/Create_a_Balanced_Measurement_using_SCPI.md). Note: For Application Measurements see [CALC:CUST:DEF](Custom.md#CustDef)  
Examples | CALC4:PAR:EXT 'ch4_S33', 'S33' 'Defines an S33 measurement calculate2:parameter:define:extended 'ch1_a', 'b9, 1' 'logical receiver notation for unratioed meas of test port 9 receiver with source port 1. calculate2:parameter:define:extended 'ch1_a', 'b9/a10,1' 'logical receiver notation for ratioed meas of test port 9 receiver divided by the reference receiver for port 10 using source port 1  
Query Syntax | Not Applicable; see [Calc:Par:Cat?](Parameter.md#cpc)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter:DELete[:NAME] <Mname>

Applicable Models: All (Write-only) Deletes the specified measurement. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<Mname> | String \- Name of the measurement  
Examples | CALC:PAR:DEL 'TEST'  
calculate2:parameter:delete 'test'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate:PARameter:DELete:ALL

Applicable Models: All (Write-only) Deletes all measurements on the VNA. See
Critical Note  
---  
Parameters |   
Examples | CALC:PAR:DEL:ALL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter:MNUMber[:SELect] <n>[,fast]

Applicable Models: All (Read-Write) Sets and returns the selected measurement
for the channel using the Tr#. Most CALC: commands require that this, or
[CALC:PAR:SEL](Parameter.md#cps), be sent before a setting change is made to
that measurement. Each channel can have one selected measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement to be selected. If unspecified, <cnum> is set to 1.  
<n> | Numeric - Measurement number. These are the same numbers you see in the Tr1, Tr2 annotation next to the parameter name on the VNA screen.  
[fast] | Optional. The VNA display is NOT updated. Therefore, do not use this argument when an operator is using the VNA display. Otherwise, sending this argument results in much faster sweep speeds. There is NO other reason to NOT send this argument.  
Examples | CALC:PAR:MNUM 2 calculate2:parameter:mnumber:select 3,fast  
Query Syntax | CALCulate<cnum>:PARameter:MNUMber[:SELect]? There is NO query available to determine if the FAST argument has been set.  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 (Trace number when factory preset is performed)  
  
* * *

## CALCulate<cnum>:PARameter:MODify <param> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
is replaced with [CALC:PAR:MOD:EXT](Parameter.md#ModExtend). This command
will continue to work for up to 4 port parameters.  (Write-only) Modifies a
standard measurement using the same arguments as
[CALC:PAR:DEF](Parameter.md#cpd). To modify an FCA measurement, use
[CALC:CUST:MOD](Custom.md#Modify). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. The selected measurement on that channel will be changed. If unspecified, <cnum> is set to 1.  
<param> | Measurement parameter to change to. Use the same <param> arguments as [CALC:PAR:DEF](Parameter.md#cpd).  
Examples | SYST:PRESET CALC:PAR:DEF "MyMeas", S11 CALC:PAR:SEL "MyMeas" CALC:PAR:MOD AR1 'changes the selected S11 measurement to an A/R1 measurement  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter:MODify:EXTended <param>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA Note: This
command replaces [CALC:PAR:MOD](Parameter.md#modify) as it allows
modification of measurements using [external multiport
testsets](../../../System/External_Testset_Control.htm). (Write-only) Modifies
a standard measurement using the same arguments as
[CALC:PAR:DEF:EXT](Parameter.md#DefineExtend).  To modify an Application
measurement, use [CALC:CUST:MOD](Custom.md#Modify). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. The selected measurement on that channel will be changed. If unspecified, <cnum> is set to 1.  
<param> | (String) New measurement parameter. Use the same <param> arguments as [CALC:PAR:DEF:EXT](Parameter.md#DefineExtend).  
Examples | SYST:PRESET CALC:PAR:DEF:EXT "MyMeas", "S10_1" CALC:PAR:SEL "MyMeas" CALC:PAR:MOD:EXT "a4b4,1" 'changes the selected S10_1 measurement to an a4/b4 measurement with source port 1  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter:SELect <Mname>[,fast]

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Read-Write)
Sets the selected measurement. Most CALC: commands require that this command
be sent before a setting change is made. One measurement on each channel can
be selected at the same time.

  * Use [CALC:PAR:MNUM](Parameter.md#MnumSel) to select a measurement by Tr# number. [Learn more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.md).
  * To obtain a list of currently named measurements, use [CALC:PAR:CAT?](Parameter.md#ParCatExtended)

  
---  
Parameters |   
<cnum> | Channel number of the measurement to be selected. If unspecified, <cnum> is set to 1.  
<Mname> | String - Name of the measurement. CASE-SENSITIVE. Do NOT include the parameter name that is returned with Calc:Par:Cat?  
[fast] | Optional. The VNA display is NOT updated. Therefore, do not use this argument when an operator is using the VNA display. Otherwise, sending this argument results in much faster sweep speeds. There is NO other reason to NOT send this argument.  
Examples | CALC:PAR:SEL 'TEST' calculate2:parameter:select 'test',fast  
Query Syntax | CALCulate:PARameter:SELect? There is NO query available to determine if the FAST argument has been set.  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "CH1_S11_1" (Trace name when factory preset is performed)  
  
* * *

## CALCulate<cnum>:PARameter:TAG:NEXT?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
a string that is guaranteed to be unique and valid for use with CALC:PAR:DEF.  
---  
Parameters |   
<cnum> | Channel number of the trace. If unspecified, <cnum> is set to 1.  
Examples | CALC:PAR:TAG:NEXT?  
calculate2:parameter:tag:next?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter:TNUMber?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the trace number of the selected trace. Select a trace using
[Calc:Par:Select](Parameter.md#cps).  
---  
Parameters |   
<cnum> | Channel number of the trace. If unspecified, <cnum> is set to 1.  
Examples | CALC:PAR:TNUM?  
calculate2:parameter:tnumber?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:PARameter:WNUMber?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the window number of the selected trace. Select a trace using
[Calc:Par:Select](Parameter.md#cps).  
---  
Parameters |   
<cnum> | Channel number of the selected trace. If unspecified, <cnum> is set to 1.  
Examples | CALC:PAR:WNUM?  
calculate2:parameter:wnumber?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

