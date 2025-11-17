# LFE Calibration

The procedure in this topic describes how to perform a calibration using the
[Cal All Calibration Wizard](../../S3_Cals/Calibrate_All_Channels.md) method,
which allows multiple channel calibration in a single session.

Note: Beginning with the A.12.80 release, Cal All has been extended in order
to deal with the new Low Frequency Extension option. If a user has a mixture
of LFE and non-LFE channels and they would like to use Calibrate All to
calibrate them at the same time, two calibration channels are created to
account for the hardware differences between the two situations. When using
the GUI or COM to set calibration and stimulus conditions, the settings are
applied to both calibration channels. With SCPI, the user can query the
primary guided calibration channel using
[SYST:CAL:ALL:GUID:CHAN:VAL?](../../Programming/GP-
IB_Command_Finder/SystCalAll.htm#GuideChan). This will return the primary
calibration channel. When subsequent Guided Cal commands are used, settings
will be transferred to the second calibration channel. If there is a desire to
set these settings separately, the user should query for all Cal All
Calibration channels with [SYST:CAL:ALL:GUID:CHAN:LIST?](../../Programming/GP-
IB_Command_Finder/SystCalAll.htm#SYSTem:CALibrate:ALL:GUIDed:CHANnel:CATalog).
The user should set values for the primary calibration first, and then
secondary calibrations. When initializing the calibration and acquiring steps,
use the primary cal all channel number.

For information about other calibration methods that can be used, refer to the
following links:

  * [Basic Cal](../../S3_Cals/Calibration_Wizard.md#BasicCal)
  * [Smart Cal](../../S3_Cals/Calibration_Wizard.md#GuidedCal)
  * [Response Cal](../../S3_Cals/Calibration_Wizard.md#unguided)
  * [Source Power Cal](../../S3_Cals/PwrCalibration.md#SourcePowerCal)

## Cal All Procedure

  1. Ensure that the measurement classes to calibrate are active.

  2. Press Sweep > Source Control > LF Extension ON.

  3. Ensure that the measurement frequency range is set properly.

  4. Press Cal > Main > Other Cals > Cal All... to launch the following dialog showing the active measurement classes:

![](../../assets/images/LFE_Cal_Channels.png)

  5. Check the measurement classes to calibrate.

  6. Select the ports, then click on the Apply to all channels button to apply the port selections to all channels.

  7. Click Next, then confirm or change the calibration properties in the Measurement Class Cal Properties dialog.

  8. Click Next. to access the Calibration Attenuator Settings dialog.

![](../../assets/images/Cal%20Atten%20Settings.png)

  9. In the Calibration Attenuator Settings dialog, perform the following:

     1. Set the attenuator settings. [Learn more](../../S3_Cals/Calibrate_All_Channels.md#CalAttnSettingsDiag).

     2. Click on the Noise Reduction button to improve measurement accuracy. [Learn more](../../S2_Opt/Trce_Noise.md).

     3. Click on the Mechanical Devices button to view all switches and attenuators in the VNA. [Learn more](../../System/Mechanical_Devices.md).

  10. Click Next, then select the DUT connectors and calibration kits in the Select DUT Connectors and Cal Kits dialog.

  11. .Click Next to access the Power Cal Settings dialog.

![](../../assets/images/Power%20Cal%20Settings.png)

  12. In the Power Cal Settings dialog, perform the following:

     1. Check Use Multiple Sensors if more than one power sensor is needed to cover the frequency range then select a sensor from the Sensor down menu.

     2. Learn more about [Accuracy Tolerance](../../S3_Cals/Guided_Power_Calibration.md#Accuracy) and [Max Number of Readings](../../S3_Cals/Guided_Power_Calibration.md#Accuracy).

  13. Click Next and follow the calibration process until completed.

