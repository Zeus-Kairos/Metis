## ECalUserCharacterizer Object

* * *

### Description

Controls the settings used to perform an ECal User Characterization. An
S-Parameter channel must already be calibrated. These commands will then
measure the ECal module with adapters, cables, or fixtures to be included in
the User Characterization, allow descriptive text to be entered, then save the
User Characterization to the ECal module.

Up to 12 User Characterizations can be stored in an ECal module.

You can NOT perform a remote User Characterization of a 4-port ECal module
using a 2-port VNA. This can only be done from the front panel user interface.

### Accessing the ECalUserCharacterizer Interface

Access the Interface through the ICalManager Object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application")  
  
Dim mgr as ICalManager  
Set mgr = app.GetCalManager  
Dim ecalCharacterizer  
Set ecalCharacterizer = mgr.GetECalUserCharacterizer()

### See Also:

Example: [Perform an ECal User
Characterization](../../COM_Example_Programs/Perform_an_ECal_User_Characterization.htm)

[VNA Automation
Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

[About User Characterization](../../../S3_Cals/ECal_User_Characterization.md)

### Methods

|

### Interface

[See History](IMixer_Interface.md#History) | 

### Description  
  
---|---|---  
[AcquireStep](../Methods/AcquireStep_Method.md) |  ECalUserCharacterizer |  Measure the ECal module.  
[GenerateSteps](../Methods/GenerateSteps_Method.md) |  ECalUserCharacterizer |  Returns the number of steps required to complete the calibration.  
[GetStepDescription](../Methods/Get_StepDescription_Method.md) |  ECalUserCharacterizer |  Returns the description of the specified step in the calibration process.  
[Initialize](../Methods/Initialize_ECal.md) |  ECalUserCharacterizer |  Superseded with [InitializeEx Method](../Methods/InitializeEx_Method.md)  
[InitializeEx](../Methods/InitializeEx_Method.md) |  ECalUserCharacterizer2 |  Initiates a User Characterization of an ECal module.  
[SaveToDiskMemory](../Methods/SaveToDiskMemory_Method.md) |  ECalUserCharacterizer2 |  Saves the User Characterization to VNA disk memory.  
[SaveToECal](../Methods/SaveToECal_Method.md) |  ECalUserCharacterizer |  Saves the User Characterization to the ECal module.  
  
### Properties

|

###

|

### Description  
  
[CharacterizationNumber](../Properties/CharacterizationNumber_Property.md) |  ECalUserCharacterizer |  Sets and reads the number to which the user characterization will be stored in the ECal module.   
[ConnectorType](../Properties/ConnectorType_ECal_Property.md) |  ECalUserCharacterizer |  Sets or queries the connector type for the specified port.  
[ECalID](../Properties/ECalID_Property.md) |  ECalUserCharacterizer |  Select the model and serial number of the ECal module to be characterized.  
[InSituCharacterization](../Properties/InSituCharacterization_Property.md) |  ECalUserCharacterizer3 |  Sets or returns whether the CalPod module will be characterized as an in situ device.  
[PortDescription](../Properties/PortDescription_Property.md) |  ECalUserCharacterizer |  Sets and reads the description of the adapters, cable, or fixture to be included in the user characterization.  
[SupportsInSituCharacterization](../Properties/SupportsInSituCharacterization_Property.md) |  ECalUserCharacterizer3 |  Returns whether the device is a CalPod module  
[UserDescriptionofPNA](../Properties/UserDescriptionOfPNA_Property.md) |  ECalUserCharacterizer |  Sets and reads a user description of the VNA used to perform the User Characterization.  
[UserName](../Properties/UserName_Property.md) |  ECalUserCharacterizer |  Sets and reads the description of the person and/or company who is producing the ECal user characterization.  
[ValidConnectorTypes](../Properties/ValidConnectorType_Property.md) |  ECalUserCharacterizer |  Returns a list of connector names that are valid for use with user-characterized ECal modules.  
  
### IECalUserCharacterizer History

Interface |  Introduced with VNA Rev:  
---|---  
IECalUserCharacterizer |  8.33  
IECalUserCharacterizer2 |  9.00  
  
* * *

