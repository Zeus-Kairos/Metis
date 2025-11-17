# Cables Collection

* * *

Description

Child of the [UncertaintyManager](UncertaintyManager_Object.md) Object. A
collection that provides a mechanism for iterating through the Cable objects.

### Accessing the Cables collection

Get a handle to an individual cable by specifying an item of the Cables
collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim cabs As Cables  
Set cabs = app.UncertaintyManager.Cables(1)  

### See Also:

  * [Cable Object](Cable_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Limit Line Testing Example](../../COM_Example_Programs/Limit_Line_Testing_Example_with_COM.md)

### Methods

|

### Description  
  
---|---  
[Item](../Methods/Item_Method.md) |  Get a handle by number to a cable in the cables collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of cables in the collection.  
  
### IUncertaintyCables History

Interface |  Introduced with VNA Rev:  
---|---  
IUncertaintyCables |  10.40

