# COM versus SCPI

* * *

There are two methods you can use to remotely control the VNA: COM and SCPI.
The following topics can help you choose the method that best meets your
needs:

  * [Software Connection](COM_versus_SCPI.md#soft)

  * [Physical Connection](COM_versus_SCPI.md#phys)

  * [Programming Languages](COM_versus_SCPI.md#lang)

[Other Topics about COM Concepts](Learning_about_COM.md)

### Software Connection

COM uses a binary protocol, allowing you to directly invoke a VNA feature.
This is more efficient than SCPI. For example, the following statement calls
directly into the VNA, executing the routine GetIDString.

PNA.GetIDString()

SCPI is a text based instrument language. To retrieve the ID string, you would
send the following text string to the VNA:

IbWrite( "*IDN?")

The VNA SCPI parser would first decode this text string to determine that the
user has asked for the VNA to identify itself. Then the parser would call the
COM method GetIDString().

### The Physical Connection

Internal Control

With either COM or SCPI, the best throughput is attained by using the VNA's
internal PC to execute your test code. However, if your test code uses too
much system resources (CPU cycles and/or memory), this will slow the VNA's
performance.

Using the SICL I/O Libraries, you can also connect to the VNA from a program
running on the VNA.

External Control

You can control the VNA from a remote PC using either COM or SCPI.

COM \- (Component Object Model) can be used to access any program like the VNA
(835x.exe) or library (.dll) that exposes its features using a COM compliant
object model. These programs or libraries are called "servers". Programs (like
your remote program on your PC) that connect to and use the features of these
servers are called "clients."

With COM, the server and the client do not need to reside on the same machine.
DCOM, or distributed COM, makes the location of the server transparent to the
client. When you access the VNA from a remote computer, you are using DCOM. In
this case, the mechanical transport is a LAN (local area network).

However, using COM can add additional complexity:

  * There are some DCOM security issues that may be a problem for you. [Learn more.](http://na.support.keysight.com/pna/DCOMSecurity.html)

  * Using the default interface when compiling type libraries results in code that will only run with the latest firmware. [Learn more.](PNA_Automation_Interfaces.md)

SCPI \- Using a GPIB interface card in a remote computer, you can connect to
the instrument using a GPIB cable. There are some constraints on the length of
this cable and the number of instruments that can be daisy-chained together.

Using the Keysight SICL I/O libraries, you can connect to the instrument over
a LAN connection.

(LAN or INTERNAL) You can send SCPI commands using COM with the
[ScpiStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object.

If you have legacy code written in SCPI for another network analyzer, you may
be able to leverage that code to control the VNA. However, the VNA uses a
different platform than previous Keysight Network Analyzers. Therefore, not
all commands have a direct replacement. See the VNA Code Translator
Application.

### Programming Languages

You can program the VNA with either COM or SCPI using several languages. The
most common include:

Keysight VEE \- With this language you can send text based SCPI commands and
also use automation. VEE 6.0 or later is recommended.

Visual Basic \- This language has great support for automation objects and can
be used to drive SCPI commands. The use of VISA drivers for your GPIB hardware
interface will make the task of sending SCPI commands easier.

C++ \- This language can do it all. It is not as easy to use as the above two,
but more flexible.

* * *

