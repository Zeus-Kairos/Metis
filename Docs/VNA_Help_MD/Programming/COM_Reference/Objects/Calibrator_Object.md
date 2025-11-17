# Calibrator Object

* * *

### See Also

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Calibrator Methods and Properties](Calibrator_Object.md#ICalibrator)

  * ICalData Interface for putting and getting typed Calibration data.

  * [Superseded commands](../../Replacement_Commands.md)

### Description

The Calibrator object, a child of the channel, is used to perform an Unguided
calibration.

Important! Do NOT use commands from the
[GuidedCalibration](GuidedCalibration_Object.md) object when performing an
Unguided calibration. Use ONLY the Calibrator object. You can NOT perform a
full 3 or 4-port using the Calibrator object. You must use the
[GuidedCalibration object](GuidedCalibration_Object.md).  
---  
  
There must be a measurement present for the calibrator to use or you will
receive a "no measurement found" error. Therefore, to perform a 2-port cal,
you must have any S-parameter measurement on the channel. For a 1-port
measurement, you must have the measurement (S11 or S22) on the channel. The
same is true for a response measurement.

There are a number of approaches to calibration with the calibrator object:

  * You can collect data yourself and download it to the ACQUISITION buffer. The acquisition buffer holds the actual measured data for each standard. See the VNA [data map](../../DataMapSet.md).

  1. Calibrator.[SetCalInfo](../Methods/SetCalInfo_Method.md)

  2. Connect a standard

  3. Trigger a sweep

  4. Retrieve the data for the standard

  5. Download the data - calibrator.[putStandard](../Methods/Put_Standard_Method.md)

  6. Repeat for each standard

  7. Calibrator.[CalculateErrorCoefficients](../Methods/Calculate_Error_Coefficients_Method.md)

  * You can tell the calibrator to acquire a standard. In this case, the calibrator collects the data and places it in the ACQUISITION buffer.

  1. Calibrator.[SetCalInfo](../Methods/SetCalInfo_Method.md)

  2. Connect a standard

  3. Calibrator.[AcquireCalStandard2](../Methods/AcquireCalStandard2_Method.md)

  4. Repeat for each standard

  5. Calibrator.[CalcuateErrorCoefficients](../Methods/Calculate_Error_Coefficients_Method.md)

  * You can put previously-retrieved error terms in the error correction buffer.

  1. [PutErrorTerm](../Methods/Put_Error_Term_Method.md)

  2. Repeat for each term

  3. Measurement.[Caltype](../Properties/CalKitType_Property.md) = pick one

  * You can also "piece together" a 2-port cal from two 1-port cals (S11 and S22) and four response (thru) cals. The system will detect that all the standards needed for a 2-port cal have been acquired even though they may not have gathered at the same time.

### Accessing the Calibrator object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim cal As ICalibrator  
Set cal = app.ActiveChannel.Calibrator

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Learn about reading and writing Calibration data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.md)

### Methods

|

### Interface

[See History](Calibrator_Object.md#Interface1) | 

### Description  
  
---|---|---  
[AcquireCalConfidenceCheckECAL](../Methods/AcquireCalConfidenceCheckECAL.md) |  ICalibrator |  Superseded with AcquireCalConfidenceCheckECALEx  
[AcquireCalConfidenceCheckECALEx](../Methods/AcquireCalConfidenceCheckECALex_Method.md) |  ICalibrator4 |  Transfers ECAL confidence data into analyzer memory  
[AcquireCalStandard](../Methods/Acquire_Cal_Standard_Method.md) |  ICalibrator |  Superseded with AcquireCalStandard2  
[AcquireCalStandard2](../Methods/AcquireCalStandard2_Method.md) |  ICalibrator |  Causes the analyzer to measure a calibration standard. Also provides for sliding load.  
[CalculateErrorCoeffecients](../Methods/Calculate_Error_Coefficients_Method.md) |  ICalibrator |  Generates Error Terms from standard and actual data in the error correction buffer.  
[DoECAL1Port](../Methods/DoECAL1Port_Method.md) |  ICalibrator |  Superseded with DoECAL1PortEx  
[DoECAL1PortEx](../Methods/DoECAL1PortEx_Method.md) |  ICalibrator4 |  Completes a 1 port ECAL  
[DoECAL2Port](../Methods/DoECAL2Port_Method.md) |  ICalibrator |  Superseded with DoECAL2PortEx  
[DoECAL2PortEx](../Methods/DoECAL2PortEx_Method.md) |  ICalibrator4 |  Completes a 2 port ECAL  
[DoneCalConfidenceCheckECAL](../Methods/DoneCalConfidenceCheckECAL.md) |  ICalibrator |  Concludes an ECAL confidence check  
[DoReceiverPowerCal](../Methods/DoReceiverPowerCal_Method.md) |  ICalibrator5 |  Perform a receiver power cal.  
[DoResponseCal](../Methods/DoResponseCal_Method.md) |  ICalibrator9 |  Perform a response (normalization) cal.  
[GetCalKitTypeString](../Methods/GetCalKitTypeString_Method.md) |  ICalibrator8 |  Returns information about the attached modules  
[GetECALModuleInfo](../Methods/Get_ECAL_Module_Info_Method.md) |  ICalibrator |  Superseded with Get ECALModuleInfoEx  
[Get ECALModuleInfoEx](../Methods/Get_ECALModuleInfoEx_Method.md) |  ICalibrator4 |  Returns information about the attached module  
[getErrorTerm](../Methods/Get_Error_Term_Method.md) |  ICalibrator |  Superseded with [GetErrorTermByString](../Methods/Get_ErrorTermByString_Method.md)  
[getStandard](../Methods/Get_Standard_Method.md) |  ICalibrator |  Superseded with [GetStandardByString](../Methods/Get_StandardByString_Method.md)  
[putErrorTerm](../Methods/Put_Error_Term_Method.md) |  ICalibrator |  Superseded with [PutErrorTermByString](../Methods/Put_ErrorTermByString_Method.md)  
[putStandard](../Methods/Put_Standard_Method.md) |  ICalibrator |  Superseded with [PutStandardByString](../Methods/Put_StandardByString_Method.md)  
[SaveCalSets](../Methods/Save_CalSets_Method.md) |  ICalibrator |  Superseded with [CalSet.Save](../Methods/Save_CalSet_Method.md)  
[setCalInfo](../Methods/SetCalInfo_Method.md) |  ICalibrator |  Specifies the type of calibration and prepares the internal state for the rest of the calibration.  
  
### Properties

|

### Interface

|

### Description  
  
[AcquisitionDirection](../Properties/AcquisitionDirection_Property.md) |  ICalibrator |  Specifies the direction in a 2-Port cal using one set of standards.  
[CalKitType](../Properties/CalKitTypeCalibrator_Property.md) |  ICalibrator10 |  Sets and returns the name of the Cal Kit to use for unguided cal.  
[CalKitTypes](../Properties/CalKitTypes_Property.md) |  ICalibrator10 |  Returns the names of the first 50 mechanical cal kits in your VNA that can be used for unguided calibrations.  
[ECALCharacterization](../Properties/ECALCharacterization_Property.md) |  ICalibrator2 |  Superseded with ECALCharacterizationEx  
[ECALCharacterizationEx](../Properties/ECALCharacterizationEx_Property.md) |  ICalibrator4 |  Specifies which set of characterization data within an ECal module will be used for ECal operations with that module.  
[ECALCharacterizationIndexList](../Properties/ECALCharacterizationIndexList_Property.md) |  ICalibrator6 |  Returns a list of characterizations stored in the specified ECal module.  
[ECAL Isolation](../Properties/ECALIsolation_Property.md) |  ICalibrator |  Specifies whether the acquisition of the ECal calibration should include isolation or not.  
[ECALModuleNumberList](../Properties/ECALModuleNumberList_Property.md) |  ICalibrator6 |  Returns a list of index numbers to be used for referring to the ECal modules that are currently attached to the VNA.  
[ECALPortMap](../Properties/ECALPortMap_Property.md) |  ICalibrator3 |  Superseded with ECALPortMapEx  
[ECALPortMapEx](../Properties/ECALPortMapEx_Property.md) |  ICalibrator4 |  Specifies which ports of the ECal module are connected to which ports of the VNA.  
[IsECALModuleFound](../Properties/IsECALModuleFound_Property.md) |  ICalibrator |  Superseded with IsECALModuleFoundEx  
[IsECALModuleFoundEx](../Properties/IsECALModuleFoundEx_Property.md) |  ICalibrator4 |  Superseded with [ECALCharacterizationIndexList](../Properties/ECALCharacterizationIndexList_Property.md) and [ECALModuleNumberList](../Properties/ECALModuleNumberList_Property.md)  
[IsolationAveragingIncrement](../Properties/IsolationAveragingIncrement_Property.md) |  ICalibrator7 |  Value to increase the channel's averaging factor.  
[OrientECALModule](../Properties/OrientECALModule_Property.md) |  ICalibrator3 |  Specifies if the VNA should perform orientation of the ECal module during calibration.  
[Simultaneous2PortAcquisition](../Properties/Simultaneous2PortAcquisition_Property.md) |  ICalibrator |  Allows the use of 2 sets of standards at the same time.  
  
###  ICalibrator History

Interface |  Introduced with VNA Rev:  
---|---  
ICalibrator |  1.0  
ICalibrator2 |  3.1  
ICalibrator3 |  3.1  
ICalibrator4 |  3.5  
ICalibrator5 |  5.0  
ICalibrator6 |  5.26  
ICalibrator7 |  7.21  
ICalibrator8 |  8.1  
ICalibrator9 |  9.1  
ICalibrator10 |  9.2  
  
ICalData Interface

#### Description

Contains methods for putting Calibration data in and getting Calibration data
out of the analyzer using typed data. This interface transfers data more
efficiently than variant data. However, this interfaces is only usable from
VB6, C, & C++. All other programming languages must use the [ICalSet
interface](CalSet_Object.htm).

There is also an [ICalData Interface](CalSet_Object.md#ICalData2) on the
CalSet Object

[Learn about reading and writing Calibration
data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

### Methods

|

### Description  
  
---|---  
[getErrorTermComplex](../Methods/Get_Error_Term_Complex_Method.md) |  Retrieves error term data  
[getStandardComplex](../Methods/Get_Standard_Complex_Method.md) |  Retrieves calibration data from the acquisition data buffer (before error-terms are applied).  
[putErrorTermComplex](../Methods/Put_Error_Term_Complex_Method.md) |  Puts error term data  
[putStandardComplex](../Methods/Put_Standard_Complex_Method.md) |  Puts calibration data into the acquisition data buffer (before error-terms are applied).  
  
### Properties

|

### Description  
  
None |   
  
### ICalData History

Interface |  Introduced with VNA Rev:  
---|---  
ICalData |  1.0  
|  
  
  

