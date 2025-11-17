# ComTraceColors Object

* * *

### Description

Provides access to the methods and properties used to modify the VNA Display
and Print colors.

Both the Display and Print [ComColor objects](ComColors_Object.md) contain 8
Trace objects (1 to 8).

'1st Trace' is NOT always Trace1 (Tr1). For example, the first trace in a
window might be Tr2 which is drawn with the "1st Trace" pen.

The first 8 traces are drawn with the defined pen colors. The next eight
traces reuse the same colors, and so forth. For example, if all traces are
numbered sequentially, the 9th and 17th traces are drawn using the same color
as the 1st trace.

### Accessing the ComTraceColors object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835X.Application")  
Set displayColors = app.Preferences.DisplayColors  
'or  
'Set printColors = app.Preferences.PrintColors  
dim Trace1  
  
Set Trace1 = displayColors.Trace(1)  
Trace1.DataAndLimits = RGB(1,251,1)

### See Also:

  * [Modify Display Colors](../../COM_Example_Programs/Modify_Display_Colors.md) Example

  * [About VNA Display Colors](../../../System/Display_Colors.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](Capabilities_Object.md#Interface1) | 

###  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[DataAndLimits](../Properties/DataAndLimits_Property.md) | ITraceColors | Set and return the color of Data and Limit Lines for nth trace in a window.  
[Markers](../Properties/Markers_Property.md) | ITraceColors | Set and return the color of data trace markers for nth trace in a window.  
[Memory](../Properties/Memory_Property.md) | ITraceColors | Set and return the memory trace color for nth trace in a window.  
[MemoryMarkers](../Properties/MemoryMarkers_Property.md) | ITraceColors | Set and return the color of memory trace markers for nth trace in a window.  
  
###  ITraceColors History

I Interface | Introduced with VNA Rev:  
---|---  
ITraceColors | 9.0  
  
* * *

