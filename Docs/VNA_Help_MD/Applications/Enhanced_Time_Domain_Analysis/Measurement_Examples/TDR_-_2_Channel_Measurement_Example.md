# 2 Channel Measurement Example

  * Overview

  * Procedure

[Other topics about Measurement Examples](Measurement_Examples.md)

## Overview

This example shows a 2 channel measurement in the Advanced Mode.

2 channel measurements allow you to make the following measurements:

  * TDR measurement on channel 1

  * More customized S-parameter measurement on channel 2

Note: S-parameter measurements in Channel 1 are used for the time domain
transformation. In order to ensure correct time domain results, the
S-parameter settings for TDR are not accessible by the user. The optimum
settings are calculated within the TDR algorithm. However, there are cases
when the user may want specific settings for their S-parameter measurements.
For these cases, another channel is used for customization (TDR works for
Channel 1 only).

Here is the sequence of this example.

  * Setup for channel 1

  1.      1. Deskew

     2. Auto DUT length

     3. Set rise time

     4. Setup limit table for the trace 1

  * Setup for channel 2

  1.      1. Setup start and stop frequency and IF Bandwidth.

     2. Setup Sdd11 of Balance-Balance measurement

     3. Setup limit table for the trace 1

     4. Full 4-port calibration with ECal

  * Measurement for channel 1

  1.      1. Trigger

     2. Auto scale

  * Measurement for channel 2

  *     1. Trigger

## Procedure

### Preparation for 2 Channel Measurement

  1. Connect E-Cal on the USB port on the front panel.

  2. Connect cables to all test ports.

  3. Activate [Advanced Mode](../Advanced_Mode/Activating_and_Deactivating_Advanced_Mode.md#Activating_Advanced_Mode) (Do not select the Use Advanced Calibration Methods check box)

  4. Click the Stop Single button to stop the trigger.

Using Hardkey/SoftTab/Softkey (on the right side of the screen):

  1. Press Trigger > Main > Trigger... to access the Trigger dialog.

  2. Under Trigger Scope select Active Channel then click OK.

  3. Press System > System Setup > Sound then adjust the setting to 0 (zero) to turn off the beeper warning.

### Setup for Channel 1

  1. Click the Setup tab in the TDR GUI.

  2. Click Setup Wizard (under Basic).

  3. Set the measurement condition using the Setup Wizard:

     1. Select Deskew (under Error Correction) then click Next >.

     2. Click the Differential 2-Port button, then click Next >.

     3. Click the Deskew button, then click Next >.

     4. Click the Measure button, then click Next >.

     5. Set the Rise Time to 45 ps and select 20-80% from the Definition drop-down list.

     6. Click the Finish button.

#### Limit Test Setup

Using Hardkey/SoftTab/Softkey (on the right side of the screen):

  1. Ensure that Trace 1 is selected.

  2. Press Math > Analysis > Limits... to access the Limit Test Setup dialog.

  3. Check Limit Test ON to turn on the limit test.

  4. Check Limit Line ON to turn on the limit line then click OK.

  5. Click Math > Analysis > Limit Table then select Limit to display the limit table.

  6. Edit the table as shown below.

| Type | Begin Stimulus | End Stimulus | Begin Response | End Response  
---|---|---|---|---|---  
1 | Max | 0 s | 1 ns | 105 U | 105 u  
2 | Min | 0 s | 1 ns | 75 U | 75 U  
  
### Setup for Channel 2

  1. Click Trace > Trace Setup > Add Trace then select New Trace + Channel + Window.

  2. Click Trigger > Main > Hold.

  3. Press the Freq hardkey. A table is displayed below the window.

Note: When pressing the Freq hardkey, the table is shown in Channel 1 since
the sweep is set to segment. For channel 2, the default would be linear sweep,
so the necessary parameters will need to be set up using the softkeys.

  4. Edit the table as shown below.

| State | Start | Stop | Points | IFBW | Power  
---|---|---|---|---|---|---  
1 | On | 1 GHz | 3 GHz | 29 | 10 kHz | 5 dBm  
  
  5. Press Cal > Fixtures > Apply Fixtures ON to turn on the fixture simulator.

  6. Click Setup > Layout > Measure... to access the Measure dialog.

  7. In the Measure dialog, select the Balanced tab.

  8. Check the desired balanced measurement (for example, Sdd21), then click Apply to view the measurement result.

  9. When finished, click OK.

#### Full 4-port Calibration

  1. Connect 4 Port Ecal with the cables.

  2. Press Cal > Other Cals > Ecal....

  3. Follow the wizard for a 4-Port ECal.

#### Limit Test Setup

Using Hardkey/SoftTab/Softkey (on the right side of the screen):

  1. Press Math > Analysis > Limits... to access the Limit Test Setup dialog.

  2. Check Limit Test ON to turn on the limit test.

  3. Check Limit Line ON to turn on the limit line then click OK.

  4. Click Math > Analysis > Limit Table then select Limit to display the limit table.

  5. Edit the table as shown below.

| Type | Begin Stimulus | End Stimulus | Begin Response | End Response  
---|---|---|---|---|---  
1 | Min | 100 MHz | 1.25 GHz | -1.5 dB | -5 dB  
2 | Min | 1.25 GHz | 2.5 GHz | -5 dB | -7.5 dB  
3 | Min | 2.5 GHz | 7.5 GHz | -7.5 dB | -25 dB  
  
### Measurement in Channel 1

  1. Connect the DUT with the cables.

  2. Click the Stop Single button in the TDR GUI to make one single measurement.

  3. Select Trace 1.

  4. Click Auto Scale in the TDR GUI, then select All Traces.

### Measurement in Channel 2

  1. Select the S-parameter trace of interest.

  2. Click Trigger > Main > Single to make one single measurement.

