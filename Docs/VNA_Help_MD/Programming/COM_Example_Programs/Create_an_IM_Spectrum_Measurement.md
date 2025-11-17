# Create an IM Spectrum Measurement

* * *

This VBScript example creates IM Spectrum measurement based on passed
parameters.

This subprogram is extracted from the macro on the VNA that produces an IM
spectrum channel from the Marker function. You can see the entire program at
C:\Program Files\Keysight\Network Analyzer\Applications\IMD\IMD.VBS.

This VBScript (*.vbs) program must be used as part of a program that supplies
the required parameters. When complete, it can be run as a macro in the VNA.
To do this, copy the following code into a text editor file such as Notepad
and save it on the VNA hard drive as IMD.vbs.

[Learn how to setup and run the macro](../Using_Macros.md).

[See SweptIMD Object.](../COM_Reference/Objects/SweptIMD_Object.md)

'' SetupIMSpectrum '' Setup an IM Spectrum (non-converter) channel based upon
supplied parameters sub SetupIMSpectrum(app, MkrPos, ToneSpacing, TonePower)
dim objIMXChan, objIMDChan dim Fstart, Fstop, NumPoints, ToneFc set objIMXChan
= objIMSChan.CustomChannelConfiguration set objIMDChan =
objSIMDChan.CustomChannelConfiguration NumPoints = objSIMDChan.NumberOfPoints
select case objIMDChan.SweepType case naIMDToneCWSweep ToneFc =
objIMDChan.FrequencyCenter case naIMDTonePowerSweep Fstart =
objIMDChan.TonePowerStart(0) Fstop = objIMDChan.TonePowerStop(0) TonePower =
CalcMkrValue(Fstart, Fstop, MkrPos, NumPoints) ToneFc =
objIMDChan.FrequencyCenter case naIMDToneCenterFreqSweep Fstart =
objIMDChan.FrequencyCenterStart Fstop = objIMDChan.FrequencyCenterStop ToneFc
= CalcMkrValue(Fstart, Fstop, MkrPos, NumPoints) case naIMDDeltaFrequencySweep
ToneFc = objIMDChan.FrequencyCenter Fstart = objIMDChan.DeltaFrequencyStart
Fstop = objIMDChan.DeltaFrequencyStop ToneSpacing = CalcMkrValue(Fstart,
Fstop, MkrPos, NumPoints) case naIMDToneSegmentSweep ToneFc = MarkerXValue end
Select objIMXChan.FrequencyCenter = ToneFc objIMXChan.DeltaFrequency =
ToneSpacing objIMXChan.TonePower(0) = TonePower objIMXChan.TonePower(1) =
TonePower app.ActiveMeasurement.Trace.ReferenceValue = TonePower + 10
objIMSChan.continuous end Sub  
---  
  
* * *

