# ExternalPulseGenerator Object

* * *

Description

The ExternalPulseGenerator object allows you to set unique properties and
methods for each external pulse generator.

### Accessing the ExternalPulseGenerator Object

You can obtain a handle to an ExternalSource Object through
[ExtendedProperties](../Properties/ExtendedProperties_Property.md)

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count externalDevices.Add "81110" dim
newExternalDevice Set newExternalDevice = externalDevices.Item("81110")
newExternalDevice.DeviceType = "Pulse Generator" newExternalDevice.Driver =
"AGPULSEGEN" newExternalDevice.Active = True
newExternalDevice.IOConfiguration= "GPIB0::19::INSTR" dim extPulseGen Set
extPulseGen = newExternalDevice.ExtendedProperties extPulseGen.HighAmplitude =
3  
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
  
[HighAmplitude](../Properties/HighAmplitude_Property.md) | ExternalPulseGenerator | Sets the High amplitude (voltage).  
[LoadImpedance](../Properties/LoadImpedance_Property.md) | ExternalPulseGenerator | Sets the Load impedance.  
[LowAmplitude](../Properties/LowAmplitude_Property.md) | ExternalPulseGenerator | Sets the Low amplitude (voltage).  
[PrimaryMode](../Properties/MasterMode_Property.md) | ExternalPulseGenerator2 | Sets the primary mode for the ext. pulse generator.  
[OutputChannel](../Properties/OutputChannel_Property.md) | ExternalPulseGenerator | Sets the Output channel (port) of the pulse generator.  
[SourceImpedance](../Properties/SourceImpedance_Property.md) | ExternalPulseGenerator | Sets the Source impedance.  
  
### ExternalPulseGenerator History

Interface | Introduced with VNA Rev:  
---|---  
IExternalPulseGenerator | 9.50  
ExternalPulseGenerator2 | 9.50

