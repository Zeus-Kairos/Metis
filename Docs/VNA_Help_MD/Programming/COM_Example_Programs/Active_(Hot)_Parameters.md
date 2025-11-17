# Active (Hot) Parameters

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as <filename>.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

### See Also

[ActiveParametersApp Object](../COM_Reference/Objects/HotS22App_Object.md)

[See other COM Examples](COM_Example_Intro.md)

'Demonstration of Active Parameters setup.  
Dim app  
Set app = CreateObject("AgilentPNA835x.Application")  
app.Preset app.CreateCustomMeasurementEx 2, "Active Parameters", "IPwr"  
Set ActParam = app.ActiveChannel.CustomChannelConfiguration ActParam.SweepType
= 3 'naHOTS22MultiSweep ActParam.StartPowerIn3DSweep = -15 'Start power -15dBm  
ActParam.StopPowerIn3DSweep = 0 'Stop power 0dBm  
ActParam.PowerStepsIn3DSweep = 4 '4 steps with -15,-10,-5,0dBm
ActParam.DisplayInputPower(2) = 0 ' Set the display as the 0dBm input  
---

