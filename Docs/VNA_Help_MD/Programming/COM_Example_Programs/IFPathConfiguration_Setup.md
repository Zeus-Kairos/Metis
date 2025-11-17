# IFPathConfiguration Setup

* * *

The following demonstrates how to:

  * Set the Source 1 Pulse Mod to enable

  * Set the Source 2 Pulse Mod to disable. In effect, this sets Source 2 to 'CW' (or OFF)

  * Set the Pulse Mod drive to Pulse1

[See the entire list of IF Path Configuration
settings](../../IFAccess/IF_Path_Configuration.htm#elements).

' Create / Get the VNA application Dim app Set app =
CreateObject("AgilentPNA835x.Application") ' Preset the instrument app.Preset
' Get a channel interface on which to operate Dim chan Set chan =
app.ActiveChannel ' Set the Source 1 Pulse Mod to enable
chan.PathConfiguration.Element("Src1Out1PulseModEnable").Value = "Enable" '
Set the Source 2 Pulse Mod to disable
chan.PathConfiguration.Element("Src2Out1PulseModEnable").Value = "Disable" '
Set the Pulse Mod drive to Pulse1
chan.PathConfiguration.Element("PulseModDrive").Value = "Pulse1"  
---

