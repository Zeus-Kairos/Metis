# CalibrateAllChannels Object

* * *

### Description

Use this interface to Calibrate All Channels.

[See Cal All Channels
limitations](../../../S3_Cals/Calibrate_All_Channels.htm#Limitations).

### Accessing the CalibrateAllChannels Object

Dim app as AgilentPNA835x.Application Dim CalMgr Set CalMgr =
app.GetCalManager Dim calAll Set calAll = CalMgr.CalibrateAllChannels 'Then
get a handle to the GuidedCal object Dim guidedCal Set guidedCal =
CalAll.GuidedCalibration  
---  
  
### See Also:

  * [Example program](../../COM_Example_Programs/Perform_a_CalAllChannels_Calibration.md)

  * Learn about [Calibrate All Channels](../../../S3_Cals/Calibrate_All_Channels.md).

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

In the following table ICalibrateAllChannels is abbreviated to ICalAllChans

### Methods

|

### Interface

[See History](CalManager_Object.md#Interface1) | 

### Description  
  
---|---|---  
[Reset](../Methods/Reset_\(CalAll\)_Method.md) | ICalAllChans | Resets all properties associated with the Cal All session to their default values.  
  
### Properties

|

###

|

###  
  
[CalibrationPorts](../Properties/CalibrationPorts_Property.md) | ICalAllChans | For each channel, sets and returns the ports to be calibrated.  
[Channels](../Properties/Channels_Property.md) | ICalAllChans | Sets and returns the list of channels to be calibrated during the Cal All session.  
[GeneratedCalsets](../Properties/GeneratedCalsets_Property.md) | ICalAllChans | Returns the cal set names that were produced by the cal all session.  
[GuidedCalibration](GuidedCalibration_Object.md) | ICalAllChans | Provides access to the GuidedCal object. Use this to perform the Calibration.  
[IFBW](../Properties/IFBW_Property.md) | ICalAllChans | Sets and returns the IFBW for a Cal All calibration.  
[IndependentPowerCalibration](../Properties/IndependentPowerCalibration_Property.md) | ICalAllChans2 | Returns a handle to an IndependentPowerCalibration object. Use this to add a power calibration for any port during a Cal All.  
[PathConfigurationElement](../Properties/PathConfigurationElement_Property.md) | ICalAllChans | Sets and returns the Path Configuration settings for a Cal All calibration.  
[PowerLevel](../Properties/PowerLevel-\(CalAll\)_Property.md) | ICalAllChans | Sets and returns the power level at which a Cal All calibration is to be performed.  
[PowerOffset](../Properties/PowerOffset_\(CalAll\)_Property.md) | ICalAllChans | Sets and returns the power offset value for a Cal All calibration.  
[PropertyNames](../Properties/PropertyNames_Property.md) | ICalAllChans | Returns the settable properties for the current cal all session.  
[PropertyNamesByMeasurementClass](../Properties/PropertyNamesByMeasurementClass_Property.md) | ICalAllChans | Returns the list of settable cal-all properties associated with the specified measurement class.  
[PropertyValue](../Properties/PropertyValue_Property.md) | ICalAllChans | Sets and returns a value for a specific property name  
[PropertyValues](../Properties/PropertyValues_Property.md) | ICalAllChans | Returns the valid property values for a specific property name.  
[ReceiverAttenuator](../Properties/ReceiverAttenuator_Property.md) | ICalAllChans | Sets and returns the Receiver Attenuator setting for a Cal All calibration.  
[SourceAttenuator](../Properties/SourceAttenuator_Property.md) | ICalAllChans | Sets and returns the Source Attenuator setting for a Cal All calibration.  
[SParameterCalPorts](../Properties/SParameterCalPorts_Property.md) | ICalAllChans | Returns a list of ports to be calibrated.  
[UserCalsetPrefix](../Properties/UserCalsetPrefix_Property.md) | ICalAllChans | Sets and returns the prefix to be used when saving User CalSets that result from the Cal All session.  
  
###  ICalibrateAllChannels History

Interface | Introduced with VNA Rev:  
---|---  
ICalibrateAllChannels | 9.50  
ICalibrateAllChannels2 | 12.80  
  
* * *

* * *

