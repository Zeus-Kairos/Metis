# Set Up an EVM Measurement

To compute EVM, the input and output response of the DUT in the frequency
domain is measured. Spectrum correlation is then performed to compute the EVM.
The procedures in this topic describe how to measure the equalized EVM of the
DUT (non-linear contribution) and the un-equalized EVM of the DUT (Includes
non-linear and linear distortion due to frequency dispersion).

In this topic:

  * EVM Measurement Criteria
  * Equalized EVM of the DUT (non-linear contribution)
  * Un-equalized EVM of the DUT (Includes non-linear and linear distortion due to frequency dispersion)

## EVM Measurement Criteria

The procedures in the list below must be performed prior to making EVM
measurements. For purposes of this example, the DUT used is an amplifier and
the Modulation Type is Flat Tones.

  * Required set up procedures:
    * [Hardware Setup for Amplifiers](Hardware_Setup_for_Amplifier.md)
    * Create a Modulation Distortion Channel
    * [Set Up a Sweep](Set_Up_a_Sweep.md)
    * [Set Up the RF Path](Set_Up_the_RF_Path.md)
    * [Set Up the External Source](Set_Up_the_External_Source.md)
    * [Set Up a Flat Tones Modulation Type](Set_Up_a_Flat_Tones_Modulation_Type.md)
  * Calibration procedures:
    * [Phase Reference Wizard](../../FreqOffset/Phase_Reference_Calibration.md)
    * [S-Parameter Calibration](S-Parameter_Calibration.md)
    * [Source Modulation Calibration](Modulation_Flatness_and_Power_Calibration.md)

## Equalized EVM of the DUT (non-linear contribution)

  1. If the Modulation Distortion Setup dialog is not displayed, press Freq > SA Frequency > MOD Setup....
  2. The Sweep, RF Path, Modulate, or Measure tab functions can now be selected.

  3. Select the Measure tab.  
  
![](../../assets/images/ModDistortion_MeasureTab_BandPower.png)

  4. In the Measurement Type pull down menu, select EVM.  
  
![](../../assets/images/ModDistortion_MeasureTab_EVM.png)

  5. Click on the Autofill button to automatically fill in the measurement settings for all bands from the currently active modulation file loaded in the source. Therefore, changing the settings in the following steps is optional.

  6. To offset the Carrier integration bandwidth relative to the Carrier LO used to generate the modulation signal, use the up/down arrows in the Carrier Offset Freq field or double-click in the field then enter the value using the displayed keypad.

  7. To set the Carrier integration bandwidth for the distortion measurement, use the up/down arrows in the Carrier Integ BW field or double-click in the field then enter the value using the displayed keypad. The IBW is used to determine total signal power within a specified frequency span.

  8. To adjust other measurement settings, click on the Measurement Details... button:  
  
![](../../assets/images/ModDistortion_MeasurementDetailsDialog_Converters.png)

     1. To set the frequency span window used for modeling the DUT's gain and distortion, use the up/down arrows in the Distortion Measurement Correlation Aperture field or double-click in the field then enter the value using the displayed keypad. Checking Auto will automatically set Distortion Measurement Correlation Aperture to window size.

     2. To select the IF filter anti-aliasing path, click on the ADC Anti-alias Filter pull down menu then select Auto, Wide, or Narrow. Auto will automatically set the ADC Filter setting based on the ADC Sampling Frequency. If the currently selected modulation waveform was created with Nyquist Rejection = OFF, then the VNA will measure the signal using the Narrow anti-alias filter in the receiver. Wide selects the ADC 38 MHz IF filter path. Narrow selects the ADC 11 MHz IF filter path. A warning message will appear if the Narrow IF filter path is selected and the Resolution Bandwidth is > 1 MHz.

     3. To set the measurement filter to either None (default) or RRC (root-raised-cosine filter), click on the Modulation Filter pull down menu then make the selection. With RRC selected, Alpha sets the Alpha factor of the filter and Symbol Rate sets the Symbol Rate of the filter. If Auto is selected, the Symbol Rate from the file is used. If no Symbol Rate is indicated in the file, then the Symbol Rate will be approximated from the bandwidth of the signal.

     4. To set the scaling factor applied to the EVM measurements. Enter a value between 0.1 and 1.0. The default is 1.0 using the up/down arrows in the EVM Normalization field.

     5. To set the DUT noise figure, use the up/down arrows in the Nominal DUT NF field or double-click in the field then enter the value using the displayed keypad. This value is used by the EVM measurement. This setting adds noise to the measurement for more realistic results. The default is 0 dB. Setting the noise figure to a low value (-200 dB) will make EVM measurements without the effects of noise.

     6. Click on the OK button.

  9. Click on the Apply button to apply the setting changes made in this dialog.

  10. Click on the OK button to close the dialog.

  11. Ensure that the VNA Trigger is set to Continuous. Press Trigger > Main > Continuous.

  12. The Distortion Table is displayed below the measurement area. Each column represents a measurement parameter. The measurement parameters shown in the Distortion Table below are the default parameters selected for an EVM measurement.  
  
![](../../assets/images/ModDistortion_DistortionTable_EVM3.png)

  13. The measurement parameters are selected using the [Distortion Table Setup](Displaying_Distortion_Parameters.md#Distortion_Table_dialog_help) dialog. To add or change parameters, press Meas > Main > Distortion Table... or right-click on the Distortion Table displayed below the measurement area then select Edit Columns... in the pop-up menu. The Distortion Table Setup dialog is displayed:  
  
![](../../assets/images/ModDistortion_DistortionTableSetup2.png)  

  14. Select the EVM tab.  
  
![](../../assets/images/ModDistortion_DistortionTable_EVM4.png)

  15. Check the desired measurement parameters then click on the OK button.

  16. To view a trace displaying the equalized EVM of the DUT (non-linear contribution), perform the following:

     1. Press Meas > Main > Other... then click on the "..." button. The Measure dialog is displayed:  
  
![](../../assets/images/ModDistortion_MeasurementParameters_Main1.png)

     2. Select the Distortion tab to display distortion traces:  
  
![](../../assets/images/ModDistortion_MeasurementParameters_Distortion1.png)

     3. Check EVMDistEq21 then click on the OK button.

  17. The following is an example of a typical trace and Distortion Table showing equalized distortion of the DUT:  
  
![](../../assets/images/ModDistortion_EVM_EqualizedDistortion.png)

## Un-equalized EVM of the DUT (Includes non-linear and linear distortion due
to frequency dispersion)

After setting up and performing an EVM measurement as described in the above
procedure, perform the following procedure for a measurement that includes
non-linear and linear distortion due to frequency dispersion.

  1. Press Meas > Main > Distortion Table... or right-click on the Distortion Table displayed below the measurement area then select Edit Columns... in the pop-up menu.

  2. In the Distortion Table Setup dialog, select the EVM tab.  
  
![](../../assets/images/ModDistortion_DistortionTable_EVM4.png)

  3. Check the EVM DistUn21 % parameter then click on the OK button. The added parameter is displayed as a new column in the Distortion Table displayed below the measurement area.

  4. To view a trace displaying the un-equalized EVM of the DUT, perform the following:

     1. Press Meas > Main > Other... then click on the "..." button. The Measure dialog is displayed:  
  
![](../../assets/images/ModDistortion_MeasurementParameters_Main1.png)

     2. Select the Distortion tab to display distortion traces:  
  
![](../../assets/images/ModDistortion_MeasurementParameters_Distortion1.png)

     3. In the Distortion tab, check New trace. If any parameters are currently checked, uncheck them.

     4. Check EVMDistUn21 then click on the OK button.

  5. The following is an example of a typical trace and Distortion Table showing un-equalized distortion of the DUT:  
  
![](../../assets/images/ModDistortion_EVM_UnEqualizedDistortion.png)

