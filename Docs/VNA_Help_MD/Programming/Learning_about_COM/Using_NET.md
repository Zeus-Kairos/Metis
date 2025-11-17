# Using COM from .NET

* * *

To communicate with the VNA from Microsoft .NET enabled languages such as C#
and Visual Basic.NET perform the following steps:

  1. [Configure your PC and VNA for COM-DCOM Programming](Configure_for_COM-DCOM_Programming.md).

  2. Reference the type library within the development environment (see the following [exception for managed C++ projects](Using_NET.md#Exception).) In the process of referencing the type library, a .NET assembly is created that wraps the VNA type library with a .NET friendly interface. This .NET assembly is called an Interop Assembly.

Note: ONLY 32-bit compiler option is supported (64-bit is NOT supported).

Exception for managed C++ projects: To generate the Interop Assembly for
managed C++ projects, you must use the tlbimp.exe utility. This utility is
described in the MSDN documentation. On your PC, click Start then Run then
type: tlbimp.exe 835x.tlb and click OK. After doing this you can use the
#using directive to include the Interop Assembly on managed C++ projects.

### Example: Creating a .NET object from C#

The following is an example that shows how to create a .NET object that
connects to the VNA over DCOM. In this example, machineName is either the DNS
name or the IP address of the VNA to connect with.

Type pna = Type.GetTypeFromProgID("AgilentPNA835x.Application", machineName);

AgilentPNA835x.IApplication app =
(AgilentPNA835x.IApplication)Activator.CreateInstance(pna);

### See C# Example Programs:

[Perform a Guided Cal with
C#](../COM_Example_Programs/Perform_a_Guided_Cal_with_CSharp.htm)

[Using C#](../COM_Example_Programs/Using_CSharp.md)

### Registering the VNA Primary Interop Assembly (PIA) (OPTIONAL)

The PIA is NOT necessary to communicate with the VNA. The following procedure
is useful only when there are two .NET programs that want to share the same
VNA interface definitions. Without the PIA, each .NET application would use
its own Interop Assembly.

To register the PIA on a machine, you need to have the common language runtime
(CLR) installed. This is included with Visual Studio.NET. Then perform the
following steps:

Note: In the following steps, replace <local directory> with the full path
name of the specified file on your PC.

  1. Run the PNAProxy.exe program as described in [Configure for COM-DCOM Programming](Configure_for_COM-DCOM_Programming.md).

  2. On the VNA, copy C:/Program Files/Keysight/Network Analyzer/Automation/AgilentPNA835x.dll to a local directory on your PC. Make a note of this directory.

  3. On your PC, click Start, then Run, then type: regasm <local directory> /AgilentPNA835x.dll and click OK to register the dll.

  4. Again, click Start, then Run, then type: gacutil /i <local directory> /AgilentPNA835x.dll and click OK to add the assembly to the Global Assembly Cache (GAC).

To Uninstall the PIA, perform the following:

  1. On your PC, click Start, then Run, then type: gacutil /u <local directory> /AgilentPNA835x.exe and click OK to remove the assembly from the GAC.

  2. On your PC, click Start, then Run, then type: regasm /unregsiter <local directory> / agilentpna835x.dll and click OK to unregister the assembly.

  3. To uninstall PNA Proxy.exe use the Add/Remove Programs utility in the control panel.

* * *

