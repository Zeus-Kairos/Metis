# Configure for COM-DCOM Programming

* * *

Before developing or running a COM program, you should first establish
communication between your PC and the analyzer. This process is referred to as
gaining Access to the analyzer. You should then register the VNA type library
on your PC.

DCOM (Distributed Component Object Model) refers to accessing the VNA from a
remote PC.

COM refers to accessing the VNA application from the analyzer PC.

  * [Access Concepts](Configure_for_COM-DCOM_Programming.md#Concepts)

  * [Access Procedures](Configure_for_COM-DCOM_Programming.md#Procedure)

  * [Register the VNA Type Library on Your PC](Configure_for_COM-DCOM_Programming.md#Register)

  * [Problems?](Configure_for_COM-DCOM_Programming.md#Problems)

Note: After performing a [Firmware Upgrade](../../Support/FW_upgrade.md) you
must copy the new type library to your development PC to get access to new COM
commands. See Register the analyzer on your PC.

[Other Topics about COM Concepts](Learning_about_COM.md)

Note: 64-bit compiler option is supported.

Access Concepts

VNAs are shipped from the factory such that Everyone has permission to launch
and access the VNA application via COM/DCOM. The term Everyone refers to a
different range of users depending on whether the VNA is a member of a Domain
or Workgroup (it must be one or the other; not both). By default, the VNA is
configured as members of a workgroup. Therefore, Everyone includes only those
users who have been given logon accounts on the VNA.

### Workgroup

A workgroup is established by the VNA administrator declaring the workgroup
name and declaring the VNA as a member of the workgroup. A workgroup does not
require a network administrator to create it or control membership.

Everyone includes only those users who have been given logon accounts on the
VNA.

By default, the VNA is configured as members of a workgroup named WORKGROUP.

Note: To setup a logon account for a new user, see [Additional
Users](../../S0_Start/NewUsers.htm).  
The easiest method of gaining DCOM access, is to make the user's account name
and password on the VNA to EXACTLY match their PC logon account name and
password.

### Domain

A domain is typically a large organizational group of computers. Network
administrators maintain the domain and control which machines have membership
in it.

Everyone includes those people who have membership in the domain. In addition,
those with logon accounts can also access the analyzer.

### Summary

  * A Workgroup requires no maintenance, but allows DCOM access to only those users with a log-on account for the VNA.

  * A Domain requires an administrator, but all members of the domain and those with logons to the analyzer are allowed DCOM access to the VNA.

The following section "Access Procedures" provides a tighter level of security
allowing only selected (not Everyone) domain and workgroup users DCOM Access
and Launch capability of the VNA.

Access Procedures

Perform this procedure for the following reasons:

  * To allow only selected users (not everyone) remote Access and remote Launch capability to the VNA. Launch capability is starting the VNA application if it is not already open.

  * To verify that you have DCOM access to the analyzer.

Note: Before doing this procedure, you must first have a logon account on the
VNA. See [VNA User Accounts](../../S0_Start/NewUsers.md)

The following procedure grants specific users DCOM access and launch
capability of the VNA application:

To perform this procedure, you must first [minimize the
VNA](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#Minimize)
application.

[How do I know which Operating System I
have?](../../S0_Start/Windows_Considerations.htm)

Windows 7  
---  
On the VNA, click the Windows Start button  
In the Search programs and files text field, type cmd then press Enter  
In the cmd: window, type dcomcnfg  
Open the following folder sequence: Component Services Computers My Computer
DCOM Config Right click Keysight PNA Series Click Properties  
Click the Security tab  
Under Access Permissions, click Customize, then click Edit  
Select Everyone, then click Remove  
Click Add  
Type a group name or user account name  
Click OK  
Under Launch Permissions, click Customize, then click Edit  
Select Everyone, then click Remove  
Click Add  
Type a group name or user account name  
Click OK  
  
Windows 10  
---  
On the VNA, click the Type here to search icon  
In the Type here to search text field, type cmd then press Enter  
In the cmd: window, type dcomcnfg  
Open the following folder sequence: Component Services Computers My Computer
DCOM Config Right click Keysight PNA Series Click Properties  
Click the Security tab  
Under Access Permissions, click Customize, then click Edit  
Select Everyone, then click Remove  
Click Add  
Type a group name or user account name  
Click OK  
Under Launch and Activation Permissions, click Customize, then click Edit  
Select Everyone, then click Remove  
Click Add  
Type a group name or user account name  
Click OK  
  
Register the VNA Type Library on Your PC

The type library contains the VNA object model. On your PC, there is a
Registry file that keeps track of where object models are located. Therefore,
you must register the type library on the PC that will be used to develop code
and run the program. It is much more efficient to have the type library
registered at design time (BEFORE running your COM program).

Do the following two items before proceeding:

  1. Connect your PC and the VNA to LAN.

  2. Either map a drive to the analyzer or copy the type library files on a floppy disk or other media. See [Drive Mapping.](../../S5_Output/Drive_Mapping.md)

Note: To register the type library on your PC, you must be logged on as an
administrator of your PC. Learn about [User
Accounts.](../../S0_Start/NewUsers.htm)

This procedure will do the following:

  * Register the Network Analyzer application on your PC.

  * Copy and register the proxystub (835xps.DLL) onto the PC.

  * Copy and register the VNA type library (835x.tlb) onto the PC.

  * Copy and register the FCA type library (fca.tlb) onto the PC.

  1. Using Windows Explorer on your PC, find the Analyzer's C: drive. The drive will not be named "C:" on your PC, but a letter you assigned when mapping the drive.

  2. Navigate to Program Files / Keysight / Network Analyzer / Automation

  3. Double-click pnaproxy.exe and follow the prompts to Install PNA Proxy. If the installation offers a choice of Modify, Repair, or Remove, then select Remove. Then double-click on pnaproxy.exe again.

  4. When prompted, type the Computer name of the VNA ([Learn how to find this](../../S0_Start/ComputerProperties.md#computerName)).

  5. After the install program runs, the VNA and FCA type library should be registered on your PC.

  6. Your programming environment may require you to set a reference to the VNA type library now located on your PC. In Visual Basic, click Project, References. Then browse to C:/Program Files/Common Files/Keysight/PNA Select 835x.tlb

### Problems?

  * These procedures will fail if there are any programs using the VNA type library (for example: Visual basic, VEE, Visual Studio, or any other application program that may communicate with the VNA).

  * Perform the following procedure if the previous procedure did not return an error, but you cannot connect to the VNA.

  * If you received an error, check that both the account name and password used on both the VNA and PC match EXACTLY.

  1. [Map a drive](../../S5_Output/Drive_Mapping.md) from your remote PC to the VNA. Note the drive letter your PC assigns to the VNA.  
Substitute this drive letter for VNA in the following procedure.

  2. On your PC, go to a DOS prompt c:>

  3. Type PNA: (for example o:)

  4. Type cd program files/Keysight/network analyzer/automation

  5. Type copy 835xps.dll c:/program files/common files/Keysight/pna

  6. Type copy 835x.tlb c:/program files/common files/Keysight/pna

If you will NOT be using [FCA commands](../../FreqOffset/FCA_Use.md), skip
steps 7,.8, and 9.

  7. Type cd..

  8. Type cd extensions/fca

  9. Type copy fca.tlb c:/program files/common files/Keysight/pna

  10. If it is not already there, copy regtlib.exe from PNA:/WINNT to your C:/<windows>/system32 directory (<windows> is OS-dependent- it is either windows or WINNT)

  11. Type regtlib C:/program files/common files/Keysight/pna/835x.tlb

  12. Type regsvr32 C:/program files/common files/Keysight/pna/835xps.dll

  13. Type regtlib C:/program files/common files/Keysight/pna/fca.tlb

Perform the [Access Procedure](Configure_for_COM-
DCOM_Programming.htm#Procedure) after doing these steps.

* * *

