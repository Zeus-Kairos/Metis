# GuidedCalibration Object

* * *

### Description

Contains the methods and properties used to perform a Guided Calibration.

Important! Do NOT use commands from the [Calibrator](Calibrator_Object.md)
(Unguided calibration) object when performing a Guided calibration. Use ONLY
the GuidedCalibration object. The ONLY exception is: Use
[OrientECalModule_Property](../Properties/OrientECALModule_Property.md) and
[ECalPortMapEx_Property](../Properties/ECALPortMapEx_Property.md) on the
[Calibrator Object](Calibrator_Object.md) to specify orientation for both
guided and unguided calibrations.  
---  
  
A Guided Calibration must be performed on the Active Channel. To activate a
channel, activate any measurement on that channel. Do this using
[meas.Activate,](../Methods/Activate_Method.md) which requires you already
have a handle to the measurement.

### Accessing the GuidedCalibration object

For standard S-parameter channels:

Dim app as AgilentPNA835x.Application  
Dim CalMgr  
Set CalMgr = App.GetCalManager  
Dim guidedCal  
Set guidedCal = CalMgr.GuidedCalibration

To calibrate an [Application](../../../Applications/Applications.md) channel,
see [CreateCustomCalEx](../Methods/CreateCustomCalEx_Method.md) Method.

### THRU Pairs sequence

The Smart/Guided Cal logic always determines the best calibration based on
your specified connectors and ports. The following three commands overwrite
the SmartCal logic. Send these commands ONLY if you have a deliberate reason
for overwriting the SmartCal logic.

  * [ThruPortList](../Properties/ThruPortList_Property.md)
  * [PathThruMethod](../Properties/PathThruMethod_Property.md)
  * [PathCalMethod](../Properties/PathCalMethod_Property.md)

When sending one or more of these commands, they must be sent in the following
sequence with the other commands listed here. Note: The
[Initialize](../Methods/Initialize_Method.md) command is sent before and
after these three commands.

  1. [ConnectorType](../Properties/ConnectorType_Property.md) (ports)
  2. [CalKitType](../Properties/CalKitType_fca_Property.md) (ports)
  3. [Initialize](../Methods/Initialize_Method.md)
  4. [ThruPortList](../Properties/ThruPortList_Property.md)
  5. [PathThruMethod](../Properties/PathThruMethod_Property.md)
  6. [PathCalMethod](../Properties/PathCalMethod_Property.md)
  7. calMethod = guidedCal.[PathCalMethod](../Properties/PathCalMethod_Property.md) (ports) (recommended)
  8. [Initialize](../Methods/Initialize_Method.md)

  
---  
  
### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[AcquireStep](../Methods/AcquireStep_Method.md) |  IGuidedCalibration |  Acquire data for a cal step.  
[ApplyDeltaMatchFromCalSet](../Methods/ApplyDeltaMatchFromCalSet_Method.md) |  IGuidedCalibration2 |  Apply a cal as Delta Match Cal.  
[GenerateErrorTerms](../Methods/GenerateErrorTerms_Method.md) |  IGuidedCalibration |  Generates the error terms for the calibration.  
[GenerateGlobalDeltaMatchSequence](../Methods/GenerateGlobalDeltaMatchSequence_Method.md) |  IGuidedCalibration2 |  Initiates a global delta match calibration.  
[GenerateSteps](../Methods/GenerateSteps_Method.md) |  IGuidedCalibration |  Request to generate a connection list and return the number of steps required.  
[GetCompatibleCalKits](../Methods/GetCompatibleCalKits_Method.md) |  IGuidedCalibration5 |  Returns the list of cal kits for the connector type.  
[GetIsolationPaths](../Methods/GetIsolationPaths_Method.md) |  IGuidedCalibration3 |  Gets the list of port pairings for which isolation standards will be measured during calibration.  
[GetStepDescription](../Methods/Get_StepDescription_Method.md) |  IGuidedCalibration |  Query description of a step.  
[Initialize](../Methods/Initialize_Method.md) |  IGuidedCalibration |  Initial setup with channel context for the remote cal object.  
[ResetStep](../Methods/ResetStep_Method.md) |  IGuidedCalibration10 |  Resets the specified guided cal connection step as unmeasured.  
[SetIsolationPaths](../Methods/SetIsolationPaths_Method.md) |  IGuidedCalibration3 |  Sets the list of port pairings for which isolation standards will be measured during calibration.  
[SetupMeasurementsForStep](../Methods/SetupMeasurementsForStep_Method.md) |  IGuidedCalibration4 |  Show the Cal Window, or custom Cal Window, before acquiring a Cal standard.  
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[CalKitType](../Properties/CalKitType_fca_Property.md) |  IGuidedCalibration |  Sets the cal kit for the port.  
[CompatibleCalKits](../Properties/CompatibleCalKits_Property.md) |  IGuidedCalibration |  Superseded with [GetCompatibleCalKits Method](../Methods/GetCompatibleCalKits_Method.md)  
[ConnectorType](../Properties/ConnectorType_Property.md) |  IGuidedCalibration |  Sets the connector type for the port.  
[CustomCalConfiguration](../Properties/CustomCalConfiguration_Property.md) |  IGuidedCalibration4 |  Provides access to additional Properties and Methods which extends the GuidedCal Object.  
[IsolationAveragingIncrement](../Properties/IsolationAveragingIncrement_Property.md) |  IGuidedCalibration3 |  Value by which to increment the channel's averaging factor during measurement of isolation standards.  
[IterationCountForStep](../Properties/IterationCountForStep_Property.md) |  IGuidedCalibration10 |  Returns the number of iterative measurement acquisitions that has been made for the specified step.  
[MinimumIterationsForStep](../Properties/MinimumIterationsForStep_Property.md) |  IGuidedCalibration10 |  Returns the minimum number of required iterative measurement acquisitions for the specified step.  
[PathCalMethod](../Properties/PathCalMethod_Property.md) |  IGuidedCalibration3 |  Specifies the calibration method for each port pair.  
[PathThruMethod](../Properties/PathThruMethod_Property.md) |  IGuidedCalibration3 |  Specifies the calibration THRU method for each port pair.  
[PerformPowerCalibration](../Properties/PerformPowerCalibration_Property.md) |  IGuidedCalibration7 |  Perform Guided Power Cal.  
[PortsNeedingDeltaMatch](../Properties/PortsNeedingDeltaMatch_Property.md) |  IGuidedCalibration2 |  Returns port numbers that need delta match cal.  
[PowerCalibrationPowerLevel](../Properties/PowerCalibrationPowerLevel_Property.md) |  IGuidedCalibration6 |  Sets power level for power cal in several applications.  
[PowerSensorCalKitType](../Properties/PowerSensorCalKitType_Guided%20Property.md) |  IGuidedCalibration6 |  Sets Cal Kit for power cal in several applications.  
[PowerSensorConnectorType](../Properties/PowerSensorConnectorType_Guided_Property.md) |  IGuidedCalibration6 |  Sets Power sensor connector for power cal in several applications.  
[PowerTableFilename](../Properties/PowerTableFilename_Property.md) |  IGuidedCalibration9 |  Loads a file that defines a power table.  
[SlidingLoadAcquisitionBehavior](../Properties/SlidingLoadAcquisitionBehavior_Property.md) |  IGuidedCalibration10 |  Specifies the behavior for guided cal steps that involve a sliding load.  
[ThruCalMethod](../Properties/ThruCalMethod_Property.md) |  IGuidedCalibration |  Superseded with [PathCalMethod](../Properties/PathCalMethod_Property.md) and [PathThruMethod](../Properties/PathThruMethod_Property.md)  
[ThruPortList](../Properties/ThruPortList_Property.md) |  IGuidedCalibration |  Sets the thru connection port pairs.  
[UncertaintyEnabled](../Properties/UncertaintyEnabled_Property.md) |  IGuidedCalibration11 |  Enables Dynamic Uncertainty.  
[UseCalWindow](../Properties/UseCalWindow_Property.md) |  IGuidedCalibration |  Obsolete \- Use [Custom Cal Window](../../CalTopic.md#CustomWindow) commands.  
[ValidConnectorTypes](../Properties/ValidConnectorType_Property.md) |  IGuidedCalibration |  Gets Valid Connector Types.  
  
###  IGuidedCalibration History

Interface |  Introduced with VNA Rev:  
---|---  
IGuidedCalibration |  5.0  
IGuidedCalibration2 |  5.25  
IGuidedCalibration3 |  7.11  
IGuidedCalibration4 |  8.0  
IGuidedCalibration5 |  9.0  
IGuidedCalibration6 |  9.10  
IGuidedCalibration7 |  9.30  
IGuidedCalibration8 |   
IGuidedCalibration9 |  9.42  
IGuidedCalibration10 |  9.85  
IGuidedCalibration11 |  10.40  
  
* * *

