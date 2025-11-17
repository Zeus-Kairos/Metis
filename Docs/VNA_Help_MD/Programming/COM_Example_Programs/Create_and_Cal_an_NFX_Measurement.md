# Create and Cal an NFX Measurement

* * *

This program does the following:

  * Setup a Noise Figure SC21 Measurement

  * Calibrate Noise Figure channel

  * Optional - Configure for an Embedded LO

To run this program, make the following edits, highlighted in yellow:

  * Set host to your VNA computer name

  * Set tunerECal and pullECal to your ECal model and info

  * Set ENR to correct file name and location

  * Set connector types for ECal, power sensor, and noise source

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as NFX.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

### See Also

[CreateCustomMeasEX
command](../COM_Reference/Methods/CreateCustomMeasurementEx_Method.htm)

[NoiseFigure Object](../COM_Reference/Objects/NoiseFigure_Object.md)

[NoiseCal Object](../COM_Reference/Objects/NoiseCal_Object.md)

[Converter_Object](../COM_Reference/Objects/Converter_Object.md)

[GuidedCal Object](../COM_Reference/Objects/GuidedCalibration_Object.md)

[EmbeddedLO Object](../COM_Reference/Objects/EmbeddedLO_Object.md)

### Learn About...

[Noise Figure on
Converters](../../Applications/Noise_Figure_on_Converters.htm)

[Noise Cal](../../Applications/Noise_Cal.md)

[See other COM Examples](COM_Example_Intro.md)

option explicit 'NFx sweep type ' naLinearSweep = 0 ' naCWTimeSweep = 2
'Converter sweep mode ' naSwept = 0 ' naFixed = 1 'Embedded LO tuning mode '
Broadband and precise = 0 ' Precise only = 1 ' None = 2 dim app dim chan dim
nfx dim host host = "MyPNA" set app =
CreateObject("Agilentpna835x.application", host) app.reset call SetupNFX
'optional if not doing embedded LO 'call SetupEmbeddedLO call CalNFX sub
SetupNFX dim tunerEcal tunerECal = "N4691-60003 ECal 00591" ' create NFX
traces app.CreateCustomMeasurementEx 1, "Noise Figure Converters", "NF", 1
app.CreateCustomMeasurementEx 1, "Noise Figure Converters", "SC21", 1 'set
channel and application objects set chan = app.ActiveChannel set nfx =
chan.CustomChannelConfiguration dim converter set converter =
chan.GetConverter() ' Set channel properties chan.single 1 chan.sweeptype = 0
'naLinearSweep chan.numberofpoints = 201 chan.IFBandwidth = 1.e3 ' Set nfx
properties nfx.noiseaveragestate = true nfx.noiseaveragefactor = 10
nfx.noisetuner = tunerECal nfx.NoiseTunerIn = "B" nfx.NoiseTunerOut = "A"
nfx.NoiseBandwidth = 8e6 nfx.noisegain = 0 'low ' converter properties
converter.InputRangeMode = 0 ' swept converter.LORangeMode(1) = 1 'fixed
converter.OutputRangeMode = 0 'swept converter.InputStartFrequency = 8.0e8
converter.InputStopFrequency = 3.0e8 converter.LOFixedFrequency(1) = 1.5825e10
converter.LOPower(1) = -10 converter.Calculate 2 'calculateOutput
converter.LOName(1) = "Port 3" converter.Apply chan.Single 1 end sub sub
CalNFX ' Set ecal and noise tuner dim SparamECal SparamECal = "N4693-60001
User 2 ECal 00012" chan.single 1 dim calMgr set calMgr = app.GetCalManager dim
nfxCal set nfxCal = CalMgr.CreateCustomCalEx(1) dim nfxCalExt set nfxCalExt =
nfxCal.CustomCalConfiguration nfxCalExt.ENRFile = "C:\Program
Files(x86)\Keysight\Network Analyzer\Noise\346C_44420601.enr" 'setup
calibration nfxCal.Initialize 1, true 'dut connector nfxCal.ConnectorType(1) =
"APC 3.5 female" nfxCal.ConnectorType(2) = "APC 3.5 female"
nfxCal.CalKitType(1) = SparamECal nfxCal.CalKitType(2) = SparamECal 'power
sensor connector nfxCal.PowerCalibrationPowerLevel(1) = -20
nfxCal.PowerSensorConnectorType(2) = "APC 3.5 male"
nfxCal.PowerSensorCalkitType(2) = SparamECal 'noise source connector
nfxCalExt.NoiseSourceConnectorType = "APC 3.5 male"
nfxCalExt.NoiseSourceCalKitType = SparamECal nfxCalExt.CalMethod = "Vector"
nfxCalExt.EnableLOPowerCal(1) = False nfxCalExt.ForceDeEmbedENRAdapter = False
nfxCalExt. ForceDeEmbedSensorAdapter = False 'step through calsteps dim steps
steps = nfxcal.GenerateSteps dim i , str for i = 1 to steps str =
nfxcal.GetStepDescription(i) msgbox str nfxcal.AcquireStep i next dim guid
guid = nfxcal.generateerrorterms wscript.echo "Calibration created calset
guid: ", guid chan.continuous end sub sub SetupEmbeddedLO ' Set embedded LO
properties dim ELO set ELO = converter.ConverterEmbeddedLO ELO.NormalizePoint
= 101 ELO.TuningMode = 0 ' Broadband and precise ELO. TuningIFBW = 3.0e4
ELO.MaxPreciseTuningIterations = 5 ELO.PreciseTuningTolerance = 1
ELO.TuningSweepInterval = 1 ELO.IsOn = true chan.Single 1 end sub  
---  
  
* * *

