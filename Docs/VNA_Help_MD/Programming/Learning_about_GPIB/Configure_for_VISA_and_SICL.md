## Configure for SCPI LAN using SICL / VISA

* * *

  * [VNA Supported Interfaces](Configure_for_VISA_and_SICL.md#Interfaces)

  * [Keysight I/O Libraries](Configure_for_VISA_and_SICL.md#IOLibraries)

  * [SICL / VISA Programs Running on the VNA](Configure_for_VISA_and_SICL.md#Progs on the PNA)

  * [Configure the VNA for SICL / VISA](Configure_for_VISA_and_SICL.md#Configure)

  * [Configure the External Controller](Configure_for_VISA_and_SICL.md#ConfigurePC)

[Other Topics about GPIB Concepts](Learning_about_GPIB.md)

### VNA Supported Interfaces

The VNA supports the following interfaces for SICL / VISA communication:

  * LAN \- as a remote GPIB interface. The VNA LAN is presented as a virtual GPIB interface. It does NOT support simple TCPIP-based control. Therefore, when configuring the Keysight IO libraries on your PC, add a REMOTE GPIB interface, which uses the LAN client interface.

  * GPIB \- requires that your external controller have a GPIB card.

Note: For optimum LAN interface performance, use
[COM](../Learning_about_COM/COM_versus_SCPI.md) to control the VNA. SCPI
commands can be sent to the VNA using the COM
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object.

The following interfaces are NOT supported:

  * USB

  * Serial

### Important Note:

To enable VISA or SICL communication over LAN, you must do the following:

  1. On the VNA, click Utility, System, System Setup..., then select Remote Interface....
  2. Check SICL Enabled. To automatically enable SICL when the VNA is booted, check Automatically enable on Startup.
  3. Click OK. 

The VNA is now ready to be controlled over LAN. [Learn more about this dialog
box](How_to_Configure_for_GPIB_SCPI_and_SICL.htm#configure).  
---  
  
### Keysight I/O Libraries

The Keysight I/O libraries includes the drivers to allow you to communicate
with Keysight test instruments. Every VNA is shipped with the Keysight I/O
libraries installed. We recommend you do NOT upgrade the Keysight I/O
libraries on the VNA as unexpected results may occur. If you choose to upgrade
the Keysight I/O libraries on the VNA, do NOT change the default folder path
in the InstallShield Wizard.

To communicate with the VNA, the Keysight I/O libraries must also be installed
on your external controller. To purchase the Keysight I/O libraries, or
download a free upgrade, go to [www.Keysight.com](http://www.Keysight.com) and
search for IO Libraries. Scroll to find Software, Firmware & Drivers.

### SICL / VISA Programs Running on the VNA

You can run your SICL / VISA program on the VNA to control the VNA. Although
the Keysight I/O libraries are already installed on the VNA, it is configured
as the Host. You must also configure a SICL or VISA LAN Client interface on
the VNA, specifying the LAN hostname of that same VNA.

If your program uses the COM interface to VISA, and is compiled on a PC with
the Keysight IO Libraries Suite (version 14 or later), and the resulting
executable is copied and run on the VNA, it will produce a type mismatch
error. This is because the VNA has the M version of Keysight I/O libraries.
The following Visual Basic code is an example of how to avoid this error when
communicating with the VNA from within the VNA:

Dim rm As IResourceManager  
Dim fmio As IFormattedIO488  
Set rm = CreateObject("AgilentRM.SRMCls")  
Set fmio = CreateObject("VISA.BasicFormattedIO")  
Set fmio.IO = rm.Open("GPIB0::22")  
fmio.WriteString "*IDN?" & Chr(10)  
MsgBox fmio.ReadString()  

### Controlling the VNA over LAN while controlling other instruments over GPIB

The VNA can NOT be both a controller and talker/listener on the same GPIB bus.
Using SICL / VISA, you can use LAN to control the VNA, leaving the VNA free to
use the rear-panel GPIB interface to control other GPIB devices.

### Configure the VNA for SICL / VISA

  1. Open the Keysight Connection Expert.

  2. Select each GPIB Interface and verify (or make) the default settings in the following table. These settings are REQUIRED when using a 82357A USB / GPIB Interface with the VNA.

  3. When complete, click Accept to close the Keysight Connection Expert.

VISA Interface Name |  SICL Interface Name |  Dialog box title |  Description  
---|---|---|---  
GPIB0 |  gpib0 |  GPIB Using NI-488.2 |  VNA Rear-panel GPIB connector. This GPIB interface can be used to control the VNA OR for the VNA to control external equipment. IT CAN NOT DO BOTH IN THE SAME PROGRAM. [Learn more about pass-through options.](How_to_Configure_for_GPIB_SCPI_and_SICL.md#configure)  
GPIB1 |  hpib7 |  Internal Instrument Configuration |  Internal interface for programs running on the VNA to control itself.  
GPIB4 |  inst0 |  Internal Instrument Configuration |  Used for [LXI compliance](../../S0_Start/LXI_Compliance.md). Do NOT delete this interface.  
  
### Configure the External Controller

Please refer to the Keysight I/O libraries documentation to learn how to
configure your controller to communicate with the VNA. These links can show
you how to find the following VNA information:

  * [VNA full computer name](../../S0_Start/ComputerProperties.md#computerName)

  * [GPIB Address](GP-IB_Fundamentals.md#address)

  * [IP Address](../../S0_Start/ComputerProperties.md#IP)

This [example program](../GPIB_Example_Programs/Establish_a_VISA_Session.md)
can help test your VISA configuration.

* * *

