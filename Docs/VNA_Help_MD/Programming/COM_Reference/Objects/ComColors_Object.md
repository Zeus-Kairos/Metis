# ComColors Object

* * *

### Description

Provides access to the methods and properties used to modify the VNA Display
and Print colors.

### Accessing the ComColors object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835X.Application")  
Set displayColors = app.Preferences.DisplayColors  
'or  
'Set printColors = app.Preferences.PrintColors  
displayColors.ActiveLabels = 657930

### See Also:

  * [ComTraceColors Object](ComTraceColors_Object.md)

  * [Modify Display Colors](../../COM_Example_Programs/Modify_Display_Colors.md) Example

  * [About VNA Display Colors](../../../System/Display_Colors.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

[See History](Capabilities_Object.md#Interface1) | 

###  
  
---|---|---  
[LoadTheme](../Methods/LoadTheme_Method.md) | IColors | Load a color theme from a disc file.  
[ResetTheme](../Methods/ResetTheme_Method.md) | IColors | Resets the current theme to the default VNA colors.  
[StoreTheme](../Methods/StoreTheme_Method.md) | IColors | Saves the current color theme to a disc file.  
  
### Properties

|

###

|

### Description  
  
[ActiveLabels](../Properties/ActiveLabels_Property.md) | IColors | Sets labels and grid frame colors in the active window.  
[ActiveBackground](../Properties/ActiveBackground_Property.md) | IColors2 | Set and return the background color for the active window on the VNA display or hardcopy print.  
[Background](../Properties/Background_Property.md) | IColors | Set and return the background color for the inactive windows on the VNA display or hardcopy print.  
[FailedTraces](../Properties/FailedTraces_Property.md) | IColors | Set and return the limit line color of failed traces.  
[Grid](../Properties/Grid_Property.md) | IColors | Set and return the inner lines of all grid in all windows.  
[InactiveLabels](../Properties/InactiveLabels_Property.md) | IColors | Set and return the Inactive (not selected) Window Labels.  
[Trace](ComTraceColors_Object.md) | IColors | Provides access to the [ComTraceColors Object](ComTraceColors_Object.md) for setting colors for the first 8 traces  
  
###  IColors History

I Interface | Introduced with VNA Rev:  
---|---  
IColors | 9.0  
IColors2 | 9.2  
  
* * *

