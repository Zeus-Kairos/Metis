# E5091Testset Object

* * *

Description

There can be two test sets connected and controlled by the VNA at any time.

The item number in the testsets collection is set by the DIP switches on the
test set rear-panel. The valid item numbers are 1 and 2. If the test set DIP
switches are set to 1, then item number in the collection is 1, and so forth.
See your E5091A documentation for more information.

If the specified test set is not connected to USB or not ON, then setting
[Enabled](../Properties/Enabled_Property.md) = True will return an error. All
other properties can be set when the test set is not connected.

### Accessing the E5091Testset object

Child of the Application Object. Get a handle to a E5091Testset object by
specifying an item of the collection.

Dim pna  
Set pna = CreateObject("AgilentPNA835x.Application")  
Dim testsets As E5091Testsets  
Set testsets = pna.E5091Testsets  
Dim tset1 As E5091Testset  
Set tset1 = testsets(1)

### See Also:

  * [E5091Testset Control COM Example](../../COM_Example_Programs/E5091Testset_Control.md)

  * [E5091 TestSet Control](../../../System/E5091_TestSet_Control.md)

  * [E5091Testsets Collection](E5091Testset_Collection.md)

  * [TestsetControl Object](TestsetControl_Object.md) (for different test sets)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Description  
  
---|---  
None |   
  
### Properties

|

### Description  
  
[ControlLines](../Properties/ControlLines_Property.md) |  Sets the control lines of the specified E5091A.  
[Enabled](../Properties/Enabled_Property.md) |  Enables and disables (ON/OFF) the port mapping and control line output of the specified testset.  
[ID](../Properties/ID_Property.md) |  Returns the test set ID number.  
[NumberOfPorts](../Properties/NumberOfPorts_Testset_Property.md) |  Reads the number of ports (7 or 9) that are on the specified E5091A test set.  
[OutputPort](../Properties/OutputPort_Property.md) |  Switches an input to one of the valid outputs on the specified E5091A.  
[ShowProperties](../Properties/ShowProperties_Property.md) |  Turns ON and OFF the display of the test set control status bar.  
  
### E5091Testset History

Interface |  Introduced with VNA Rev:  
---|---  
IE5091Testset |  5.2

