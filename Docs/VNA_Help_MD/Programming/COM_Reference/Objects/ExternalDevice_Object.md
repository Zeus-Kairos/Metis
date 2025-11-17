# ExternalDevice Object

* * *

Description

ExternalDevice objects allow you to set properties and methods for each
external device.

### Accessing the ExternalDevice Object

Obtain a handle to an External Device by specifying an item in the [External
Devices collection.](ExternalDevices_Collection.htm)

Although the following example shows how to create a PMAR external device, you
can substitute any supported external device for "PMAR" and DeviceType: "Power
Meter".

### Supported External Device Objects

[ExternalSource Object](ExternalSource_Object.md)

[ExternalDCDevice Object](ExternalDCDevice_Object.md)

[PowerSensorAsReceiver Object](PowerSensorAsReceiver_Object.md)

[ExternalPulseGenerator Object](ExternalPulseGenerator_Object.md)

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count externalDevices.Add "NewPMAR" dim
newExternalDevice Set newExternalDevice = externalDevices.Item("NewPMAR")
newExternalDevice.DeviceType = "Power Meter"
newExternalDevice.IOConfiguration= "GPIB0::14::INSTR"
newExternalDevice.IOEnable = true  
---  
  
### See Also:

[The VNA Object Model](The_Analyzer_Object_Model.md)

Learn how to [Configure an External
Device](../../../System/Configure_an_External_Device.htm)

### Methods

|

### Interface

[See History](ExternalDevice_Object.md#History) | 

### Description  
  
---|---|---  
[LoadFile](../Methods/LoadFile_ED_Method.md) |  IExternalDevice2 |  Recalls an external device configuration file from the VNA hard drive. Currently, only DC Meter and DC Supply devices are supported.  
[SaveFile](../Methods/SaveFile_ED_Method.md) |  IExternalDevice2 |  Saves an external device configuration file to the VNA hard drive. Currently, only DC Meter and DC Supply devices are supported.  
  
### Properties

|

###

|

### Description  
  
[Active](../Properties/Active_ExtDev_Property.md) |  IExternalDevice |  Sets and returns the state of activation for an external device.  
[DeviceType](../Properties/DeviceType_Property.md) |  IExternalDevice |  Sets and returns the DeviceType (source, power meter) for the external device.  
[Driver](../Properties/Driver_Property.md) |  IExternalDevice |  Sets and returns the external device driver (model).  
[ExtendedProperties](../Properties/ExtendedProperties_Property.md) |  IExternalDevice |  Provides access to properties that are unique to the external device type.  
[IOConfiguration](../Properties/IOConfiguration_Property.md) |  IExternalDevice |  Sets and returns the method of communication and address for the external device.  
[IOEnable](../Properties/IOEnable_Property.md) |  IExternalDevice |  Sets and returns whether an external device is available for IO communication with the VNA.  
[Name](../Properties/Name_ExtDev_Property.md) |  IExternalDevice |  Sets and returns the name of the External Device.  
[TimeOut](../Properties/TimeOut_Property.md) |  IExternalDevice |  Sets and returns the time out value for communication with the external device.  
  
### ExternalDevice History

Interface |  Introduced with VNA Rev:  
---|---  
IExternalDevice |  9.0  
IExternalDevice2 |  9.50  
  
* * *

