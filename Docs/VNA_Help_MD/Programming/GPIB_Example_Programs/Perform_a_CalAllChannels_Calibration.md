# Perform a Cal All Channels Calibration

* * *

There are two sets of commands used to automate a Cal All Channels
Calibration: SYST:CAL:ALL <commands> and SENS<chan>:CORR:COLL:GUIDed
<commands>.

## SYST:CAL:ALL <commands>

The general sequence for setting up the Cal All session is as follows:

  1. Select the channels to calibrate using the SYST:CAL:ALL:SEL command.

  2. Select the ports to calibrate using the SYST:CAL:ALL:CHAN:PORTs command.

  3. Set the properties that are available in Cal All that are relevant to the channels you are calibrating using the SYST:CAL:ALL:MCLass:PROP:VAL <name>,<val> command. For example, setting <name> to "Include Power Calibration" and <val> to "true" will include a source and receiver power calibration in the Cal All calibration.

  4. Query the channel number to use for the remaining cal commands. This channel is used for the sole purpose of acquiring cal data and finds the highest available channel number.

Note: You must query this number  do not assume that it will always be a
particular value. For example:  
a.chan = SYST:CAL:ALL:GUIDed:CHAN?

## SENS<chan>:CORR:COLL:GUIDed <commands>

These commands are identical to the command used for a single channel
calibration. However, the number used for the SENSe header is determined by
the SYST:CAL:ALL:GUIDed:CHAN? command. The general sequence is as follows:

  1. Set up the power sensor using the SENS:CORR:COLL:GUID:PSENsor commands if you will be performing a power calibration (source and receiver power cal).

  2. Set up the connector family and gender per port using the **SENS:CORR:COLL:GUID:CONN:PORT** **command.**

  3. Set up the cal kit per port using the **SENS:CORR:COLL:GUID:CKIT:PORT** command.

  4. Initialize the session using the SENS:CORR:COLL:GUID:INIT command.

  5. Query the number of steps using the SENS:CORR:COLL:GUID:STEPs? command.

  6. Acquire each step using the SENS:CORR:COLL:GUID:ACQ command.

  7. Save the calset using the SENS:CORR:COLL:GUID:SAVE command.

## Cal All Examples

[1-Port, 1-Channel, no Power Cal, with ECal
Module](CalAll_1-Port_1-Chan_ECal.htm)

[2-Port, 1-Channel, no Power Cal, with ECal
Module](CalAll_2-Port_1-Chan_ECal.htm)

[2-Port, 1-Channel, with Power Cal, with ECal
Module](CalAll_2-Port_1-Chan_PwrCal_ECal.htm)

[2-Port, 2-Channel, with Power Cal, with ECal
Module](CalAll_2-Port_2-Chan_PwrCal_ECal.htm)

[Noise Figure Cal All](CalAll_Noise_Figure.md)

[Noise Figure Cal All with USB noise
source](CallAll_Noise_Figure_USBNoiseSource.htm)

[SMC Cal All](CalAll_SMC.md)

[IMD 2nd Order Cal All](CalAll_IMD.md)

[Cal All for Mixer Channel](Cal_All_for_Mixer_Channel.md)

[Independent Power Calibration](Independent_Power_Calibration.md)

[Multiple Instances of Calibrate All
Channels](Multiple_Instances_of_Calibrate_All_Channels.htm)

[Cal All SMC Split Cal](CalAll_SMC_Split_Cal.md)

[Cal All Independent Calibration
Channels](Cal_All_Independent_Calibration_Channels.htm)

[Cal All Multi-Channel Independent Calibration Channels](Cal_All_Multi-
Channel_Independent_Calibration_Channels.htm)

Each VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the code into a text editor file, such as Notepad, and save it on the VNA
hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See CalAll SCPI commands](../GP-IB_Command_Finder/SystCalAll.md)

[Learn about Cal All](../../S3_Cals/Calibrate_All_Channels.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

* * *

* * *

