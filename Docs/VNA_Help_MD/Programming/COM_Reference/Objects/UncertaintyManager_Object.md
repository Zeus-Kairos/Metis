# UncertaintyManager Object

* * *

### Description

Provides access to the properties and methods that are used to characterize
Dynamic Uncertainties (Option S93015A/B).

### Accessing the UncertaintyManager object

Get a handle to a the UncertaintyManager through the Application Object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim uMgr as UncertaintyManager  
Set uMgr = app.UncertaintyManager

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

[See History](CalManager_Object.md#Interface1) | 

### Description  
  
---|---|---  
[Recall](../Methods/Recall_uncert_Method.md) |  UncertaintyManager |  Loads an uncertainty workspace (*.ml4) file.  
[Save](../Methods/Save_uncert_Method.md) |  UncertaintyManager |  Saves an uncertainty workspace (*.ml4) file.  
  
### Properties

|

###

|

###  
  
[CableRepeatabilityEnabled](../Properties/CableRepeatabilityEnabled_Property.md) |  UncertaintyManager |  Allows cable repeatability data to contribute to the uncertainty of a calibration.  
[Cables](Cables_Collection.md) |  UncertaintyManager |  Provides access to the collection of characterized cables used in Dynamic Uncertainty calibrations.  
[Characterizer](Characterizer_Object.md) |  UncertaintyManager |  Provides access to the Methods and Properties used to perform Uncertainty characterizations.  
[MaximumUncertaintyPoints](../Properties/MaximumUncertaintyPoints_Property.md) |  UncertaintyManager |  Sets and returns maximum number of points for which uncertainties are to be computed.  
[PortNoiseEnabled](../Properties/PortNoiseEnabled_Property.md) |  UncertaintyManager |  Allows noise data to contribute to the uncertainty of a calibration.  
[Ports](Ports_Collection.md) |  UncertaintyManager |  Provides access to the collection of VNA ports used in Dynamic Uncertainty calibrations.  
[StandardDefinitionsEnabled](../Properties/StandardDefinitionsEnabled_Property.md) |  UncertaintyManager |  Allows cal standard data to contribute to the uncertainty of a calibration.  
  
###  IUncertaintyManager History

Interface |  Introduced with VNA Rev:  
---|---  
IUncertaintyManager |  10.40

