# MeasurementEquation Object

* * *

### Description

Provide commands for creating an equation.

[Learn more about Equation Editor](../../../S4_Collect/Equation_Editor.md)

### Accessing the Equation object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim eq As MeasurementEquation  
Set eq = app.ActiveMeasurement.Equation

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
---|---|---  
[GetLibraryFunctions](../Methods/GetLibraryFunctions_Method.md) | IMeasurementEquation2 | Returns the functions in an imported (loaded) DLL.  
[ImportLibrary](../Methods/ImportLibrary_Method.md) | IMeasurementEquation2 | Imports an Equation Editor DLL.  
[IsLibraryImported](../Methods/IsLibraryImported_Method.md) | IMeasurementEquation2 | Returns whether a DLL has been imported into the VNA.  
[RemoveLibrary](../Methods/RemoveLibrary_Method.md) | IMeasurementEquation2 | Removes an imported an Equation Editor DLL from the VNA.  
  
### Properties

|

### Interface

[See History](Preferences_Object.md#history) | 

### Description  
  
[FastProcessing](../Properties/FastProcessing_Property.md) | IMeasurementEquation3 | Set and return equation editor trace update delay  
[Text](../Properties/Text_Property.md) | IMeasurementEquation | Sets the Equation  
[State](../Properties/State_Property.md) | IMeasurementEquation | Sets the Equation enabled state  
[Valid](../Properties/Valid_Property.md) | IMeasurementEquation | Returns whether the equation is presently valid.  
  
### Example Program using these commands:

Dim na Dim meas Set na = CreateObject("AgilentPNA835x.Application") Set meas =
na.ActiveMeasurement 'Define the measurement meas.Equation.Text =
"mysillyequ=sqrt(AR1_1)" 'Check to see if the equation is valid valid_e =
meas.Equation.Valid MsgBox valid_e 'Turn on the Equation Editor
meas.Equation.State = True  
---  
  
###  IMeasurementEquation History

Interface | Introduced with VNA Rev:  
---|---  
IMeasurementEquation | 6.03  
IMeasurementEquation2 |   
IMeasurementEquation3 | 13.20  
  
* * *

