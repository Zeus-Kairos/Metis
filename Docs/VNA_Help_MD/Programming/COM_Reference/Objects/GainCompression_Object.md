# Gain Compression Object

* * *

### Description

Controls the Gain Compression Application settings.

### Accessing the GainCompression object

Dim app as AgilentPNA835x.Application
app.[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)(1,
"Gain Compression", "CompIn21", 1) Dim GCA Set GCA =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)  
---  
  
### See Also:

  * Example Programs

  *     * [Create and Cal a Gain Compression Measurement](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md)

    * [Create and Cal a GCX Measurement](../../COM_Example_Programs/Create_and_Cal_a_GCX_Measurement.htm.md)

  * [GainCompressionCal Object](GainCompressionCal_Object.md)

  * [About Gain Compression Application](../../../Applications/Gain_Compression_Application.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

Note: Set the Start/Stop Frequency and Start/Stop Power Settings using the
[Channel Object](Channel_Object.md).

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
[GetRaw2DData](../Methods/GetRaw2DData_Method.md) | IGainCompression | Reads Gain Compression data from specified location.  
[GetDataIm](../Methods/GetDataIm_Method.md) | IGainCompression | Reads Imaginary part of specified frequency or power points.  
[GetDataRe](../Methods/GetDataRe_Method.md) | IGainCompression | Reads REAL part of specified frequency or power points.  
[SetPortMap](../Methods/SetPortMap_Method.md) | IGainCompression | Maps the VNA ports to the DUT ports  
  
### Property

|

### Interface

|

### Description  
  
[AcquisitionMode](../Properties/AcquisitionMode_Property.md) | IGainCompression | Set and read the method by which gain compression data is acquired.  
[CompressionAlgorithm](../Properties/CompressionAlgorithm_Property.md) | IGainCompression | Set and read the algorithm method used to compute gain compression.  
[CompressionBackoff](../Properties/CompressionBackoff_Property.md) | IGainCompression | Set and read value for the BackOff compression algorithm.  
[CompressionDeltaX](../Properties/CompressionDeltaX_Property.md) | IGainCompression | Set and read the 'X" value in the delta X/Y compression algorithm.  
[CompressionDeltaY](../Properties/CompressionDeltaY_Property.md) | IGainCompression | Set and read the 'Y" value in the delta X/Y compression algorithm.  
[CompressionInterpolation](../Properties/CompressionInterpolation_Property.md) | IGainCompression | Sets whether or not to interpolate the final power level when the measured compression level deviates from the specified level.  
[CompressionLevel](../Properties/CompressionLevel_Property.md) | IGainCompression | Set and read the decrease in gain which indicates that the amplifier is compressing.  
[DeviceInputPort](../Properties/DeviceInputPort_Property.md) | IGainCompression | Read the VNA port number which is connected to the DUT input.  
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) | IGainCompression | Read the VNA port number which is connected to the DUT output.  
[EndOfSweepOperation](../Properties/EndOfSweepOperation_Property.md) | IGainCompression | Set and read the action which should be taken at the end of the last frequency or power sweep in the measurement.  
[InputLinearPowerLevel](../Properties/InputLinearPowerLevel_Property.md) | IGainCompression | Set and read the input power level that should produce linear gain.  
[MaximumNumberOfPoints](../Properties/MaximumNumberOfPoints.md) | IGainCompression | Returns the maximum possible number of data points.  
[NumberOfFrequencyPoints](../Properties/NumberOfFrequencyPoints_Property.md) | IGainCompression | Set and read the number of data points in each frequency sweep.  
[NumberOfPowerPoints](../Properties/NumberOfPowerPoints_Property.md) | IGainCompression | Set and read the number of data points in each power sweep.  
[ReadDCAtCompression](../Properties/ReadDCAtCompression_Property.md) | IGainCompression5 | Set and read the DC meter at the compression point.  
[ReverseLinearPowerLevel](../Properties/ReverseLinearPowerLevel_Property.md) | IGainCompression | Set and read the reverse power level to the DUT.  
[SafeSweepCoarsePowerAdjustment](../Properties/SafeSweepCoarsePowerAdjustment_Property.md) | IGainCompression | Set and read the Safe Sweep COARSE power adjustment.  
[SafeSweepDCParameter](../Properties/SafeSweepDCParameter_Property.md) | IGainCompression6 | Set and read the name of the external DC device.  
[SafeSweepEnable](../Properties/SafeSweepEnable_Property.md) | IGainCompression | Set and read the (ON | OFF) state of Safe Sweep mode.  
[SafeSweepFinePowerAdjustment](../Properties/SafeSweepFinePowerAdjustment_Property.md) | IGainCompression | Set and read the Safe Sweep FINE power adjustment.  
[SafeSweepFineThreshold](../Properties/SafeSweepFineThreshold_Property.md) | IGainCompression | Set and read the compression level in which Safe Sweep changes from the COARSE power adjustment to the FINE power adjustment.  
[SafeSweepMaximumDCLimit](../Properties/SafeSweepMaximumDCLimit_Property.md) | IGainCompression6 | Set and read the maximum limit of the external DC device.  
[SafeSweepMaximumLimit](../Properties/SafeSweepMaximumLimit_Property.md) | IGainCompression4 | When the DUT Output reaches this value, the input power to the DUT is no longer incremented at that frequency.  
[SaturationLevel](../Properties/SaturationLevel_Property.md) | IGainCompression3 | Set and read the deviation dB from the maximum Pout.  
[SearchFailures](../Properties/SearchFailures_Property.md) | IGainCompression | Read number of points that did not achieve compression.  
[SearchSummary](../Properties/SearchSummary_Property.md) | IGainCompression | Returns if a compression search is complete, and if the search was a success or failure.  
[SmartSweepMaximumIterations](../Properties/SmartSweepMaximumIterations_Property.md) | IGainCompression | Set and read the maximum number of iterations to be used to find the compression level in a SMART sweep.  
[SmartSweepSettlingTime](../Properties/SmartSweepSettlingTime_Property.md) | IGainCompression | Set and read SMART sweep settling time.  
[SmartSweepShowIterations](../Properties/SmartSweepShowIterations_Property.md) | IGainCompression | Set and read whether to show results for each SMART sweep iteration.  
[SmartSweepTolerance](../Properties/SmartSweepTolerance_Property.md) | IGainCompression | Set and read the level of tolerance to be used to find the compression level in a SMART sweep.  
[TotalIterations](../Properties/TotalIterations_Property.md) | IGainCompression2 | Returns the total number of iteration required for the SMART Sweep.  
[TotalNumberOfPoints](../Properties/TotalNumberOfPoints_Property.md) | IGainCompression | Set and read the total number of data points.(Freq x Power)  
  
###  IGainCompression History

Interface | Introduced with VNA Rev:  
---|---  
IGainCompression | 8.0  
IGainCompression2 | 8.2  
IGainCompression3 | 9.0  
IGainCompression4 | 9.2  
IGainCompression5 | 10.49  
IGainCompression6 | 13.60  
  
* * *

