# SMCType Object

* * *

### Description

Contains the methods and properties to perform an Scalar Measurement
Calibration for the Frequency Converter Application (option S93083A/B).

### Accessing the SMCType object

See an example which [creates and calibrates an SMC
measurement](../../COM_Example_Programs/Create_and_Cal_an_SMC_Measurement.htm).

You can also do the following:

Set app = CreateObject("AgilentPNA835x.Application") Set CalMgr =
app.GetCalManager Set guidedCal = CalMgr.CreateCustomCalEx(1) Set SMC =
guidedCal.CustomCalConfiguration SMC.ConnectorType(1) = "APC 3.5 male"  
---  
  
### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](SMC_Type_Object.md#history) | 

### Description  
  
---|---|---  
[AcquireStep](../Methods/AcquireStep_Method.md) | ISMCType | Acquire the measurement data for the specified step in the calibration process.  
[GenerateErrorTerms](../Methods/GenerateErrorTerms_Method.md) | ISMCType | Generates the error terms for the calibration.  
[GenerateSteps](../Methods/GenerateSteps_Method.md) | ISMCType | Returns the number of steps required to complete the calibration.  
[GetStepDescription](../Methods/Get_StepDescription_Method.md) | ISMCType | Returns the description of the specified step calibration process.  
[ImportDataSet](../Methods/ImportDataSet_Method.md) | ISMCType4 | Imports separate power meter data for SMC cal.  
[Initialize](../Methods/Initialize_Method.md) | ISMCType | Begins a calibration.  
  
### Properties

|

###

|

### Description  
  
[AutoOrient](../Properties/AutoOrient_Property.md) | ISMCType | Sets ECAL module automatic orientation ON or OFF.  
[CalibrationPort](../Properties/CalibrationPort_Property.md) | ISMCType | Sets or returns the calibration source port for the calibration.  
[CalKitType](../Properties/CalKitType_fca_Property.md) | ISMCType | Sets and returns a calibration kit type for calibration.  
[CompatibleCalKits](../Properties/CompatibleCalKits_Property.md) | ISMCType | Returns a list of cal kits that are compatible with the connector type for the specified port.  
[ConnectorType](../Properties/ConnectorType_Property.md) | ISMCType | Sets or queries the connector type for the specified port.  
[Do2PortEcal](../Properties/Do2PortEcal_Property.md) | ISMCType | Superseded \- Replaced by [CalKitType](../Properties/CalKitType_fca_Property.md) Specify ECAL or Mechanical calibration.  
[EcalCharacterization](../Properties/ECALCharacterization_smc_Property.md) | ISMCType | Superseded \- Replaced by [CalKitType](../Properties/CalKitType_fca_Property.md) Specifies the characterization data within an ECal module to be used for the calibration.  
[EcalOrientation](../Properties/EcalOrientation_Property.md) | ISMCType | Specifies which port of the ECal module is connected to which port of the VNA when the AutoOrient property = False.  
[EnableLOPowerCal](../Properties/EnableLOPowerCal_Property.md) | ISMCType5 | Enable LO Power Cal  
[FixedDelay](../Properties/FixedDelay_Property.md) | ISMCType5 | Set and return the known delay through the calibration mixer.  
[MixerCharacterizationFile](../Properties/MixerCharacterizationFile_Property.md) | ISMCType5 | Set the filename of the S2P file used to characterize the calibration mixer.  
[NetworkFilename](../Properties/NetworkFilename_Property.md) | ISMCType2 | Specifies the S2P filename to embed or de-embed on the input or output of your mixer measurement.  
[NetworkMode](../Properties/NetworkMode_Property.md) | ISMCType2 | Embed (add) or de-embed (remove) circuit network effects on the input and output of your mixer measurement.  
[OmitIsolation](../Properties/OmitIsolation_Property.md) | ISMCType | Superseded \- Replaced by [SetIsolationPaths](../Methods/SetIsolationPaths_Method.md) and [GetIsolationPaths](../Methods/GetIsolationPaths_Method.md) Sets and returns whether Isolation portion of the calibration will be performed or not.  
[SeparatePowerCal](../Properties/SeparatePowerCal_Property.md) | ISMCType4 | Use a Thru standard or to use two power sensor connections during the SMC power cal  
[ThruCalMethod](../Properties/ThruCalMethod_fca_Property.md) | ISMCType | Superseded \- Replaced by [PathThruMethod Property](../Properties/PathThruMethod_Property.md) Sets and returns the method for performing the thru portion of the calibration.  
[ValidConnectorTypes](../Properties/ValidConnectorType_Property.md) | ISMCType | Returns a list of connector types for which there are calibration kits.  
  
###  ISMCType History

Interface | Introduced with VNA Rev:  
---|---  
ISMCType | 3.5  
ISMCType2 | 6.0  
ISMCType4 | 9.0

