# The Rules and Syntax of SCPI

* * *

Most of the commands used for controlling instruments on the GPIB are SCPI
commands. The following sections will help you learn to use SCPI commands in
your programs.

  * [Branches on the Command Tree](The_Rules_and_Syntax_of_SCPI_Commands.md#paths)

  * [Command and Query](The_Rules_and_Syntax_of_SCPI_Commands.md#query)

  * [Multiple Commands](The_Rules_and_Syntax_of_SCPI_Commands.md#mult)

  * [Command Abbreviation](The_Rules_and_Syntax_of_SCPI_Commands.md#abrev)

  * [Bracketed (Optional) Keywords](The_Rules_and_Syntax_of_SCPI_Commands.md#mnem)

  * [Vertical Bars (Pipes)](The_Rules_and_Syntax_of_SCPI_Commands.md#pipes)

  * [MIN and MAX Parameters](The_Rules_and_Syntax_of_SCPI_Commands.md#min)

[Other Topics about GPIB Concepts](Learning_about_GPIB.md)

Branches on the Command Tree

All major functions on the analyzer are assigned keywords which are called
ROOT commands. (See GPIB Command Finder for a list of SCPI root commands).
Under these root commands are branches that contain one or more keywords. The
branching continues until each analyzer function is assigned to a branch. A
root command and the branches below it is sometimes known as a subsystem.

For example, under [SOURce:POWer](../GP-IB_Command_Finder/source.md) are
several branch commands.

Sometimes the same keyword, such as STATE, is used in several branches of the
command tree. To keep track of the current branch, the analyzer's command
parser uses the following rules:

  * Power On and Reset \- After power is cycled or after *RST, the current path is set to the root level commands.

  * Message Terminators \- A message terminator, such as a <NL> character, sets the current path to the root command level. Many programming language output statements send message terminators automatically. Message terminators are described in Sending Messages to the Analyzer.

  * Colon (:) \- When a colon is between two command keywords, it moves the current path down one level in the command tree. For example, the colon in :SOURCE:POWER specifies that POWER is one level below SOURCE. When the colon is the first character of a command, it specifies that the following keyword is a root level command. For example, the colon in :SOURCE specifies that source is a root level command.

Note: You can omit the leading colon if the command is the first of a new
program line. For example, the following two commands are equivalent:  
SOUR:POW:ATT:AUTO  
:SOUR:POW:ATT:AUTO

  * <WSP> \- Whitespace characters, such as <tab> and <space>, are generally ignored. There are two important exceptions:

  *     * Whitespace inside a keyword, such as :CALC ULATE, is not allowed.

    * Most commands end with a parameter. You must use whitespace to separate these ending parameters from commands. Always refer to the command documentation. In the following example, there is whitespace between STATE and ON.

CALCULATE1:SMOOTHING:STATE ON

  * Comma (,) \- If a command requires more than one parameter, you must separate adjacent parameters using a comma. For example, the SYSTEM:TIME command requires three values to set the analyzer clock: one for hours, one for minutes, and one for seconds. A message to set the clock to 8:45 AM would be SYSTEM:TIME 8,45,0. Commas do not affect the current path.

  * Semicolon(;) \- A semicolon separates two commands in the same message without changing the current path. See [Multiple Commands](The_Rules_and_Syntax_of_SCPI_Commands.md#mult) later in this topic.

  * IEEE 488.2 Common Commands \- Common commands, such as *RST, are not part of any subsystem. An instrument interprets them in the same way, regardless of the current path setting.

Command and Query

A SCPI command can be an Event command, Query command (a command that asks the
analyzer for information), or both. The following are descriptions and
examples of each form of command. GPIB Command Finder lists every SCPI command
that is recognized by the analyzer, and its form.

Form |  Examples  
---|---  
Event commands - cause an action to occur inside the analyzer. |  :INITIATE:IMMEDIATE  
Query commands - query only; there is no associated analyzer state to set. |  :SYSTem:ERRor?  
Command and query - set or query an analyzer setting. The query form appends a question mark (?) to the set form |  :FORMat:DATA ! Command  
:FORMat:DATA? ! Query  
  
Multiple Commands

You can send multiple commands within a single program message. By separating
the commands with semicolons the current path does not change. The following
examples show three methods to send two commands:

  1. Two program messages:

SOURCE:POWER:START 0DBM  
SOURCE:POWER:STOP 10DBM

  2. One long message. A colon follows the semicolon that separates the two commands causing the command parser to reset to the root of the command tree. As a result, the next command is only valid if it includes the entire keyword path from the root of the tree:

SOURCE:POWER:START 0DBM;:SOURCE:POWER:STOP 10DBM

  3. One short message. The command parser keeps track of the position in the command tree. Therefore, you can simplify your program messages by including only the keyword at the same level in the command tree.

SOURCE:POWER:START 0DBM;STOP 10DBM

Common Commands and SCPI Commands

You can send Common commands and SCPI commands together in the same message.
(For more information on these types of commands see [GP-IB Fundamentals](GP-
IB_Fundamentals.htm).) As in sending multiple SCPI commands, you must separate
them with a semicolon.

Example of Common command and SCPI commands together

*RST;SENSE:FREQUENCY:CENTER 5MHZ;SPAN 100KHZ

Command Abbreviation

Each command has a long form and an abbreviated short form. The syntax used in
this Help system use uppercase characters to identify the short form of a
particular keyword. The remainder of the keyword is lower case to complete the
long form.

SOUR - Short form  
SOURce - Long form

Either the complete short form or complete long form must be used for each
keyword. However, the keywords used to make a complete SCPI command can be a
combination of short form and long form.

The following is unacceptable \- The first three keywords use neither short or
long form.

SOURc:Powe:Atten:Auto on

The following is acceptable \- All keywords are either short form or long
form.

SOUR:POWer:ATT:AUTO on

In addition, the analyzer accepts lowercase and uppercase characters as
equivalent as shown in the following equivalent commands:

source:POW:att:auto ON  
Source:Pow:Att:Auto on

Optional [Bracketed] Keywords

You can omit some keywords without changing the effect of the command. These
optional, or default, keywords are used in many subsystems and are identified
by brackets in syntax diagrams.

Example of Optional Keywords

The HCOPy subsystem contains the optional keyword IMMediate at its first
branching point. Both of the following commands are equivalent:

"HCOPY:IMMEDIATE"

"HCOPY"

The syntax in this Help system looks like this:

HCOPy[:IMMediate]

Vertical Bars | Pipes

Vertical bars, or "pipes", can be read as "or". They are used in syntax
diagrams to separate alternative parameter options.

Example of Vertical Bars:

SOURce:POWer:ATTenuation:AUTO <on|off>

Either ON or OFF is a valid parameter option.

MIN and MAX Parameters

The special form parameters "MINimum" and "MAXimum" can be used with commands
that specify single frequency (Hz) and time (seconds) as noted in the command
documentation. Note: Also with these commands, kHZ, MHz, and GHz are accepted
as suffixes/units.

The short form (min) and long form (minimum) of these two keywords are
equivalent.

  * MAXimum refers to the largest value that the function can currently be set to

  * MINimum refers to the smallest value that the function can currently be set to.

For example, the following command sets the start frequency to the smallest
value that is currently possible:

SENS:FREQ:START MIN

In addition, the max and min values can also be queried for these commands.

For example, the following command returns the smallest value that Start
Frequency can currently be set to:

SENS:FREQ:START? MIN

An error will be returned if a numeric parameter is sent that exceeds the MAX
and MIN values.

For example, the following command will return an "Out of range" error
message.

SENS:FREQ:START 1khz

* * *

