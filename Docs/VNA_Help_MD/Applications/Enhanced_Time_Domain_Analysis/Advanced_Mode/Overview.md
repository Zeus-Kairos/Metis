# Overview

  * Feature

  * Advanced Mode Considerations

[Other topics about Advanced Mode](Advanced_Mode.md)

## Feature

The following table shows the comparison of Advanced and Basic Modes.

Mode |  Feature |  TDR Application (User Interface) |  Hard Key on Front Panel |  Soft Keys (right side of the screen) |  [Measurement Class](../../../S1_Settings/Measurement_Classes.md) Selection |  Indicators  
---|---|---|---|---|---|---  
Advanced1 | 

  * Customized TDR/S-parameter measurements in TDR (Ch1)  
  
Such as:

  * More Marker Functions
  * Limit Test
  * TRL Calibration
  * Two channel measurements (Ch1 for TDR/Ch2 for Network Measurement)

|  Available |  Available |  Available |  Available but not recommended |  [TDR indicator](../Overview/TDR_Screen_Area.md#Channel_Window) \+ SVC indicator  In [Instrument status bar](../../../Front_Panel/XScreen.md#Status)  
Basic |  Easy to use |  Available |  Locked except for Trace Prev, Trace Next, Trace Max and keys in numeric key pad. |  Hidden |  Not Available |  [TDR indicator](../Overview/TDR_Screen_Area.md#Channel_Window) In [Instrument status bar](../../../Front_Panel/XScreen.md#Status)  
  
1 Setting VNA-TDR to Advanced Mode enables VNA functions which are disabled in
Basic Mode. It is possible to set up features that will result in unexpected
measurement results. Therefore, only advanced users should use Advanced Mode.

The [sample measurements](../Measurement_Examples/Measurement_Examples.md)
are shown in the measurement examples.

## Advanced Mode Considerations

In the Advanced Mode, you can access all VNA functions. The setting you
changed may affect the measurement unexpectedly. The measurement may not be
correct if you have such a case. Therefore, the measurement performance is not
guaranteed in the Advanced Mode.

It is known that changing the following settings can cause incorrect
measurement.

Hard key |  Do not use  
---|---  
Meas |  Single end 1 port: Parameters related with ports 2, 3 and 4  
Single end 2 port/Differential 1 port: Parameters related with ports 3 and 4  
Trace |  Add / Delete Traces  
Display |  Data Math, Equation Editor  
Sweep Setup |  Start/Stop/Center/Span Points Sweep Type Frequency Offset  
Calibration |  Fixture Simulator, AFR (If you want to use AFR, create a snp file in standard class, then use the embedding in adv waveform)  
Marker Function |  Marker -> Start, Marker -> Stop  
  
Here is another caution in the Advanced Mode.

Function |  Note  
---|---  
Meas |  Change parameter when Port extension on |  This may cause to tilt the wave form in the time domain . Use TDR GUI to select parameter.  
Display |  Increasing Num of Trace |  This may cause to tilt the wave form in the time domain.  
Analysis |  Fixture Simulator |  This may cause to tilt the wave form in the time domain.  
Transform > Window > Impulse width or Step Rise |  The range of these settings is narrower than one of the Rise Time in the TDR GUI. Use TDR GUI to set the rise time.  
Calibration |  Increasing Port Extension |  This may cause to exceed the DUT length limitation.  
Scale |  Increasing Electrical Delay |  This may cause to exceed the DUT length limitation.  
Ave |  IF Bandwidth |  Even if you have narrow IF Bandwidth, you may not have noise reduction at lower frequency.

