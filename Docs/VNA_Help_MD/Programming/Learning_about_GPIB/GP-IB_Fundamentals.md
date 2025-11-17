# GPIB Fundamentals

* * *

The General Purpose Interface Bus (GPIB) is a system of hardware and software
that allows you to control test equipment to make measurements quickly and
accurately. This topic contains the following information:

  * [The GPIB Hardware Components](GP-IB_Fundamentals.md#hard)

  * [The GPIB / SCPI Programming Elements](GP-IB_Fundamentals.md#soft)

  * [Specifications](GP-IB_Fundamentals.md#spec)

  * [GPIB Interface Capability Codes](GP-IB_Fundamentals.md#code)

Note: All of the topics related to programming assume that you already know
how to program, preferably using a language that can control instruments.

[Other Topics about GPIB Concepts](Learning_about_GPIB.md)

The GPIB Hardware Components

The system bus and its associated interface operations are defined by the IEEE
488 standard. The following sections list and describe the main pieces of
hardware in a GPIB system:

Early VNA models had only ONE GPIB connector. These models could control other
GPIB devices using one of, or a combination of, the following methods:

  * Use the SCPI [SYST:COMM:GPIB:RDEV](../GP-IB_Command_Finder/SystCommunicate.md#close): commands.
  * Use VISA or SICL over LAN to accomplish this. See an [example](../GPIB_Example_Programs/ControllTalkListen.md).
  * Use USB / GPIB Interface

Note: Current VNA models have dedicated Controller and Talker/Listener GPIB
ports. [See how to configure these
ports.](How_to_Configure_for_GPIB_SCPI_and_SICL.htm)  
---  
  
### Controllers

Controllers specify the instruments that will be the talker and listener in a
data exchange. The controller of the bus must have a GPIB interface card to
communicate on the GPIB.

  * The Active Controller is the computer or instrument that is currently controlling data exchanges.

  * The System Controller is the only computer or instrument that can take control and give up control of the GPIB to another computer or instrument, which is then called the active controller.

### Talker / Listener Instruments and GPIB Addresses

  * Talkers are instruments that can be addressed to send data to the controller.

  * Listeners are instruments that can be addressed to receive a command, and then respond to the command. All devices on the bus are required to listen.

Every GPIB instrument must have its own unique address on the bus. The VNA
address (default = 716) consists of two parts:

  1. The Interface select code (typically 7) indicates which GPIB port in the system controller is used to communicate with the device.

  2. The primary address (16) is set at the factory. You can change the primary address of any device on the bus to any number between 0 and 30. To change the analyzer address click [System / Configure / SICL-GPIB](How_to_Configure_for_GPIB_SCPI_and_SICL.md#SICL).

A secondary address is sometimes used to allow access to individual modules in
a modular instrument system, such as a VXI mainframe. The VNA does NOT have a
secondary address.

### Cables

GPIB Cables are the physical link connecting all of the devices on the bus.
There are eight data lines in a GPIB cable that send data from one device to
another. There are also eight control lines that manage traffic on the data
lines and control other interface operations.

You can connect instruments to the controller in any arrangement with the
following limitations:

  * Do not connect more than 15 devices on any GPIB system. This number can be extended with the use of a bus extension.

  * Do not exceed a total of 20 meters of total cable length or 2 meters per device, whichever is less.

  * Avoid stacking more than three connectors on the back panel of an instrument. This can cause unnecessary strain on the rear-panel connector.

The GPIB / SCPI Programming Elements

The following software programming elements combine to become a GPIB program:

  * [GPIB / SCPI Commands](GP-IB_Fundamentals.md#command)

  * [Programming Statements](GP-IB_Fundamentals.md#statement)

  * [Instrument Drivers](GP-IB_Fundamentals.md#drivers)

### GPIB Commands

The GPIB command is the basic unit of communication in a GPIB system. The
analyzer responds to three types of GPIB commands:

1\. IEEE 488.1 Bus-management Commands

These commands are used primarily to tell some or all of the devices on the
bus to perform certain interface operations.

All of the functions that can be accomplished with these commands can also be
done with IEEE 488.2 or SCPI commands. Therefore, these commands are not
documented in this Help system. For a complete list of IEEE 488.1 commands
refer to the IEEE 488 standard. Examples of IEEE 488.1 Commands

  * CLEAR \- Clears the bus of any pending operations

  * LOCAL - Returns instruments to local operation

2\. IEEE 488.2 Common Commands

These commands are sent to instruments to perform interface operations. An
IEEE 488.2 common command consists of a single mnemonic and is preceded by an
asterisk ( * ). Some of the commands have a query form which adds a "?" after
the command. These commands ask the instrument for the current setting. See a
complete list of the [Common Commands](../GP-
IB_Command_Finder/Common_Commands.htm) that are recognized by the analyzer.
Examples of IEEE 488.2 Common Commands

  * *OPC - Operation Complete

  * *RST \- Reset

  * *OPT? - Queries the option configuration

3\. SCPI Commands

The Standard Commands for Programmable Instruments (SCPI) is a set of commands
developed in 1990. The standardization provided in SCPI commands helps ensure
that programs written for a particular SCPI instrument are easily adapted to
work with a similar SCPI instrument. SCPI commands tell instruments to do
device specific functions. For example, SCPI commands could tell an instrument
to make a measurement and output data to a controller. Examples of SCPI
Commands:

CALCULATE:AVERAGE:STATE ON

SENSE:FREQUENCY:START?

For more information on SCPI:

  * T[he Rules and Syntax of SCPI Commands](The_Rules_and_Syntax_of_SCPI_Commands.md) provides more detail of the SCPI command structure.

  * [SCPI Command Tree](../GP-IB_Command_Finder/SCPI_Command_Tree.md) is a complete list of the SCPI commands for the analyzer

### Programming Statements

SCPI commands are included with the language specific I/O statements to form
program statements. The programming language determines the syntax of the
programming statements. SCPI programs can be written in a variety of
programming languages such as VEE, HP BASIC, or C++. Example of a Visual Basic
statement:

  * GPIB.Write "SOURCE:FREQUENCY:FIXED 1000 MHz"

[Note about
examples](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

### Instrument Drivers

Instrument drivers are subroutines that provide routine functionality and can
be reused from program to program. GPIB industry leaders have written
standards for use by programmers who develop drivers. When programmers write
drivers that comply with the standards, the drivers can be used with
predictable results. To comply with the standard, each instrument driver must
include documentation describing its functionality and how it should be
implemented.

GPIB Specifications

Interconnected devices - Up to 15 devices (maximum) on one contiguous bus.

Interconnection path - Star or linear (or mixed) bus network, up to 20 meters
total transmission path length or 2 meters per device, whichever is less.

Message transfer scheme - Byte-serial, bit-parallel, asynchronous data
transfer using an interlocking 3-wire handshake.

Maximum data rate - 1 megabyte per second over limited distances, 250 to 500
kilobytes per second typical maximum over a full transmission path. The
devices on the bus determine the actual data rate.

Address capability - Primary addresses, 31 Talk and 31 Listen; secondary
addresses, 961 Talk and 961 Listen. There can be a maximum of 1 Talker and up
to 14 Listeners at a time on a single bus. See also previous section on [GPIB
addresses.](GP-IB_Fundamentals.htm#address)

GPIB Interface Capability Codes

The IEEE 488.1 standard requires that all GPIB compatible instruments display
their interface capabilities on the rear panel using codes. The codes on the
analyzer, and their related descriptions, are listed below:

SH1 | full source handshake capability  
---|---  
AH1 | full acceptor handshake capability  
T6 | basic talker, serial poll, no talk only, unaddress if MLA (My Listen Address)  
TEO | no extended talker capability  
L4 | basic listener, no listen only, unaddress if MTA (My Talk Address)  
LEO | no extended listener capability  
SR1 | full service request capability  
RL1 | full remote / local capability  
PPO | no parallel poll capability  
DC1 | full device clear capability  
DT1 | full device trigger capability  
C1 | system controller capability  
C2 | send IFC (Interface Clear) and take charge controller capability  
C3 | send REN (Remote Enable) controller capability  
C4 | respond to SRQ (Service Request)  
  
* * *

