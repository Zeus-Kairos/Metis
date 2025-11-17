# Characterizer Object

* * *

### Description

Provides access to the properties and methods that are used to characterize
Noise and Cables for the Dynamic Uncertainty application.

### Accessing the Characterizer object

Get a handle to the Characterizer object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim oChar as Characterizer  
Set oChar = app.UncertaintyManager.Characterizer  

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
[InitiateCableCharacterization](../Methods/InitiateCableCharacterization_Method.md) |  IUncertaintyCharacterizer |  Initiates a Cable Repeatability characterization  
[InitiateNoiseCharacterization](../Methods/InitiateNoiseCharacterization_Method.md) |  IUncertaintyCharacterizer |  Initiates a Noise characterization  
  
### Properties

|

###

|

###  
  
[GuidedCalibration](GuidedCalibration_Object.md) |  IUncertaintyCharacterizer |  Returns a handle in order to perform a Guided Calibration.  
  
###  IUncertaintyManager History

Interface |  Introduced with VNA Rev:  
---|---  
IUncertaintyManager |  10.40

