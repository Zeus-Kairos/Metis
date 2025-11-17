# Cable Object

* * *

### Description

Provides access to the properties and methods that are used to reset data
associated with the cable object.

### Accessing the Cable object

Get a handle to the Cable object through the Cables Collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim oCables as UncertaintyManager  
Set oCables = app.UncertaintyManager.Cables  
  
Dim oCable1 as Cables(1)

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

### Methods

|

### Interface

[See History](CalManager_Object.md#Interface1) | 

### Description  
  
---|---|---  
[ResetRepeatability](../Methods/ResetRepeatability_Method.md) | IUncertaintyCable | Resets (clears) the repeatability data associated with the cable object.  
  
### Properties

|

###

|

###  
  
[Name](../Properties/Name_uncert_Property.md) | IUncertaintyCable | Return the cable name.  
  
###  IUncertaintyCable History

Interface | Introduced with VNA Rev:  
---|---  
IUncertaintyCable | 10.40

