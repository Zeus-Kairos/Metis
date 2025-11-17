# Set Up Noise Figure Port Mapping

* * *

This program demonstrates how to change source and receive ports when
measuring noise figure. It assumes that option 029 ("Fully Corrected Noise
Figure") is installed.

If only option 028 ("Noise figure measurements using standard receivers") is
installed, switching ports is simpler, since only one noise receiver selection
is available.

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as NF.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

### See Also

[Noise Figure Object](../COM_Reference/Objects/NoiseFigure_Object.md)

[Create and Cal a NoiseFigure
Measurement](Create_and_Cal_a_NoiseFigure_Measurement.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

option explicit ' Noise receiver enumerations dim naStandardReceiver,
naNoiseReceiver ' standard VNA receiver naStandardReceiver = 0  ' dedicated
noise receiver (option 029 only) naNoiseReceiver = 1 dim pna, windowNum,
channelNum set pna = CreateObject("Agilentpna835x.application") windowNum = 1
channelNum = 1 pna.Reset ' Create Noise Figure measurement dim
noise,noiseChan,noiseConfig set noise =
pna.CreateCustomMeasurementEx(channelNum, "Noise Figure Cold Source", "NF",
windowNum) set noiseChan = pna.ActiveChannel ' provides access to noise-
specific channel properties set noiseConfig =
noiseChan.CustomChannelConfiguration  'To change from the default input/output
port settings of ' source port = VNA1, receive port = VNA2, ' you must first
change the noise receiver, ' then select the desired ports. dim srcPort,
rcvPort ' set port mapping to source port = VNA3, receive port = VNA4 srcPort
= 3 rcvPort = 4 ' use VNA receiver for noise measurements
noiseConfig.NoiseReceiver = naStandardReceiver  noiseConfig.SetPortMap
srcPort, rcvPort ' To revert back to using the noise receiver, the source '
and receive ports must be set to their default values ' BEFORE switching to
the noise receiver.  ' Otherwise, a COM exception will be thrown. ' restore
defaults: source=VNA1, receiver=VNA2 noiseConfig.SetPortMap 1,2  ' use
dedicated noise receiver for noise measurements noiseConfig.NoiseReceiver =
naNoiseReceiver  
---

