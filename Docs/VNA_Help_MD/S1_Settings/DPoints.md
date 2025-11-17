# Number of Points

* * *

A data point is a sample of data representing a measurement at a single
stimulus value. You can specify the number of data points that the analyzer
measures across a sweep. (A "sweep" is a series of consecutive data point
measurements, taken over a sequence of stimulus values.)

The analyzer sweep time changes proportionally with the number of points.
However, the overall measurement cycle time does not. See [Technical
Specifications](../Specs/ManualChoice.htm#Speed) for more information on how
the number of points, and other settings, affect the sweep time.

#### How to change the number of data points

Select a number or click Custom to invoke a [dialog
box](DPoints.htm#customDiag)  
---  
Using Hardkey/SoftTab/Softkey  
  
  1. Press Sweep > Main > Number of Points.

  
[![](../assets/images/SeeProg.gif)](../Programming/CF_Sweep_Commands_-
_Standard.htm#Main_Tab_Commands)  
  
Number of Points dialog box help  
---  
Specifies the number of data points that the analyzer gathers during a
measurement sweep. The default value is 201. Note: Some [measurement
classes](Measurement_Classes.htm) (such as
[GCA](../Applications/Gain_Compression_Application.md#Features) and [Swept
IMD](../Applications/Swept_IMD.htm#Features)) may have different maximum
points limitations. Two data points are required for [Time
Domain](../Time/TimeDomain.htm). Tips:

  * To achieve the greatest trace resolution, use the maximum number of data points.
  * For faster throughput use the smallest number of data points that will give you acceptable resolution.
  * To find an optimized number of points, look for a value where there is not a significant difference in the measurement when you increase the number of points.
  * To ensure an accurate measurement calibration, perform the calibration with the same number of points that will be used for the measurement.

The number of points is the number of data items collected in one sweep. It
can be set for each channel independently.

  * To obtain a higher trace resolution against the stimulus value, choose a larger value for number of points.
  * To obtain higher throughput, keep the number of points to a smaller value within an allowable trace resolution.
  * To obtain higher measurement accuracy after calibration, perform calibration using the same number of points as in actual measurements.

  
  
* * *

