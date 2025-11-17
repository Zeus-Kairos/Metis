# Trace Object

* * *

### Description

The Trace object controls how the measurement data is displayed. You can
control scale, reference position, and value from the Trace Object.

### Accessing a Trace object

There are several ways to get a handle to a trace.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim trace As Trace

Then you can do any of the following:

Set trace = app.NAWindows(1).traces(1)

set trace = app.NAWindows.item(1).ActiveTrace

set trace = app.ActiveNAWindow.traces.item(1)

set trace = app.ActiveNAWindow.ActiveTrace

Set trace = app.Measurements(1).trace

Set trace = app.ActiveMeasurement.trace

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Traces, Channels, and Windows on the VNA](../../../S0_Start/Traces_Channels_and_Windows.md)
  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](Trace_Object.md#history) | 

### Description  
  
---|---|---  
[Autoscale](../Methods/Autoscale_Method.md) |  ITrace |  Autoscales the trace or all of the traces in the selected window. Shared with the NAWindow Object  
[Move](../Methods/Move_Method.md) |  ITrace3 |  Moves a trace from one window to another.  
  
### Property

|

###

|

### Description  
  
[Measurement](../Properties/Measurement_Property.md) |  ITrace2 |  Returns a measurement handle from trace object.  
[Name](../Properties/Name_trace_Property.md) |  ITrace |  Sets or returns the trace name  
[ReferencePosition](../Properties/Reference_Position_Property.md) |  ITrace |  Sets or returns the Reference Position of the active trace.  
[ReferenceValue](../Properties/Reference_Value_Property.md) |  ITrace |  Sets or returns the value of the Y-axis Reference Level of the active trace.  
[YScale](../Properties/YScale_Property.md) |  ITrace |  Sets or returns the Y-axis Per-Division value of the active trace.  
  
###  ITrace History

Interface |  Introduced with VNA Rev:  
---|---  
ITrace |  1.0  
ITrace2 |  9.40  
ITrace3 |  9.50

