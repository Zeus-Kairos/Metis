# Read and Write Calibration Data using COM

* * *

Calibration data in the VNA is stored in Cal Sets. [Learn more about Cal
Sets](../../S3_Cals/Cal_Sets.htm)

You can read or write two types of Calibration data:

  * Error Terms \- calculated data using standard measurement data and the algorithms for the specified cal type.

  * Standard Measurement data -raw data resulting from the measurement of a calibration standard.

Each of these data are available in the VNA in either variant data or typed
data. [Learn more about variant and typed data](COM_Data_Types.md#var)

[Other Topics about COM Concepts](Learning_about_COM.md)

### Calibration / Cal Set Interfaces

There are several interfaces associated with Calibration.

### [ICalibrator](../COM_Reference/Objects/Calibrator_Object.md)

This interface is the original interface provided with the first version of
the VNA. It provides remote access to the "Unguided" Calibration wizard. This
interface can perform 1 and 2 port calibrations as well as response cals.

This interface can also read and write error terms from/to a Cal Set. However,
ICalibrator is NOT recommended for this purpose. The
[ICalSet2](../COM_Reference/Objects/CalSet_Object.md) Interface is better
suited for reading and writing error terms.

See a vbscript example of [how to perform a 2-port Cal and read the cal
data.](../COM_Example_Programs/Perform_an_Unguided_Cal_using_COM.htm)

###
[IGuidedCalibration](../COM_Reference/Objects/GuidedCalibration_Object.md)

This interface provides the methods and properties used by the Guided
Calibration wizard. With this interface you can perform multi-port
calibrations (1 to 4 port cals), but no response cals.

### [ICalSet2](../COM_Reference/Objects/CalSet_Object.md) and
[ICalData3](../COM_Reference/Objects/CalSet_Object.md#ICalData3)

These interfaces provide access to the Cal Set contents. You can read and
write error terms with both of these interfaces.

  * ICalSet2 uses Variant data, which means it is usable from vbscript. 

  * ICalData3 uses "typed" data, which means it can be used from any automation engine that can read the type library (VEE, VB, C++, etc.). Typed arguments (such as float or single) are more efficient than variants, so use the ICalData3 interface where better performance is needed.

[See a vbscript example of how to read Cal Set
data.](../COM_Example_Programs/COM_Reading_CalSet_Examples.htm)

### [ICalSet3](../COM_Reference/Objects/CalSet_Object.md)

This interface provides access to the stimulus attributes of the Cal data:
frequency, power, number of points. These are the stimulus conditions under
which the Cal Set was created.

* * *

