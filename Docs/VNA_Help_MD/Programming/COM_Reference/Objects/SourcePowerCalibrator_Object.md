# SourcePowerCalibrator Object

* * *

Description

This object is a child of the Application object and is a vehicle for
performing source power calibrations.

### Accessing the SourcePowerCalibrator Object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim ispc As ISourcePowerCalibrator  
Set ispc = app.SourcePowerCalibrator

Note: If you see this error: The target NA stimulus channel has not been set.
With the SourcePowerCalibrator object, you must first call SetCalInfoEx with
the channel number. SetCalInfoEx must not be made against a temporary copy of
the SourcePowerCalibrator object. Or this error: Channel not found. It is
either because you set the wrong channel number in the SetCalInfoEx call or
because the SourcePowerCalibrator object is unique in that you MUST use the
SAME instance of the SourcePowerCalibrator object for every property that is
set. Do this by naming/setting a variable as in this vbs example: set
sourcepowercalibrator = app.sourcepowercalibrator  
---  
  
### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

Note: Interface ISourcePowerCalibrator is abbreviated as ISPC in the following
table.

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

[See History](SourcePowerCalibrator_Object.md#history) | 

### Description  
  
---|---|---  
[AbortPowerAcquisition](../Methods/AbortPowerAcquisition_Method.md) |  ISPC |  Aborts a source power cal acquisition sweep that is currently in progress.  
[AcquirePowerReadings](../Methods/AcquirePowerReadings_Method.md) |  ISPC |  Superseded with [AcquirePowerReadingsEx](../Methods/AcquirePowerReadingsEx_Method.md)  
[AcquirePowerReadingsEx](../Methods/AcquirePowerReadingsEx_Method.md) |  ISPC4 |  Initiates a source power cal acquisition.  
[ApplyPowerCorrectionValues](../Methods/ApplyPowerCorrectionValues_Method.md) |  ISPC |  Superseded with [ApplyPowerCorrectionValuesEx](../Methods/ApplyPowerCorrectionValuesEx_Method.md)  
[ApplyPowerCorrectionValuesEx](../Methods/ApplyPowerCorrectionValuesEx_Method.md) |  ISPC5 |  Applies correction values after completing a source power cal acquisition sweep. Optionally perform a calibration of the reference receiver used in the source power cal.  
[CheckPower](../Methods/CheckPower_Method.md) |  ISPC2 |  Measures power at a specific frequency. Used to test power level before and/or after applying a source power calibration.  
[LaunchPowerMeterSettingsDialog](../Methods/LaunchPowerMeterSettingsDialog_Method.md) |  ISPC2 |  Launches the Power Meter Settings dialog on the VNA.  
[SetCalInfo](../Methods/SetCalInfo_\(power\)_Method.md) |  ISPC |  Superseded with [SetCalInfoEx Method](../Methods/SetCalInfoEx_Method.md)  
[SetCalInfo2](../Methods/SetCalInfo2_\(power\)_Method.md) |  ISPC3 |  Superseded with [SetCalInfoEx Method](../Methods/SetCalInfoEx_Method.md)  
  
### [SetCalInfoEx Method](../Methods/SetCalInfoEx_Method.md)

|

### ISPC4

|  Specifies the channel and source port to be used for the source power
calibration.  
  
###
[SetPowerAcquisitionDevice](../Methods/SetPowerAcquisitionDevice_Method.md)

|

### ISPC3

|  Sets the power sensor channel (A or B) to be used. This method is ONLY
necessary when performing an SMC calibration.  
  
### Properties

|

### Interface

|

### Description  
  
[CalPower](../Properties/CalPower_Property.md) |  ISPC |  Specifies the power level that is expected at the desired reference plane.  
[IterationsTolerance](../Properties/IterationsTolerance_Property.md) |  ISPC3 |  Sets the maximum desired deviation from the sum of the test port power and the offset value.  
[LastCalPassedTolerance](../Properties/LastCalPassedTolerance.md) |  ISPC7 |  Returns pass / fail status of the user-specified tolerance limits on the target cal power.  
[MaximumIterationsPerPoint](../Properties/MaximumIterationsPerPoint_Property.md) |  ISPC3 |  Specifies maximum number of readings to take at each data point for iterating the source power.  
[PowerAcquisitionDevice](../Properties/PowerAcquisitionDevice_Property.md) |  ISPC2 |  Specifies the power sensor channel (A or B) that is currently selected for use at a specific frequency.  
[PowerLossSegments (collection)](PowerLossSegments_Collection.md) |  ISPC2 |  Collection for iterating through the segments of the power loss table used in source power calibration.  
[PowerMeterGPIBAddress](../Properties/PowerMeterGPIBAddress_Property.md) |  ISPC |  Specifies the GPIB address of the power meter.  
[PowerMeterInterfaces](PowerMeterInterfaces_Collection.md) |  ISPC6 |  Collection for getting a handle to the available power meters.  
[PowerSensors (collection)](PowerSensors_Collection.md) |  ISPC2 |  Collection for iterating through the PowerSensor objects which are connected to the power meter for a source power cal.  
[ReadingsPerPoint](../Properties/ReadingsPerPoint_Property.md) |  ISPC |  Specifies the maximum power readings for power meter settling.  
[ReadingsTolerance](../Properties/ReadingsTolerance_Property.md) |  ISPC3 |  Power meter settling tolerance value.  
[USBPowerMeterCatalog](../Properties/USBPowerMeterCatalog_Property.md) |  ISPC6 |  Returns a list of USB power meters that are connected to the VNA.  
[UsePowerLossSegments](../Properties/UsePowerLossSegments_Property.md) |  ISPC |  Specifies if subsequent calls to the AcquirePowerReadings method will make use of the loss table (PowerLossSegments).  
[UsePowerSensorFrequencyLimits](../Properties/UsePowerSensorFrequencyLimits_Property.md) |  ISPC |  Specifies if subsequent calls to the AcquirePowerReadings method will make use of power sensor frequency checking capability.  
  
###  ISourcePowerCalibrator History

Interface |  Introduced with VNA Rev:  
---|---  
ISourcePowerCalibrator |  2.0  
ISourcePowerCalibrator2 |  3.5  
ISourcePowerCalibrator3 |  4.0  
ISourcePowerCalibrator4 |  6.2  
ISourcePowerCalibrator5 |  7.2  
ISourcePowerCalibrator6 |  7.5  
ISourcePowerCalibrator7 |  9.2

