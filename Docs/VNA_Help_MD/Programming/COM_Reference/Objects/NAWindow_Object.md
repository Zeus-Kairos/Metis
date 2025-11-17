# NAWindow Object

* * *

### Description

The NAWindow object controls the part of the display that contains the
graticule, or what is written on the display.

### Accessing the NaWindow object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim window As NAWindow  
Set window = app.NAWindows(1)  
window.AutoScale

or

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", "analyzerName")  
  
app.NAWindows(1).AutoScale

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[Autoscale](../Methods/Autoscale_Method.md) |  INaWindow |  Autoscales all measurements in the window. Shared with the Trace Object  
[ShowMarkerReadout](../Methods/Show_Marker_Readout_Method.md) |  INaWindow |  Shows and Hides the Marker readout for the active marker in the upper-right corner of the window object.  
[ShowTable](../Methods/Show_Table_Method.md) |  INaWindow |  Shows or Hides the specified table for the active measurement in the lower part of the window object.  
  
### Properties

|

###

|

### Description  
  
[ActiveTrace](../Properties/Active_Trace_Property.md) |  INaWindow |  Sets a trace to the Active Trace.  
[LimitTestXPosition](../Properties/LimitTestXPosition_Property.md) |  INaWindow4 |  Sets the X-axis position of the Limit Line Pass/Fail indicator.  
[LimitTestYPosition](../Properties/LimitTestYPosition_Property.md) |  INaWindow4 |  Sets the Y-axis position of the Limit Line Pass/Fail indicator.  
[MarkerReadout](../Properties/MarkerReadout_Property.md) |  INaWindow |  Sets and reads the state of the Marker readouts.  
[MarkerReadoutResponsePlaces](../Properties/MarkerReadoutResponsePlaces_Property.md) |  INAWindow3 |  For the Y-axis (response), sets the number digits to display after the decimal point in marker readouts.  
[MarkerReadoutSize](../Properties/MarkerReadoutSize_Property.md) |  INaWindow |  Specifies the size of font used when displaying Marker readout in the selected window.  
[MarkerReadoutsPerTrace](../Properties/MarkerReadoutsPerTrace_Property.md) |  INAWindow3 |  Sets the number of marker readouts to display per trace.  
[MarkerReadoutStimulusPlaces](../Properties/MarkerReadoutStimulusPlaces_Property.md) |  INAWindow3 |  For the X-axis (stimulus), sets the number digits to display after the decimal point in marker readouts.  
[MarkerReadoutXPosition](../Properties/MarkerReadoutXPosition_Property.md) |  INAWindow3 |  Sets the X-axis position of marker readouts.  
[MarkerReadoutYPosition](../Properties/MarkerReadoutYPosition_Property.md) |  INAWindow3 |  Sets the Y-axis position of marker readouts.  
[MarkerSymbol](../Properties/MarkerSymbol_Property.md) |  INAWindow3 |  Sets the symbol to display for marker position.  
[MarkerSymbolsAboveTrace](../Properties/MarkerSymbolsAboveTrace_Property.md) |  INaWindow4 |  Specifies whether or not to force marker symbols to be displayed above the trace  
[OneMarkerReadoutPerTrace](../Properties/OneReadoutPerTrace_Property.md) |  INaWindow |  Superseded with [MarkerReadoutsPerTrace Property](../Properties/MarkerReadoutsPerTrace_Property.md)  
[ScaleCouplingMethod](../Properties/ScaleCouplingMethod_Property.md) |  INaWindow2 |  Sets and returns the method of scale coupling.  
[ScaleCouplingState](../Properties/ScaleCouplingState_Property.md) |  INaWindow2 |  Enables and disables scale coupling for the specified window.  
[Title](../Properties/Title_Property.md) |  INaWindow |  Writes or reads a custom title for the window.  
[TitleState](../Properties/Title_State_Property.md) |  INaWindow |  Turns ON and OFF the window title.  
[Traces](Traces_Collection.md) |  INaWindow |  Collection for getting a handle to a trace or iterating through the traces in a window.  
[WindowNumber](../Properties/WindowNumber_Property.md) |  INaWindow |  Reads the number of the active window.  
[WindowState](../Properties/Window_State_Property.md) |  INaWindow |  Maximizes or minimizes a window. Shared with the Application Object  
  
###  INaWindow History

Interface |  Introduced with VNA Rev:  
---|---  
INaWindow |  1.0  
INaWindow2 |  9.0  
INaWindow3 |  9.30  
INaWindow4 |  10.30

