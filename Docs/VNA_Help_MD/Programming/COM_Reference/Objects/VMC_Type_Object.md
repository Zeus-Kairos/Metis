# VMC Type Object

* * *

Description

Contains the methods and properties to perform a Vector Measurement
Calibration for the Frequency Converter Application (option S93083A/B).

### Accessing the VMCType object

See an example which [creates and calibrates a VMC
measurement](../../COM_Example_Programs/Create_and_Cal_a_VMC_Measurement.htm).

You can also do the following:

Set app = CreateObject("AgilentPNA835x.Application") Set CalMgr =
app.GetCalManager Set guidedCal = CalMgr.CreateCustomCalEx(1) Set VMC =
guidedCal.CustomCalConfiguration VMC.ConnectorType(1) = "APC 3.5 male"  
---  
  
### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](VMC_Type_Object.md#history) | 

### Description  
  
---|---|---  
[AcquireStep](../Methods/AcquireStep_Method.md) | IVMCType | Acquire the measurement data for the specified step in the calibration process.  
[GenerateErrorTerms](../Methods/GenerateErrorTerms_Method.md) | IVMCType | Generates the error terms for the calibration.  
[GenerateSteps](../Methods/GenerateSteps_Method.md) | IVMCType | Returns the number of steps required to complete the calibration.  
[GetStepDescription](../Methods/Get_StepDescription_Method.md) | IVMCType | Returns the description of the specified step in the calibration process.  
[Initialize](../Methods/Initialize_Method.md) | IVMCType | Begins a calibration.  
  
### Properties

|

###

|

### Description  
  
[AutoOrient](../Properties/AutoOrient_Property.md) | IVMCType | Sets ECAL module automatic orientation ON or OFF.  
[CalKitType](../Properties/CalKitType_fca_Property.md) | IVMCType | Sets and returns a calibration kit type for calibration.  
[CharacterizeMixerOnly](../Properties/CharacterizeMixerOnly_Property.md) | IVMCType | Sets and returns whether to perform a mixer characterization ONLY or full 2-port calibration.  
[CharFileName](../Properties/CharFileName_Property.md) | IVMCType | Specifies the .S2P mixer characterization file name.  
[CharMixerReverse](../Properties/CharMixerReverse_Property.md) | IVMCType2 | Specifies the direction in which to characterize the calibration mixer.  
[CompatibleCalKits](../Properties/CompatibleCalKits_Property.md) | IVMCType | Returns a list of cal kits that are compatible with the connector type for the specified port.  
[ConnectorType](../Properties/ConnectorType_Property.md) | IVMCType | Sets or queries the connector type for the specified port.  
[Do1PortEcal](../Properties/Do1PortEcal_Property.md) | IVMCType | Superseded with [CalKitType](../Properties/CalKitType_fca_Property.md) Specify ECAL or Mechanical calibration for the mixer characterization portion of a VMC calibration.  
[Do2PortEcal](../Properties/Do2PortEcal_Property.md) | IVMCType | Superseded with [CalKitType](../Properties/CalKitType_fca_Property.md) Specify ECAL or Mechanical calibration for the 2-port calibration portion of a VMC calibration.  
[EcalCharacterization](../Properties/ECALCharacterization_vmc_Property.md) | IVMCType | Superseded with [CalKitType](../Properties/CalKitType_fca_Property.md) Specifies the characterization data within an ECal module to be used for the calibration.  
[EcalOrientation1Port](../Properties/EcalOrientation1Port_Property.md) | IVMCType | For Mixer Characterization ONLY - Specifies which port of the ECal module is connected to which port of the VNA  
[EcalOrientation2Port](../Properties/EcalOrientation2Port_Property.md) | IVMCType | For full 2-port VMC cal - Specifies which port of the ECal module is connected to which port of the VNA  
[EnableLOPowerCal](../Properties/EnableLOPowerCal_Property.md) | IVMCType4 | Perform LO Power Cal  
[LoadCharFromFile](../Properties/LoadCharFromFile_Property.md) | IVMCType | Specifies and loads a mixer characterization (S2P) file.  
[NetworkFilename](../Properties/NetworkFilename_Property.md) | IVMCType3 | Specifies the S2P filename to embed or de-embed on the input or output of your mixer measurement.  
[NetworkMode](../Properties/NetworkMode_Property.md) | IVMCType3 | Embed (add) or de-embed (remove) circuit network effects on the input and output of your mixer measurement.  
[OmitIsolation](../Properties/OmitIsolation_Property.md) | IVMCType | Superseded \- Replaced by [SetIsolationPaths](../Methods/SetIsolationPaths_Method.md) and [GetIsolationPaths](../Methods/GetIsolationPaths_Method.md) Sets and returns whether Isolation portion of the calibration will be performed or not.  
[ThruCalMethod](../Properties/ThruCalMethod_fca_Property.md) | IVMCType | Superseded \- Replaced by [PathThruMethod Property](../Properties/PathThruMethod_Property.md) Sets and returns the method for performing the thru portion of the calibration.  
[ValidConnectorTypes](../Properties/ValidConnectorType_Property.md) | IVMCType | Returns a list of connector types for which there are calibration kits.  
  
###  IVMCType History

Interface | Introduced with VNA Rev:  
---|---  
IVMCType | 3.5  
IVMCType2 | 3.53  
IVMCType3 | 6.0  
IVMCType4 | 9.1

