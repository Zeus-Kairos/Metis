# IEEE 488.2 Common Commands

* * *

### [*CLS \- Clear Status](Common_Commands.md#cls)

### [*ESE \- Event Status Enable](Common_Commands.md#ese)

### [*ESE? \- Event Status Enable Query](Common_Commands.md#eseq)

### [*ESR? \- Event Status Enable Register](Common_Commands.md#esr) \- See
[*ESR? programming example](../GPIB_Example_Programs/_ESR__Sweep_Complete.md)

### [*IDN? \- Identify](Common_Commands.md#idn)

### [*OPC \- Operation complete command](Common_Commands.md#opc)

### [*OPC? \- Operation complete query](Common_Commands.md#opcq)

### [*OPT? \- Identify Options Query](Common_Commands.md#opt)

### [*RST \- Reset](Common_Commands.md#rst)

### [*SRE \- Service Request Enable](Common_Commands.md#sre)

### [*SRE? \- Service Request Enable Query](Common_Commands.md#sreq)

### [*STB? \- Status Byte Query](Common_Commands.md#stbq)

### [*TST? \- Result of Self-test Query](Common_Commands.md#tstq)

### [*WAI \- Wait](Common_Commands.md#wai)

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

### *CLS - Clear Status

Clears the instrument status byte by emptying the error queue and clearing all
event registers. Also cancels any preceding *OPC command or query. See [Status
Commands](Status.htm) and [Reading the Analyzer's Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *ESE - Event Status Enable

Sets bits in the standard event status enable register. See [Status
Commands](Status.htm) and [Reading the Analyzer's Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *ESE? - Event Status Enable Query

Returns the results of the standard event enable register. The register is
cleared after reading it. See [Status Commands](Status.md) and [Reading the
Analyzer's Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *ESR - Event Status Enable Register

Reads and clears event status enable register. See [Status
Commands](Status.htm) and [Reading the Analyzer's Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *IDN? - Identify

Returns a string that uniquely identifies the analyzer. The string is of the
form "Keysight Technologies",<model number>,<serial "number>,<software
revision>" .

Note: Beginning with Rev 6.01, this command now returns the software revision
with 6 digits instead of 4. For example, A.06.01.02.

For 4 state CALPod support the following is required.

  * CCT (configurable command table) version 1.4

  * Controller FPGA version 8.4

* * *

### *OPC \- Operation complete command

Generates the OPC message in the standard event status register when all
pending overlapped operations have been completed (for example, a sweep, or a
Default). See [Understanding Command
Synchronization.](../Learning_about_GPIB/Understanding_Command_Synchronization.htm)

* * *

### *OPC? - Operation complete query

Returns an ASCII "+1" when all pending overlapped operations have been
completed. See [Understanding Command
Synchronization](../Learning_about_GPIB/Understanding_Command_Synchronization.htm)

* * *

### *OPT? - Identify Options Query

Returns a comma-separated string identifying the analyzer option
configuration.

[See a list of VNA options](../../Support/Configurations.md). Refer also to
the [option number
differences](../../Support/Configurations.htm#OPT_and_Options_COM_Behavior)
between the common option numbers and those returned using this command.

See also
[SYST:CAP:LIC:CAT?](SystCapability.md#SYSTem:CAPability:LICenses:CATalog) for
the installed product license .

* * *

### *RST - Reset

Executes a device reset and cancels any pending *OPC command or query, exactly
the same as a [SYSTem:PRESet](System.md#pre) with one exception: Syst:Preset
does NOT reset [Calc:FORMAT](Calculate/Format_Calc.md#format) to ASCII. The
contents of the analyzer's non-volatile memory are not affected by this
command.

* * *

### *SRE - Service Request Enable

Before reading a status register, bits must be enabled. This command enables
bits in the service request register. The current setting is saved in non-
volatile memory. See [Status Commands](Status.md) and [Reading the Analyzer's
Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *SRE? - Service Request Enable Query

Reads the current state of the service request enable register. The register
is cleared after reading it. The return value can be decoded using the table
in [Status Commands](Status.md). See also [Reading the Analyzer's Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *STB? - Status Byte Query

Reads the value of the instrument status byte. The register is cleared only
when the registers feeding it are cleared. See [Status Commands](Status.md)
and [Reading the Analyzer's Status
Registers.](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

* * *

### *TST? - Result of Self-test Query

Returns the result of a query of the analyzer hardward status. An 0 indicates
no failures found. Any other value indicates one or more of the following
conditions exist. The value returned is the Weight (or sum of the Weights) of
the existing conditions. For example:

  * If 4 is returned from *TST?, an Overpower condition exists.

  * If 6 is returned, both Unleveled and Overpower conditions exists.

* * *

Bit | Weight | Description | Bit is set to 1 when the following conditions exist:  
---|---|---|---  
0 | 1 | Phase Unlock | The source has lost phaselock. This could be caused by a reference channel open or a hardware failure.  
1 | 2 | Unleveled | The source power is unleveled. This could be a source is set for more power than it can deliver at the tuned frequency. Or it could be caused by a hardware failure.  
2 | 4 | Not used  
3 | 8 | EE Write Failed | An attempted write to the EEPROM has failed. This is possibly caused by a hardware failure.  
4 | 16 | YIG Cal Failed | The analyzer was unable to calibrate the YIG. Either the phaselock has been lost or there has been a hardware failure.  
5 | 32 | Ramp Cal Failed | The analyzer was unable to calibrate the analog ramp generator due to a possible hardware failure.  
6 | 64 | Not used  
  
* * *

### *WAI - Wait

Prohibits the instrument from executing any new commands until all pending
overlapped commands have been completed. See [Understanding Command
Synchronization](../Learning_about_GPIB/Understanding_Command_Synchronization.htm)

* * *

