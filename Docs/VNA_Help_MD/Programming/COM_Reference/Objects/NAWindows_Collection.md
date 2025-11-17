# NAWindows Collection

* * *

### Description

A collection object that provides a mechanism for iterating through the
Application windows.

### Accessing the NaWindows collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim windows As NAWindows  
Set windows = app.NAWindows

### See Also:

  * [NAWindow Object](NAWindow_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[Add](../Methods/Add_NAWindows_Method.md) |  Adds a window to the NAWindows collection.  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a window in the collection.  
[Remove](../Methods/Remove_Method.md) |  Removes a window from the NAWindows collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of windows on the analyzer.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the current Application.

