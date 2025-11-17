# ExternalTestsets Collection

* * *

Description

ExternalTestsets collection provides access to a TestsetControl object. Only
one external testset can be controlled by the VNA at any time.

#### Accessing the ExternalTestsets collection

The ExternalTestsets collection is a property of the main Application Object.
You can obtain a handle to a testset by specifying an item in the collection.

### Visual Basic Example

Dim pna  
Dim testsets As ExternalTestsets  
Dim tset1 As TestsetControl  
Set pna = CreateObject("AgilentPNA835x.Application")  
Set testsets = pna.ExternalTestsets  
Set tset1 = testsets(1)  
' make COM calls on tset1 object  
End Sub

### See Also:

[ExternalTestset Control COM
Example](../../COM_Example_Programs/External_Testset_Control.htm)

[About External TestSet Control](../../../System/External_Testset_Control.md)

[TestsetControl Object](TestsetControl_Object.md)

[The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Description  
  
---|---  
[Add](../Methods/Add_Testset_Method.md) |  Adds a testset to the collection and loads a test set configuration file.  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a testset in the collection.  
[TestsetCatalog](../Methods/TestsetCatalog_Method.md) |  Returns a list of supported test sets.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of items in a collection of objects.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the current naNetworkAnalyzer application.  
  
### ExternalTestsets History

Interface |  Introduced with VNA Rev:  
---|---  
IExternalTestsets |  6.0  
IExternalTestsets |  6.2

