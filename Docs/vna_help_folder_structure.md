# VNA_Help_MD Folder Structure and Description

## Root Directory: c:\Apps\Metis\Docs\VNA_Help_MD

## Summary

The VNA_Help_MD folder contains comprehensive documentation for Keysight VNA (Vector Network Analyzer) instruments. The documentation is organized in a logical workflow sequence (S0-S5) from getting started to output, along with specialized sections for applications, GUI reference, SCPI commands, tutorials, and support information. The structure follows a progression from basic to advanced topics, allowing users to find relevant information based on their needs and experience level.

## Documentation Structure

### Main Documentation Folders

#### Applications/
- **Description**: Contains documentation for various VNA applications and measurement classes
- **Contents**: Detailed guides for specialized measurements like Noise Figure, Gain Compression, Swept IMD, Spectrum Analysis, Phase Noise, Time Domain Analysis, etc.
- **Key Files**: Applications.md (overview of available application options), Noise_Figure.md, Gain_Compression_Application.md, etc.
- **Subfolders**:
  - **Enhanced_Time_Domain_Analysis/**: Provides advanced time domain measurement capabilities
    - **Contents**: Advanced mode operations, waveform analysis, eye diagrams, mask testing, and TDR (Time Domain Reflectometry) measurements
    - **Key Subfolders**: Advanced_Mode/, Advanced_Waveform_Analysis/, Eye_Diagram_and_Mask_Test/, Making_Measurements/, Measurement_Examples/, Overview/, Setting_Up_the_Measurement/, TDR_Quick_Start/
    - **Key File**: Enhanced_Time_Domain_Analysis.md
  
  - **Modulation_Distortion/**: Covers modulation distortion measurements and digital pre-distortion (DPD)
    - **Contents**: Setup procedures for amplifiers and converters, calibration methods, modulation file creation, and various modulation analysis techniques including EVM (Error Vector Magnitude) and ACP (Adjacent Channel Power)
    - **Key Files**: Overview.md, Modulation_Distortion_Measurement.md, DPD_Modeling.md, Set_Up_a_Converter.md, Set_Up_an_EVM_Measurement.md
  
  - **Phase_Noise/**: Documents phase noise measurement capabilities and techniques
    - **Contents**: Configuration, setup, and measurement procedures for phase noise, AM noise, spurious signals, and integrated noise
    - **Key Files**: Overview.md, Setting_Up_a_Phase_Noise_Measurement.md, Displaying_Phase_Noise_Parameters.md

#### FreqOffset/
- **Description**: Covers frequency offset measurements and frequency converting device measurements
- **Contents**: Documentation on Frequency Offset Mode, Frequency Converter Application (FCA), SMC/VMC measurements, and related calibration
- **Key Files**: Frequency_Offset_Mode.md, FCA_Use.md, SMC_Measurements.md

#### Front_Panel/
- **Description**: Provides information about the analyzer's front panel interface
- **Contents**: Front panel screen navigation, controls, and jumpers configuration
- **Key Files**: XScreen.md (front panel interface), XTour.md (front panel overview), FPJumpersChoice.md

#### GUI_Reference/
- **Description**: Comprehensive reference for all GUI elements and parameter settings
- **Contents**: Detailed documentation for all softkeys, dialogs, and settings organized by function
- **Key Files**: Freq.md, Meas.md, Cal.md, Power.md, Sweep.md, and many more covering each GUI section

#### IFAccess/
- **Description**: Covers IF (Intermediate Frequency) access and external test head configurations
- **Contents**: Information about connecting external test heads and IF access options
- **Key Files**: N5264A.md (external test head documentation)

#### Programming/
- **Description**: Comprehensive programming documentation for the VNA, including command references, example programs, and guides for remote control via different interfaces (COM, GPIB, SCPI)
- **Contents**: Programming guides, SCPI commands, example programs, and detailed documentation for various programming interfaces
- **Key Files**: Programming_Guide.md - Overview of VNA programming capabilities, Command_Finder.md - Tool for locating specific commands, Programming_Commands_History.md - Historical documentation of commands, Accessing_Data_Descriptions.md - How to access measurement data, New_Programming_Commands.md - Documentation for new commands
- **Subfolders**:
  - **COM_Reference/**: Contains the comprehensive COM object model documentation for VNA automation
    - **Subfolders**: Events/ - VNA COM event documentation, Methods/ - COM method references, Objects/ - COM object hierarchy and properties, Properties/ - Detailed COM property documentation
  
  - **COM_Example_Programs/**: Contains numerous example programs demonstrating how to control the VNA using COM automation
    - **Contents**: Examples for various measurement types (S-parameters, noise figure, IMD), calibration procedures, data retrieval, and advanced features
    
  - **GP-IB_Command_Finder/**: Organized SCPI command reference documentation for GPIB control
    - **Contents**: Commands grouped by functionality (Calculate, Display, Source, System, etc.)
    
  - **GPIB_Example_Programs/**: Extensive collection of SCPI-based programming examples in various languages
    - **Contents**: Examples for measurements, calibrations, instrument control, and data handling
    
  - **Learning_about_COM/**: Tutorials and guides for COM programming with the VNA
    - **Contents**: COM fundamentals, data types, event handling, and configuration
    
  - **Learning_about_GPIB/**: Tutorials and guides for GPIB/SCPI programming with the VNA
    - **Contents**: GPIB fundamentals, SCPI syntax, data retrieval, and Python basics
    
  - **VEE_Examples/**: Programming examples specifically for Agilent VEE
    - **Contents**: Basic control examples, calibration examples

#### Rear_Panel/
- **Description**: Information about the analyzer's rear panel connectors and interfaces
- **Contents**: Rear panel connection details for different VNA models
- **Key Files**: XRtour.md (PNA-X and N522xB), N523xRP.md (N523xB), XPulseIO.md, XPwrIO.md

#### Support/
- **Description**: Contains support, troubleshooting, and maintenance information
- **Contents**: Error messages, firmware upgrade, calibration procedures, system verification, and technical support contacts
- **Key Files**: Tshoot.md (troubleshooting), FW_upgrade.md, Licenses.md, PNA_Errors.md, SCPI_Errors.md, Tech_Supp.md

#### System/
- **Description**: System-level configurations and preferences
- **Contents**: System settings, preferences, and configuration options
- **Key Files**: Preferences.md, System_Topics.md

#### Time/
- **Description**: Covers time domain measurements and analysis
- **Contents**: Time domain capabilities and measurements
- **Key Files**: TimeDomain.md

#### Tutorials/
- **Description**: Tutorials and guides for various measurement techniques
- **Contents**: Step-by-step tutorials for specific measurements, application notes, and videos
- **Key Files**: Tutorials1.md (overview), App_Notes.md, Videos.md, NABasics.md, and various measurement tutorials

#### Assets/
- **Description**: Supporting media resources for the documentation
- **Contents**: Images, CSS stylesheets, JavaScript files, and miscellaneous resources
- **Subfolders**: css/, images/, js/, misc/

### Sequential Workflow Documentation (S0-S5)

#### S0_Start/
- **Description**: Getting started and initial setup information
- **Contents**: Quick start guide, basic operation, and initial configuration
- **Key Files**: Getting_Started.md, NewUsers.md, Meas_Seq.md, Using_Help.md, Connectivity.md

#### S1_Settings/
- **Description**: Configuration and setup procedures for measurements
- **Contents**: Information on setting measurement parameters, frequency range, power levels, etc.
- **Key Files**: Select_a_Measurement_State.md, Frequency_Range.md, Power_Level.md, Sweep.md, Trigger.md

#### S2_Opt/
- **Description**: Optimization techniques for measurements
- **Contents**: Methods to optimize measurement accuracy, speed, and performance
- **Key Files**: Optimize.md, Fast_Swp.md, Dyn_Rge.md, Trce_Noise.md, Effects_Accy.md

#### S3_Cals/
- **Description**: Calibration procedures and concepts
- **Contents**: Comprehensive guides on calibration methods, standards, and best practices
- **Key Files**: Calibration.md, Calibration_Wizard.md, Using_ECal.md, TRL_Calibration.md, PwrCalibration.md

#### S4_Collect/
- **Description**: Data collection and analysis methods
- **Contents**: How to collect, view, and analyze measurement data
- **Key Files**: Analyze_Data.md, Markers.md, Math_Operations.md, Equation_Editor.md

#### S5_Output/
- **Description**: Data output and management
- **Contents**: How to save, export, and print measurement results
- **Key Files**: Outputting_Data.md, Print.md, SaveRecall.md

### Root-Level Files

- **Critical_Information.md**: Important safety and usage information
- **Glossary.md**: Glossary of terms used in the documentation
- **Home.md**: Main landing page for the help documentation
- **Product_and_Solution_Cybersecurity.md**: Cybersecurity information for the product
- **Whats_New.md**: Release notes and new features