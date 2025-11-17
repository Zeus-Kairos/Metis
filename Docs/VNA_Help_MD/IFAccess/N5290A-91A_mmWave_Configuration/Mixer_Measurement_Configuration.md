# Mixer Measurement Configuration

Mixer measurements can be made at mmWave frequencies using
[SMC](../../FreqOffset/SMC_Measurements.md). (VMC measurements are NOT
supported. See Supported Applications.)

In this topic:

  * Requirements
  * Limitations
  * Hardware Connections
  * Procedure
  * Measuring Harmonic Mixers
  * SMC Calibration

### See Also

  * [SMC Measurements](../../FreqOffset/SMC_Measurements.md)
  * [SMC mixer setup dialog](../../Applications/MixerConverter_Setup.md#MixerSetupTab)
  * Supported Applications

## Requirements

  * For 2-port VNAs, connect External Source to the VNA GPIB Controller port. Learn how to [Configure an External Source](../../System/Configure_an_External_Device.md).
  * Connect the [10 MHz reference signal](../../Rear_Panel/XRtour.md#10M) of an external source to the VNA

## Limitations

  * 2-port systems require external source for LO
  * VMC measurements are NOT supported

## Hardware Connections

### Connections with a 4-port mmWave system

Upconverters

  * DUT Input - Connect to Standard VNA port 2 or port 4.

  * DUT LO - Connect mmWave module to test set Port 3.

  * DUT Output - Connect mmWave module to test set Port 1.

Downconverters

  * DUT Input - Connect mmWave module to test set Port 1.

  * DUT LO - Connect mmWave module to test set Port 3.

  * DUT Output - Connect to Standard VNA port 2 or port 4.

### Connections with a 2-port mmWave system

Upconverters - requires a mmWave module as a source at the DUT LO and a mmWave
module as a receiver at the DUT Output:

  * DUT Input - Connect to Standard VNA port 2.

  * DUT LO - Connect the RF cable of the mmWave module to an external source or the VNA (SRC2) second source.

  * DUT Output - Connect the mmWave module to the test set port 1.

Downconverters \- requires two mmWave modules as sources

  * DUT Input - Connect the mmWave module to the test set port 1.

  * DUT LO - Connect the RF cable of the mmWave module to an external source or the VNA (SRC2) second source.

  * DUT Output - Connect to Standard VNA port 2.

## Procedure

  1. Connect your DUT to the mmWave system as described in Hardware Connections.

  2. Configure this dialog ([Millimeter Module Configuration](Millimeter_Configuration.md#MillimeterDiagHelp)).

  3. For banded mixer measurements only, check Mixer Mode.

  4. Press OK. This presets the VNA.

  5. Create an SMC measurement:

     1. Press Setup > Main > Meas Class....

     2. Select SMC, then either:

     3.         * OK delete the existing measurement, or

        * New Channel to create the measurement in a new channel.

     3. An SC21 measurement is displayed.

  4. [Make mixer settings](../../Applications/MixerConverter_Setup.md) in the same way as with standard SMC measurements. Only two DUT ports can be swept in frequency. The remaining DUT port must be a fixed frequency. See configuration used for harmonic mixers.

  5. [Increase power](../../S1_Settings/Power_Level.md#Advanced) for mmWave modules that are connected directly to a VNA port or external source.

  6. Calibrate using the SMC Calibration.

## Measuring Harmonic Mixers

Harmonic mixers have a multiplier circuit in the LO port of the DUT. Enter the
multiplier value in the numerator of the X LO port in the [SMC mixer setup
dialog](../../Applications/MixerConverter_Setup.htm#MixerSetupTab). This will
provide the correct LO frequencies out of the appropriate source.

### SMC Calibration

With a configured SMC measurement active, perform the [Cal All
Procedure](Calibration.htm#Cal_All_Procedure).

