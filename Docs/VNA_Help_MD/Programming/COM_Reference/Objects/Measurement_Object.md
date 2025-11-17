# Measurement Object

* * *

See [IArrayTransfer Interface](Measurement_Object.md#IArrayTransfer) for
putting and getting typed data.

See [IMixer Interface](IMixer_Interface.md) (used with [Option
S93083A/B](../../../Support/Configurations.htm#083))

### Description

The Measurement object is probably the most used object in the VNA Object
Model. A measurement object represents the chain of data processing algorithms
that take raw data from the channel and make it ready for display, which then
becomes the scope of the [Trace object](Trace_Object.md).

A Measurement object is defined by it's parameter (S11, S22, A/R1, B and so
forth). The measurement object is associated with a
[channel](Channel_Object.md) which drives the hardware that produces the data
that feeds the measurement. The root of a measurement is the raw data. This
buffer of complex paired data then flows through a number of processing
blocks: error-correction, trace math, phase correction, time domain, gating,
formatting. All of these are controlled through the measurement object.

The ACTIVE measurement is the measurement that will be acted upon if you make
a setting from the front panel. It is the measurement whose "button" is
pressed in the window with the red "active window" frame. If you create a new
measurement, that measurement becomes the active measurement.

Therefore, all automation methods with the word "Active" in them refer to the
object associated with the Active measurement, whether that object is a
Channel, Window, Trace or Limit line.

Learn about the [IMeasurement2
Interface](Measurement_Object.htm#IMeasurement2Interface) for reading stimulus
properties.

### Accessing the Measurement object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim meas As IMeasurement  
Set meas = app.ActiveMeasurement

or

Set meas = app.Measurements(n)

You can access four other objects through the Measurement object: markers,
limit test, transform, and gating. For example, because each measurement has
its own set of markers, you can set a marker by doing this:

Dim meas as measurement  
Set meas = app.ActiveMeasurement  
meas.marker(1).Stimulus = 900e6

### IMeasurement2 Interface

Some of the properties and methods for the IMeasurement2 Interface return
stimulus values that are set using the channel object. The following is the
reason these properties and methods are duplicated.

Every measurement carries with it a snapshot of the stimulus properties of the
channel that were in effect when the measurement last acquired data.
Therefore, it is the measurement that provides the most accurate stimulus
description of its data. Any change made to the channel after the measurement
was acquired renders the IChannel interface unreliable in terms of describing
the measurement.

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[Activate](../Methods/Activate_Method.md) | IMeasurement | Makes a measurement the active measurement.  
Shared with the Marker Object  
[ActivateMarker](../Methods/Activate_Marker_Method.md) | IMeasurement | Makes a marker the Active Marker.  
[ChangeParameter](../Methods/Change_Parameter_Method.md) | IMeasurement | Changes the parameter of the measurement.  
[DataToDivisor](../Methods/DataToDivisor_Method.md) | IMeasurement | Superseded with [DoReceiverPowerCal Method](../Methods/DoReceiverPowerCal_Method.md)  
[DataToMemory](../Methods/DataToMemory_Method.md) | IMeasurement | Stores the active measurement into memory.  
[Delete](../Methods/Delete_Method.md) | IMeasurement | Deletes the measurement object.  
[DeleteAllMarkers](../Methods/DeleteAllMarkers_Method.md) | IMeasurement | Deletes all of the markers from the measurement.  
[DeleteMarker](../Methods/Delete_Marker_Method.md) | IMeasurement | Deletes a marker from the active measurement.  
[getData](../Methods/Get_Data_Method.md) | IMeasurement | Retrieves Complex data from analyzer memory  
[GetDataBuffer](../Methods/GetDataBuffer_Method.md) | IMeasurement19 | Retrieves trace data (Y data) from the modulation distortion measurement.  
[GetDataBufferCompact](../Methods/GetDataBufferCompact_Method.md) | IMeasurement19 | Retrieves compact signal trace data (Y data) from the modulation distortion measurement.  
[getDataByString](../Methods/Get_DataByString_Method.md) | IMeasurement | Retrieves variant data from the specified location in your choice of formats.  
[GetFilterStatistics](../Methods/Get_Filter_Statistics_Method.md) | IMeasurement | Returns all four Filter Statistics  
[GetReferenceMarker](../Methods/Get_Reference_Marker_Method.md) | IMeasurement | Returns a handle to the reference marker.  
[Get SnPData](../Methods/Get_SnPData_Method.md) | IMeasurement3 | Returns SnP data.  
[GetSnpDataWithSpecifiedPorts](../Methods/Get_SnpDataWithSpecifiedPorts_Method.md) | IMeasurement7 | Returns sNp data for the specified ports.  
[GetTraceStatistics](../Methods/Get_Trace_Statistics_Method.md) | IMeasurement | Returns the Trace Statistics.  
[GetXAxisValues](../Methods/Get_XAxisValues_Method.md) | IMeasurement2 | Returns the stimulus values for the measurement.  
[GetXDataBuffer](../Methods/GetXDataBuffer_Method.md) | IMeasurement19 | Retrieves frequency tone data from the modulation distortion measurement.  
[GetXDataBufferCompact](../Methods/GetXDataBufferCompact_Method.md) | IMeasurement19 | Retrieves compact signal frequency tone data from the modulation distortion measurement.  
[InterpolateMarkers](../Methods/Interpolate_Markers_Method.md) | IMeasurement | Turns All Marker Interpolation ON and OFF for the measurement.  
[putDataComplex](../Methods/Put_Data_Complex_Method.md) | IMeasurement | Puts complex data into one of five data buffers.  
[putDataScalar](../Methods/Put_Data_Scalar_Method.md) | IMeasurement | Puts formatted variant data into the measurement results buffer.  
[SearchFilterBandwidth](../Methods/Search_Filter_Bandwidth_Method.md) | IMeasurement | Searches the domain with the current BW target.  
[TraceHoldClear](../Methods/TraceHoldClear_Method.md) | IMeasurement16 | Resets the currently-stored data points to the live data trace and restarts the currently-selected Trace Hold type.  
[WriteSnpFileWithSpecifiedPorts](../Methods/WriteSnpFileWithSpecifiedPorts_Method.md) | IMeasurement7 | Write sNp data for specified ports to a file.  
  
### Properties

|

### Interface

|

### Description  
  
[ActiveMarker](../Properties/ActiveMarker_Property.md) | IMeasurement | Returns a handle to the Active Marker object.  
[ActiveXAxisRange](../Properties/ActiveXAxisRange_Conv_Property.md) | IMeasurement14 | Sets the X-axis range to display for GCX, SMC, and VMC measurements.  
[BalancedMeasurement](BalancedMeasurement_Object.md) | IMeasurement5 | Sets the measurement type that is used with balanced topologies.  
[BandwidthTarget](../Properties/Bandwidth_Target_Property.md) | IMeasurement | The insertion loss value at which the bandwidth of a filter is measured.  
[BandwidthTracking](../Properties/Bandwidth_Tracking_Property.md) | IMeasurement | Turns Bandwidth Tracking function ON and OFF.  
[CalibrationName](../Properties/CalibrationName_Property.md) | IMeasurement2 | Returns the name of the cal type.  
[CalibrationType](../Properties/Calibration_Type_Property.md) | IMeasurement | Superseded with [CalibrationTypeID_property](../Properties/CalibrationTypeID_property.md)  
[CalibrationTypeID](../Properties/CalibrationTypeID_property.md) | IMeasurement2 | Sets or returns the cal type for the current measurement.  
[Center](../Properties/Center_Meas_Property.md) | IMeasurement2 | Returns the stimulus value of the center point for the measurement.  
[channelNumber](../Properties/Channel_Number_Property.md) | IIMeasurement | Returns the channel number.  
Shared with the Channel Object  
[CustomMeasurementConfiguration](../Properties/CustomMeasurementConfiguration_Property.md) | IIMeasurement12 | Provides access to custom measurement properties and methods.  
[Domain](../Properties/Domain_Property.md) | IMeasurement2 | Returns the domain (frequency, time, power) for the measurement.  
[ElectricalDelay](../Properties/Electrical_Delay_Property.md) | IMeasurement | Sets electrical delay.  
[ElecDelayMedium](../Properties/ElecDelayMedium_Property.md) | IMeasurement2 | Sets or returns the characteristic of the electrical delay medium.  
[ElecDistanceDelay](../Properties/ElecDistanceDelay_Property.md) | IMeasurement11 | Sets delay in distance  
[ElecDistanceDelayUnit](../Properties/ElecDistanceDelayUnit_Property.md) | IMeasurement11 | Sets distance units  
[ErrorCorrection](../Properties/Error_Correction_Property.md) | IMeasurement | Set or get the state of error correction for the measurement.  
[ErrorCorrectionIndicator](../Properties/ErrorCorrectionIndicator_Property.md) | IMeasurement14 | Returns the error correction status of the measurement.  
[FilterBW](../Properties/Filter_BW_Property.md) | IMeasurement | Returns the results of the SearchBandwidth method.  
[FilterCF](../Properties/Filter_CF_Property.md) | IMeasurement | Returns the Center Frequency result of the SearchBandwidth method.  
[FilterLoss](../Properties/Filter_Loss_Property.md) | IMeasurement | Returns the Loss value of the SearchBandwidth method.  
[FilterQ](../Properties/Filter_Q_Property.md) | IMeasurement | Returns the Q (quality factor) result of the SearchBandwidth method.  
[Format](../Properties/Format_Property.md) | IMeasurement | Sets display format.  
[FormatUnit](../Properties/FormatUnit_Property.md) | IMeasurement9 | Sets units for unratioed measurements.  
[Gating](Gating_Object.md) | IMeasurement | Controls Time Domain Gating.  
[GroupDelayAperture](GroupDelayAperture_Object.md) | IMeasurement13 | Provides access to the Group Delay Aperture settings.  
[InterpolateCorrection](../Properties/Interpolate_Correction_Property.md) | IMeasurement | Turns ON and OFF the calculation of new error terms when stimulus values change.  
[InterpolateMemory](../Properties/InterpolateMemory_Property.md) | IMeasurement18 | Sets or returns the state of the memory data interpolation.   
[InterpolateNormalization](../Properties/InterpolateNormalization_Property.md) | IMeasurement | Superseded with [DoReceiverPowerCal Method](../Methods/DoReceiverPowerCal_Method.md)  
[IsSparameter](../Properties/IsSParameter_Property.md) | IMeasurement2 | Returns true if measurement represents an S-Parameter.  
[LimitTest](Limit_Test_Collection.md) | IMeasurement | Collection for iterating through the Limit Segment objects (Limit Lines).  
[LimitTestFailed](../Properties/LimitTestFailed_Property.md) | IMeasurement | Returns the results of limit testing  
[LoadPort](../Properties/LoadPort_Property.md) | IMeasurement | Returns the load port number associated with an S-parameter reflection measurement.  
[LogMagnitudeOffset](../Properties/LogMagnitudeOffset_Property.md) | IMeasurement | Superseded with [DoReceiverPowerCal Method](../Methods/DoReceiverPowerCal_Method.md)  
[MagnitudeOffset](../Properties/MagnitudeOffset_Property.md) | IMeasurment4 | Offsets the magnitude of the entire data trace to a specified value.  
[MagnitudeSlopeOffset](../Properties/MagnitudeSlopeOffset_Property.md) | IMeasurment4 | Offsets the magnitude of the data trace to a value that changes linearly with frequency.  
[Marker](Marker_Object.md) | IMeasurement | Provides access to Marker settings.  
[Marker State](../Properties/MarkerState_Property.md) | IMeasurement3 | Sets or returns the ON / OFF state of a marker.  
[Mean](../Properties/Mean_Property.md) | IMeasurement | Returns the mean value of the measurement.  
[MeasurementEquation](MeasurementEquation_Object.md) | IMeasurement6 | Access Equation Editor  
[Name](../Properties/Name_Meas_Property.md) | IMeasurement | Sets or returns the name of the measurement.  
[NAWindow](NAWindow_Object.md) | IMeasurement | Controls the part of the display that contains the graticule, or what is written on the display.  
[Normalization](../Properties/Normalization_Property.md) | IMeasurement | Superseded with [DoReceiverPowerCal Method](../Methods/DoReceiverPowerCal_Method.md)  
[Number](../Properties/Number_meas_Property.md) | IMeasurement | Returns the number of the measurement.  
[NumberOfPoints](../Properties/NumberofPoints_meas_Property.md) | IMeasurement2 | Returns the Number of Points of the measurement.  
[Parameter](../Properties/Parameter_Property.md) | IMeasurement | Returns the measurement Parameter.  
[PeakToPeak](../Properties/PeakToPeak_Property.md) | IMeasurement | Returns the Peak to Peak value of the measurement.  
[PhaseOffset](../Properties/Phase_Offset_Property.md) | IMeasurement | Sets the Phase Offset for the active channel.  
[PNOP](PNOP_Object.md) | IMeasurement13 | Provides access to the Power Normal Operating Point marker search object.  
[PSaturation](PSaturation_Object.md) | IMeasurement13 | Provides access to the Power Saturation marker search object.  
[ReceivePort](../Properties/ReceivePort_Property.md) | IMeasurement2 | Returns the receiver port of the measurement.  
[ReferenceMarkerState](../Properties/ReferenceMarkerState_Property.md) | IMeasurement | Turns the reference marker ON or OFF  
[ShowStatistics](../Properties/Show_Statistics_Property.md) | IMeasurement | Displays and hides the measurement statistics (peak-to-peak, mean, standard deviation) on the screen.  
[Smoothing](../Properties/Smoothing_Property.md) | IMeasurement | Turns ON and OFF data smoothing.  
[SmoothingAperture](../Properties/Smoothing_Aperture_Property.md) | IMeasurement | Specifies or returns the amount of smoothing as a ratio of the number of data points in the measurement trace.  
[SourcePort](../Properties/SourcePort_Property.md) | IMeasurement2 | Returns the source port of the measurement.  
[Span](../Properties/Span_Meas_Property.md) | IMeasurement2 | Returns the stimulus span (stop \- start) for the measurement.  
[StandardDeviation](../Properties/Standard_Deviation_Property.md) | IMeasurement | Returns the standard deviation of the measurement.  
[Start](../Properties/Start_Meas_Property.md) | IMeasurement2 | Returns the stimulus value of the first point for the measurement.  
[StatisticsRange](../Properties/Statistics_Range_Property.md) | IMeasurement | Sets the User Range number for calculating measurement statistics.  
[Stop](../Properties/Stop_Meas_Property.md) | IMeasurement2 | Returns the stimulus value of the last point for the measurement.  
[Trace](Trace_Object.md) | IMeasurement | Controls scale, reference position, and reference line.  
[TraceDeviationType](../Properties/TraceDeviationType_Property.md) | IMeasurement20 | Calculates deviation from a least-squares fit line.  
[TraceHoldType](../Properties/TraceHoldType_Property.md) | IMeasurement16 | Sets the type of trace hold to perform.  
[TraceMath](../Properties/Trace_Math_Property.md) | IMeasurement | Performs math operations on the measurement object and the trace stored in memory.  
[TraceMax](../Properties/TraceMax_Property.md) | IMeasurement10 | Maximizes the active trace.  
[TraceTitle](../Properties/TraceTitle_Property.md) | IMeasurement8 | Writes and reads a trace title.  
[TraceTitleState](../Properties/TraceTitleState_Property.md) | IMeasurement8 | Turns trace title ON and OFF  
[Transform](Transform_Object.md) | IMeasurement | Controls Time Domain transforms.  
[Uncertainty](Uncertainty_Object.md) | IMeasurement17 | Returns a handle to the (Dynamic) Uncertainty Object.  
[UserRangeMax](../Properties/User_Range_Max_Property.md) | IMeasurement15 | Sets the stimulus stop value for the specified User Range.  
[UserRangeMin](../Properties/User_Range_Min_Property.md) | IMeasurement15 | Sets the stimulus start value for the specified User Range.  
[View](../Properties/View_Property.md) | IMeasurement | Sets (or returns) the type of trace displayed on the screen.  
[WGCutoffFreq](../Properties/WGCutoffFreq_Property.md) | IMeasurement2 | Sets or returns the value of the waveguide cut off frequency.  
[XAxis](../Properties/XAxis_Property.md) | IMeasurement17 | Sets the X-axis of the selected measurement to a DC Source.  
[XAxisDomain](../Properties/XAxisDomain_Property.md) | IMeasurement17 | Sets and returns the X-Axis domain of the selected DIQ measurement.  
  
### IMeasurement History

Interface | Introduced with VNA Rev:  
---|---  
IMeasurement | 1.0  
IMeasurement2 | 3.0  
IMeasurement3 | 4.0  
IMeasurement4 | 4.2  
IMeasurement5 | 5.0  
IMeasurement7 | 6.2  
IMeasurement8 | 7.2  
IMeasurement9 | 8.35  
IMeasurement10 | 8.35  
IMeasurement11 | 8.50  
IMeasurement12 | 9.00  
IMeasurement13 | 9.20  
IMeasurement14 | 9.22  
IMeasurement15 | 9.40  
IMeasurement16 | 10.25  
IMeasurement17 | 10.30  
IMeasurement18 | 10.49  
IMeasurement19 | 13.60  
IMeasurement20 | 13.80  
  
IArrayTransfer Interface

### Description

Contains methods for putting data in and getting data out of the analyzer
using typed data. This interface transfers data more efficiently than the
IMeasurement Interface. However, this interface is only usable from VB6, C,
and C++.

[See a VB.net example using this
interface](../../COM_Example_Programs/Get_Data_using_VB.NET.htm).

### Methods

|

### Description  
  
---|---  
[getComplex](../Methods/Get_Complex_Method.md) | Retrieves real and imaginary data from the specified buffer.  
[getNAComplex](../Methods/Get_NAComplex_Method.HTM) | Retrieves typed NAComplex data from the specified buffer.  
[getPairedData](../Methods/Get_Paired_Data_Method.md) | Retrieves magnitude and phase data pairs from the specified buffer.  
[getScalar](../Methods/Get_Scalar_Method.md) | Retrieves scalar data from the specified buffer.  
[putComplex](../Methods/Put_Complex_Method.md) | Puts real and imaginary data into the specified buffer.  
[putNAComplex](../Methods/Put_NAComplex_Method.md) | Puts typed NAComplex data into the specified buffer.  
[putScalar](../Methods/Put_Scalar_Method.md) | Puts scalar data into the measurement result buffer.  
  
### Properties

|

### Description  
  
None |   
  
### IArrayTransfer History

Interface | Introduced with VNA Rev:  
---|---  
IArrayTransfer | 1.0

