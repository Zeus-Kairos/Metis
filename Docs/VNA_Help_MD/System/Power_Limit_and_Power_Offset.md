# Power Limit and Power Offset

* * *

  * [Overview](Power_Limit_and_Power_Offset.md#Overview)

  * [How to access Power Limit and Power Offset settings](Power_Limit_and_Power_Offset.md#How)

[Other System Topics](System_Topics.md)

Overview

### Power Limit (Global scope)

### Notes

  * The power limit can NOT be set for power levels which are below the power level that is required by the analyzer to achieve phase lock - approximately -30 dBm.

  * Because [Fast Sweep mode](../S1_Settings/Sweep.md#Fast) allows power spiking, it is NOT allowed when a power limit is enabled.

  * Components that are added to the RF path are accounted for by entering their loss (negative) or gain (positive) in the [Power Offset](Power_Limit_and_Power_Offset.md#Offset) section of the dialog box.

  * [VNA Applications](../Applications/Applications.md) may change RF path components. For example, IMD for Converters may change the combiner path and add an amplifier for LO input. Compensation is NOT made for these changes and port power may exceed the power limit or port power may be clipped unnecessarily.

  * Power limiting does NOT clip power spikes that may occur during [frequency band crossings](../S1_Settings/Frequency_Range.md#BandCrossings).

  * [External test set ports](External_Testset_Control.md) are also included for power limiting.

### Power Offset (Channel scope)

Power Offset provides a method of compensating port power for added
attenuation or amplification in the source path. The result is that power at
the specified port, all dialogs, and annotation, reflects the added
components.

#### How to access the Offsets and Limits settings

Also accessed through the [Preferences](Preferences.md) dialog.  
---  
Using Hardkey/SoftTab/Softkey |  Using a mouse  
  
  1. Press Power > Leveling & Offsets > Offsets and Limits...

|

  1. Click Stimulus
  2. Select Power
  3. Select Offsets and Limits...

  
[![](../assets/images/SeeProg.gif)](../Programming/CF_Power_Commands_-
_Standard.htm#Leveling___Offsets_Tab_Commands)  
  
Offsets and Limits dialog box help  
---  
![](../assets/images/offsets%20and%20limits_power.png) Click a WHITE cell to
change values. Shaded cells can NOT be changed. [Remote
commands](../Programming/XStimulusTopic.htm#Limits) can be sent to lock and
unlock the dialog box (UI) settings.

### Limit Source Power

Limits the source power at each test port for ALL channels. Use this feature
to protect DUTs that are sensitive to overpowering at the input. Source Power
levels that exceed the Limit at the specified port are clipped at the limit,
the power level in the Source Power column turns red, and an error message is
displayed on the screen. The Power Limit settings and PLimit status indicator
survive [Instrument Preset](../S1_Settings/Preset_the_Analyzer.md). When an
Instrument State is [recalled](../S5_Output/SaveRecall.md#file_recall), the
current Power Limit settings are applied to the recalled state. To learn more,
see Power Limit Overview (scroll up). State

  * ON \- Power is limited to the adjacent value at the specified source port and displays PLimit in the status bar indicating that a power limit is ON.
  * OFF \- Power is NOT limited to this value, but to the maximum power of the source.

**Limit Always** \- Limit the source power at all times. **Limit During Cal**
\- Limit the source power during calibration. For VNA models with a second
internal source, the Port 1 Src2 Power Limit setting is NEVER available. Make
the setting at the standard Port 1.

### Power Offset

Power Offset provides a method of compensating port power for added
attenuation or amplification in the source path. The result is that power at
the specified port, all dialogs, and annotation reflects the added components.

  * For amplification, use positive offset.
  * For attenuation, use negative offset.

Important Note: Power Offset is added AUTOMATICALLY when a [Source Power
Calibration](../S3_Cals/PwrCalibration.htm#SourcePowerCalDiagIm), [Guided
Power Cal](../S3_Cals/Guided_Power_Calibration.htm), or Power Compensation is
ON with Fixture Embed/Deembed. If you are NOT seeing the correct power level
at your DUT, view the power Offset column in this dialog for unexpected
offsets. Optionally change the Source Power or Port Power values so that the
following equation reflects your requirement: Source Power + Power Offset =
Port Power Source Cal ON / OFF

### Notes

  * Power Offset can be used with [Power Sweeps](../S1_Settings/Power_Level.md#PwrSweep). When a power sweep is enabled, the Start and Stop power levels are reported in this dialog.
  * When port power offsets are used, port powers are automatically [uncoupled](../S1_Settings/Power_Level.md#Power_Coupling). Port powers may not be coupled again until all port offsets are zero.
  * Cal All does not automatically use the specified power offset during a calibration. To use a power offset for one or more ports when performing a Cal All, you must set the power offset value in the Cal All wizard.

Power Step Size: Specify the arrow key up/down step resolution. The setting is
kept even after preset and power off/on. Power Spin Size: Specify the rotary
Knob spin resolution. The setting is kept even after preset and power off/on.
OK Closes the dialog box.  
  
* * *

