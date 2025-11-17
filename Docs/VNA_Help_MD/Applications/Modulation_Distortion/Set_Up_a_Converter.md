# Set Up a Converter

Note: M983xA does not support this.

For purposes of these examples, only 1 converter stage will be configured.

In this topic:

  * Procedure for Converter without Embedded LO
  * Procedure for Converter with Embedded LO

## Procedure for Converter without Embedded LO

  1. If the Modulation Distortion Setup dialog is not displayed, press Freq> SA Frequency > MOD Setup....

  2. The Sweep, RF Path, Mixer, Modulate, or Measure tab functions can now be selected.

  3. Select the Mixer tab.  
  
![](../../assets/images/ModDistortion_MixerTab.png)

  4. In the Converter Stages pull down menu, select 1.

  5. Click on the Source Name pull down menu then select Port 3. This is the LO source.

  6. Adjust the Power using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad.

  7. Click on the Leveling pull down menu then select Open Loop or Internal. The Open Loop selection does not use ALC or receiver leveling. The Internal selection uses ALC leveling.

  8. Adjust the receiver Attenuator using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad.

  9. Adjust the LO frequency using the up/down arrows or by double-clicking in the data entry field and entering the frequency using the displayed keypad. 

  10. Set the multiplier and denominator. The combination of numerator / denominator forms a fractional value that is multiplied by the input and LO frequency ranges. [Learn more](../MixerConverter_Setup.md#Multplier).

  11. Adjust the Input using the up/down arrows or by double-clicking in the data entry field and entering the frequency using the displayed keypad. This is the same as Carrier Freq In in the Sweep tab.

  12. Click on the Output equation pull down menu then select the mixer configuration calculated from the output mixer equation selection.

  13. To save the mixer setup, click on the Save... button then enter the file name and directory path.

## Procedure for Converter with Embedded LO

The following procedure describes how to set up measurements of mixers that
have a fixed LO inside the DUT.

  1. If the Modulation Distortion Setup dialog is not displayed, press Freq> SA Frequency > MOD Setup....

  2. The Sweep, RF Path, Mixer, Modulate, or Measure tab functions can now be selected.

  3. Select the Mixer tab.  
  
![](../../assets/images/ModDistortion_MixerTab.png)

  4. In the Converter Stages pull down menu, select 1.

  5. Adjust the LO frequency using the up/down arrows or by double-clicking in the data entry field and entering the frequency using the displayed keypad. 

  6. Set the multiplier and denominator. The combination of numerator / denominator forms a fractional value that is multiplied by the input and LO frequency ranges. [Learn more](../MixerConverter_Setup.md#Multplier).

  7. Adjust the Input using the up/down arrows or by double-clicking in the data entry field and entering the frequency using the displayed keypad. This is the same as Carrier Freq In in the Sweep tab.

  8. Click on the Output equation pull down menu then select the mixer configuration calculated from the output mixer equation selection.

  9. Click on the Setup... button. The Embedded LO dialog is displayed:  
  
![](../../assets/images/ModDistortion_EmbeddedLODialog1.png)

  10. Check the Enable Embedded LO check box.

  11. Click on the Tuning Method pull down menu. These settings determine the amount of time spent versus the degree of accuracy to which the LO Frequency is measured. Accuracy is compromised when noise starts to appear on the measurement trace. Select from the following:

     * Broadband and Precise Does the entire tuning process for each background sweep. 

     * Precise Only Does NOT perform broadband tuning on each sweep. Use this setting when the embedded LO is stable. The signal (after broadband) must be within ½ the tuning IFBW. If the signal will always be within ½ the IFBW, broadband tuning is not needed. 

     * Disable Tuning Only the previously measured LO Frequency Delta is applied to the reference mixer LO and VNA receivers.

  12. Set the Tune every interval at which tuning is performed before a measurement sweep using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad. For example, 'Tune every 3 sweeps' means that every third measurement sweep is preceded by tuning sweeps. If the embedded LO drifts, or if regularly changing DUTs, set it to 'Tune every 1 sweep'.

  13. Set the Broadband Search frequency span over which to measure the embedded LO frequency using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad.

  14. Set the Noise BW used for Broadband and Precise tuning sweeps using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad. This sets the resolution in the Broadband sweeps.

  15. Set the Max Iterations of Precise sweeps to make using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad. When this number is reached, the final measurement is used.

  16. Set the Tolerance using the up/down arrows or by double-clicking in the data entry field and entering the value using the displayed keypad. When two consecutive Precise measurements are made within this value, the final measurement is used. If this is not achieved within the Max Iterations value, then the last measurement is used. 

  17. Click on the Find Now button to find and measure the actual LO frequency using the current dialog settings. This data is displayed in the Status box. 

  18. The LO Frequency Delta displays the absolute difference between the measured embedded LO frequency and the LO setting that is entered in the Mixer Tab dialog.

  19. Click on the OK button.

  20. In the Mixer tab, click on the Apply button to apply the settings. 

  21. To save the mixer setup, click on the Save... button then enter the file name and directory path.

