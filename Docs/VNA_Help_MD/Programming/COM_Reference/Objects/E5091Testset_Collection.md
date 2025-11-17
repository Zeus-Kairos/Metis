# E5091Testsets Collection

* * *

Description

Two testsets can be connected and controlled by the VNA at any time.

The item number in the testsets collection is set by the DIP switches on the
testset rear-panel. The valid item numbers are 1 and 2. If the testset DIP
switches are set to 1, then item number in the collection is 1, and so forth.
See your E5091A documentation for more information.

If the specified testset is not connected to USB or not ON, then setting
[Enabled](../Properties/Enabled_Property.md) = True will return an error. All
other properties can be set when the testset is not connected.

### Accessing the E5091Testsets collection

Child of the Application Object. Get a handle to one of the [E5091Testset
objects](E5091Testset_Object.htm) by specifying an item of the collection.

Dim pna  
Set pna = CreateObject("AgilentPNA835x.Application")  
Dim testsets As E5091Testsets  
Set testsets = pna.E5091Testsets  
Dim tset1 As E5091Testset  
Set tset1 = testsets(1)

### See Also:

  * [E5091Testset Control COM Example](../../COM_Example_Programs/E5091Testset_Control.md)

  * [E5091Testset Object](E5091Testset_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Description  
  
---|---  
[Item](../Methods/Item_Method.md) | Use to get a handle to a testset in the collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) | Returns the number of items in a collection of objects.  
[Parent](../Properties/Parent_Property.md) | Returns a handle to the current naNetworkAnalyzer application.  
  
### E5091Testsets History

Interface | Introduced with VNA Rev:  
---|---  
IE5091Testsets | 5.2

