# Sense:Correction:Extension Commands

* * *

Performs and applies Port Extensions.

SENSe:CORRection:EXTension: AUTO | [CONFig](CorrExtension.md#autoConfig) | [DCOFfset](CorrExtension.md#AutoDCOffset) | [LOSS](CorrExtension.md#AutoLoss) | [MEASure](CorrExtension.md#autoMeas) | [PORT](CorrExtension.md#autoPort) | [RESet](CorrExtension.md#autoReset) | [STARt](CorrExtension.md#autoStart) | [STOP](CorrExtension.md#autoStop) PORT | [DISTance](CorrExtension.md#portDist) | [FREQuency](CorrExtension.md#PortExtFreqX) | INCLude | [[STATe]](CorrExtension.md#PortExtIncl) | [LDC](CorrExtension.md#LossDC) | [LOSS](CorrExtension.md#PortExtLoss) | [MEDium](CorrExtension.md#portMedium) | [SYSMedia](CorrExtension.md#sysMedia) | [SYSVelocity](CorrExtension.md#sysVelocity) | [[TIME]](CorrExtension.md#PortTime) | [UNIT](CorrExtension.md#UNIT) | [VELFactor](CorrExtension.md#portVF) | [WGCutoff](CorrExtension.md#portWGC) RECeiver | [[TIME]](CorrExtension.md#RecTime) [[STATe]](CorrExtension.md#ExtState)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Port Extensions](../../../S3_Cals/Port_Extensions.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:CONFig <char>

Applicable Models: All (Read-Write) Sets the frequencies used to calculate
Automatic Port Extension. [Learn more about calculating Automatic Port
Extension.](../../../S3_Cals/Port_Extensions.htm#AutoPortExtensions)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Frequencies to be used: CSPN Use current frequency span. AMKR \- Use active marker frequency. USPN \- Use custom user span. Use [SENS:CORR:EXT:AUTO:STAR](CorrExtension.md#autoStart) and [SENS:CORR:EXT:AUTO:STOP](CorrExtension.md#autoStop) to specify start and stop frequency.  
Examples | SENS:CORR:EXT:AUTO:CONF CSPN  
sense2:correction:extension:auto:config amkr  
Query Syntax | SENSe<cnum>:CORRection:EXTension:AUTO:CONFig ?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | CSPN  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:DCOFfset <bool>

Applicable Models: All (Read-Write) Specifies whether or not to include DC
Offset as part of automatic port extension. [Learn more about Automatic DC
Offset](../../../S3_Cals/Port_Extensions.htm#PlusDCOffset). Only allowed when
[SENS:CORR:EXT:AUTO:LOSS](CorrExtension.md#AutoLoss) is set to ON.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | ON (or 1) - Includes DC Offset correction. OFF (or 0) - Does NOT include DC Offset correction.  
Examples | SENS:CORR:EXT:AUTO:DCOF 1  
sense2:correction:extension:auto:dcoffset off  
Query Syntax | SENSe<cnum>:CORRection:EXTension:AUTO:DCOFfset?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON (1)  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:LOSS <bool>

Applicable Models: All (Read-Write) Specifies whether or not to include loss
correction as part of automatic port extension. [Learn more about Loss
Compensation](../../../S3_Cals/Port_Extensions.htm#LossCompensation) in port
extension.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | ON (or 1) - Includes Loss correction. OFF (or 0) - Does NOT include Loss correction.  
Examples | SENS:CORR:EXT:AUTO:LOSS 1  
sense2:correction:extension:auto:loss off  
Query Syntax | SENSe<cnum>:CORRection:EXTension:AUTO:LOSS?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON (1)  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:MEASure <char>

Applicable Models: All (Write-only) Measures either an OPEN or SHORT standard.
When this command is sent, the VNA acquires the measurement with which to set
automatic port extensions. This command should be preceded by the
CALCulate:PARameter:MNUMber <num> where num is the trace number of a
measurement on the specified channel. [Learn more about which standard to
measure.](../../../S3_Cals/Port_Extensions.htm#MeasStandard)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Standard to be measured. Choose from: OPEN Measure OPEN standard SHORt Measure SHORT standard  
Examples | SENS:CORR:EXT:AUTO:MEAS OPEN  
sense2:correction:extension:auto:measure short  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:PORT<n> <bool>

Applicable Models: All (Read-Write) Enables and disables automatic port
extensions on the specified port.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<n> | VNA Port number to enable or disable for automatic port extensions.  
<bool> | ON (or 1) - Enable OFF (or 0) - Disable  
Examples | SENS:CORR:EXT:AUTO:PORT2 0  
sense2:correction:extension:auto:port4 on  
Query Syntax | SENSe<cnum>:CORRection:EXTension:AUTO:PORT<n>?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | All ports ON (enabled)  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:RESet

Applicable Models: All (Write-only) Clears old port extension delay and loss
data in preparation for acquiring new data. Send this command prior to sending
a new series of [SENS:CORR:EXT:AUTO:MEAS](CorrExtension.md#autoMeas). If
acquiring both OPEN and SHORT standards, do not send this command between
those acquisitions.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:CORR:EXT:AUTO:RES  
sense2:correction:extension:auto:reset  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:STARt <value>

Applicable Models: All (Read-Write) Set the start frequency for custom user
span. [Learn more about User
Span.](../../../S3_Cals/Port_Extensions.htm#Search)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | User span start value. Must be within the frequency range of the active channel and less than the value set by SENS:CORR:EXT:AUTO:STOP.  
Examples | SENS:CORR:EXT:AUTO:STAR 1E9  
sense2:correction:extension:auto:start 200e6  
Query Syntax | SENSe<cnum>:CORRection:EXTension:AUTO:STARt <value>?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Start frequency of the current active channel.  
  
* * *

## SENSe<cnum>:CORRection:EXTension:AUTO:STOP <value>

Applicable Models: All (Read-Write) Set the stop frequency for custom user
span. [Learn more about User
Span.](../../../S3_Cals/Port_Extensions.htm#Search)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | User span stop value. Must be within the frequency range of the active channel and greater than the value set by SENS:CORR:EXT:AUTO:STARt  
Examples | SENS:CORR:EXT:AUTO:STOP 1E9  
sense2:correction:extension:auto:stop 200e6  
Query Syntax | SENSe<cnum>:CORRection:EXTension:AUTO:STOP <value>?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Stop frequency of the current active channel.  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:DISTance <value> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the port extension delay in physical length
(distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number that will receive the delay setting. If unspecified, value is set to 1.  
<value> | Physical length of fixture of added transmission line. First specify units with [SENS:CORR:EXT:PORT:UNIT](CorrExtension.md#UNIT).  
Examples | SENS:CORR:EXT:PORT1:DIST 12  
sense2:correction:extension:port2:distance .003  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:DISTance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:FREQuency<n> <value> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the frequency for the Freq and Loss pair number
and for the specified port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the freq/loss settings. If unspecified, value is set to 1.  
<n> | Freq and Loss pair number. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | Frequency value. Choose a frequency within the frequency span of the VNA.  
Examples | SENS:CORR:EXT:PORT1:FREQ1 10E9  
sense2:correction:extension:port2:freq2 2E10  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:FREQuency<n>?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 GHz  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:INCLude<n>[:STATe] <bool>
Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the ON/OFF state for the Freq and Loss pair
number and for the specified port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the Freq/Loss settings. If unspecified, value is set to 1.  
<n> | Freq and Loss pair. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | State of Freq and Loss values for port extension. 0 or OFF Specified Freq and Loss values are OFF 1 or ON Specified Freq and Loss values are ON  
Examples | SENS:CORR:EXT:PORT:INCL 0  
sense2:correction:extension:port2:include2:state on  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:INCLude[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:LDC <value> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the Port Loss at DC value for the specified port
number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port number to receive Loss value. If unspecified, value is set to 1.  
<value> | Loss in dB. Choose a value between -90 and 90  
Examples | SENS:CORR:EXT:PORT:LDC 1.5 sense2:correction:extension:port2:ldc .1  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:LDC?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:LOSS<n> <value> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the Loss value for the specified port number.
[Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the Freq/Loss settings. If unspecified, value is set to 1.  
<n> | Loss "Use" number. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | Loss in dB. Choose a value between -90 and 90  
Examples | SENS:CORR:EXT:PORT:LOSS1 1 sense2:correction:extension:port2:loss2 .1  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:LOSS<n>?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:MEDium <char> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the media type of the added fixture or
transmission line. See also
[SENS:CORR:EXT:PORT:SYSMedia](CorrExtension.md#sysMedia) Note: This command
affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which media type is being set. If unspecified, value is set to 1.  
<char> | Medium type. Choose from:

  * COAX
  * WAVEguide

  
Examples | SENS:CORR:EXT:PORT:MED COAX sense2:correction:extension:port2:medium waveguide  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:MEDium?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | COAX  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT:SYSMedia <bool> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the state of coupling with the system Media
type. [Learn more.](../../../S3_Cals/Port_Extensions.md#PortDiag) Note: This
command potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Coupling state. Choose from:

  * ON (or 1) - Media type is coupled with the system setting.
  * OFF (or 0) - Media type is NOT coupled with the system setting.

  
Examples | SENS:CORR:EXT:PORT:SYSM 1 sense2:correction:extension:port:sysmedia off  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT:SYSMedia?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON (Coupled)  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:SYSVelocity <bool> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the state of coupling with the system Velocity
Factor value. [Learn more.](../../../S3_Cals/Port_Extensions.md#PortDiag)
Note: This command potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which system Velocity Factor coupling is being set. If unspecified, value is set to 1.  
<bool> | Coupling state. Choose from:

  * ON (or 1) - Velocity Factor is coupled with the system setting.
  * OFF (or 0) - Velocity Factor is NOT coupled with the system setting.

  
Examples | SENS:CORR:EXT:PORT:SYSV 1 sense2:correction:extension:port2:sysvelocity off  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:SYSVelocity?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON (Coupled)  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>[:TIME] <num> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets the extension delay value in time at the specified port.
Must also set SENS:CORR:EXT ON. Note: This command affects ALL measurements on
the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the extension. If unspecified, value is set to 1.  
<num> | The port extension in seconds; may include suffix. Choose a number between: -1E18 and 1E18  
Examples | SENS:CORR:EXT:PORT 2MS  
sense2:correction:extension:port2 .00025  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum> [:TIME]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT:UNIT <char> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the units for specifying port extension delay in
physical length (distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<char> | Units for delay in distance. Choose from:

  * METer
  * FEET
  * INCH

  
Examples | SENS:CORR:EXT:PORT:UNIT MET  
sense2:correction:extension:port:unit inch  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METer  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:VELFactor <value> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the velocity factor of the fixture or added
transmission line.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which velocity factor is being set. If unspecified, value is set to 1.  
<value> | Velocity Factor. Set [SENS:CORR:EXT:PORT:SYSV](CorrExtension.md#sysVelocity) to use the system velocity factor.  
Examples | SENS:CORR:EXT:PORT:VELF .6 sense2:correction:extension:port2:velfactor 1  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:VELFactor?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | System Velocity Factor  
  
* * *

## SENSe<cnum>:CORRection:EXTension:PORT<pnum>:WGCutoff <value> Superseded

Applicable Models: All The command set of
[SENSe<cnum>:CORRection:EXTension:PORT:XXXX](CorrExtension.md) is changed to
[CALCulate:FSIMulator:DRAFt:EXTension:PORT:YYYY](../Calculate/FSimulatorDraft.md)
and
[CALCulate:FSIMulator::EXTension:PORT:YYYY?](../Calculate/FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the cuttoff (minimum) frequency of the added
waveguide fixture or transmission line.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which media type is being set. If unspecified, value is set to 1.  
<value> | Cutoff frequency in Hz. This value is ignored when [SENS:CORR:EXT:PORT:MED](CorrExtension.md#portMedium) is set to COAX for the same port.  
Examples | SENS:CORR:EXT:PORT:WGC 1e8 sense2:correction:extension:port2:wgcutoff 100Mhz  
Query Syntax | SENSe<cnum>:CORRection:EXTension:PORT<pnum>:WGCutoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | System Media Cutoff Frequency  
  
* * *

## SENSe<cnum>:CORRection:EXTension:RECeiver<Rnum>[:TIME] <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the extension value at the specified receiver. Must also set [SENS:CORR:EXT
ON](CorrExtension.htm#ExtState). Note: Before using this command you must
select a measurement using
[CALC:MEAS:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine). You can
select one measurement for each channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<Rnum> | Number of the receiver that will receive the extension. If unspecified, value is set to 1  
Choose from: 1 for Receiver A 2 for Receiver B  
<num> | The electrical length in seconds; may include suffix. Choose a number between:  
-10 and 10  
Examples | SENS:CORR:EXT:REC 2MS  
sense2:correction:extension:receiver2:time .00025  
Query Syntax | SENSe<cnum>:CORRection:EXTension:RECeiver<Rnum> [:TIME]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:CORRection:EXTension[:STATe] <ON | OFF> Superseded

Applicable Models: All This command is changed to [CALC:FSIM:DRAFt:SECTion:EXTension:ENABle <ON | OFF>](../Calculate/FSimulatorDraft.md#SectExtEnab) and [CALC:FSIM:SECTion:EXTension:ENABle?](../Calculate/FSimulatorActive.md#SectExtEnab). Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Turns port extensions ON or OFF.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - turns port extensions ON. OFF (or 0) - turns port extensions is OFF.  
Examples | SENS:CORR:EXT ON  
sense2:correction:extension:state off  
Query Syntax | SENSe<cnum>:CORRection:EXTension[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

