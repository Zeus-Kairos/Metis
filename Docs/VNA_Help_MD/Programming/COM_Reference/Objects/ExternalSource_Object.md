# ExternalSource Object

* * *

Description

The ExternalSource object allows you to set unique properties and methods for
each external source.

### Accessing the ExternalSource Object

You can obtain a handle to an ExternalSource Object through
[ExtendedProperties](../Properties/ExtendedProperties_Property.md)

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count externalDevices.Add "NewPSG" dim
newExternalDevice Set newExternalDevice = externalDevices.Item("NewPSG")
newExternalDevice.DeviceType = "Source" newExternalDevice.IOConfiguration=
"GPIB0::14::INSTR" dim PSG Set PSG = newExternalDevice.ExtendedProperties
PSG.DwellPerPoint = 5  
---  
  
### See Also:

[Configure an External
Device](../../../System/Configure_an_External_Device.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[DwellPerPoint](../Properties/DwellPerPoint_Property.md) | IExternalSource | Sets and returns the dwell time for an external source.  
[EnableModulationControl](../Properties/EnableModulationControl_Property.md) | IExternalSource2 | Enables/disables control of modulation in an external source.  
[IsEnhancedModulationControl](../Properties/IsEnhancedModulationControl_Property.md) | IExternalSource3 | Enables/disables control of modulation in an external source capable of downloading modulation files.  
[TriggerMode](../Properties/TriggerMode_ExtDev_Property.md) | IExternalSource | Sets and returns the trigger mode (Software / Hardware) for an external source.  
[TriggerPort](../Properties/TriggerPort_Property.md) | IExternalSource | Sets and returns the VNA port through which an external source is to be triggered.  
  
### ExtendedProperties History

Interface | Introduced with VNA Rev:  
---|---  
IExternalSource | 9.0  
IExternalSource2 | 10.49  
IExternalSource3 | 13.60  
  
* * *

