# VNA Configurations and Options

Included with each VNA is a mouse and keyboard. This topic presents VNA models
that are supported with this firmware release and the available options.

  * [N524xB PNA-X Series](Configurations.md#PNAX)

  * [VNA N522xB Series](Configurations.md#N522x)

  * [VNA N523xB (Updated PNA-L) Series](Configurations.md#N523x)

  * [mmWave Model](Configurations.md#mmwave)

  * PNA N5290A/N5291A Options

  * PNA N5291A170/N5291A220 Options

  * [Measurement Receiver](Configurations.md#N5264) N5264B

  * Common VNA Options

  * Certification Options for ALL Models

  * *OPT? and Options COM Behavior

  * [Warranty Period](Configurations.md#suppopts)

### See Also

  * [VNA Series Configuration Guide](http://literature.cdn.Keysight.com/litweb/pdf/5990-7745EN.pdf) (requires an Internet connection)

  * Click Help then About Network Analyzer to view the options that are installed on your VNA.

  * [Other Support Topics](Support_Overview.md)

N524xB PNA-X Series

[See Block Diagrams](PNAX_Block_Diagrams.md)

  * N5249B: 10 MHz to 8.5 GHz

  * N5241B: 10 MHz to 13.5 GHz

  * N5242B: 10 MHz to 26.5 GHz

  * N5244B: 10 MHz to 43.5 GHz

  * N5245B: 10 MHz to 50.0 GHz

  * N5247B: 10 MHz to 67 GHz

  * N5264B: Measurement Receiver [Learn more](../IFAccess/N5264A.md)

### PNA-X Options

[See other options that MAY be offered on the PNA-X
models](Configurations.htm#options)

[See NVNA Brochure for more PNA-X
options.](http://literature.cdn.Keysight.com/litweb/pdf/5989-8575EN.pdf)

Option |  Required Model/Options |  Description  
---|---|---  
201 |  None |  2-port base model. Includes six front-panel access loops.  
205 |  N5241B and N5242B only |  2-port base model adds six front-panel jumpers, R1 reference receiver switch, and low frequency extension (LFE).  
217 |  NOT available on N5247B S93080A/B |  2-port standard test set (includes six front-panel access loops), power range, and source and receiver attenuators (extended power range). |  Model |  Source Attn |  Receiver Attn  
---|---|---  
N5241B/42B/49B |  0 to 65 dB in 5 dB steps |  0 to 35 dB in 5 dB steps  
N5244B/45B |  0 to 60 dB in 10 dB steps |  0 to 35 dB in 5 dB steps  
  
Note: For N5247B models, the extended power range is available ONLY with Opt
219 and 419.  
  
219 |  None |  2-port standard test set (includes six front-panel access loops), power range, source and receiver attenuators (extended power range), and bias-tees. |  Model |  Source Attn |  Receiver Attn  
---|---|---  
N5241B/42B/49B |  0 to 65 dB in 5 dB steps |  0 to 35 dB in 5 dB steps  
N5244B/45B |  0 to 60 dB in 10 dB steps |  0 to 35 dB in 5 dB steps  
N5247B |  0 to 50 dB in 10 dB steps |  0 to 50 dB in 10 dB steps  
222 |  NOT available on N5247B |  2-port standard test set (includes six front-panel access loops), power range, source and receiver attenuators (extended power range), internal second source, a combiner, and mechanical switches to the 2-port analyzer. Allows high-power measurements up to 20 Watts (+43 dBm). from 10 MHz to 26.5 GHz. Similar to the PNA-X -219 or -419 but deletes the bias tees from the test set. [Learn more.](../Tutorials/High_Power_PNA-X.md#H85)  
224 |  S93080A/B |  2-port standard test set (includes six front-panel access loops), power range, source and receiver attenuators (extended power range), internal second source, a combiner, mechanical switches to the 2-port analyzer, and bias tees.  
401 |  None |  4-port model base model. Includes twelve front-panel access loops.  
417 |  NOT available on N5247B |  4-port standard test set (includes twelve front-panel access loops), power range, internal second source (Option 080 recommended), and source and receiver attenuators (extended power range). See table above for values. Note: For N5247B models, the extended power range is available ONLY with Opt 219 and 419.  
419 |  (S93080A/B recommended) |  4-port standard test set (includes twelve front-panel access loops), power range, internal second source (Option 080 recommended), and source and receiver attenuators (extended power range), and bias-tees. See table above for values.  
422 |  NOT available on N5247B |  4-port standard test set (includes six front-panel access loops), power range, source and receiver attenuators (extended power range), internal second source, a combiner, and mechanical switches to the 4-port analyzer. Allows high-power measurements up to 20 Watts (+43 dBm). from 10 MHz to 26.5 GHz. Similar to the PNA-X -219 or -419 but deletes the bias tees from the test set. [Learn more.](../Tutorials/High_Power_PNA-X.md#H85)  
423 |  S93080A/B |  4-port standard test set (includes six front-panel access loops), power range, source and receiver attenuators (extended power range), internal second source, a combiner, mechanical switches to the 4-port analyzer, and bias tees.  
425 |  All Models |  4-port configurable test set, source and receiver attenuators, internal second source, combiner, mechanical switches, and low frequency extension (LFE).  
425 |  S93029A/B |  4-port configurable test set, source and receiver attenuators, internal second source, combiner, mechanical switches, low frequency extension (LFE), and noise receiver.  
UNY |  PNA-X N522xB |  Provides Enhanced Phase Noise performance for the RF sources. For mixer group delay measurements UNY will improve noise by 8X. For IMD measurements, UNY provides better noise floor when the tone spacing is less than 100 kHz.  
XSB |  PNA-X |  Adds a synthesizer output from 10 MHz to 13.5 GHz to the SRC3 connector on the rear panel. Requires Opt. 422 or 423.  
  
PNA N522xB Series

[See Block Diagrams.](N522x_Block_Diagrams.md)

[See Specs](../Specs/ManualChoice.md)

  * N5221B: 10 MHz to 13.5 GHz

  * N5222B: 10 MHz to 26.5 GHz

  * N5224B: 10 MHz to 43.5 GHz

  * N5225B: 10 MHz to 50.0 GHz

  * N5227B: 10 MHz to 67 GHz

The N522xB models are identical to the PNA-X series except:

  * N522xB 2-port models are NOT available with 2 sources.

  * N522xB option numbering is slightly different.

  * N522xB models do NOT have internal RF switches or combiners (no [RF Path Configuration](../S1_Settings/Path_Configurator.md)). This has many measurement implications.

  * N522xB models do NOT have [rear-panel access to RF Paths](../Rear_Panel/XRtour.md#RFPath).

  * N522xB models do NOT offer a Noise Receiver (Opt S93029A/B).

### PNA N522xB Options

[See other options that MAY be offered on the N522xB
models](Configurations.htm#options)

Option |  Required Model/Options |  Description  
---|---|---  
200 |  None |  2-port model with single RF source.  
201 |  All Models |  To Opt 200, adds six front-panel jumpers and R1 reference receiver switch.  
205 |  All Models |  To Opt 200, adds six front-panel jumpters, R1 reference receiver switch, and low frequency extension (LFE).  
217 |  NOT available on N5227B 200 and [S93080A/B](Configurations.md#080) |  To Opt 201, adds source and receiver attenuators . |  Model |  Source Attn |  Receiver Attn  
---|---|---  
N5221B/22B |  0 to 65 dB in 5 dB steps |  0 to 35 dB in 5 dB steps  
N5224B/25B |  0 to 60 dB in 10 dB steps |  0 to 35 dB in 5 dB steps  
N5227B |  0 to 50 dB in 10 dB steps |  0 to 50 dB in 10 dB steps  
  
Note: For N5227B models, the extended power range is available ONLY with Opt
219 and 419.  
  
219 |  200 |  To Opt 217 adds bias-tees between each source and each test port.  
220 |  All Models |  2-port model adds source and receiver attenuators, and low frequency extension (LFE).  
400 |  None |  4-port model with two sources.  
401 |  400 |  To Opt 400, adds 12 front-panel jumpers and R1 reference receiver switch.  
405 |  All Models |  4-port base model adds six front-panel jumpers, R1 reference receiver switch, and low frequency extension (LFE).  
417 |  400 |  To Opt 401 adds source and receiver attenuators. See table above for values. Note: For N5227B models, the extended power range is available ONLY with Opt 219 and 419.  
419 |  400 (S93080A/B recommended) |  To Opt 417 adds bias-tees between each source and each test port.  
420 |  All Models |  4-port model adds source and receiver attenuators, and low frequency extension (LFE).  
  
N523xB (Updated PNA-L) Series

[See Specs](../Specs/ManualChoice.md)

  * N5231B: 300 kHz to 13.5 GHz 2-port / 4-port

  * N5232B: 300 kHz to 20.0 GHz 2-port / 4-port

  * N5234B: 10 MHz to 43.5 GHz 2-port ONLY

  * N5235B: 10 MHz to 50.0 GHz 2-port ONLY

  * N5239B: 300 kHz to 8.5 GHz 2-port ONLY

The N523xB models are identical to the N5230C series except:

  * N523xB models have a PNA-X look and feel.

  * N523xB models are NOT available with 2 sources.

  * ALL N5231B, N5232B, and N5239B models require a [Delta Match calibration](../S3_Cals/Delta_Match_Calibration.md).

### N523xB Options

[See other options that MAY be offered on the N523xB
models](Configurations.htm#options)

Option |  Required Model/Options |  Description  
---|---|---  
200 |  None |  Base 2-port model.  
216 |  None |  To base 2-port model, adds:

  * Six front-panel jumpers
  * Source Attenuator: 60 dB with 10 dB steps.

  
400 |  None |  Base 4-port model. Available ONLY on N5231B and N5232B  
416 |  None |  To base 4-port model, adds:

  * Six front-panel jumpers
  * Source Attenuator: 60 dB with 10 dB steps.

  
  
Millimeter Wave VNA

PNA Model |  Frequency Range |  Ports |  Connector Type  
---|---|---|---  
N5250C (discontinued) |  10 MHz to 110 GHz |  2 |  1.0 mm  
N5251B |  10 MHz to 110 GHz |  2 |  1.0 mm  
Test heads to 325 GHz are also available.  
  
### PNA N5290A/N5291A Options

Option |  Required Model/Options |  Frequency Range |  Ports  
---|---|---|---  
201 |  N5222B VNA with Option 205 N5292A Test Set with Options 200 and 222 Two N5293AX03 Frequency Extenders (N5290A) Two N5295AX03 Frequency Extenders (N5291A) |  900 Hz to 110 GHz (N5290A) 900 Hz to 120 GHz (N5291A) |  2  
202 |  N5227B VNA with Option 205 N5292A Test Set with Options 200 and 224 Two N5293AX03 Frequency Extenders (N5290A) Two N5295AX03 Frequency Extenders (N5291A) |  900 Hz to 110 GHz (N5290A) 900 Hz to 120 GHz (N5291A) |  2  
401 |  N5242B VNA with Option 425 N5292A Test Set with Options 400 and 442 Four N5293AX03 Frequency Extenders (N5290A) Four N5295AX03 Frequency Extenders (N5291A) |  900 Hz to 110 GHz (N5290A) 900 Hz to 120 GHz (N5291A) |  4  
402 |  N5242B VNA with Option 425, S93029A/B N5292A Test Set with Options 400 and 442 Four N5293AX03 Frequency Extenders (N5290A) Four N5295AX03 Frequency Extenders (N5291A) |  900 Hz to 110 GHz (N5290A) 900 Hz to 120 GHz (N5291A) |  4  
403 |  N5247B VNA with Option 425, S93029A/B N5292A Test Set with Options 400 and 444 Four N5293AX03 Frequency Extenders (N5290A) Four N5295AX03 Frequency Extenders (N5291A) |  900 Hz to 110 GHz (N5290A) 900 Hz to 120 GHz (N5291A) |  4  
  
### PNA N5291A170/N5291A220 Options

Option |  Required Model/Options |  Frequency Range |  Ports  
---|---|---|---  
S93300B |  N5291A N5295A Frequency Extender 170 GHz Frequency Extender |  900 Hz to 130 GHz 115 GHz to 170 GHz |  2  
S93301B |  N5291A N5295A Frequency Extender 220 GHz Frequency Extender |  900 Hz to 130 GHz 128 GHz to 220 GHz |  2  
  
## Measurement Receiver

Block Diagrams are available at the end of each
[specifications](../Specs/ManualChoice.md) document.

PNA Model |  Frequency Range |  Ports |  Connector Type |  Reference  
Receivers |  Front Panel jumpers  
---|---|---|---|---|---  
N5264B [Learn more](../IFAccess/N5264A.md) |  IF Frequencies only |  0 |  N/A |  1 |  N/A  
  
### Options

108 \- Built-in 26.5 GHz LO source with +10 dBm output power. S93118A/B \-
Fast-CW mode enables 500 million point data buffer.  
  
## Common Options

The following options are common to more than one VNA family. For PNA-B model
and E5080A which is shipped after Sep 2017, the software option is provided as
a product number S93xxxA for PNA and S96xxxA for ENA(E5080A). The fixed,
transportable, perpetual and time limitation options are available.

Software Product/Option |  Available on models: |  Description  
---|---|---  
S93007A/B |  ALL models |  Automatic Fixture Removal Mathematically removes, or de-embeds, a characterized test fixture from displayed measurement results. [Learn more](../S3_Cals/Auto_Fixture_Removal.md)  
S93010A/B |  ALL models |  Time-domain Adds time-domain capability to analyzer. The serial number of the analyzer must be specified when ordering this kit. Software upgrade. [Learn more about Time Domain](../Time/TimeDomain.md) [Learn how this option is enabled.](Option_Enable.md)  
S93011A/B |  ALL models |  Enhanced Time Domain Analysis Adds time domain reflectometry (TDR) and time domain transmission (TDT) capability to analyzer. [Learn more](../Applications/Enhanced_Time_Domain_Analysis/Enhanced_Time_Domain_Analysis.md). Note: The S93011A/B license can be used for the standard Time Domain measurements.  
S93015A/B |  ALL models |  Real-time S-Parameter and Power Measurement Uncertainty Display the measurement uncertainty dynamically ('real-time') on the same screen as the measurement trace. [Learn more](../S3_Cals/Dynamic_Uncertainty.md).  
020 |  PNA-X N522xB |  Add [IF inputs on the rear panel](../Rear_Panel/XRtour.md#IF) for antenna and millimeter-wave.  
021 |  PNA-X N522xB |  Add pulse modulator to internal Source1. [Learn more.](../IFAccess/IF_Path_Configuration.md)  
022 |  PNA-X 2-source N522xB models |  Add pulse modulator to internal Source2. [Learn more.](../IFAccess/IF_Path_Configuration.md)  
S93025A/B |  PNA-X N522xB |  Basic pulsed-RF measurements. Learn more.  
S93026A/B |  PNA-X N522xB Enhanced version of Opt S93025A/B |  Integrated Pulsed Application Provides average pulse and point-in-pulse measurements. Learn more.  
S9x027B |  All Models with 029 |  Allows VNA with Option 029 to use specialized mechanical noise tuners on the input port. [Learn more](../Applications/Noise_Figure.md#Noise_Figure_Option_027).  
S93029A/B |  PNA-X with S93080A/B and one of the following:  
219, 222, 224, 419, 423 or 422 |  Noise Figure Application Adds hardware and firmware for high-accuracy noise figure measurements on [amplifiers](../Applications/Noise_Figure.md) or [converters](../Applications/Noise_Figure_on_Converters.md) using internal low-noise receivers or a standard VNA receiver.  
H29 |  N5244B or N5245B with 423 and S93080A/B. |  (Obsolete) Same as Opt S93029A/B for the N5242B, but on a [N5244B or N5245B](Configurations.md#PNAX). [Learn more.](../Applications/Noise_Figure.md#OptionsExplained)  
S93050B |  ALL Models |  Send wideband IQ data up to an analysis bandwidth of 1.5 GHz to the 89600 VSA software.[ Learn more](../Applications/Spectrum_Analyzer.md#IQ_generation_and_VSA_89600_connection).  
S93051B |  ALL Models |  Send wideband IQ data up to an analysis bandwidth of 4.0 GHz to the 89600 VSA software.[ Learn more](../Applications/Spectrum_Analyzer.md#IQ_generation_and_VSA_89600_connection).  
S930317B |  PNA/PNA-X |  Phase Noise Application, up to 70 GHz Note: This feature applies ONLY to instruments with serial prefix 6021 and above.  
S930321B |  PNA/PNA-X |  Phase Noise Application, up to 125 GHz Note: This feature applies ONLY to instruments with serial prefix 6021 and above.  
S930700B |  PNA/PNA-X |  Modulation Distortion, up to 8.5 GHz [Learn more](../Applications/Modulation_Distortion/Overview.md).  
S930701B |  PNA/PNA-X |  Modulation Distortion, up to 13.5 GHz [Learn more](../IFAccess/Low_Frequency_Extension/Overview.md).  
S930702B |  PNA/PNA-X |  Modulation Distortion, up to 26.5 GHz [Learn more](../IFAccess/Low_Frequency_Extension/Overview.md).  
S930704B |  PNA/PNA-X |  Modulation Distortion, up to 43.5 GHz [Learn more](../IFAccess/Low_Frequency_Extension/Overview.md).  
S930705B |  PNA/PNA-X |  Modulation Distortion, up to 50 GHz [Learn more](../IFAccess/Low_Frequency_Extension/Overview.md).  
S930707B |  PNA/PNA-X |  Modulation Distortion, up to 67 GHz [Learn more](../IFAccess/Low_Frequency_Extension/Overview.md).  
S93072B |  PNA-X |  Arbitrary Waveform Generation on All Ports This application software allows you to generate arbitrary waveforms including multitone signals, limited to 6.2866 microseconds max period. It must be on a frequency grid of (M/N) * 600 MHz. [Learn more](../Applications/Modulation_Distortion/Modulation_Distortion_Settings.md#Source).  
S93074B |  PNA/PNA-X |  Hybrid Source Bandwidth When using a hybrid source as an external device, this option removes bandwidth limits for the following frequency ranges: Between 4.8 GHz and 31.8 GHz you can exceed 2.2 GHz bandwidth. Between 31.8 GHz and 37 GHz you can exceed 550 MHz bandwidth. Between 37 GHz and 90 GHz you can exceed 2.2 GHz bandwidth. [Learn more](../System/Configure_an_External_Device.md).  
S93080A/B |  PNA-X N522xB |  Frequency Offset Mode (FOM) Enables you to set the VNA source independently from where the receivers are tuned. This capability is important for measuring mixers and converters. [Learn more](../FreqOffset/Frequency_Offset_Mode.md).  
S93082A/B |  ALL models |  Scalar Mixer Measurements (SMC) Allows Only the Scalar Mixer Converter (SMC) portion of the Frequency Converter Measurement Application. Provides the same intuitive user-interface, easy calibration, and external source control for making fixed and swept LO Scalar Mixer measurements. When used with a multiport VNA or [external test set](../System/External_Testset_Control.md), SMC is only available on VNA ports 1 and 2. PNA requires Opt S93080A/B. ENA S96082A includes FOM function. [Learn more.](../FreqOffset/FCA_Use.md)  
S93083A/B |  PNA-X N522xB |  Frequency Converter Application (FCA) Provides an intuitive user-interface for making extremely accurate conversion loss and absolute group delay measurements on mixers and converters. Exceptional amplitude and phase accuracy is achieved through two calibration techniques: Scalar Mixer Calibration and Vector Mixer Calibration. The application also provides automatic control of all of Keysight's major signal sources. Requires Opt S93080A/B. [Learn more](../FreqOffset/FCA_Use.md)  
S93084A/B |  PNA-X N522xB |  Embedded LO Provides the ability to measure frequency converters that have an embedded LO. [Requires at least one Converter App option.](../Applications/MixerConverter_Setup.md) [Learn more](../Applications/Embedded_LO.md)  
S93086A/B |  PNA-X N522xB |  Gain Compression Application. (GCA) Provides fast and accurate gain compression measurements. [Learn more.](../Applications/Gain_Compression_Application.md)  
S93087A/B |  PNA-X N522xB  
(NOT available with Opt 200 or 400) |  Swept IMD and IM Spectrum. Provides fast and accurate Swept IMD and IM Spectrum measurements on amplifiers and converters. [Learn more.](../Applications/IMD_App.md) Requires Opt S93080A/B.  
S93088A/B |  PNA-X N522xB (NOT available with 2-port models) |  Source Phase Control Provides coherent phase measurements. [Learn more.](../S1_Settings/Phase_Control.md)  
S93089A/B |  4-port models: PNA-X N522xB |  Differential IQ Provides controls to set any source to any frequency range, any power level, and any phase. Then measure any receiver, any frequency range, with match correction. [Learn more](../Applications/Differential_IQ.md).  
S930900A/B |  ALL models |  Spectrum Analysis, up to 8.5 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S930901A/B |  ALL models except N5239B and N5249B |  Spectrum Analysis, up to 13.5 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S930902A/B |  ALL models except N5221B, N5231B, N5239B, N5241B, N5249B |  Spectrum Analysis, up to 26.5 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S930904A/B |  N5224B, N5225B, N5227B, N5234B, N5235B, N5244B, N5245B, N5247B |  Spectrum Analysis, up to 43.5 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S930905A/B |  N5225B, N5227B, N5235B, N5245B, N5247B |  Spectrum Analysis, up to 50 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S930907A/B |  N5227B, N5247B |  Spectrum Analysis, up to 67 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S930909A/B |  N5222B, N5224B, N5225B, N5227B, N5242B, N5244B, N5245B, N5247B |  Spectrum Analysis, up to 90 GHz [Learn more](../Applications/Spectrum_Analyzer.md).  
S93093A/B |  N5222B, N5224B, N5225B, N5227B, N5242B, N5244B, N5245B, N5247B |  Spectrum Analysis, up to 125 GHz [Learn more](../IFAccess/External_Test_Head_Configuration.md#Spectrum_Analyzer_Measurements).  
S93094A/B |  N5222B, N5224B, N5225B, N5227B, N5242B, N5244B, N5245B, N5247B |  Spectrum Analysis, up to and beyond 125 GHz [Learn more](../IFAccess/External_Test_Head_Configuration.md#Spectrum_Analyzer_Measurements).  
108 |  N5264B Only |  Adds an internal 10 MHz to 26.5 GHz LO source. [Learn more.](../IFAccess/N5264A.md#InternalLO)  
S93110A/B |  4-Port PNA-X models with 2 sources |  Active (Hot) Parameters [Learn more.](../Applications/Active_Match.md)  
S93111A/B |  4-Port PNA-X models with 2 sources |  Active (Hot) Parameters - restricted to 50 GHz [Learn more.](../Applications/Active_Match.md)  
S93118A/B |  PNA-X N522xB |  Fast CW Mode Enables 500 million point data buffer. [Learn more.](../IFAccess/FIFO_and_other_Antenna_Features.md#FastCW)  
S93460A/B |  4-port PNA-X and N522xB |  iTMSA Adds firmware for Integrated True Mode Balanced measurements. [Learn more.](../Applications/iTMSA.md)  
S93551A/B |  ALL models |  N-port capabilities Adds fully integrated measurements at all of the available test ports using a multiport testset. [Learn more](../System/External_Testset_Control.md#551). Solutions and VNA requirements depend on the supported test set. See <http://www.Keysight.com/find/multiport>  
S93898A/B |  ALL models |  Built-in performance test software  
  
Certification Options for ALL Models

The following options are available for your VNA.

Option |  Supported Models |  Description  
---|---|---  
S93898A/B |  All models |  Perpetual license for built-in performance test software. Adds built-in performance testing and calibration software for self-maintainers. Requires additional equipment. See your VNA Service Guide for more information on equipment required.  
UK6 |  ALL except N5250A |  Complete set of measurement data which was acquired from testing your VNA to published specifications. Includes calibration label, calibration certificate, and data report. Conforms to ISO 9001.  
---|---|---  
1A7 |  ALL except N5250A |  Complete set of measurement data which was acquired from testing your VNA to published specifications. Includes calibration label, ISO 17025 calibration certificate, data report, measurement uncertainties and guard bands on all specifications. Conforms to ISO17025 and ISO 9001.  
  
*OPT? and Options COM Behavior

Some of the VNA option numbers returned when using the *OPT? SCPI command or
IApplication::Options COM command are not the same as the option numbers
returned when using the SYST:CAP:LIC:CAT? command or IApplication::Licenses
COM command. The following table shows how the common option numbers map to
the option numbers reported when using *OPT? command or the
IApplication::Options COM command.

Software Product Number |  *OPT? SCPI or Options COM Response |  Description  
---|---|---  
S93007A/B,S95007A,S96007A, S97010A |  007 |  Automatic Fixture Removal  
S93010A/B,S95010A, S96010A, S97010A |  010 |  Time-domain  
S93015A/B |  015 |  Dynamic Uncertainty for S-Parameters  
S93025A/B |  025 |  Add four internal pulse generators  
S93026A/B, S95026A, S97026A |  008 |  Integrated Pulsed Application  
S93029A/B, |  028 |  Noise Figure application only  
S93029A/B, S95029B, S97029B |  028 + 080 |  Noise Figure application + Frequency Offset Mode (FOM) for converter applications  
S95029A, S97029A |  029 |  Noise Figure application + Noise Figure receiver or Noise Figure receiver only  
S93080A/B |  080 |  Frequency Offset Mode (FOM)  
S93082A/B, S95082A, S96082A, S97082A |  082 + 080 (Others), 082 (ENA) |  Scalar Mixer Converter (SMC) + Frequency Offset Mode (FOM) for converter applications  
S93083A/B, S95083A, S97083A |  083 + 080 |  Frequency Converter Application (FCA) + Frequency Offset Mode (FOM) for converter applications  
S93084A/B, S95084A, S97084A |  084+ 080 |  Embedded LO + Frequency Offset Mode (FOM)  
S93086A/B, |  086 + 080 |  Gain Compression Application (GCA) + Frequency Offset Mode (FOM) for converter applications  
S96086A, S95086A, S97086A |  086 |  Gain Compression Application (GCA)   
S93087A/B |  087 + 080 |  Swept IMD and IM Spectrum + Frequency Offset Mode (FOM) for converter applications  
S93088A/B |  088 |  Source Phase Control  
S93089A/B |  089 + 080 |  Differential IQ + Frequency Offset Mode (FOM)  
S95090A, S97090A |  090 + 080 |  Spectrum analysis+ Frequency Offset Mode (FOM)  
S930900A/B |  090 + 900 |  Spectrum analysis, up to 8.5 GHz + Frequency Offset Mode (FOM)  
S930901A/B |  090 + 901 |  Spectrum analysis, up to 13.5 GHz + Frequency Offset Mode (FOM)  
S930902A/B |  090 + 902 |  Spectrum analysis, up to 26.5 GHz + Frequency Offset Mode (FOM)  
S930904A/B |  090 + 904 |  Spectrum analysis, up to 43.5 GHz + Frequency Offset Mode (FOM)  
S930905A/B |  090 + 905 |  Spectrum analysis, up to 50 GHz + Frequency Offset Mode (FOM)  
S930907A/B |  090 + 907 |  Spectrum analysis, up to 67 GHz + Frequency Offset Mode (FOM)  
S930909A/B |  090 + 909 |  Spectrum analysis, up to 90 GHz + Frequency Offset Mode (FOM)  
S93093A/B |  093 + 080 |  Extend Spectrum Analyzer to 110 GHz + Frequency Offset Mode (FOM)  
S93094A/B |  094 + 080 |  Extend Spectrum Analyzer to above 110 GHz+ Frequency Offset Mode (FOM)  
S93118A/B |  118 |  Fast CW Mode  
S93460A/B |  460 |  iTMSA  
S93551A/B, S95551A, S97551A |  551 |  N-port capabilities  
S96790A |  790 |  Measurement Wizard Assistant Software  
S93898A/B |  898 |  Built-in performance test software  
S94510A/B |  510 |  Nonlinear component characterization  
S94511A/B |  511 |  Nonlinear component characterization, restricted to 50 GHz  
S94514A/B |  514 |  Nonlinear X-parameters  
S94518A/B |  518 |  Nonlinear pulse envelope domain  
S94520A/B |  520 |  Arbitrary load-impedance X-parameters  
S94521A/B |  520 |  Arbitrary load-control, X-parameters  
S94522A/B |  520 |  Arbitrary load-control, device characterization  
  
Documentation

Description  
---  
Printed versions of VNA Help in pdf format are available at
[www.Keysight.com/find/pna](http://www.Keysight.com/find/pna). (Apr.2005)  
A documentation CD-ROM is no longer included with each VNA shipment
(Feb.2005).  
To download a service guide for your VNA, or the latest version of VNA Help,
visit [www.Keysight.com/find/pna](http://www.Keysight.com/find/pna), search
for your VNA model, then click Library.  
  
VNA Warranty Period

The actual warranty on your instrument depends on the date it was ordered as
well as whether or not any warranty options were purchased at that time. To
determine the exact warranty on your instrument, contact [Keysight
Technologies](Tech_Supp.htm) with the model and serial number of your
instrument.

For online information about Keysight's service and support products visit:
[www.Keysight.com/find/tm_services](http://www.Keysight.com/find/tm_services).

* * *

