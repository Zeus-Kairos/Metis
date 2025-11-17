# Set Up a Flat Tones Modulation Type

  1. If the Modulation Distortion Setup dialog is not displayed, press Freq> SA Frequency > MOD Setup....

  2. The Sweep, RF Path, Modulate, or Measure tab functions can now be selected.

  3. Select the Modulate tab.  
  
![](../../assets/images/ModDistortion_ModulateTab_4.png)

  4. In the Modulate tab, click on the Create... button to access the Create Modulation dialog.  
  
![](../../assets/images/ModDistortion_CreateModulation_Compact2.png)

  5. In the Modulation Type pull down menu, select Flat Tones.   
  
![](../../assets/images/ModDistortion_CreateModulation_Flat_Tones2.png)

  6. In the Source Name pull down menu, select the source. If it is not in the list, select Add Source... then refer to [Set Up the External Source](Set_Up_the_External_Source.md) to set up a source.

  7. Click on the Calculate button then under Calculated Result, verify that the signal looks reasonable.

  8. To make adjustments to the settings, perform the following procedure (optional):

     1. To adjust the frequency span of the modulated carrier, click in the Signal Span data entry field then use the up/down arrows or double-click in the data entry field then enter the frequency using the displayed keypad. 

     2. To adjust the distance between each tone, click in the Tone Spacing data entry field then use the up/down arrows or double-click in the data entry field then enter the frequency using the displayed keypad. 

     3. To adjust the number of odd or even tones, select either  Nmbr Tones, Odd or Nmbr Tones, Even, click in the data entry field, then use the up/down arrows to make a change. This setting forces the optimizer to choose an odd or even number of tones. The optimizer will also choose an offset such that the carrier lands on one of the tones.

     4. To adjust the carrier offset value relative to the carrier LO frequency, click in the Carrier Offset data entry field then use the up/down arrows or double-click in the data entry field then enter the frequency using the displayed keypad. 

     5. To select a phase type, click on the Phase Type pull down menu then select Random, Fixed, or Parabolic. The Random Phase Seed sets the phase seed when Random phase is the Phase Type.

     6. To adjust the the scaling factor used for the waveform (full scale = 100%), click in the DAC Scaling data entry field then use the up/down arrows or double-click in the data entry field then enter the value using the displayed keypad. This ensures that the DAC filter does not output a signal that is larger than the DAC's maximum output level, which can cause distortion in the system. Setting the scaling factor to 100% will usually cause excessive distortion.

     7. With the Enable Optimizer check box checked, the calculated modulated signal will be optimized according to the constraints defined in Optimize Signal group box. For more information, refer to the description for [Enable Optimizer](Create_Modulation_Files.md#Enable_Optimizer) and the [Optimizer Setup](Create_Modulation_Files.md#OptimizerSetupDialog) dialog.

     8. To adjust the allowed tolerance for tone spacing when calculating the modulation signal, select Frequency Tolerance from the Optimize Signal pull down menu, click in its data entry field, then use the up/down arrows or double-click in the data entry field then enter the tolerance using the displayed keypad.

     9. To adjust minimum period of the waveform greater than or equal to the specified value (seconds), select Min Waveform Period from the Optimize Signal pull down menu, click in its data entry field, then use the up/down arrows or double-click in the data entry field then enter the period using the displayed keypad.

     10. To adjust minimum number of tones greater than or equal to the specified value, select Min Number of Tones from the Optimize Signal pull down menu, click in its data entry field, then use the up/down arrows or double-click in the data entry field then enter the number of tones using the displayed keypad. This will ignore the Number of Tones selection.

     11. To adjust maximum tone spacing less than or equal to the specified value (Hz), select Max Tone Spacing from the Optimize Signal pull down menu, click in its data entry field, then use the up/down arrows or double-click in the data entry field then enter the maximum tone spacing using the displayed keypad. This will ignore the Tone Spacing selection.

     12. After making any adjustments, click on the Calculate button then, under Calculated Result, verify that the signal looks reasonable. 

  9. Click the Save... button and save the flat tone file. The filename is displayed below the display window.  
  
![](../../assets/images/ModDistortion_FlatTones_Filename.png)

  10. In the Display pull down menu, select Spectrum-Ideal. Signals similar to the following should be displayed:  
  
![](../../assets/images/ModDistortion_FlatTones_Spectrum.png)

  11. In the Display pull down menu, select Time. Signals similar to the following should be displayed:  
  
![](../../assets/images/ModDistortion_FlatTones_TimeDomain.png)

  12. In the Display pull down menu, select CCDF. The following plot represents the complementary cumulative distribution function (CCDF) curve of the flat tones test signal, as well as the Gaussian distribution (pink trace):  
  
![](../../assets/images/ModDistortion_FlatTones_CCDF.png)

  13. Increasing the number of tones results in the following:

  14. Finer tone spacing.

  15. Longer period for the test signal.

  16. More accurate CCDF as shown below.

Number of Tones = 1,001 | Number of Tones = 10,001  
---|---  
![](../../assets/images/ModDistortion_FlatTones_CCDF.png) | ![](../../assets/images/ModDistortion_FlatTones_CCDF_10001Tones.png)  
  
  14. Click on the OK button. The modulation file is uploaded to the external source.

  15. The Autofill Measurements message is displayed asking whether to autofill measurement frequencies or not. These frequencies are in the Measure tab. [Learn more](Modulation_Distortion_Settings.md#Autofill).  
  
![](../../assets/images/ModDistortion_AutofillMeasurements.png)

  16. Click Yes.

