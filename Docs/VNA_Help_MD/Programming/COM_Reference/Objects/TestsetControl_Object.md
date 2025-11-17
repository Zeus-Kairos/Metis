# TestsetControl Object

* * *

Description

A TestsetControl object is used to control one of the [supported test
sets](../../../System/External_Testset_Control.htm#Supported). Only one
external test set can be controlled by the VNA at any time. The Testset
Control object appears as an item in the ExternalTestsets collection, which in
turn is a property of the main application object.

If the specified test set is not connected to the VNA or is not ON, then
setting [Enabled](../Properties/Enabled_Property.md) = True will return an
error. All other properties can be set even if the test set is not connected.

Note: The ONLY way to load a test set configuration file is by sending the
[testsets.Add](../Methods/Add_Testset_Method.md) method. There is no method
to query the test set type. See an [example
program](../../COM_Example_Programs/External_Testset_Control.htm).

#### Accessing a TestsetControl object

The [ExternalTestsets collection](ExternalTestsets_Collection.md) is a
property of the main Application Object. You can obtain a handle to a testset
object by specifying an item in the collection.

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

  * [E5091A Testset Object](E5091Testset_Object.md)

  * [About External Testset Control](../../../System/External_Testset_Control.md)

  * [External Testset Control Example](../../COM_Example_Programs/External_Testset_Control.md)

  * [ExternalTestsets Collection](ExternalTestsets_Collection.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Interface

([See history](TestsetControl_Object.md#history)) | 

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[ControlLines](../Properties/ControlLines_Property.md) |  ITestsetControl |  Sets the control lines of the specified Test set.  
[Enabled](../Properties/Enabled_Property.md) |  ITestsetControl |  Enables and disables (ON/OFF) the port mapping and control line output of the specified test set.  
[ID](../Properties/ID_Property.md) |  ITestsetControl |  Returns the test set ID number.  
[Label](../Properties/Label_Testset_Property.md) |  ITestsetControl |  Returns the label on a given channel for the specified test set.  
[NumberOfPorts](../Properties/NumberOfPorts_Testset_Property.md) |  ITestsetControl |  Reads the number of ports that are on the specified test set.  
[OutputPorts](../Properties/OutputPorts_Property.md) |  ITestsetControl |  Sets or returns the port mappings for ALL ports.  
[PortCatalog](../Properties/PortCatalog_Property.md) |  ITestsetControl |  Returns the selections available for a given logical port.  
[SelectPort](../Properties/SelectPort_Property.md) |  ITestsetControl |  Sets and returns the logical port value.  
[ShowProperties](../Properties/ShowProperties_Property.md) |  ITestsetControl |  Turns status bar display of test set properties on or off.  
[Type](../Properties/Type_ts_Property.md) |  ITestsetControl |  Returns the test set model.  
  
### ExternalTestset History

Interface |  Introduced with VNA Rev:  
---|---  
ITestsetControl |  6.0

