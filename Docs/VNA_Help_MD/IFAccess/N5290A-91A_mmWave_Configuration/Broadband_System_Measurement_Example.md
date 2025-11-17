# Broadband System Measurement Setup

Broadband refers to mmWave configurations with a frequency range of 900 Hz to
110 GHz (N5290A) or 900 Hz to 120 GHz (N5291A). This configuration spans the
entire frequency range in a single sweep.

After minimal setup shown below, the N5290A/91A functions the same as a
standard VNA. All ports can be used at mmWave frequencies or a combination as
required.

In this topic:

  * Limitations
  * Setting Up a Measurement

## Limitations

  * ONLY the applications listed in Supported Applications are supported
  * No automatic power leveling. However, after performing an [Installation Calibration](Millimeter_Configuration.md#Installation_Cal), the source power at the output of the N5293A or N5295A Frequency Extender is adjusted.
  * Simultaneous broadband and banded measurements NOT supported
  * Applications that require the use of source and receiver attenuators DO NOT apply to a millimeter wave system

### See Also

  * Supported Applications
  * [Supported Configurations](Supported_Configurations.md)
  * [Low Frequency Extension (LFE)](../Low_Frequency_Extension/Overview.md)

## Setting Up a Measurement

  1. Press Setup > External Hardware > Millimeter Config.
  2. Select N5291A Broadband (or N5290A Broadband).

![](../../assets/images/N5291A_Config_Dialog.png)

  3. Note the ports selected for Enable Modules. Frequency Extenders connected to the test set are automatically detected. Configure as necessary.
  4. Press OK. This closes the dialog.
  5. To change the start frequency below 10 MHz (minimum of 900 Hz), press Freq > Main > Start then enter the start frequency below 10 MHz. The following dialog is displayed.

![](../../assets/images/EnableLFEWarningDialog.png)

  6. Click OK.
  7. To change the stop frequency, press Freq > Main > Stop then enter the stop frequency.

