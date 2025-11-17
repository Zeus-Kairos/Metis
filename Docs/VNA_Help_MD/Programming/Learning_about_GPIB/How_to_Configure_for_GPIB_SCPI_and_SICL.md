# Configure for GPIB, SCPI, and SICL

* * *

The following settings are used to configure the analyzer for remote control
using SCPI commands.

#### How to Configure for SICL / GPIB Operation  
  
---  
Using Hardkey/SoftTab/Softkey |  Using a mouse  
  
  1. Press System > System Setup > Remote Interface....

|

  1. Click Utility
  2. Select System
  3. Select System Setup
  4. Select Remote Interface...

  
[![](../../assets/images/SeeProg.gif)](../CF_System_Commands.md#System_Setup_Tab_Commands)  
  
Remote Interface dialog box help  
---  
![](../../assets/images/RemoteInterfaceDialog1.png)

### GPIB

Use the National Instruments interface or the ACE (Keysight Connection Expert)
interface to change the System Controller address. Use the VNA as the system
controller of external devices. Learn about the [VNA as controller.](GP-
IB_Fundamentals.htm#cont) See the rear panel of the
[VNA-X](../../Rear_Panel/XRtour.md) and N522x models.

### SICL

SICL Enabled When checked, the analyzer is capable of running GPIB programs on
its computer to control analyzer functions. The programs must be run from a
GPIB-capable programming environment (VEE, Visual Basic). This mode does not
allow control of external GPIB instruments. To uncheck this box, exit the VNA
application - (Click File, then Exit). The VNA restarts with the SICL enabled
box unchecked unless Automatically Enable on Startup is checked. Learn more
about  Note: When SICL Enabled is checked, the VNA VXI-11.2 interface is
enabled, and if the VNA hard disk image is new enough to have the VXI-11.3
interface, it also enables that. . Address Sets the VNA address. Automatically
Enable on Startup When checked, SICL Enabled is automatically selected when
starting the VNA application.

### LAN Sockets/Telnet

Provides ability to communicate with the VNA from a PC that uses a Windows, or
non-Windows, operating system.

  * These settings are checked by default. If you have security concerns, clear these check boxes.
  * These settings remain after the VNA is shutdown and restarted.

Sockets Enabled When checked, provides the ability to control the VNA from a
remote SCPI program using port number 5025. [See the C# example that
illustrates how this is done.](../GPIB_Example_Programs/Socket_Client.htm)
Telnet Enabled When checked, provides the ability to send single SCPI commands
from a remote Windows, or non-Windows, PC to the VNA using port number 5024.
How to send single SCPI commands using Telnet:

  1. On the remote PC, click Start, then type cmd in the Search programs and files text field.
  2. Type: telnet <computer name> 5024  
where <computer name> is the full computer name of the VNA.

  3. A Telnet window with a SCPI> prompt should appear on the remote PC screen.
  4. From the SCPI prompt:

  1.      * Type single SCPI commands
     * If an invalid SCPI command is sent, the prompt will disappear. Press Enter or Ctrl C to recover the SCPI prompt.
     * To exit the telnet window click X in the upper-right corner.
     * To get a normal telnet prompt, press Ctrl ] (closing bracket).
     * To close the normal telnet window, type Quit and press Enter.

### HiSLIP

HiSLIP has the same functionality as VXI 11 (SICL) with better performance.
Therefore, it is enabled by default on the analyzer. Address 0 by default. No
change is necessary. On the remote computer, use address string
TCPIP0::<hostname>::hislip<address>. ("hislip" is case-sensitive).

### Security

Enable Remote Drive Access When checked allows access to the hard disk. The
default is unchecked. When unchecked, hard disk access is blocked and any of
the following commands will return an error: MMEM:CAT:FILE? MMEM:CAT:STAT?
MMEM:CAT:CSTAte? MMEM:CAT:CSARchive? MMEM:CAT:CORRection? MMEM:CDIR? MMEM:COPY
MMEM:DELete MMEM:MOVE MMEM:MDIRectory MMEM:RDIRectory MMEM:TRANsfer[?]
SYST:SHORcut:EXECute

### SCPI Monitor / Input

Show SCPI Parser Console Launches a window that is used to send single
SCPI/GPIB commands from the analyzer keyboard. This window can also be used to
capture the SCPI traffic used over HiSLIP. (See also, [SCPI Parser
Console](../SCPIParserConsole.htm).)

  * Type a valid command, with appropriate arguments and press enter.
  * Use the arrow keys to recall previous commands.

IO Monitor enables monitoring activity on the remote control.
![](../../assets/images/iomonitor.png) Clicking on the Configure button
accesses the IO Monitor Configuration dialog to enable/disable this function.
![](../../assets/images/iomonitorconfig.png) Enabling the IO monitor provides
detailed error message with debug information.

#### Example of Error message:

  * On: -109, "Missing parameter; calc:par:def aaa<Err>
  * Off: -109, "Missing parameter"

Disabling the IO monitor increases measurement speed.  
  
* * *

