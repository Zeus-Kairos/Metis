# What's New

* * *

Notes

  * The latest version includes changes from all previous versions.
  * See [New Programming Commands](Programming/New_Programming_Commands.md)
  * To see the code version that is currently installed on the VNA, click Help, then About NA...

  
---  
  
### What's New in VNA Code Version A.19.30.xx

  * [Automatic Fixture Removal](S3_Cals/Auto_Fixture_Removal.md) 2025 updates

  * Added [External Noise Amplifier](Applications/Noise_Figure.md#External_Noise_Amplifier) feature

  * Added rectangular filter selection for fast IF bandwidths

    * [GUI](S2_Opt/Trce_Noise.md#IFBW_Shape)

    * [SCPI](Programming/GP-IB_Command_Finder/Sense/XSensIF.md#SENSeIFBANDwidthFILTer)

  * [Multi-channel source support](System/Configure_an_External_Source.md#ExtSourceConfig)

  * Manually enter the approximate de-embedded fixture length

    * [GUI](Applications/Enhanced_Time_Domain_Analysis/Advanced_Waveform_Analysis/Using_De-embedding.md)

    * [SCPI](Programming/GP-IB_Command_Finder/Calculate/TDR.md#DeemLeng)

### What's New in VNA Code Version A.19.15.xx

  * Windows 11 support

  * Added a [Rescan](Programming/SCPIParserConsole.md#Status) button to the [SCPI Parser Console](Programming/SCPIParserConsole.md) to monitor USB usage

### What's New in VNA Code Version A.19.10.xx

  * Added [Import Power Cal and Source PMax Table Cal in Power Cal Setting](S3_Cals/Guided_Power_Calibration.md#PowerCalSettings)

  * [Leaky Calibration](S3_Cals/Leakage_Calibration.md)

  * Updated [Save Data As dialog](S5_Output/SaveRecall.md#SaveDataAs)

  * Updated [Power Cal Settings dialog](S3_Cals/Calibrate_All_Channels.md#PowerCal diag)

  * Added [Burst Mode](Applications/Modulation_Distortion/Create_Modulation_Files.md#OptimizerSetupDialog) to the Optimizer Setup dialog for creating modulation files

  * Updated [Split Port Calibration in Call All](S3_Cals/Calibrate_All_Channels.md#SplitPortCal)

  * Updated Banded 2D Calibration:

    * [Banded System Measurement Setup](IFAccess/N5290A-91A_mmWave_Configuration/Banded_System_Measurement_Example.md)

    * [Banded Millimeter Configuration dialog](IFAccess/N5290A-91A_mmWave_Configuration/Millimeter_Configuration.md#Banded_Millimeter_Configuration_Dialog)

    * Added Millimeter Source Linearity Cal to [Banded Installation Calibration](IFAccess/N5290A-91A_mmWave_Configuration/Calibration.md#Millimeter_Wave_Dialog)

  * Updated Hybrid Source Calibration:

    * [Multiplier External Device dialog](System/Configure_a_Hybrid_Source.md#External_Device_Hybrid_Multiplier)

    * [Hybrid Multiplier Installation Cal dialog](System/Configure_a_Hybrid_Source.md#Hybrid_Multiplier_Installation_Cal)

### What's New in VNA Code Version A.19.00.xx

  * This help includes: [Example Setup for U7229x Amplifier Control](Programming/GPIB_Example_Programs/NF_U7229x_Amplifier_Control.md)

### What's New in VNA Code Version A.18.40.xx

  * [Split Port Calibration in Call All](S3_Cals/Calibrate_All_Channels.md#SplitPortCal)

  * Updated Modulation Properties dialog for [Spectrum Analyzer](Applications/Modulation_Distortion/Modulation_Flatness_and_Power_Calibration.md#Modulation_Properties_Dialog) and [Modulation Distortion](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#Modulation_Properties) applications

  * [Phase Reference Import Port](S3_Cals/Calibrate_All_Channels.md#MeasClassCalProp_SMC)

  * [Extend receiver selection for NF to include MM heads](Applications/Noise_Figure.md#Requirements)

  * [Virtual Port Indicator](S1_Settings/Customize_Your_Analyzer_Screen.md#active_port)

  * [Cal Power Off Preference](System/Preferences.md#Cal_power_off)

  * [Power Offset/Limit During Cal](System/Power_Limit_and_Power_Offset.md#Power_Limit)

  * [Link VNA to 89600 VSA](Applications/Modulation_Distortion/Link_VNA_to_89600_VSA.md) and [Digital Predistortion (DPD)](Applications/Modulation_Distortion/DPD_Overview.md) for E5081A. 

  * Added [phase stitching type, export raw data and show ADC range](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#MeasurementDetailsDialog) in MOD setup.

  * Added Operating Gain and updated descriptions of power traces in [Distortion Measurement Parameters](Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md)

### What's New in VNA Code Version A.17.60.xx

  * [Isolation Calibration is available in 2 port calibration using a mechanical cal kit.](S3_Cals/Calibration_Wizard.md#EnableIsolation)

  * [Smith Chart can be displayed during Noise Figure Calibration](Applications/Noise_Cal.md#DisplaySmithChart)

  * [Ecal Temperature Query](Programming/New_Programming_Commands.md#ECalTemperatureQuery)

  * [Generic Ecal Control commands which supports multi-port Ecal (over 4 ports)](Programming/GP-IB_Command_Finder/Control.md#EcalPathState)

  * [Added capability to turn off noise receiver pulling during calibration](Applications/Noise_Cal.md#MeasNoiseParams)

  * [Added support for importing Python files into the equation editor](S4_Collect/Equation_Editor_Import_Functions.md#Import)  
(See also, [Equation Editor and
Python](S4_Collect/Equation_Editor_with_Python.htm))

  * [Hybrid Source enhancements](System/Configure_a_Hybrid_Source.md#External_Device_Hybrid_SSB_Mixer)

  * Added Pulse Timing dialog for Standard measurements

  * [Added LO Phase Calibration adjustment](Support/LO_Phase_Calibration.md)

  * [X-axis Annotation setting for All or ActiveTrace](S1_Settings/Customize_Your_Analyzer_Screen.md#XaxisAnntationForAllTrace)

### What's New in VNA Code Version A.17.35.xx

  * [Include Loss](Applications/Enhanced_Time_Domain_Analysis/Setting_Up_the_Measurement/Performing_Error_Corrections.md#Full_CalibrationECal) in TDR fixture compensation 

  * (S9x029B, Licensed Feature) [Macro Control for NF measurement path switching](Programming/GP-IB_Command_Finder/Sense/Noise.md#SweMacrFilRNP)

### What's New in VNA Code Version A.17.20.xx

  * [Focus Tuner support with Noise Figure Application](Applications/Noise_Figure.md#Noise_Figure_Option_027)

  * [New SMU (PZ2100A, PZ2121A, PZ2131A) Support ](System/Configure_an_External_Device.md)

  * [SCPI Recorder](Programming/SCPI_Recorder.md)

  * [Multiple Memory Traces](S4_Collect/Math_Operations.md#Data-_New_Trace)

  * [Segment Trigger](S1_Settings/Trigger.md#TriggerDiag) (PNA only)

  * [IO Control Per Segment](S1_Settings/Sweep.md#Handler_Port_A) (PNA only)

  * [Calset Property Dialog shows more information](S3_Cals/Cal_Sets.md#CalSetProps)

  * [Cal Kit Editor Change](S3_Cals/Translating_8510_Models.md)

  * [Improved Edit Visa Address](System/Configure_an_External_Device.md#Edit_VISA_Address_dialog_box_help)

  * [MOD/X DC trace](Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md)

  * [Save and Recall Calibration Configuration](S3_Cals/Calibration_Wizard.md#Calibration_Summary)

  * [DUT SNP simulation for SMC and GCA /GCX](S0_Start/Simulator.md) (Simulator only)

  * [ECal emulation on VNA simulator](S0_Start/Simulator.md) (Simulator only)

### What's New in VNA Code Version A.17.10.xx

  * Added [Noise-Figure Option E29](Applications/Noise_Figure.md#OptionsExplained) (low-noise receivers to 67 GHz) for the N5247B

### What's New in VNA Code Version A.17.00.xx

  * [Trace statistics for Smith Chart format can also be displayed in units of impedance (ohms)](S4_Collect/Math_Operations.md#StatisticsDialog)

  * [Added compacting and max NMSE to Dynamic Gain model details](Applications/Modulation_Distortion/Create_DPD.md#Model_Details_dialog_help)

  * [Added a Hybrid Source driver, which combines a source and a mixer to create a high-frequency source. This new driver selection appears the External Device Configuration dialog.](System/Configure_an_External_Device.md)

### What's New in VNA Code Version A.16.20.xx

  * [Added new SCPI Example Programs in Python Environment](Programming/GPIB_Example_Programs/SCPI_Example_Programs.md#SCPI_Example_Programs)

  * Modulation Distortion Enhancements:

    * [Added Ideal Wave Trace](Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md#New_Trace_Dialog)

    * [Added Nominal DUT NF](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#Nominal_DUT_NF)

    * [Added PAPR prioritization for Compact Modulation](Applications/Modulation_Distortion/Create_Modulation_Files.md#Peak-to-Avg)

    * [Auto Save VSA state within VNA state file](Applications/Modulation_Distortion/Link_VNA_to_89600_VSA.md#Auto_Save_VSA_state_within_VNA_state_file)

  * [IMD Multiple Receiver Configurations](Applications/Swept_IMD.md#Receiver_Configuration) [requires active Option S9x087A/B KeysightCare subscription]

  * [Actual Wave and 8-term error correction method in IMD/IMDX](S3_Cals/Guided_Power_Calibration.md#8-term_error_correction) [requires active Option S9x087A/B KeysightCare subscription]

  * [Added Dynamic Gain in Digital Predistortion (DPD)](Applications/Modulation_Distortion/Create_DPD.md#_Create_Modeled_DPD_procedure_with_Dynamic_Gain_DPD_model.)

  * [Support DPD in Modulation Distortion Converters Measurement Class (MODX)](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#Create_DPD)

  * [Multi-sensor Power Calibration for SMC/GCX](FreqOffset/SMC_Measurements.md#Use_Multiple_Sensors) [requires active Option S93082B, S93083B, or S93086B KeysightCare subscription]

### What's New in VNA Code Version A.15.75.xx

  * [Digital Predistortion (DPD)](Applications/Modulation_Distortion/DPD_Overview.md) [requires active Option S93070xB KeysightCare subscription]

  * [Digital Modulation Creation](Applications/Modulation_Distortion/Create_Modulation_Files.md#Create_Modulation) [requires active Option S93090xB or S93070xB KeysightCare subscription]

  * N5291A170 (170 GHz) and N5291A220 (220 GHz) Millimeter Wave Broadband Measurements Systems

  * [Added embedded LO setup to SMC Mixer Setup dialog](Applications/MixerConverter_Setup.md#Embedded_LO)

  * Single Port EVM Analysis for Modulation Distortion Measurements [requires active Option S93070xB KeysightCare subscription]

    * [8 parameters to Distortion Table](Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md#EVM_tab)

    * [4 parameters to Measurement Parameters](Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md#Distortion_Tab_Measurement_Parameters)

  * [NF Automatic Switch Control](Applications/Noise_Figure.md#Using_External_Switches_in_the_Noise_Figure_Application) [requires active Option S93029B KeysightCare subscription]

  * Added [four new Windows types](Applications/Enhanced_Time_Domain_Analysis/Making_Measurements/Setting_Up_Parameters_on_Each_Trace.md#Window) for TDR [requires active Option S93010B or S93011B KeysightCare subscription]

### What's New in VNA Code Version A.15.65.xx

  * [Cal Update](S3_Cals/Drift_Calibration.md) [Licensed Feature]

  * [Absolute Phase](FreqOffset/SMC_plus_Phase.md#HowEnableSMCPhase) (SMC + Phase)

  * [4 GHz Analysis Bandwidth](Support/Configurations.md#S93051B) (Option S93051B)

  * [Autotune Spectrum](Applications/Modulation_Distortion/Link_VNA_to_89600_VSA.md#Spectrum_Autoset) (VSA Setup dialog)

  * Added Preference

    * [Cal: Use Unknown thru math for SOLT methods](System/Preferences.md#Cal:_Use_Unknown_thru_math_for_SOLT_methods)

### What's New in VNA Code Version A.15.60.xx

  * Support N755xA ECal modules

  * Support L8990M Switch matrix [Licensed Feature]

  * Modulation Distortion

    * Add support for 8-term correction

### What's New in VNA Code Version A.15.55.xx

  * Spectrum Analyzer Application Enhancements

    * [Enable Phase Stitching from hardware time stamps](Applications/Spectrum_Analyzer.md#Enable_Phase_Stitching_from_HW_timestamps)

    * [Compute SA Time Domain IQ](Applications/Spectrum_Analyzer.md#Compute_Time_Domain_IQ)

    * [Export IQ Data](Applications/Spectrum_Analyzer.md#Export_IQ_data)

  * [Link VNA to 89600 VSA](Applications/Modulation_Distortion/Link_VNA_to_89600_VSA.md)

  * [Internal Source Modulation](S1_Settings/Internal_Source_Modulation.md)

  * [Noise Calibration Source Temperature](Applications/Noise_Cal.md#Source_Temperature)

  * [Window Type](Time/TimeDomain.md#WindDiag) added to Time Domain Setup dialog [Licensed Feature]

### What's New in VNA Code Version A.15.40.xx/A.15.50.xx

  * [Save/Load mixer files in CSV format](Applications/MixerConverter_Setup.md#CSV_Files) [Licensed Feature]

  * Smart Cal Ports

    * [Use existing SrcCal when measuring cal standards](S3_Cals/Calibration_Wizard.md#GuidedSelCalType)

  * Pulse Setup Primary Clock

  * Support for [U1832A/B/C/D and U1833A/B/C/D Noise Sources](Applications/Noise_Figure.md#NoiseSource) [Licensed Feature]

### What's New in VNA Code Version A.15.30.xx

  * [Software Support Licensing](Support/Software_Support.md)

  * [AFR Config and 2X Thru for N port](S3_Cals/Auto_Fixture_Removal.md#Specify)

  * [Updates to Fixture Simulator](S3_Cals/Fixture_Simulator.md#FGMain)

  * Compensate Only For De-Embeds (Fixture Generator)

  * [Modulation Distortion: Select font size of the Distortion Table](Applications/Modulation_Distortion/Displaying_Distortion_Parameters.md#Font_Size)

### What's New in VNA Code Version A.15.05.xx

  * [SA Phase Stitching](Applications/Spectrum_Analyzer.md#Compute_Phases)

  * Added function to [Phase functions](Applications/Gain_Compression_Application.md#CompressionTab) for Gain Compression / Gain Compression for Converters applications

### What's New in VNA Code Version A.15.00.xx

  * Support for CPU 3.5

  * Added [20 MHz Reference](S1_Settings/Reference.md)

  * Added [PathWave Calibration Advisor](GUI_Reference/System.md#PahtWave_Calibration_Advisor)

  * [IF Response Adjustment](Support/Adjust_Overview.md#IF_Response_Adjustment) (applies ONLY to instruments with new DDS source)

### What's New in VNA Code Version A.14.80.xx

  * [IF BW Shape](S2_Opt/Trce_Noise.md#IFBW_Shape)

  * Enhance the [Fixture Simulator](S3_Cals/Fixture_Simulator.md)

  * [LO Feedthru Monitor](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#LOFeedthuMonitordialog)

  * [Simulator](S0_Start/Simulator.md) (Option S94050B and S94051B)

  * [Residual Noise](Applications/Phase_Noise/Configuring_Phase_Noise.md#Noise_Type)

  * [Option S93072B Arbitrary Waveform Generation on XSB Port](Support/Configurations.md#S93072B)

  * Added [Ext. Source Port](S1_Settings/Phase_Control.md#Ext_Source_Port) to Phase Control

  * Added [Phase Control functions](Applications/Differential_IQ.md#SourceConfigurationDiag) to Differential I/Q application

  * Added [Phase functions](Applications/Gain_Compression_Application.md#CompressionTab) to Gain Compression / Gain Compression for Converters applications

  * Support for [P9336a + PSG external driver](System/Configure_an_External_Device.md#driver) (P9336A USB I/Q Arbitrary Waveform Generator with E8267D PSG Vector Signal Generator)

  * Support for Waveguide Cal Kits

### What's New in VNA Code Version A.14.60.xx

  * [Multiline TRL Calibration](S3_Cals/Multiline_TRL_Calibration.md)

  * Support for [P9336A USB I/Q Arbitrary Waveform Generator](System/Configure_an_External_Device.md#P9336A)

  * Support for [USB Noise Source](Applications/Noise_Figure.md#NoiseSource)

  * [Connecting with PathWave Vector Signal Analysis (89600 VSA)](Applications/Vector_Signal_Analyzer_for_PXIUSB.md)

  * [Edit Multitone](Applications/Modulation_Distortion/Create_Modulation_Files.md#Edit_Multitone)

### What's New in VNA Code Version A.14.40.xx

  * [Phase Noise](Applications/Phase_Noise/Overview.md) application (Option S93031xB )

  * Modulation Distortion application enhancements:

    * [Power Sweep](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#Power_Sweep)

    * [LO Feedthru Cal](Applications/Modulation_Distortion/Modulation_Flatness_and_Power_Calibration.md#Modulation_Cal_Setup)

  * [Global Source](S1_Settings/Global_Source.md)

  * [TMSA Enhancements](S1_Settings/Measurement_Parameters.md#topology)

  * [Drivers for External Compound Sources](System/Configure_an_External_Device.md#Compound_Sources)

### What's New in VNA Code Version A.14.20 .xx

  * Support for 64 bit 835x application

  * [Option XSB 3rd RF Source](Support/Configurations.md#XSB) (can be enabled by firmware license and requires Option 422 or 423)

  * [Option UNY Enhanced Phase Noise](Support/Configurations.md#UNY) (can be enabled by firmware license)

  * [Point leveling mode for receiver leveling](S1_Settings/Receiver_Leveling.md)

  * [Up to 500 Windows](S0_Start/Traces_Channels_and_Windows.md#window)

  * [Up to 100 Traces per Window](S0_Start/Traces_Channels_and_Windows.md#window)

  * [Enhancements to Correction Methods](S3_Cals/Guided_Power_Calibration.md#MatchingDialog)

  * [Enhancements to Balanced Setup](S1_Settings/Measurement_Parameters.md#topology)

  * [Enhancements to Integrated True Mode Stimulus Application](Applications/iTMSA.md#BalancedTopDiag) (iTMSA)

  * [Frequency Reference](S1_Settings/Reference.md)

### What's New in VNA Code Version A.13.95.xx

  * [Modulation Distortion Converters](Applications/Modulation_Distortion/Modulation_Distortion_Settings.md)

  * [AM Distortion](S4_Collect/Math_Operations.md#AM_Distortion)

  * [Trace deviation](S4_Collect/Math_Operations.md#Trace_Deviation)

### What's New in VNA Code Version A.13.80.xx

  * [Modulation Distortion](Applications/Modulation_Distortion/Overview.md) application enhancements (Option S93070xB)

  * [Receiver IF Cal](Applications/Modulation_Distortion/Delta_IF_Cal.md) for Modulation Distortion measurements

  * [Modulation Distortion Swept Cal Power](Applications/Modulation_Distortion/Modulation_Flatness_and_Power_Calibration.md#Cal_Power_Type:)

  * [Cal All - Split Cal and Independent Calibration Channels](S3_Cals/Calibrate_All_Channels.md#Split_Cal_and_Independent_Calibration_Channels)

### What's New in VNA Code Version A.13.60.xx

  * [Modulation Distortion](Applications/Modulation_Distortion/Overview.md) application (Option S93070xB)

  * [DC limits added to SMART Sweep Safe Mode](Applications/Gain_Compression_Application.md#Safe)

  * [Spectrum Analysis enhancements - dual-band configuration](Applications/Spectrum_Analyzer.md#Dual-Band_Configuration)

  * [Device Expert (DE)](S1_Settings/Device_Measurement_eXpert_Lite_\(DMX\).md)

  * [Mechanical Counter](Support/Mechanical_Counter.md)

### What's New in VNA Code Version A.13.55.xx

  * [TDR mode frequency limits](Applications/Enhanced_Time_Domain_Analysis/Setting_Up_the_Measurement/Performing_Manual_Setup.md#Freq_Limits_Config)

  * [Noise Figure Option S93027B](Applications/Noise_Figure.md#Noise_Figure_Option_027) (directly control mechanical tuners)

  * Support for U205xXA/U206xXA Series USB Power Sensors

### What's New in VNA Code Version A.13.50.xx

  * [Noise Power Ratio measurements](S1_Settings/Noise_Power_Ratio_\(NPR\)_Settings.md)

  * Support for new [Low Frequency Extension options](IFAccess/Low_Frequency_Extension/Overview.md#Model_Compatibility)

  * Banded millimeter wave [installation calibration](IFAccess/N5290A-91A_mmWave_Configuration/Calibration.md#Banded_RF_Cal)

  * [Calibration with power meter uncertainties](System/Configure_a_Power_Meter_As_Receiver.md#Power_Meter_Uncertainties)

  * New [SA Analysis Markers](S4_Collect/Markers.md#Spectrum_Analyzer_Marker_Search)

  * [TDR mode frequency limits](Applications/Enhanced_Time_Domain_Analysis/Setting_Up_the_Measurement/Performing_Manual_Setup.md#Freq_Limits_Config)

  * Support for Windows 10

### What's New in VNA Code Version A.13.25.xx

  * [1-port balanced measurements for iTMSA](Applications/iTMSA.md#BalancedTopDiag)

  * [Support for external DC meter for SA channel measurements](Applications/Spectrum_Analyzer.md#HowMeasParams)

  * [Active Hot Parameters](Applications/Active_Match.md) application (Option S93110A/B, S93111A/B)

  * [Support for VDI PM5 power meter](System/Install_VDI_Drivers.md)

### What's New in VNA Code Version A.13.20.xx

  * [Enhanced Time Domain Analysis (Option S93011A/B)](Applications/Enhanced_Time_Domain_Analysis/Enhanced_Time_Domain_Analysis.md)

### What's New in VNA Code Version A.13.00.xx

  * Support for Windows 10 operating system

### What's New in VNA Code Version A.12.90.xx

  * Multi-dimensional sweep on a spectrum analyzer channel

    * SCPI

    * [COM](Programming/COM_Reference/Objects/MultiDimensionalSweep_Object.md)

  * [CalPod temperature correction](S3_Cals/CalPod.md#SetupDiag)

  * [*ESR? sweep complete programming example](Programming/GPIB_Example_Programs/_ESR__Sweep_Complete.md)

### What's New in VNA Code Version A.12.85.xx

  * [Independent Power Calibration](S3_Cals/Calibrate_All_Channels.md#Setting_Up_an_Independent_Power_Calibration)

  * [Automatic Fixture Removal](Programming/GP-IB_Command_Finder/Automatic_Fixture_Removal_\(AFR\).md) (AFR) SCPI commands

  * Maximum channels increased to 500

  * Added [ISegment3](Programming/COM_Reference/Objects/Segment_Object.md) and [ISegments6](Programming/COM_Reference/Objects/Segments_Collection.md) interface commands

### What's New in VNA Code Version A.12.80.xx

  * N5290A/N5291A Broadband Network Analyzer

  * [Low Frequency Extension](IFAccess/Low_Frequency_Extension/Low_Frequency_Extension.md) (Option 205/425)

  * [Spectrum Analyzer](Applications/Spectrum_Analyzer.md) Coherence and Data export features

### What's New in VNA Code Version A.12.70.xx

  * Modernized Graphical User Interface

  *     * [Icons for adding or deleting trace/channel](S1_Settings/Customize_Your_Analyzer_Screen.md#Tools)

    * [Tabbed soft panel enabling quick access to desired functions](S1_Settings/Customize_Your_Analyzer_Screen.md#Softkey)

    * [Access popup menus with long press or right click](Front_Panel/XScreen.md#Windows)

    * [Drag & drop trace/channel/window with finger or mouse](Front_Panel/XScreen.md#Windows)

    * Easily make [complex setups](S0_Start/QuickStart_Dialog.md#S-Parameter_Dialog) and [calibrations](S3_Cals/Calibration_Wizard.md) using Wizards

    * [Customize the icons to display in the top and bottom areas](S1_Settings/Customize_Your_Analyzer_Screen.md#ToolsDialog)

    * [Register frequently-used softkeys to Favorite menu](S1_Settings/Customize_Your_Analyzer_Screen.md#Favorite)

    * [Group windows into Sheets](S0_Start/Traces_Channels_and_Windows.md#Sheet)

    * [Magnify (zoom) a portion of the display](S1_Settings/Scale.md#Magnify_Mode)

  * [Copy setups and user calibration data to other channels](S1_Settings/CopyChannels.md)

  * [Improved Segment sweep](S1_Settings/Sweep.md#segment)

  * Marker Search

  *     * [Peak Search](S4_Collect/Markers.md#PeakSearch)

    * [Multi-Peak Search](S4_Collect/Markers.md#MultiPeakSearch)

    * [Target Search](S4_Collect/Markers.md#TargetSearch)

    * [Multi-Target Search](S4_Collect/Markers.md#MultiTargetSearch)

    * [Bandwidth Search](S4_Collect/Markers.md#Bandwidth)

    * [Notch Search](S4_Collect/Markers.md#Bandwidth)

  * Unique limit test functions

  *     * [Ripple limit](S4_Collect/Use_Ripple_Limit_Test.md)

    * [Bandwidth limit](S4_Collect/Use_Bandwidth_Limit_Test.md)

    * [Point limit](S4_Collect/Use_Limits_to_Test_Devices.md#Point_Limit_Test)

  * [SCPI Parser Console for monitoring remote interface](Programming/Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.md#console)

  * [Port subset correction (devolve calibration)](S3_Cals/Port_Subset_Correction.md)

  * [Spectrum Analyzer](Applications/Spectrum_Analyzer.md) enhanced features

  * Power Range [SCPI](Programming/GP-IB_Command_Finder/SystCapability.md#POWerRange) and [COM](Programming/COM_Reference/Objects/Power_Range_Object.md) commands

### What's New in PNA Code Version A.10.49.09

  * [Cal All Channels SCPI programming examples](Programming/GPIB_Example_Programs/Perform_a_CalAllChannels_Calibration.md)
  * [Apply to all channels button in Calibrate All Selected Channels dialog](S3_Cals/Calibrate_All_Channels.md#SelectChansDiag)

### What's New in PNA Code Version A.10.49.07

  * [Support for N755xA ECal modules](S3_Cals/Using_ECal.md)

### What's New in PNA Code Version A.10.49.05

  * [Read DC at Compression Point in Smart Sweep](Applications/Gain_Compression_Application.md#ReadDCatCompressionPoint)
  * [Memory Interpolation](S4_Collect/Math_Operations.md#MemoryTraceInterpolation)
  * CalPod options (301, 302, and 304) are now standard
  * [CalPod - OSL Averages](S3_Cals/CalPod.md#OSL_Averages)
  * [CalPod - VNA CalPod Utilities](S3_Cals/CalPod.md#Utilities)

### What's New in PNA Code Version A.10.49

  * [SA Power Sweep](Applications/Spectrum_Analyzer.md#Type__Sweep)

  * [DC Source Sweep](Applications/Spectrum_Analyzer.md#DC_Sources)

  * [SA Gated Measurement Quick Setup](Applications/Gated_Measurement.md#Quick_Setup)

### What's New in PNA Code Version A.10.45

  * [Gated SA](Applications/Spectrum_Analyzer.md#Gated_SA)

  * [SA broadband and banded millimeter-wave measurements](IFAccess/External_Test_Head_Configuration.md)

  * [Support for Spectrum Analyzer measurements on PNA-L](Applications/Spectrum_Analyzer.md)

  * [Cal All for millimeter wave measurement classes](IFAccess/External_Test_Head_Configuration.md#Cal_All_Wizard)

  * Support for UXG signal generators

* * *

### What's New in PNA Code Version A.10.40

  * [Spectrum Analyzer Application](Applications/Spectrum_Analyzer.md)

  * [Dynamic Uncertainty for S-Parameters](S3_Cals/Dynamic_Uncertainty.md)

  * [Frequency Step Setting](S1_Settings/Frequency_Range.md#StartDiag)

  * [15 General-Purpose Markers per Trace](S4_Collect/Markers.md#Number_of_Markers)

  * [Marker Symbols Above Trace](S4_Collect/Markers.md#DisplayDiag)

  * [Noise Marker Format](S4_Collect/Markers.md#marker_format)

  * [Coupled Markers Method](S4_Collect/Markers.md#Coupled_Markers)

  * [Limit Line Pass/Fail Indicator Positioning](S4_Collect/Use_Limits_to_Test_Devices.md#Limitdiag)

  * [Trace Hold](S0_Start/Traces_Channels_and_Windows.md#Trace_Hold)

### Preferences

  * [Treat Marker 10 as Reference Marker](System/Preferences.md#markerPref)

  * [Draw Limit Lines in Red](System/Preferences.md#RedLimitLines)

  * [Coupled Markers](System/Preferences.md#CoupledMarkers) (3 preferences)

* * *

### What's New in PNA Code Version A.10.25

  * [Differential IQ](Applications/Differential_IQ.md)

  * [Narrowband Compensation](Applications/Noise_Figure.md#NarrowbandCompensation) to Noise Figure measurements

  * [CPM Direct Receiver Calibration](S3_Cals/CPM_Direct_Receiver_Calibration.md)

* * *

### What's New in PNA Code Version A.10.20.03

  * [Cal All for External Sources](S3_Cals/Calibrate_All_Channels.md#Features)

  * [Narrowband Compensation for Noise Figure](Applications/Noise_Figure.md#NarrowbandCompensation)

* * *

### What's New in PNA Code Version A.10.20

  * [Cal Plane Manager](S3_Cals/Cal_Plane_Manager.md)

  * [Auto Fixture Removal](S3_Cals/Auto_Fixture_Removal.md)

* * *

### What's New in PNA Code Version A.10.15

  * New N5249A PNA-X model ([Configuration](Support/Configurations.md#PNAX) | [Specs](Specs/ManualChoice.md))

* * *

### What's New in PNA Code Version A.10.00

  * [Windows® Embedded Standard 7](S0_Start/Windows_Considerations.md)

  * [HiSLiP](Programming/Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.md#SICL)

  * [Integrated CalKit Editor](S3_Cals/ModifyCalKits.md)

  * [Increased Number of Points to 100K](S1_Settings/DPoints.md#PointsDiag)

  * [Cal Kits saved and recalled using *.xkt format](S3_Cals/VNA_Cal_Kit_File_Types.md)

  * [U8480 Power Sensors Supported](S3_Cals/PwrCalibration.md#TestEquipmentRequired)

  * [Mechanical Devices: Copy Active Channel](System/Mechanical_Devices.md#MechanicalDialog)

  * [Search Within (for Markers)](S4_Collect/Markers.md#SearchWithin)

  * [Dialog Transparency](System/Dialog_Transparency.md)

  * Move App to Back

  * [System time on PNA Status Bar](S1_Settings/Customize_Your_Analyzer_Screen.md#clock)

  * [Right-click menus on Status Bar](S1_Settings/Customize_Your_Analyzer_Screen.md#StatusBar)

  * [Elimination of 3 Toolbars](S1_Settings/Customize_Your_Analyzer_Screen.md#toolbars)

  * [Enhanced MATLAB® funtionality](S4_Collect/Equation_Editor_and_MatLab.md)

* * *

### What's New in PNA Code Version A.09.90

  * [SMC Phase Reference Cal from 10 MHz](FreqOffset/Phase_Reference_Calibration.md#UnknownMixerHow)

  * [CalPod as ECal](S3_Cals/CalPod_as_ECal.md)

  * [External SMU Device](System/Configure_an_External_SMU.md)

  * Equation Editor enhancements

  *     * [New marker functions](S4_Collect/Equation_Editor.md#Functions)

    * [Use Short Names](S4_Collect/Equation_Editor.md#EquationDialog)

* * *

### What's New in PNA Code Version A.09.85

  * [Support for U2020 X-Series USB Power Sensors](S3_Cals/PwrCalibration.md#TestEquipmentRequired)

  * [Delta Match Calibration](S3_Cals/Delta_Match_Calibration.md) required on ALL N5231A, N5232A, and N5239A models.

  * [Unguided TRL Cal](S3_Cals/Calibration_Wizard.md#unguided) allowed on all PNA 4-port models

  * [Noise Parameters](Applications/Noise_Figure.md#NoiseParams)

### What's New in PNA Code Version A.09.80

  * ### Standard Measurements

  *     * [Calibrate All Channels](S3_Cals/Calibrate_All_Channels.md)

    * [SE => Balanced Topology](S1_Settings/Measurement_Parameters.md#topology)

    * [Increased Segments in Power Sensor Loss Table](S3_Cals/PwrCalibration.md#pLossCompIm)

    * [EXG Sources supported](System/Configure_an_External_Source.md#add_new_source)

    * [CalPod](S3_Cals/CalPod.md)

  * ### Application Enhancements

  *     * [SMC with Phase Reference](FreqOffset/Phase_Reference_Calibration.md)

    * [Noise Receiver Cal with Power Sensor](Applications/Noise_Cal.md#CalibratingReceiver)

    * [PNA models with 50 GHz Noise Receivers](Applications/Noise_Figure.md#50GHz)

* * *

### What's New in PNA Code Version A.09.60

  * New [N523xA models](Support/Configurations.md#N523x)

* * *

### What's New in PNA Code Version A.09.50

### Standard Measurements

  * [Unguided Cals can access 95 Cal Kits](S3_Cals/Calibration_Wizard.md#Select_V1_Cal_Kit_help)

  * [Preference setting to list Recall files](S5_Output/SaveRecall.md#file_recall)

  * [YouTube Videos](Tutorials/Videos.md)

  * [Display Menu changes](S1_Settings/Customize_Your_Analyzer_Screen.md)

  * [Undo/Redo](S1_Settings/Undo.md)

  * [Quick Start](S0_Start/QuickStart_Dialog.md)

  * [Quickly change Scale, Reference Level, and Position](S1_Settings/Scale.md#ScaleDiag)

  * [Redesigned Receiver Leveling dialog](S1_Settings/Receiver_Leveling.md)

  * New External Device configuration:

  *     * [Pulse Generators](System/Configure_an_External_Pulse_Generator.md)

    * [DC Sources and Meters](System/Configure_a_DC_Device.md)

    * [DC Source Control dialog](S1_Settings/DC_Control.md)

### Application Enhancements

  * External Pulse Generator in Integrated Pulse App

  * [IMSpectrum in mmWave](IFAccess/External_Test_Head_Configuration.md)

* * *

### What's New in PNA Code Version A.09.42

May 2013: [Support for U2020X Power
Sensors](S3_Cals/PwrCalibration.htm#TestEquipmentRequired)

* * *

  * [New N522x Models](Support/Configurations.md#N522x)

### Standard Measurements - available on all Models / Options

  * [Drag a trace to another window](Front_Panel/XScreen.md#Traces)

### Application Enhancements

  * [Copy Channels on all Applications](S1_Settings/CopyChannels.md)

  * ["Src 2 out Port 2" factory configuration on PNA-X Opt 423](S1_Settings/Path_Configurator.md#FactoryConfigs).

  * [IMD f2 Tone using External Source / Combiner](Applications/Swept_IMD.md#ConfigureDiag)

  * [IMD and IM Spectrum Tone Power Leveling settings](Applications/Swept_IMD.md#powerLeveling)

  * [IMD, IMDx, and IM Spectrum "Min" and "Max" parameters](Applications/Swept_IMD.md#ToneSelect)

  * [Use a Power Table with mmWave SMC Measurements](IFAccess/External_Test_Head_Configuration.md#Leveled)

  * [mmWave; Mixer mode - 2-port test set on 4-port PNA](IFAccess/External_Test_Head_Configuration.md#mixerHardware)

  * [Guided Power Cal for SMC](FreqOffset/SMC_Measurements.md#PowerCalSettings)

  * [ESG and PSG Sources for Phase Control](S1_Settings/Phase_Control.md#FeaturesLimitations)

* * *

### What's New in PNA Code Version A.09.33

### New Options

  * [Source Phase Control](S1_Settings/Phase_Control.md) \- Opt 088

### Application Enhancements

  * [FCA Update](FreqOffset/FCA_Use.md) \- Opt 082, and 083

### Standard Measurements - available on all Models / Options

  * [Security for External Sources](System/Frequency_Blanking.md)

  * 2-Port and 4-Port Fixture Extrapolation and Reverse Ports.

  * [Phase Coherent "R over R" measurements](S1_Settings/Phase_Coherent_Measurements.md)

  * [Use Multiple Power Sensors for Guided Power Cal](S3_Cals/Guided_Power_Calibration.md#PowerCalSettings)

  * [Perform Source Power Cal with PMAR Device](S3_Cals/PwrCalibration.md#Options)

Tip \- Do you access the same PNA dialog often? Your Favorites are always two
keystrokes away.  
---  
  
* * *

### What's New in PNA Code Version A.09.31

  * ### [Support for N1913A and N1914A Power Meters](System/Configure_a_Power_Meter_As_Receiver.md)

* * *

### What's New in PNA Code Version A.09.30

  * [N5247A - 67 GHz PNA-X](Support/Configurations.md#PNAX)

### Application Enhancements

  * [Gain Compression on Converters](Applications/Gain_Compression_for_Converters.md) (GCX)

  * [Support for Dual-Stage Converters in all Apps](Applications/MixerConverter_Setup.md)

### Standard Measurements - available on all Models / Options

  * [Enhanced S-parameter Power Cal](S3_Cals/Guided_Power_Calibration.md)

  * [Marker Display enhancements](S4_Collect/Markers.md#Display)

  * [Perform Source Power Cal at multiple power levels](S3_Cals/PwrCalibration.md#Options)

  * [IF Gain Setting](IFAccess/IF_Path_Configuration.md#IFPathConfigDiag)

  * [Receiver Overload/Compression Warning](System/Preferences.md#RcvrOverload) and [Power OFF](System/Preferences.md#SourceOFFOverload) Preferences

  * [Confirm changes on Meas Class dialog](S1_Settings/Measurement_Classes.md#StartDiag)

  * [DSP Version 5](S0_Start/HelpAbout.md#DSPchanges)

* * *

### What's New in PNA Code Version A.09.22

  * [Use any PNA-X Ports with Noise Figure Opt 028](Applications/Noise_Figure.md#Power).

* * *

### What's New in PNA Code Version A.09.20

### Application Enhancements

  * Integrated Pulse Measurements (Opt 008)

  * [Noise Figure using Standard PNA Receiver](Applications/Noise_Figure.md#OptionsExplained) (Opt 028)

  * [Noise Figure on N5244A/45A](Applications/Noise_Figure.md#OptionsExplained) (Opt H29)

  * [Edge and Level Trigger in Pulse](IFAccess/IF_Path_Configuration.md#PulseGens)

  * [Exclude SC12 Sweep for SMC (Opt 082/083)](FreqOffset/SMC_Measurements.md#SMCapplyChoices)

  * [Include Phase with SMC](FreqOffset/SMC_Measurements.md#Phase) (PNA-X with Opt 083)

  * Fixturing in Apps

  * [Max Output Power for GCA](Applications/Gain_Compression_Application.md#Safe) (Opt 086)

### Standard Measurements - available on all Models / Options

  * [Mechanical Device conflicts cause Channel Block (NOT Channel Hold)](System/Mechanical_Devices.md)

  * [PSAT Marker and Power Normal Operating Point Marker](S4_Collect/Markers.md#AboutPSATnPNOP)

  * [Group Delay Aperture Setting](Tutorials/Group_Delay6_5.md#group)

  * [Active Background Display Color](System/Display_Colors.md#dispColorDiag)

  * [Solid or Dotted Grid Lines](S1_Settings/Customize_Your_Analyzer_Screen.md#GridLines)

  * [Point Sweep on PNA C Models](S1_Settings/Sweep.md#pointSweep)

  * Fixture Power Compensation

  * [Sweep Delay](S1_Settings/Sweep.md#SweepSetupDiag)

  * [Uncertainty equations using RSS Computations](Specs/u_curve_equations.md)

  * [Preset Power Preference Setting](System/Preferences.md#PresetPower)

  * [Use Last Receiver Leveling Correction for SPC](S1_Settings/Receiver_Leveling.md#RecLevelDiag)

  * Data Save Enhancements

  *     * [Recall .SNP files to view as trace](S5_Output/SaveRecall.md#RecallingCTI)

    * ["Save Data As" Dialog](S5_Output/SaveRecall.md#SaveDataAs)

    * [Save Balanced Data as SNP files](S5_Output/SaveRecall.md#ChoosePorts)

  * Characterize Adaptor Macro Rev. A.02.10

  *     * Reverse S2P

    * Load the PNA Power Loss Table from an existing S2P file

* * *

### What's New in PNA Code Version A.09.10

  * [Noise Figure on Converters (NFX)](Applications/Noise_Figure_on_Converters.md)

  * [AgileUpdate for Customer Releases](Support/FW_upgrade.md#AgileUpdateDiag)

  * [New Help, About Capabilities](S0_Start/HelpAbout.md)

* * *

### What's New in PNA Code Version A.09.00

  * [External Device Configuration](System/Configure_an_External_Device.md)

  * [Power Meter as Receiver](System/Configure_a_Power_Meter_As_Receiver.md) (PMAR)

  * [Power Offsets and Limits](System/Power_Limit_and_Power_Offset.md)

  * [Display and Print Colors](System/Display_Colors.md)

  * [Scale Coupling](S1_Settings/Scale.md#ScaleCoupling)

  * [Mechanical Device Settings](System/Mechanical_Devices.md)

  * [Device side USB](Programming/Learning_about_GPIB/DeviceSide_USB.md)

  * [Increased Number of Channels to 200](S0_Start/Traces_Channels_and_Windows.md#channel)

  * [ECal User Chars Saved to PNA Disk Memory](S3_Cals/ECal_User_Characterization.md#DetailedUser)

### Application Enhancements

  * [GCA Compression Analysis](Applications/Gain_Compression_Application.md#Analysis)

  * [GCA Compression from Saturation](Applications/Gain_Compression_Application.md#CompFromSat)

  * [Receiver Leveling on IMD, FCA, and GCA](S1_Settings/Receiver_Leveling.md)

  * [Embedded LO on SMC and IMDx](Applications/Embedded_LO.md)

  * [Limited Port Mapping on IMD](Applications/SweptIMDLimitedPortMapping.md)

  * [Point Averaging on FCA and IMD](S2_Opt/Trce_Noise.md#averaging)

  * [SMC Measurements with mmWave Modules](IFAccess/External_Test_Head_Configuration.md#Mixer)

  * [mmWave Measurements with no Test Set](IFAccess/mmWave_Measurement_w_No_Test_Set.md)

* * *

### What's New in PNA Code Version A.08.60

  * [New 40 GHz and 50 GHz PNA-X Models](Support/Configurations.md#PNAX)

* * *

### What's New in PNA Code Version A.08.55

  * [IMDx (Swept and Spectrum) for Converters](Applications/IMD_App.md)

  * [ADC Measurements in a Gain Compression channel.](Applications/Gain_Compression_Application.md#ADC)

  * [New 13.5 GHz PNA-X Model](Support/Configurations.md#PNAX)

* * *

### What's New in PNA Code Version A.08.50

  * [Fast Antenna Features for the PNA-X](IFAccess/FIFO_and_other_Antenna_Features.md)

  * [Receiver Leveling](S1_Settings/Receiver_Leveling.md)

  * [Phase Sweep](Applications/iTMSA.md#PhaseSweep) in iTMSA

  * [Up to 25 User Macros](Programming/Using_Macros.md)

  * [Gain Compression Marker](S4_Collect/Markers.md#Compression)

  * [Port Extensions enhancements](S3_Cals/Port_Extensions.md)

  * [Electrical Delay enhancements](S2_Opt/Phase_Accy.md#ElectricalDiag)

  * [Extra Security enhancement](System/Frequency_Blanking.md#blankingDiag)

  * Save [*.CSV](S5_Output/SaveRecall.md#csv) and [*.MDF](S5_Output/SaveRecall.md#MDIF) File Types

  * Noise Figure App enhancements:

  *     * [Scalar Noise Figure measurement](Applications/Noise_Figure.md#Scalar)

    * [Incident Noise Power parameters](Applications/Noise_Figure.md#parameters)

  * MM Module enhancements:

  *     * [Power Level Control](IFAccess/External_Test_Head_Configuration.md#Leveled)

    * Supports [iTMSA](Applications/iTMSA.md)

  * [Max point count to 32,001](S1_Settings/DPoints.md#PointsDiag)

  * [Faster Power Sweeps](S1_Settings/Sweep.md#power)

* * *

### What's New in PNA Code Version A.08.35

  * [New N5264A model](IFAccess/N5264A.md)

* * *

### What's New in PNA Code Version A.08.33

  * [IMD Application](Applications/IMD_App.md) (Opt 087)

  * [Fast Sweep Mode](S1_Settings/Sweep.md#SweepSetupDiag)

  * [New Equation Editor functions](S4_Collect/Equation_Editor.md#Functions)

  * [20001 Segments in Power Loss Table](S3_Cals/PwrCalibration.md#LossCompDiag)

  * [Data Format Units](S1_Settings/Data_Format.md#FormatDiag)

  * [Marker=>CW Freq Function](S4_Collect/Markers.md#FunctionDiag)

  * [Up to 12 User Characterizations](S3_Cals/ECal_User_Characterization.md)

  * Characterize Adaptor Macro 2.0

* * *

### What's New in PNA Code Version A.08.20

  * [iTMSA](Applications/iTMSA.md)

  * [User Preferences dialog](System/Preferences.md)

  * [Uncoupled Power Sweep](S1_Settings/Power_Level.md#PwrSweep)

  * [Equation Editor Import Functions](S4_Collect/Equation_Editor_Import_Functions.md)

  * [Wider Traces Preference](Front_Panel/XScreen.md#Traces)

  * [24 Traces per Window](S0_Start/Traces_Channels_and_Windows.md#window)

  * [LXI Compliance](S0_Start/LXI_Compliance.md)

  * [GCA Enhancements](Applications/Gain_Compression_Application.md#WhatsNew)

  * [FCA - selectable ports](FreqOffset/FCA_Use.md#dutPorts)

  * [Support for N5261A and N5262A MM test sets](IFAccess/External_Test_Head_Configuration.md)

  * cXL Code Translation Software - Quick Link

* * *

### What's New in PNA Code Version A.08.00

  * [Noise Figure Application (Opt 029)](Applications/Noise_Figure.md)

  * [Gain Compression Application (Opt 086)](Applications/Gain_Compression_Application.md)

  * '[Sweep' Trigger Mode](S1_Settings/Trigger.md#TriggerMode)

  * [Custom Cal Window settings](S3_Cals/Calibration_Wizard.md#CalWindow) (remote only)

  * [New Equation Editor Functions](S4_Collect/Equation_Editor.md#Functions)

  * [Minimum Number of Points = 1](S1_Settings/DPoints.md#PointsDiag)

