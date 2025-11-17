# Set Up Receiver Leveling

* * *

The following VB Script example exercises the COM commands used to set up
Receiver Leveling.

### See Also

[About Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)

[RxLevelingConfiguration
Object](../COM_Reference/Objects/RXLevelingConfiguration_Object.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as RxLevel.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

' Demonstrate some COM commands for Receiver Leveling. Dim pna Set pna =
CreateObject("AgilentPNA835x.Application") Dim chan Set chan =
pna.ActiveChannel Dim RxLevel Set RxLevel = chan.GetRxLevelingConfiguration
Dim srcPort srcPort = 1 pna.Preset RxLevel.ReferenceReceiver(srcPort) = "R1"
RxLevel.Tolerance(srcPort)= 0.02 RxLevel.IterationNumber(srcPort)= 10
RxLevel.FastMode(srcPort)=True RxLevel.LevelingIFBW(srcPort)= 100
RxLevel.PowerOffset(srcPort)= 0 RxLevel.PowerMax(srcPort)= 20
RxLevel.PowerMin(srcPort)= -50 RxLevel.SafeMode(srcPort)= True
RxLevel.State(srcPort)= True  
---  
  
* * *

