# Traces Collection

* * *

### Description

Child of the Application Object. A collection that provides a mechanism for
getting a handle to a trace or iterating through the traces in a window.

### Accessing the Traces collection

Get a handle to the traces collection through the NaWindows collection. The
following example sets the variable trcs to the collection of traces in window
1 of the NaWindows collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim trcs As traces  
Set trcs = app.NAWindows(1).traces

### See Also:

  * [Trace Object](Trace_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a trace  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of traces in the collection.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the current Application.

