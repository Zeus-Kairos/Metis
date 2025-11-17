# Hot TDR Measurement

  * Overview
  * Checking Device Malfunction
  * Reducing Measurement Error

[Other topics about Making Measurement](Making_Measurements.md)

## Overview

Hot TDR refers to TDR measurement while the device is powered ON. During
measurement, the measurement signal is applied from the VNA to the
transmitter. However, this may cause device malfunction. In addition, the
transmitter signal from the DUT device into the VNA ports may cause
measurement error. When you measure Hot TDR, the transmitter should be
connected with Port 1 for Single END, Port1/2 for differential.

![](../../../assets/images/TDR_Transmitter.png)

## Checking Device Malfunction

The following procedure checks if the Signal Source level from the VNA does
not affect the device operation:

  1. Measure the reflection on the VNA.

  2. Save the results in [memory trace](Using_Data_and_Memory.md).

  3. Reduce the signal source level of the VNA at [Source Power](../Setting_Up_the_Measurement/Performing_Manual_Setup.md#Source_Power).

  4. Check for significant change on the trace. If the change is significant, reduce the signal source level further to avoid device malfunction.

## Reducing Measurement Error

The following procedure reduces the measurement error produced by the device
signal.

### Case 1 (For Periodic Bit Pattern)

If the output signal from device is periodic, set the data rate and execute
"Avoid Spurious". This will reduce error due to spurious:

  1. Click Setup tab and select the Hot TDR tab.

  2. At the Data Rate text box, left-click once. An Entry dialog box appears. Type the data rate value and click OK. The new value is displayed in the Data Rate text box. The Data Rate accuracy should be within ±0.5%.

  3. Click the Avoid Spurious button to execute the option. The VNA searches for spurious and changes the stimulus setting to avoid the spurious. If the Avoid Spurious is successfully executed, a check mark appears next to the Avoid Spurious button. At this point, measurement mode is changed from TDR/TDT to Hot TDR Mode and this is indicated at the [channel window](../Overview/TDR_Screen_Area.md#Channel_Window) as "TDR ?". The blue SVC indicator is also turned ON.

     1. Eye/Mask option tab is disabled in HOT TDR mode.

     2. To reset the HOT TDR mode, simply execute [preset](../Setting_Up_the_Measurement/Performing_Manual_Setup.md#Preset) or change the [DUT toplogy](../Setting_Up_the_Measurement/Performing_Manual_Setup.md#Setting_DUT_Topology).

### Case 2 (For Random Data)

If the output signal from device is random, increase averaging to reduce the
measurement error.

#### About Avoid Spurious

If Avoid Spurious fails, the "Spurious Not Found" warning message is
displayed. Check mark next to the Avoid Spurious button will not be displayed.

When the following parameter is changed, Avoid Spurious option should be
executed again:

  * Data Rate

  * DUT Length

  * Deskew

The setting of Avoid Spurious cannot be stored. To recall the condition of
Avoid Spurious, you must execute the Avoid Spurious again after recalling the
status setting.

At the execution of Avoid Spurious:

  * If the IF bandwidth is over 10 kHz, the IF bandwidth value will be set at 10 kHz.

  * If the source power is over -20 dBm, the source power will be set at -20 dBm.

