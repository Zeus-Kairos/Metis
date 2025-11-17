# Ports Collection

* * *

Description

A collection object that provides a mechanism for iterating through the
Uncertainty Manager Port objects.

### Accessing the Ports Collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim oPorts as UncertaintyManager  
Set oPorts = app.UncertaintyManager.Ports  
  
Dim oPort1 as Ports(1)

### See Also:

  * [Port Object](Port_Object.md)

  * [UncertaintyManager Object](UncertaintyManager_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[CopyNoiseToAllPorts](../Methods/CopyNoiseToAllPorts_Method.md) |  Copies the characterized noise data associated with the specified port, to all the other ports.  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a Port object in the collection.  
[ResetNoiseForAllPorts](../Methods/ResetNoiseForAllPorts_Method.md) |  Clears the characterized noise data for ALL VNA port objects in the Ports collection.  
[SelectCableForAllPorts](../Methods/SelectCableForAllPorts_Method.md) |  Selects the name of the cable to be associated with all the ports in the Ports collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of objects in the collection.  
  
### IUncertaintyPorts History

Interface |  Introduced with VNA Rev:  
---|---  
IUncertaintyPorts |  10.40

