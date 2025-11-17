### Click a box or circle to view details:

See [8510 data processing mode](../S4_Collect/Math_Operations.md#8510).

See larger [Data Processing map](dataMapLarge.md).

* * *

### Measurement - Receivers gather complex trace data which is ratioed if
required by the parameter, such as S11 or A/B. Otherwise it is raw receiver
data, such as A or B. See [Measurement
Parameters](../S1_Settings/Measurement_Parameters.htm).

* * *

### Averaging - If turned ON, data is averaged with specified number of
measurement traces. See [Averaging](../S2_Opt/Trce_Noise.md#averaging).

Data Access Point 0 \- Get or Put RAW MEASUREMENT data using:

SCPI \- Write data using [Calc:Data SDATA](GP-
IB_Command_Finder/Calculate/Data.htm#data) \- Read data from Data Access Point
1

COM \- [getData](COM_Reference/Methods/Get_Data_Method.md) and
[putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md) \-
naRawData (0)

Formatting Note: COM \- [getData](COM_Reference/Methods/Get_Data_Method.md)
allows you to request data from locations 0 to 5 in a format other than the
displayed format. SMOOTHED data is only attainable from locations 2 & 4, and
only when you request data in the same format as the displayed format. SCPI -
you can only request data in the displayed format.  
---  
  
* * *

### Acquired Cal Data -  Calibration standards are measured. When the
calibration is complete, complex data is stored in a Cal Set.

Data Access Point 6 \- Get or Put RAW CAL ACQUISITION data using:

SCPI \- None

COM \-
[getStandardComplex](COM_Reference/Methods/Get_Standard_Complex_Method.md)
and
[putStandardComplex](COM_Reference/Methods/Put_Standard_Complex_Method.md)

* * *

### Calculate Error Terms - Error terms are calculated from Acquisition data
using formulas which are appropriate for the selected calibration method.
Complex error terms are stored in a Cal Set. See [Systematic
Errors](../S3_Cals/Errors.htm#errsys).

Data Access Point 5 \- Get or Put ERROR TERM data using:

SCPI \- [Calc:Data Error Terms](GP-IB_Command_Finder/Calculate/Data.md#et)

COM \- [Error Term commands](DataTopic.md#getCalData)

Note: Normalization, formerly access location 5, no longer exists and was used
ONLY by [Receiver Power Cal](../S3_Cals/PwrCalibration.md#ReceiverPowerCal).
That cal type now uses Acquire Cal Data and Calculate Error Terms like all
other Cals.

* * *

### Apply Error Terms - If error correction is ON, error terms are applied to
the raw measurement data. Otherwise, this data is identical to Raw Measurement
Data. In addition, the Fixture Simulator functions occur at the same time as
the Apply Error Terms block.

Data Access Point 1 \- Get or Put CORRECTED data using:

SCPI \- Read data using [Calc:Data SDATA](GP-
IB_Command_Finder/Calculate/Data.htm#data) \- Write data to Data Access Point
0

COM \- [getData](COM_Reference/Methods/Get_Data_Method.md) and
[putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md) \-
naCorrectedData (1)

See [Formatting Note](Accessing_Data_Descriptions.md#Formatting)

* * *

### Equation Editor - Allows custom equations to perform advanced math
operations between data traces. See [Equation
Editor](../S4_Collect/Equation_Editor.htm)

See Equation Editor Notes:

SCPI: [Calc:Data](GP-IB_Command_Finder/Calculate/Data.md)

COM: [Get Data Method](COM_Reference/Methods/Get_Data_Method.md) or [Get
DataByString Method](COM_Reference/Methods/Get_DataByString_Method.htm).

* * *

### Normalization - No longer available

Data Access Point 5 \- - No longer available

* * *

### Trace Math - When turned ON, memory data is combined with measurement data
using the selected math function. Available functions are: Data+Mem, Data-Mem,
Data*Mem, and Data/Mem. See [Math
Operations.](../S4_Collect/Math_Operations.htm)

* * *

### Memory - Data that is stored as a result of a Data-To-Memory operation.
Each measurement can have one memory trace. The memory data parallels the
measurement data through the remaining processing blocks. For example, turning
smoothing ON will smooth both the measurement and memory traces.

Data Access Point 3 \- Get or Put MEMORY data using:

SCPI \- [Calc:Data](GP-IB_Command_Finder/Calculate/Data.md) SMEM

COM \- [getData](COM_Reference/Methods/Get_Data_Method.md) and
[putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md) \-
naRawMemory (3)

See [Formatting Note](Accessing_Data_Descriptions.md#Formatting)

* * *

### Gating - When turned ON, Filter Gating is applied to the measurement data.
Gating "virtually" removes undesired responses from selected regions of the
trace. See [Gating](../Time/TimeDomain.md#Gating).

* * *

### Phase Correction - When turned ON, applies [electrical
delay](../S2_Opt/Phase_Accy.htm#ed), [phase
offset](../S2_Opt/Phase_Accy.htm#po), and [port
extensions](../S3_Cals/Port_Extensions.htm). These are all separate features
that are controlled individually.

* * *

### Magnitude Offset - When entered, offset values are applied to the
magnitude (real) portion of the data. See [Magnitude
Offset](../S1_Settings/Scale.htm#Magnitude).

* * *

### Time Domain - When turned ON, transforms the data from the frequency
domain to the time domain. See [Time Domain](../Time/TimeDomain.md)

* * *

### Formatter - Complex data is converted into scalar data formats for screen
display and remote access. For smoothed data, request the data in the same
format as the displayed data. See [Data
Format](../S1_Settings/Data_Format.htm)

* * *

### Smoother - When turned ON, removes discontinuities in the measurement and
memory trace. See [Smoothing](../S2_Opt/Trce_Noise.md#Smoothing).

* * *

### Display - Displays the processed measurement, memory data, or both, in the
format of your choice.

Data Access Point 2 \- Get or Put MEAS RESULT data using:

SCPI \- [Calc:Data](GP-IB_Command_Finder/Calculate/Data.md) FDATA

COM \- [getData](COM_Reference/Methods/Get_Data_Method.md) and
[putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md) \-
naMeasResult (2)

Data Access Point 4 \- Get or Put MEMORY RESULT data using:

SCPI \- [Calc:Data](GP-IB_Command_Finder/Calculate/Data.md) FMEM

COM \- [getData](COM_Reference/Methods/Get_Data_Method.md) and
[putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md) \-
naMemoryResult (4)

See [Formatting Note](Accessing_Data_Descriptions.md#Formatting)

* * *

