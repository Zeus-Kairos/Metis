# External Testset Control

* * *

The following VB Script example exercises the COM commands used to control the
Z5623AK64 testset.

For a description of each command, see [TestsetControl
Object](../COM_Reference/Objects/TestsetControl_Object.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Testset.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

' Demonstrate some COM commands for external testsets. Dim pna Set pna =
CreateObject("AgilentPNA835x.Application") Sub DemoTestset(na) Dim testsets,
tset1 Dim portNum Dim chNum, address Set testsets = na.ExternalTestsets chNum
= 1 ' Load a configuration file. ' NOTE: the K64 testset is only compatible
with 4-port analyzers. address = 0 testsets.Add "Z5623AK64", address ' Get the
testset object ' in the testsets collection. Set tset1 = testsets(1) ' Show
the selections available for each port. For portNum = 1 To 4 MsgBox("Port " &
CStr(portNum) & " catalog: " & tset1.PortCatalog(portNum)) Next ' Set port
mappings on channel 1. tset1.OutputPorts(chNum) = "5 ext R,2 int R,3 int R,6
int R" ' Set control lines. tset1.ControlLines(chNum) = 85 ' Set label.
tset1.Label(chNum) = "Some label" ' Enable external testset control. This
automatically enables status bar display as well. tset1.Enabled = True End Sub
' The testset used in this demo is only usable on 4-port analyzers If
(pna.NumberOfPorts <> 4) Then MsgBox("This program only runs on 4-port
analyzers.") Else DemoTestset(pna) End If  
---

