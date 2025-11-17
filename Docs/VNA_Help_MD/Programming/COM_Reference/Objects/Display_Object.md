# Display Object

### Description

Controls the settings of the front panel screen.

### Accessing the Display object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim disp As IDisplay  
Set disp = app.Display  
---  
  
### See Also:

  * [PNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The PNA Object Model](The_Analyzer_Object_Model.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[PowerSpinResolution](../Properties/PowerSpinResolution_Property.md) | IDisplay | Set and read the power level knob resolution.  
  
### IDisplay History

Interface | Introduced with PNA Rev:  
---|---  
IDisplay | 13.25

