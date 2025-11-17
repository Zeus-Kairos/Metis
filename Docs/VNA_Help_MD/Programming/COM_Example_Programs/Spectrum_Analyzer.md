# Spectrum Analyzer

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SA.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

### See Also

[Spectrum Analyzer
Object](../COM_Reference/Objects/SpectrumAnalyzer_Object.htm)

[See other COM Examples](COM_Example_Intro.md)

' Demonstration of basic Spectrum Analyzer measurement setup using COM. set
pna=CreateObject("AgilentVNA835x.Application","hostname") set channel =
Nothing set sachannel = CreateSAMeasurement(pna) SetupLinearSweep(sachannel)
ConfigureAdvancedSettings(sachannel) ' Create a Spectrum Analyzer measurement.
' Return the custom SA channel object. Function CreateSAMeasurement(pna) '
Create a B measurement on channel 1 pna.Channels.RemoveChannelNumber(1) call
pna.CreateCustomMeasurementEx(1,"Spectrum Analyzer","B") set channel =
pna.Channels(1) set sachannel = channel.CustomChannelConfiguration set
CreateSAMeasurement = sachannel ' Set frequency range channel.centerFrequency
= 3.0E9 channel.FrequencySpan = 2.0E9 ' Center frequency step size ' Set to
Auto mode with CenterFrequencyStepSizeMode = naMANUAL|naAUTO
channel.CenterFrequencyStepSize = 20E6 ' RBW filter shape ' Choices are: ' 0 -
naNoWindow ' 1 - naWindowFlatTop ' 2 - naWindowGaussian ' 3 - naWindowBlackman
' 4 - naWindowKaiser sachannel.BandwidthShape = 4 ' naWindowKaiser ' Detector
type ' Choices are: ' 0 - naDTAverage ' 1 - naDTSample ' 2 - naDTPeak ' 3 -
naDTNormal ' 4 - naDTNegPeak ' 5 - naDTPeakSample ' 6 - naDTPeakAverage
sachannel.DetectorFunction = 2 ' naDTPeak ' Video averaging type ' Choices
are: ' 0 - naPower ' 1 - naLog ' 2 - naVoltage ' 3 - naVoltageMax ' 4 -
naVoltageMin sachannel.VideoAveragingType = 3 ' naVoltageMax avgcount =
sachannel.VideoAveragingCount ' ADC Filter sachannel.ADCFilter = 38E6 ' RBW
and VBW values sachannel.ResolutionBW = 100E3 sachannel.VideoBW = 10E3 '
RBW/VBW and Span/RBW ratios sachannel.ResolutionBWVideoBWRatio = 1.23
sachannel.SpanResolutionBWRatio = 134 End Function ' Configure a Spectrum
Analyzer measurement for Linear sweep mode on Port 1. Sub SetupLinearSweep(sa)
portnum = 1 portlabel = "Port " & CStr(portnum) ' Turn Port 1 ON
channel.SourcePortMode(portnum) = 1 ' naSourcePortOn ' Set Port 1 sweep type
to Linear ' Choices are: ' 0 - naLinearSweep ' 3 - naCWTimeSweep
sa.SourceSweepType(portlabel) = 0 ' naLinearSweep ' Set start and stop
frequencies sa.SourceStartFrequency(portlabel) = 2E9
sa.SourceStopFrequency(portlabel) = 4E9 ' Set 'Source Number of Steps'. This
is the number of frequencies to use between start and stop (inclusive). ' This
setting is channel-wide. sa.SourcePointCount = 5 ' Set 'SA Sweeps per Source
Steps'. This is the number of sweeps to take at each measurement frequency. '
This setting is also channel-wide. sa.SourceRepeatCount = 2 End Sub '
Configure a few of the Advanced Settings for SA. Sub
ConfigureAdvancedSettings(sa) ' Set the 'Image Reject' selection. ' Choices
are: ' 0 - naIRNoneHigh ' 1 - naIRNoneLow ' 2 - naIRMin ' 3 - naIRNormal ' 4 -
naIBetter ' 5 - naIRMax sa.ImageRejectMethod = 5 ' naIRMax ' Enable display of
ImageReject traces. sa.EnableImageRejectTraces = 1 ' naON ' Enable point mode.
' This forces the number of display points to match the FFT point count.
sa.EnableDetectorBypass = 1 ' naON End Sub  
---

