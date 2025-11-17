# CalSets Collection

* * *

Description

A collection object that provides a mechanism for iterating through all the
Cal Sets in the analyzer. There is no ordering to the items in the collection.
Therefore make no assumptions about the formatting of the collection.

For the Item and Remove methods, you can specify either the Cal Set string
name, or the integer item of the Cal Set in the collection.

### Accessing the CalSets collection

Get a handle to the CalSets collection through the CalManager object with the
app.[GetCalManager](../Methods/Get_CalManager_Method.md) Method.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim calsts As CalSets  
Set calsts = app.GetCalManager.CalSets

### See Also:

  * [CalSet Object](CalSet_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[Exists](../Methods/Exists_Method.md) |  ICalSets2 |  Returns whether the specified Cal Set exists  
[Item](../Methods/Item_Method.md) |  ICalSets |  Returns a handle to a CalSet object in the collection.  
[Remove](../Methods/Remove_Method.md) |  ICalSets |  Deletes the Cal Set residing at position index in the collection.  
  
### Properties

|

###

|

### Description  
  
[Count](../Properties/Count_Property.md) |  ICalSets |  Returns the number of Cal Sets in the collection.  
  
### CalSets History

Interface |  Introduced with VNA Rev:  
---|---  
ICalSets |  1.0  
ICalSets2 |  9.33  
  
* * *

  

