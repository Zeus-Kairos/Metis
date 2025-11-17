# ECalModules Collection

* * *

Description

A collection that provides access to ECal modules that are connected to the
VNA.

### Accessing the ECalModules collection

Dim app As AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application", <analyzerName>) Dim eCalMods As
ECalModules Set eCalMods = app.GetCalManager.ECalModules  
---  
  
### See Also:

  * [Using ECal](../../../S3_Cals/Using_ECal.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|  Description  
---|---|---  
[Item](../Methods/Item_Method.md) |  IECalModules |  Use to get a handle to a [ECalModule Object](ECalModule_Object.md) in the collection.  
[OutputSNPFromECal Method](../Methods/OutputSNPFromECal_Method.md) |  IECalModules2 |  Read S parameter of ECal Thur from the ECal memory and save it as s2p file.  
  
### Properties

|

### Interface

|

### Description  
  
[Count](../Properties/Count_Property.md) |  IECalModules |  Returns the number of objects in the collection.  
[Parent](../Properties/Parent_Property.md) |  IECalModules |  Returns a handle to the [CalManager](CalManager_Object.md) Object  
  
###  IECalModules History

Interface |  Introduced with VNA Rev:  
---|---  
IECalModules |  8.50  
IECalModules2 |  12.50.01  
  
* * *

