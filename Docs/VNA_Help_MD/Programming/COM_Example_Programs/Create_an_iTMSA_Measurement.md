# Create an iTMSA Measurement

* * *

The following VB Script example shows how to create an iTMSA measurement with
Power Sweep. Click each link to see a detailed description of each command.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Testset.vbs. Learn how to setup and run the macro.

dim app 'VNA App dim meas 'Measurement dim balancemeas dim balstimulus dim
chan set app = createobject("agilentpna835x.application") set chan =
app.activechannel chan.SweepType = 2 ' Set the sweep type to power sweep set
meas = app.ActiveMeasurement set balancemeas = meas.BalancedMeasurement
balancemeas.BalancedTopology.[DUTTopology](../COM_Reference/Properties/DUTTopology_Property.md)
= 2 ' Bal-Bal topology
balancemeas.BalancedStimulus.[Mode](../COM_Reference/Properties/Mode-
iTMSA_Property.htm) = 1 ' Turn on true mode 'The PNA-X balanced port numbers
are always (0)=Bal 1; (-1)=Bal2
chan.[StartPowerEx](../COM_Reference/Properties/StartPowerEx_Property.md)(0)
= -5 ' Set the balanced port 1 start power to -5 dbm chan.StopPowerEx(0) = 5 '
Set the balanced port 1 stop power to 5 dbm chan.StartPowerEx(-1) = -10 ' Set
the balanced port 2 start power to -5 dbm chan.StopPowerEx(-1) = 0 ' Set the
balanced port 2 stop power to 5 dbm  
---  
  
* * *

