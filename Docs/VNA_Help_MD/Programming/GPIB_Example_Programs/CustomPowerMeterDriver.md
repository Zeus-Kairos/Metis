# Create a Custom Power Meter Driver

* * *

This topic requires that you have a working knowledge of Visual Basic.

This topic will help you create your own power meter driver for use with
Source Power Calibration on the VNA. If you are using an Keysight Power Meter
to perform a Source Power Calibration, you do NOT need to create your own
driver.

Your Power Meter driver will be created from a template written in Visual
Basic using VISA over the GPIB bus.

Note: This procedure applies to Visual Basic 6.0. Applicability to Visual
Basic .NET has not yet been investigated.

  * [Prepare Template Files](CustomPowerMeterDriver.md#Prepare)

  * [Modify Template Files](CustomPowerMeterDriver.md#Modify)

  * [Compile, Copy, and Register, Your New Driver](CustomPowerMeterDriver.md#Compile)

  * [Test Your new Driver](CustomPowerMeterDriver.md#Test)

[Other SCPI Example Programs](SCPI_Example_Programs.md)

### Prepare Template Files

  1. Copy all the files from the VNA hard drive C:\Program Files(x86)\Keysight\Network Analyzer\Automation\Power Meter Driver Templates folder, to a folder on your development PC.

  2. In Visual Basic click File, then Open Project , find MyPowerMeter.vbp (a file you copied from the VNA). Click Open. This is a VB ActiveX EXE template, which you will fill in to become your driver.

  3. Click Project, then MyPowerMeter Properties. Click the General tab.

  4. Overwrite the Project Name with a name of your own choosing. This will be the name of your drivers type library (also the default name of your exe).

Note If the name of your exe does not match the VB Project Name with which it
was compiled, registration of the exe on the VNA will not succeed.

  5. Set the Project Description. After building your driver if you wish to test it using VB, this is the string that will show up in the VB References list of your test project, and also in the lower pane of the VB Object Browser.

  6. Set the Thread Pool size to 1 thread.

  7. Click OK to close the project properties dialog.

  8. From the VB Project menu, click References  Ensure that Keysight PNA Power Meter 1.0 Type Library and VISA Library are checked. Click OK.

Note: Keysight's implementation of VISA is installed as part of the Keysight
I/O Libraries on the VNA. For help on VISA, go to the Windows Start button on
your VNA, select Programs, Keysight IO Libraries, VISA Help.

* * *

### Modify Template Files

From Visual Basic View menu click Project Explorer. Expand the Modules and
Class Modules folders. Ensure there is one module (WinAPI) and one class
module (PowerMeter).

Let's look at the WinAPI module first.

  1. In the Project Explorer window, click WinAPI.

  2. From the View menu click Code.

There is only one line of code you should need to modify in this module: the
value of the string constant named sIDSEARCH. The comments preceding the
declaration of that string describe how to change it. The rest of this module
contains functions which will use the Microsoft Windows API to insure proper
registration of your driver on the VNA. If you know of other Windows API
functions you feel might be helpful to call from within your PowerMeter class
module (to help in formatting data, for example), this module would be the
place to declare them.

Now let's look at the class module.

  1. In the Project Explorer window, click PowerMeter.

  2. From the View menu click Properties Window. The Instancing property must be set to MultiUse. This allows other applications to create objects from this class, such that one instance of your driver EXE can supply more than one such object at a time.

  3. From the View menu click Code.

Do NOT modify the Interfaces to IPowerMeter subroutines and functions. VNA
source power cal expects to find these interfaces as they are currently
defined.

The only members that you need to supply code to are those containing Your
code here comments.

In addition, comments have been provided at the beginning of each member to
describe the information that member needs to be read from or written to the
power meter.

To get an idea of how communicate with the power meter using the VISA
functions viWrite and viRead, examine the code which has been implemented for
you in IPowerMeter_Connect, IPowerMeter_QueryMeter, and
IPowerMeter_WriteMeter.

* * *

### Compile, Copy, and Register Your New Driver

When your driver is ready to run, you will first need to compile it into an
EXE.

From the File menu select Make exe.

After compiling, the following will instruct VB to use the same ID (GUID)
every time you re-compile your project.

  1. From the Project menu, click PowerMeter Properties.

  2. On the Component tab, select Binary Compatibility and click ...

  3. Browse to and select your project EXE. Click Open.

  4. Click OK to close Project Properties.

  5. Save your project.

  6. Copy your driver EXE file to a folder on your VNA (do NOT use C:\Program Files(x86)\Keysight\Network Analyzer\Automation\Power Meter Driver Templates folder).

  7. Run the EXE file. A message box will pop up reporting whether or not registration was successful. If not successful, it will make a suggestion on what to fix.

When your driver is properly registered, VNA Source Power Cal should be able
to associate it with the ID string of your power meter.

* * *

### Test Your Power Meter Driver

We have also provided a Visual Basic project to test your new Power Meter
driver. This project individually calls every IPowerMeter method and property
in your driver to verify that it performs correctly. Before running the test
your PC and VNA must be configured to communicate using DCOM.

  1. Connect your PC and the VNA to LAN.

  2. Add your PC logon to the VNA. Both logons and password must match to communicate using DCOM. See [Additional VNA users](../../S0_Start/NewUsers.md).

  3. Configure your driver using DCOM Config on the VNA. This will give you permission to launch and access the driver. See [Configure for COM-DCOM Programming](../Learning_about_COM/Configure_for_COM-DCOM_Programming.md).

### Modify the Test Project

  1. In Visual Basic click File, then Open Project , find MyPowerMeterTest.vbp (a file you copied from the VNA). Click Open.

  2. From the Project menu, click References  From the list, find and check your new Power Meter Driver. (It should have been registered on your PC when you successfully made your driver EXE.) Click OK.

  3. From the View menu click Code.

  4. Modify the CreateObject line as follows:  
Replace MyPowerMeter with the Project Name that you chose for your driver  
Replace MyPNA with the Computer Name of your VNA.  
For example:

Set PowerMeterObj = CreateObject("AcmeBrand.PowerMeter", "AGILENT-PNA123")

(This assumes that you kept PowerMeter as class module name in your driver.)

### Run the Test Project

Ensure your power meter is connected to the VNA with a GPIB cable.

Put the VNA in system controller mode:

  1. From the VNA System menu point to Configure then click SICL/GPIB.

  2. In the GPIB box click System Controller.

Run the test project. If there are no errors, the driver is created
successfully. If there are errors, try to figure out what went wrong and fix
it. Then re-compile, re-copy the .exe to the VNA, and re-run the test. You
should not need to re-register the driver or re-modify the test program.

