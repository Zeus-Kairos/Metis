# Create and Cal a Noise Figure Measurement

* * *

This example program creates a Noise Figure measurement, then calibrates the
measurement.

You MUST change the ECal Identification strings (in Blue font).

Optional: Uncomment the following lines (in Blue font) to change these
settings:

  * Noise Receiver = Noise Receiver to Std (VNA) Receiver

  * Cal Method = "Vector" to "Scalar"

  * Receiver Characterization Method = "NoiseSource" to "Power Meter"

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Noise.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

### See Also

[NoiseFigure Object.](../COM_Reference/Objects/NoiseFigure_Object.md)

[Accessing the NoiseFigure object and NoiseCal object using
C#](Create_and_Cal_a_NoiseFigure_Measurement.htm#Bonus)

[See other COM Examples](COM_Example_Intro.md)

windowNum = 1 channelNum = 1 set
pna=CreateObject("AgilentPNA835x.Application") set scpi = pna.ScpiStringParser
pna.reset ' Create noise figure measurement set noise =
pna.createcustommeasurementex(channelNum, "NoiseFigure", "NF", windowNum) set
noisechan = pna.activechannel ' Create object to access noise-specific channel
attributes set noiseConfig = pna.activechannel.CustomChannelConfiguration '
Create guided noise calibration object on our channel set noisecal =
pna.GetCalmanager.CreateCustomCalEx(channelNum) set noiseCalExtension =
noisecal.CustomCalConfiguration noiseCalExtension.NoiseSourceCold = 300 '
Substitute appropriate ECal identification strings here tunerEcal =
"N4691-60004 ECal 02821" pullEcal = "N4691-60004 ECal 02297" ' configuration
ConfigureChannel ConfigureNoiseSettings ' perform calibration
SetupCalAttributes_Insertable SetupNoiseSource FinishCalibration ' \-----
Support subroutines ------ ' Configure noise channel sub ConfigureChannel
noisechan.startfrequency = 500e6 noisechan.stopfrequency = 5.0e9
noisechan.numberofpoints = 201 noisechan.IFBandwidth = 1.0E3 end sub '
Configure noise-specific channel settings sub ConfigureNoiseSettings
noiseConfig.NoiseReceiver = 1 'Noise Receiver ' noiseConfig.NoiseReceiver = 0
'Std VNA Receiver noiseConfig.noiseaveragestate = true
noiseConfig.NoiseAverageFactor = 40 noiseConfig.NoiseTuner = tunerEcal
noiseConfig.NoiseTunerIn = "B" noiseConfig.NoiseTunerOut = "A"
noiseConfig.NoiseBandwidth = 8e6 end sub sub SetupCalAttributes_Insertable
noisecal.Initialize channelNum, true noisecal.ConnectorType( 1 ) = "APC 3.5
female" noisecal.ConnectorType( 2 ) = "APC 3.5 male" noisecal.CalKitType (1) =
pullEcal noisecal.CalKitType (2) = pullEcal
noiseCalExtension.NoiseSourceConnectorType = "APC 3.5 male"
noiseCalExtension.NoiseSourceCalKitType = pullEcal noiseCalExtension.CalMethod
= "Vector" ' noiseCalExtension.CalMethod = "Scalar"
noiseCalExtension.RcvCharMethod = "NoiseSource" 'Can NOT be used with Std VNA
Rcvr ' noiseCalExtension.RcvCharMethod = "PowerMeter" end sub sub
SetupNoiseSource ' specify the ENR file for the noise source
noiseCalExtension.ENRFile = "c:\users\public\network
analyzer\documents/346C_MY44420454.enr" noiseCalExtension.NoiseSourceCold =
301.1 end sub ' Build the connection list and acquire the calibration sub
FinishCalibration steps = noisecal.GenerateSteps for i = 1 to steps str =
noisecal.GetStepDescription( i ) msgbox str noisecal.AcquireStep i next guid =
noisecal.GenerateErrorTerms wscript.echo "Calibration created calset guid:
",guid end sub  
---  
  
### Bonus: Accessing the NoiseFigure object and NoiseCal object using C#

Replace <hostname> with the full computer name of your VNA

Type pna = Type.GetTypeFromProgID("AgilentPNA835x.Application", "<hostname>");
AgilentPNA835x.Application app =
(AgilentPNA835x.Application)Activator.CreateInstance(pna); app.Reset();
app.CreateCustomMeasurementEx(1, "NoiseFigure", "NF", 1);
AgilentPNA835x.ICalManager5 calManager =
(AgilentPNA835x.ICalManager5)app.GetCalManager();
AgilentPNA835x.IGuidedCalibration4 guidedCal4 =
(AgilentPNA835x.IGuidedCalibration4) calManager.CreateCustomCalEx(1);
AgilentPNA835x.INoiseCal noiseCal =
(AgilentPNA835x.INoiseCal)guidedCal4.CustomCalConfiguration;  
---  
  
* * *

  

