# VNA User Accounts and Passwords

* * *

Important: When the VNA power is switched on, it AUTOMATICALLY logs into
Windows using the default user name and password. You do NOT need to log on.
This gives anyone full access to the analyzer. The following steps can be
taken to increase security of your VNA.

  * Require users to logon when the VNA computer is turned ON - [Learn how.](NewUsers.md#HowtoRequireLogon)

  * Setup individual accounts on the VNA with varying level of access - [Learn how](NewUsers.md#AddAccounts).

See Also: [User-Specific VNA Settings](NewUsers.md#User-Specific_Settings)

Please read about Anti-virus protection for your VNA

## Existing User Accounts

The following user accounts already exist on new VNAs.

Important: For the highest security, it is recommended to change the passwords
on your device from these defaults.

User Name |  Password |  Type |  Description  
---|---|---|---  
Instrument |  measure4u |  Administrator |  Auto Log On is activated by default.  
KeysightOnly |  (Contact Keysight) |  Administrator for Service |  For user maintenance purpose.  
  
Note: The user name is not case sensitive. The password is case sensitive.

Note: The VNA local policies are set so that, if logon is required, you must
retype the user name (and password) every time. Do not change the local
policies on the VNA.

## Add or Change User Accounts, Passwords, and require Logon

If the analyzer is in a secure environment, you can setup VNA users by name
and grant various levels of access.

You can designate a person as the administrator and then configure the VNA to
allow others to use it with reduced permissions. That is, other people can be
signed on to use the analyzer but they will not have the ability to perform
all of the administrative functions that you can as the administrator.

The following are examples of some of the functions that can be performed with
these account types:

  * Administrator \- Can download and install firmware. The administrator can modify system-wide settings in the operating system.

  * Standard User \- Can fully use the VNA to make measurements and save state and data files. Standard Users can NOT install firmware.

### How to add a user account and require logon

Windows OS  
---  
To add a new account:  
Click Start > Settings > Accounts > Other people > Add someone else to this
PC.  
Enter the requested information then select Next.  
To change an existing account:  
Click on the user account.  
Click Change account type.  
Under Account type, select Standard User or Administrator.  
Click OK.  
  
### User-Specific VNA Settings

Almost all persistent settings in the VNA are global (apply to all users).

The following exceptions reset to their defaults when a new user account is
setup:

  * [Global PassFail Display State](../S4_Collect/Use_Limits_to_Test_Devices.md#PASS)
  * Recently used files list
  * [Global Power Limits](../System/Power_Limit_and_Power_Offset.md)
  * [Equation Editor](../S4_Collect/Equation_Editor_Import_Functions.md)  most recently used import dlls
  * [Preferences:](../System/Preferences.md)
  *     * Power Sweep Retrace Mode
    * Is Power On During Retrace

* * *

