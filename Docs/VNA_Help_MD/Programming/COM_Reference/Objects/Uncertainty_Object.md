# Uncertainty Object

* * *

### Description

Provides access to the properties and methods that are used to display
uncertainties for the measurement (Option S93015A/B).

#### Limitations

  * Calibrations can be performed for ONLY ONE channel at a time.

  * Putting Error Term data into Uncertainty Cal Sets using [remote commands](../../DataTopic.md#putCalData) is NOT supported.

### Accessing the Uncertainty object

Get a handle to the Uncertainty object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim oUncert as Uncertainty  
Set oUncert = app.ActiveMeasurement.Uncertainty  

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
[WriteUncertaintyFile](../Methods/WriteUncertaintyFile_Method.md) | IUncertainty | Saves uncertainty data for the specified ports in three different formats.  
  
### Properties

|

###

|

###  
  
[CableRepeatabilityUncertainty](../Properties/CableRepeatabilityUncertainty_Property.md) | IUncertainty | Sets and returns whether to include the cable/connection repeatability contribution for the measurement trace.  
[CoverageFactor](../Properties/CoverageFactor_Property.md) | IUncertainty | Sets and returns the coverage factor value to apply to the displayed uncertainty for the measurement trace  
[DisplayType](../Properties/DisplayType_Property.md) | IUncertainty | Sets and returns the display type for uncertainties for the measurement trace  
[ErrorTermUncertainty](../Properties/ErrorTermUncertainty_Property.md) | IUncertainty | Sets and returns whether to include the uncertainties associated with the correction error terms in the uncertainty values for the measurement trace.  
[MeasurementNoiseUncertainty](../Properties/MeasurementNoiseUncertainty_Property.md) | IUncertainty | Sets and returns whether the noise contribution is currently included in the uncertainty values for the measurement trace.  
  
###  IUncertainty History

Interface | Introduced with VNA Rev:  
---|---  
IUncertainty | 10.40

