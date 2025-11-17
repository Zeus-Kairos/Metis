# ExternalDevices Collection

* * *

### Description

ExternalDevices collection provides access to an ExternalDevice object.

### Accessing the ExternalDevices collection

The ExternalDevices collection is a property of the main Application Object.
You can obtain a handle to an External Device by specifying an item in the
collection.

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count externalDevices.Add "NewPMAR" dim
newExternalDevice Set newExternalDevice = externalDevices.Item("NewPMAR")
newExternalDevice.DeviceType = "Power Meter"
newExternalDevice.IOConfiguration= "GPIB0::14::INSTR"
newExternalDevice.IOEnable = true  
---  
  
### See Also:

Example: [Create a PMAR Device and
Measurement](../../COM_Example_Programs/Create_a_PMAR_Device_and_Measurement.htm)

[Configure an External
Device](../../../System/Configure_an_External_Device.htm)

[ExternalDevice Object](ExternalDevice_Object.md)

[The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Interface

[See History](ExternalDevices_Collection.md#History) | 

### Description  
  
---|---|---  
[Add](../Methods/Add_External_Device_Method.md) |  IExternalDevices |  Adds an external device to the system.  
[Item](../Methods/Item_Method.md) |  IExternalDevices |  Use to get a handle to an external device in the collection.  
[Remove](../Methods/Remove_Method.md) |  IExternalDevices |  Removes an external device from the system  
  
### Properties

|  | 

### Description  
  
[Count](../Properties/Count_Property.md) |  IExternalDevices |  Returns the number of devices in the ExternalDevices collection.  
[DeviceNames](../Properties/DeviceNames_Property.md) |  IExternalDevices2 |  Returns the device names in the collection  
[HasItem](../Properties/HasItem_Property.md) |  IExternalDevices |  Returns a value indicating whether the specified external devices is configured.  
[IsDevicePresent](../Properties/IsDevicePresent_Property.md) |  IExternalDevices2 |  Returns whether the named device is present on the bus for which it is configured.  
[Items](../Properties/Items_Property.md) |  IExternalDevices |  Returns an array of configured devices in the system.  
[Parent](../Properties/Parent_Property.md) |  IExternalDevices |  Returns a handle to the current [application object.](Application_Object.md)  
  
### IExternalDevices History

Interface |  Introduced with VNA Rev:  
---|---  
IExternalDevices |  9.0  
IExternalDevices2 |  9.50  
  
* * *

