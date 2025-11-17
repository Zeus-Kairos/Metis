# Drive Mapping

* * *

Drive mapping allows you to share disk drives between the VNA and an external
computer.

To prepare for Drive Mapping:

  1. Both the PC and VNA must be connected to a shared computer network

  2. You must know the full computer name of the Analyzer you are mapping TO. [Tell me how](javascript:TextPopup\(this\))

On the PC you are mapping TO

     1.         1. Click System, Windows Taskbar, Settings, Control Panel, and the System icon.

        2. Select the Network Identification tab. If desired, record the computer name

Note: This procedure requires a mouse and keyboard.

Map to a drive on the VNA from an External PC

  1. On the analyzer desktop, click Windows Explorer. Right-click on the drive you want to share. Click Sharing...

  2. In the dialog box, select Shared this folder. In the Share Name box, type in a share name for the drive. For example: C$. Click OK.

  3. On the external PC desktop, click Windows Explorer. From the Tools menu, click Map Network Drive.

  4. If the current logon on your PC is different from the current logon on the analyzer, click Connect using a different Logon to connect to using the current analyzer logon, .This logon must be registered on the external PC. To see the current logon on either the PC or analyzer, hold Ctrl \- Alt, and press Delete.

     1. In the Connect as box, type the logon currently being used by the analyzer.

     2. In the Password box, type the logon password that you use on the external computer. Click OK

  5. In the Folder box, type //computername ([prep1](Drive_Mapping.md#prep1))/share name (from step 2). (For example: //SLT1234/C$ )

  6. Click Finish.

* * *

