# Marker Object

* * *

### Description

Contains the methods and properties that control Markers.

There are two ways to control markers through COM.

  1. The [Measurement object](Measurement_Object.md) has properties that apply to ALL of the markers for that measurement.

  2. The properties on the Marker object override the Measurement object properties. For example, you can then override the format setting for an individual marker by specifying mark.Format = naLogMag on the marker object.

Marker-related commands on the Measurement Object:

  * [Activate Marker Method](../Methods/Activate_Marker_Method.md)

  * [DeleteAllMarkers Method](../Methods/DeleteAllMarkers_Method.md)

  * [DeleteMarker Method](../Methods/Delete_Marker_Method.md)

  * [GetReferenceMarker Method](../Methods/Get_Reference_Marker_Method.md)

  * [InterpolateMarkers Method](../Methods/Interpolate_Markers_Method.md)

  * [SearchFilterBandwidth Method](../Methods/Search_Filter_Bandwidth_Method.md)

  * [ActiveMarker Property](../Properties/ActiveMarker_Property.md)

  * Marker Format Property

  * [MarkerState Property](../Properties/MarkerState_Property.md)

  * [ReferenceMarkerState Property](../Properties/ReferenceMarkerState_Property.md)

Important: Learn about [programming the Reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers).

### Accessing the Marker object

To turn ON a marker, get a handle to the marker through the [measurement
object](Measurement_Object.htm). If not already activated, this command will
turn ON marker 1.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
app.ActiveMeasurement.marker(1).Format = naLinMag

You can also set the marker object to an object variable:

Dim m1 As Marker  
Set m1 = app.ActiveMeasurement.Marker(1)  
m1.Format = naMarkerFormat_LinMag

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [All about Markers](../../../S4_Collect/Markers.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[Activate](../Methods/Activate_Method.md) | IMarker | Makes an object the Active Object. Shared with the Marker Object  
[BandnoiseData](../Methods/BandnoiseData_Method.md) | IMarker6 | Returns the Y-axis data from the bandnoise marker.  
[BandpowerData](../Methods/BandpowerData_Property.md) | IMarker6 | Returns the Y-axis data from the bandpower marker.  
[SearchCompressionPoint](../Methods/SearchCompressionPoint_Method.md) | IMarker4 | Searches the marker domain for the compression level.  
[SearchMax](../Methods/Search_Max_Method.md) | IMarker | Searches the marker domain for the maximum value.  
[SearchMin](../Methods/Search_Min_Method.md) | IMarker | Searches the marker domain for the minimum value.  
[SearchNextPeak](../Methods/Search_Next_Peak_Method.md) | IMarker | Searches the marker's domain for the next largest peak value.  
[SearchPeakLeft](../Methods/Search_Peak_Left_Method.md) | IMarker | Searches the marker's domain for the next VALID peak to the left of the marker.  
[SearchPeakRight](../Methods/Search_Peak_Right_Method.md) | IMarker | Searches the marker's domain for the next VALID peak to the right of the marker.  
[SearchTarget](../Methods/Search_Target_Method.md) | IMarker | Searches the marker's domain for the target value.  
[SearchTargetLeft](../Methods/Search_Target_Left_Method.md) | IMarker | Moving to the left of the marker position, searches the marker's domain for the target value.  
[SearchTargetRight](../Methods/Search_Target_Right_Method.md) | IMarker | Moving to the right of the marker position, searches the marker's domain for the target value.  
[SetCenter](../Methods/Set_Center_Method.md) | IMarker | Changes the analyzer's center frequency to the X-axis position of the marker.  
[SetCW](../Methods/Set_CW_Method.md) | IMarker | Changes the sweep type to CW mode and makes the CW frequency the marker's frequency.  
[SetCWFreq](../Methods/SetCWFreq_Method.md) | IMarker3 | Changes the CW frequency to the frequency of the active marker.  
[SetElectricalDelay](../Methods/SetElectricalDelay_Method.md) | IMarker | Changes the measurement's electrical delay to the marker's delay value.  
[SetReferenceLevel](../Methods/SetReferenceLevel_Method.md) | IMarker | Changes the measurement's reference level to the marker's Y-axis value.  
[SetStart](../Methods/Set_Start_Method.md) | IMarker | Changes the analyzer's start frequency to the X-axis position of the marker.  
[SetStop](../Methods/Set_Stop_Method.md) | IMarker | Changes the analyzer's stop frequency to the X-axis position of the marker.  
[toSA Method](../Methods/toSA_Method.md) | IMarker6 | Creates an SA channel with a marker at the same CW frequency.  
  
### Properties

|

####

|

#### Description  
  
[BandDensityACPRState](../Properties/BandDensityACPRState_Property.md) | IMarker9 | Sets and reads the band ACPR density marker.  
[BandDensityBW](../Properties/BandDensityBW_Property.md) | IMarker8 | Sets and reads the bandwidth of the band density marker.  
[BandDensityEQSPan](../Properties/BandDensityEQSPan_Property.md) | IMarker8 | Reads the band power density equivalent span.  
[BandDensityNoiseState](../Properties/BandDensityNoiseState_Property.md) | IMarker8 | Sets and reads the band noise density state.  
[BandDensityNPRState](../Properties/BandDensityNPRState_Property.md) | IMarker9 | Sets and reads the band NPR density marker.  
[BandDensityPowerBW](../Properties/BandDensityPowerBW_Property.md) | IMarker8 | Sets and reads the band power density bandwidth.  
[BandDensityPowerState](../Properties/BandDensityPowerState_Property.md) | IMarker8 | Sets and reads the band power density state.  
[BandDensityToneBW](../Properties/BandDensityToneBW_Property.md) | IMarker8 | Sets and reads the bandwidth of the band tone density marker.  
[BandDensityToneSpacing](../Properties/BandDensityToneSpacing_Property.md) | IMarker8 | Sets and reads the tone density tone spacing.  
[BandDensityToneState](../Properties/BandDensityToneState_Property.md) | IMarker8 | Sets and reads the band tone density state.  
[BandDensityValue](../Properties/BandDensityValue_Property.md) | IMarker8 | Returns the spectral band power density.  
[BandNoisedBmpHz](../Properties/BandNoisedBmpHz_Property.md) | IMarker7 | Returns the Y-axis data from the band noise marker.  
[BandnoiseSpan](../Properties/BandnoiseSpan_Property.md) | IMarker6 | Sets and reads the frequency span of the band noise marker.  
[BandnoiseState](../Properties/BandnoiseState_Property.md) | IMarker6 | Sets and reads the state of the band noise marker.  
[BandPowerdBm](../Properties/BandPowerdBm_Property.md) | IMarker7 | Returns the Y-axis data from the band power marker.  
[BandpowerSpan](../Properties/BandpowerSpan_Property.md) | IMarker6 | Sets and reads the frequency span of the band power marker.  
[BandpowerState](../Properties/BandpowerState_Property.md) | IMarker6 | Sets and reads the state of the band power marker.  
[Bucket Number](../Properties/Bucket_Number_Property.md) | IMarker | Marker data point number.  
[CompressionLevel](../Properties/CompressionLevel_mkr_Property.md) | IMarker4 | Set and read the marker compression level.  
[CompressionPin](../Properties/CompressionPin_Property.md) | IMarker4 | Reads the input power at the marker compression level.  
[CompressionPout](../Properties/CompressionPout_Property.md) | IMarker4 | Reads the output power at the marker compression level.  
[DeltaMarker](../Properties/DeltaMarker_Property.md) | IMarker | Makes a marker relative to the reference marker  
[Distance](../Properties/Distance_Property.md) | IMarker2 | Sets or returns distance value for time domain trace.  
[Format](../Properties/Format_Marker_Property.md) | IMarker | Linear, SWR, and so forth  
[Interpolated](../Properties/Interpolated_Property.md) | IMarker | Turn marker interpolation ON and OFF  
[Number](../Properties/Number_marker_Property.md) | IMarker | Read the number of the active marker  
[OccupiedBandCenter](../Properties/OccupiedBandCenter_Property.md) | IMarker7 | Read the occupied bandwidth center frequency.  
[OccupiedBandPercent](../Properties/OccupiedBandPercent_Property.md) | IMarker7 | Sets and reads the percentage of the band span to measure.  
[OccupiedBandPowerdBm](../Properties/OccupiedBandPowerdBm_Property.md) | IMarker7 | Read the occupied bandwidth power.  
[OccupiedBandSpan](../Properties/OccupiedBandSpan_Property.md) | IMarker7 | Read the span of the occupied bandwidth.  
[OccupiedBandState](../Properties/OccupiedBandState_Property.md) | IMarker7 | Sets and reads the occupied bandwidth on/off state.  
[PeakExcursion](../Properties/Peak_Excursion_Property.md) | IMarker | Sets and reads the peak excursion value for the specified marker.  
[PeakThreshold](../Properties/Peak_Threshold_Property.md) | IMarker | Sets peak threshold for the specified marker.  
[SearchFunction](../Properties/Search_Function_Property.md) | IMarker | Emulates the Tracking function in the marker search dialog box.  
[Stimulus](../Properties/Stimulus_Property.md) | IMarker | Sets and reads the X-Axis value of the marker.  
[Target Value](../Properties/TargetValue_Property.md) | IMarker | Sets the target value for the marker when doing Target Searches.  
[Tracking](../Properties/Tracking_Property.md) | IMarker | The tracking function finds the selected search function every sweep.  
[Type](../Properties/Type_Marker_Property.md) | IMarker | Sets and reads the marker type.  
[UserRange](../Properties/User_Range_Property.md) | IMarker | Assigns the marker to the specified User Range.  
[UserRangeMax](../Properties/User_Range_Max_Property.md) | IMarker | Sets the stimulus stop value for the specified User Range.  
[UserRangeMin](../Properties/User_Range_Min_Property.md) | IMarker | Sets the stimulus start value for the specified User Range.  
[Value](../Properties/Value_Property.md) | IMarker | Reads the Y-Axis value of the marker.  
  
### Marker History

Interface | Introduced with VNA Rev:  
---|---  
IMarker | 1.0  
IMarker2 | 4.2  
IMarker3 | 8.33  
IMarker4 | 8.50  
IMarker5 |   
IMarker6 | 10.30  
IMarker7 | 12.80  
IMarker8 | 13.50  
IMarker9 | 13.60

