# IMixer Interface ([Option
S93083A/B](../../../Support/Configurations.htm#083)) - Superseded

* * *

Note: This object and all properties and methods are replaced with [Converter
Object](Converter_Object.htm) which can be used for all converter application.

### Description

Contains the methods and properties to setup FCA Mixer measurements.

For performing calibrations, use either the [SMC Type
Object](SMC_Type_Object.htm) or the [VMC Type Object](VMC_Type_Object.md).

### Accessing the IMixer Interface

Access the IMixer Interface through the Measurement Object. If the particular
type of Measurement that was created supports IMixer, then the program
determines this at run time and can access the functionality exposed by
IMixer. Because the determination of IMixer support is not made until runtime,
the program should handle the case where IMixer is not supported on the
object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", "analyzerName")  
app.Preset  
  
' FCA Measurements can't share the channel with standard measurements  
' Because preset creates a single measurement in channel 1, we first delete
the standard measurement  
Dim standardMeas As IMeasurement  
Set standardMeas = app.ActiveMeasurement  
standardMeas.Delete  
  
' Create a Measurement object, in this case using the IMeasurement interface  
Dim meas As IMeasurement  
Set meas = app.CreateCustomMeasurementEx(1, "SMC_Forward.SMC_ForwardMeas",
"SC21")  
  
' See if this measurement object supports IMixer  
Dim mixer As IMixer  
Set mixer = meas

### See Also:

[VNA Automation
Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

Example: How to create and calibrate a standard
[SMC](../../COM_Example_Programs/Create_and_Cal_an_SMC_Measurement.md) or
[VMC](../../COM_Example_Programs/Create_and_Cal_a_VMC_Measurement.md)
measurement or a [fixed output
SMC](../../COM_Example_Programs/Create_an_SMC_Fixed_Output_Meas.htm)
measurement.

### Methods

|

### Interface

[See History](IMixer_Interface.md#History) | 

### Description  
  
---|---|---  
[Apply](../Methods/Apply_Method.md) | IMixer3 | Applies mixer settings.  
[Calculate](../Methods/Calculate_Method.md) | IMixer | Automatically calculate Input and Output frequencies for mixer setup.  
[LoadFile](../Methods/LoadFile_Method.md) | IMixer | Loads a previously-configured mixer attributes file (.mxr)  
[SaveFile](../Methods/SaveFile_Method.md) | IMixer | Saves the settings for the mixer/converter test setup to a mixer attributes file.  
[SetDutPorts](../Methods/SetDutPorts_Method.md) | IMixer8 | Sets the VNA to DUT port mapping.  
  
### Properties

|

###

|

### Description  
  
[ActiveXAxisRange](../Properties/ActiveXAxisRange_Property.md) | IMixer3 | Sets or returns the swept parameter to display on the X-axis.  
[AvoidSpurs](../Properties/AvoidSpurs_Property.md) | IMixer | Sets and returns the state of the avoid spurs feature.  
[EmbeddedLO](EmbeddedLO_Object.md) | IMixer7 | Provides measurements of mixers with an embedded LO.  
[DeviceInputPort](../Properties/DeviceInputPort_FCA_Property.md) | IMixer8 | Reads the VNA port that is mapped to the DUT Input port  
[DeviceOutputPort](../Properties/DeviceOutputPort_FCA_Property.md) | IMixer8 | Reads the VNA port that is mapped to the DUT Output port  
[EnablePhase](../Properties/EnablePhase_Property.md) | IMixer12 | Include phase in SMC measurements and calibrations.  
[IFSideband](../Properties/IFSideband_Property.md) | IMixer | Sets or returns the value of the IF sideband.  
[IFStartFrequency](../Properties/IFStartFrequency_Property.md) | IMixer | Returns the start frequency of the mixer IF.  
[IFStopFrequency](../Properties/IFStopFrequency_Property.md) | IMixer | Returns the stop frequency of the mixer IF.  
[IncludeReverseSweep](../Properties/IncludeReverseSweep_Property.md) | IMixer12 | Sets or returns whether to include SC12 sweep.  
[InputDenominator](../Properties/InputDenominator_Property.md) | IMixer | Sets or returns the denominator value of the Input Fractional Multiplier.  
[InputFixedFrequency](../Properties/InputFixedFrequency_Property.md) | IMixer6 | Sets or returns the mixer fixed Input frequency value.  
[InputNumerator](../Properties/InputNumerator_Property.md) | IMixer | Sets or returns the numerator value of the Input Fractional Multiplier.  
[InputPower](../Properties/InputPower_Property.md) | IMixer | Sets or returns the value of the Input Power.  
[InputRangeMode](../Properties/InputRangeMode_Property.md) | IMixer6 | Sets or returns the Input sweep mode.  
[InputStartFrequency](../Properties/InputStartFrequency_Property.md) | IMixer | Sets or returns the start frequency of the mixer input.  
[InputStopFrequency](../Properties/InputStopFrequency_Property.md) | IMixer | Sets or returns the stop frequency of the mixer input.  
[IsInputGreaterThanLO](../Properties/InputIsGreaterThanLO_Property.md) | IMixer2 | Specifies whether to use the Input frequency that is greater than the LO or less than the LO.  
[LODenominator](../Properties/LODenominator_Property.md) | IMixer | Sets or returns the denominator value of the LO Fractional Multiplier.  
[LOFixedFrequency](../Properties/LOFixedFrequency_Property.md) | IMixer | Sets or returns the fixed frequency of the specified LO.  
[LOName](../Properties/LOName_Property.md) | IMixer | Sets or returns the LO name.  
[LONumerator](../Properties/LONumerator_Property.md) | IMixer | Sets or returns the numerator value of the LO Fractional Multiplier.  
[LOPower](../Properties/LOPower_Property.md) | IMixer | Sets or returns the value of the LO Power.  
[LORangeMode](../Properties/LORangeMode_Property.md) | IMixer3 | Sets or returns the LO sweep mode to fixed or swept.  
[LOStage](../Properties/LOStage_Property.md) | IMixer | Returns the number of LOs (1 or 2).  
[LOStartFrequency](../Properties/LOStartFrequency_Property.md) | IMixer3 | Sets or returns the start frequency of the specified LO.  
[LOStopFrequency](../Properties/LOStopFrequency_Property.md) | IMixer3 | Sets or returns the start frequency of the specified LO.  
[NominalIncidentPowerState](../Properties/NominalIncidentPowerState_Property.md) | IMixer4 | Toggles Nominal Incident Power ON and OFF.  
[NormalizePoint](../Properties/NormalizePoint_SMC_Property.md) | IMixer12 | Set or return the data point used to normalize SMC phase measurements.  
[OutputFixedFrequency](../Properties/OutputFixedFrequency_Property.md) | IMixer3 | Sets or returns the fixed frequency of the mixer output.  
[OutputRangeMode](../Properties/OutputRangeMode_Property.md) | IMixer6 | Sets or returns the Output sweep mode.  
[OutputSideband](../Properties/OutputSideband_Property.md) | IMixer | Sets or returns the value of the output sideband.  
[OutputStartFrequency](../Properties/OutputStartFrequency_Property.md) | IMixer | Sets or returns the start frequency of the mixer output.  
[OutputStopFrequency](../Properties/OutputStopFrequency_Property.md) | IMixer | Sets or returns the stop frequency of the mixer output.  
  
### IMixer History

Interface | Introduced with VNA Rev:  
---|---  
IMixer | 1.0  
IMixer2 | 3.5  
IMixer3 | 4.0  
IMixer4 | 4.8  
IMixer5 | 6.04  
IMixer6 | 6.20  
IMixer7 | 7.21  
IMixer8 | 7.5/8.2  
IMixer12 | 7.5/9.2

