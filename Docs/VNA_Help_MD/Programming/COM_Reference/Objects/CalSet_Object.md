# CalSet Object

* * *

See [ICalData Interface](CalSet_Object.md#ICalData2) for putting and getting
typed Cal Set data.

### Description

Use this interface to query and or change the contents of a Cal Set.

### Accessing the CalSet object

Get a handle to a CalSet object by using the CalSets collection. This is done
through the CalManager object with the
app.[GetCalManager](../Methods/Get_CalManager_Method.md) Method.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim calst As ICalSet  
Set calst = app.GetCalManager.CalSets.Item(1)  
'OR Get a handle by CalSet Name  
Set calst = app.GetCalManager.CalSets.Item("MyCalSet")

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Reading and Writing Calibration data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

### Methods

|

### Interface

[See History](CalSet_Object.md#Interface1) | 

### Description  
  
---|---|---  
[CloseCalSet](../Methods/Close_CalSet_Method.md) |  ICalSet |  Obsolete \- No longer necessary.  
[ComputeErrorTerms](../Methods/ComputeErrorTerms_Method.md) |  ICalSet |  Computes error terms for the CalType specified by a preceding OpenCal Set call.  
[Copy](../Methods/Copy_Method.md) |  ICalSet |  Creates a new Cal Set and copies the current Cal Set data into it.  
[EnumerateItems](../Methods/EnumerateItems_Method.md) |  ICalSet6 |  Returns a list of all name-value pairs (items) in the Cal Set.  
[getErrorTerm](../Methods/Get_ErrorTerm2_Method.md) |  ICalSet |  Superseded with [getErrorTermByString](../Methods/Get_ErrorTermByString_Method.md)  
[GetErrorTermByString](../Methods/Get_ErrorTermByString_Method.md) |  ICalSet2 |  Returns variant error term data by specifying the string name of the error term.  
[getErrorTermList](../Methods/Get_ErrorTermList_Method.md) |  ICalSet |  Superseded with [getErrorTermList2](../Methods/Get_ErrorTermList2_Method.md)  
[getErrorTermList2](../Methods/Get_ErrorTermList2_Method.md) |  ICalSet2 |  Returns a list of error term names found in a calset.  
[GetErrorTermStimulus](../Methods/GetErrorTermStimulus_Method.md) |  ICalSet7 |  Returns the stimulus values over which the specific error term was acquired.  
[GetGUID](../Methods/Get_Guid_Method.md) |  ICalSet |  Returns the GUID identifying a Cal Set  
[getStandard](../Methods/Get_Standard2_Method.md) |  ICalSet |  Superseded with [getStandardByString](../Methods/Get_StandardByString_Method.md)  
[getStandardByString](../Methods/Get_StandardByString_Method.md) |  ICalSet2 |  Returns variant standard acquisition data by specifying the string name of the standard.  
[getStandardsList](../Methods/Get_StandardsList_Method.md) |  ICalSet |  Superseded with [getStandardList2](../Methods/Get_StandardList2_Method.md)  
[getStandardList2](../Methods/Get_StandardList2_Method.md) |  ICalSet2 |  Returns a list of standard names found in a Cal Set.  
[HasCalType](../Methods/Has_CalType_Method.md) |  ICalSet |  Verifies that the Cal Set object contains the error terms required to apply the specified CalType to an appropriate measurement.  
[OpenCalSet](../Methods/Open_CalSet_Method.md) |  ICalSet |  Obsolete \- No longer necessary.  
[putErrorTerm](../Methods/Put_Error_Term_Method.md) |  ICalSet |  Superseded with [putErrorTermByString](../Methods/Put_ErrorTermByString_Method.md)  
[PutErrorTermByString](../Methods/Put_ErrorTermByString_Method.md) |  ICalSet2 |  Writes variant error term data by specifying the string name of the error term.  
[PutErrorTermStimulus](../Methods/PutErrorTermStimulus_Method.md) |  ICalSet7 |  Adds stimulus data to the specified buffer.  
[putStandard](../Methods/Put_Standard_Method.md) |  ICalSet |  Superseded with [putStandardByString](../Methods/Put_StandardByString_Method.md)  
[putStandardByString](../Methods/Put_StandardByString_Method.md) |  ICalSet2 |  Writes variant standard acquisition data by specifying the string name of the standard.  
[RemoveItem](../Methods/RemoveItem_Method.md) |  ICalSet6 |  Removes a name-value pair from the Cal Set.  
[Save](../Methods/Save_CalSet_Method.md) |  ICalSet |  Saves the current Cal Set to disk.  
[StringToNACalClass](../Methods/StringToNACalClass_Method.md) |  ICalSet |  Converts string values from GetStandardsList into enumeration data  
[StringToNAErrorTerm2](../Methods/StringtoNAErrorTerm2_Method.md) |  ICalSet |  Converts string values from GetErrorTermList into enumeration data  
  
### Properties

|

###

|

### Description  
  
[AlternateSweep](../Properties/Alternate_Sweep_Property.md) |  ICalSet3 |  Reads sweep either alternate or chopped.  
[Attenuator](../Properties/Attenuator_Property.md) |  ICalSet3 |  Returns the value of the attenuator control for the specified port number.  
[AttenuatorMode](../Properties/Attenuator_Mode_Property.md) |  ICalSet3 |  Returns the mode of operation (auto or manual) of the attenuator control for the specified port number.  
[ChannelClients](../Properties/ChannelClients_Property.md) |  ICalSet8 |  Returns the numbers of the channels using the calset.  
[ContentDescriptor](../Properties/ContentDescriptor_Property.md) |  ICalSet8 |  Returns the Cal Types from the calset.  
[CouplePorts](../Properties/Couple_Ports_Property.md) |  ICalSet3 |  Returns state of couple ports (ON or OFF)  
[CWFrequency](../Properties/CWFrequency_CS_Property.md) |  ICalSet3 |  Returns CW Frequency  
[Description](../Properties/Description_Property.md) |  ICalSet |  Set or return the descriptive string assigned to the Cal Set  
[DwellTime](../Properties/Dwell_Time_Property.md) |  ICalSet3 |  Returns the dwell time for the channel.  
[FrequencyOffsetCWOverride](../Properties/FrequencyOffsetCWOverride_Property.md) |  ICalSet3 |  Reads state of CW Override (ON or OFF)  
[FrequencyOffsetDivisor](../Properties/FrequencyOffsetDivisor_Property.md) |  ICalSet3 |  Reads Frequency Offset Divisor value  
[FrequencyOffsetFrequency](../Properties/FrequencyOffsetFrequency_Property.md) |  ICalSet3 |  Reads Offset Frequency  
[FrequencyOffsetMultiplier](../Properties/FrequencyOffsetMultiplier_Property.md) |  ICalSet3 |  Reads Frequency Offset Multiplier value  
[FrequencyOffsetState](../Properties/FrequencyOffsetState_Property.md) |  ICalSet3 |  Reads Frequency Offset state (ON or OFF)  
[IFBandwidth](../Properties/IF_Bandwidth_Property.md) |  ICalSet3 |  Reads IF Bandwidth of the channel  
[Item](../Properties/Item_Property.md) |  ICalSet6 |  Add or change a name-value pair in the Cal Set, or read the value associated with a name.  
[LastModified](../Properties/LastModified_Property.md) |  ICalSet3 |  Reads the time stamp of when the file was last modified  
[Name](../Properties/Name_Calset_Property.md) |  ICalSet4 |  Sets and returns the Cal Set name.  
[NumberOfPoints](../Properties/Number_of__Points_Property.md) |  ICalSet3 |  Returns the Number of Points of the channel.  
[OutputPorts](../Properties/OutputPorts_Property.md) |  ICalSet5 |  Returns the port mapping used for the Cal Set.  
[PowerSlope](../Properties/Power_Slope_Property.md) |  ICalSet3 |  Returns the Power Slope value.  
[Properties](../Properties/Properties_Property.md) |  ICalSet8 |  Returns the properties of the calset.  
[ReceiverAttenuator](../Properties/Receiver_Attenuator_Property.md) |  ICalSet3 |  Returns the value of the specified receiver attenuator control.  
[StartFrequency](../Properties/Start_Frequency_CS_Property.md) |  ICalSet3 |  Returns the start frequency of the channel.  
[StartPower](../Properties/Start_Power_Property.md) |  ICalSet3 |  Returns the start power of the VNA when sweep type is set to Power Sweep.  
[StimulusValues](../Properties/StimulusValues_Property.md) |  ICalSet3 |  Returns x-axis values for stimulus or response frequencies  
[StopFrequency](../Properties/Stop_Frequency_CS_Property.md) |  ICalSet3 |  Returns the stop frequency of the channel.  
[StopPower](../Properties/Stop_Power_Property.md) |  ICalSet3 |  Returns the stop power of the VNA when sweep type is set to Power Sweep.  
[SweepGenerationMode](../Properties/Sweep_Generation_Mode_Property.md) |  ICalSet3 |  Returns the method being used to generate a sweep: analog or stepped.  
[SweepTime](../Properties/Sweep_Time_Property.md) |  ICalSet3 |  Returns the sweep time of the analyzer.  
[SweepType](../Properties/Sweep_Type_Property.md) |  ICalSet3 |  Returns the type of X-axis sweep that is performed on a channel.  
[TestPortPower](../Properties/Test_Port_Power_Property.md) |  ICalSet3 |  Returns the RF power level for the channel.  
[TestSetType](../Properties/TestSetType_Property.md) |  ICalSet5 |  Returns the Test Set type used for the Cal Set.  
  
###  ICalSet History

Interface |  Introduced with VNA Rev:  
---|---  
ICalSet |  2.0  
ICalSet2 |  3.0  
ICalSet3 |  3.2  
ICalSet4 |  6.0  
ICalSet5 |  6.2  
ICalSet6 |  9.30  
ICalSet7 |  9.40  
ICalSet8 |  10.15  
  
ICalData Interface

Description

Use this interface as an alternative to the ICalSet Interface to avoid using
variants when transmitting data to and from the Cal Set

[Learn about reading and writing Calibration
data.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

### Methods

|

### Interface

[See History](CalSet_Object.md#Interface) | 

### Description  
  
---|---|---  
[get ErrorTermComplex](../Methods/Get_ErrorTermComplex2_Method.md) |  ICalData2 |  Superseded with [getErrorTermComplexByString](../Methods/Get_ErrorTermComplexByString_Method.md)  
[getErrorTermComplexByString](../Methods/Get_ErrorTermComplexByString_Method.md) |  ICalData3 |  Returns typed error term data by specifying the string name of the error term.  
[getStandardComplex](../Methods/Get_Standard_Complex_Method.md) |  ICalData2 |  Superseded with [getStandardComplexByString](../Methods/Get_StandardComplexByString_Method.md)  
[getStandardComplexByString](../Methods/Get_StandardComplexByString_Method.md) |  ICalData3 |  Returns typed standard acquisition data by specifying the string name of the standard.  
[putErrorTermComplex](../Methods/Put_ErrorTermComplex2_Method.md) |  ICalData2 |  Superseded with [putErrorTermComplexByString](../Methods/Put_ErrorTermComplexByString_Method.md)  
[putErrorTermComplexByString](../Methods/Put_ErrorTermComplexByString_Method.md) |  ICalData3 |  Writes typed error term data by specifying the string name of the error term.  
[putStandardComplex](../Methods/Put_Standard_Complex_Method.md) |  ICalData2 |  Superseded with [putStandardComplexByString](../Methods/Put_StandardComplexByString_Method.md)  
  
###
[putStandardComplexByString](../Methods/Put_StandardComplexByString_Method.md)

|  ICalData3 |  Writes typed standard acquisition data by specifying the string name of the standard.  
  
### Properties

|

###

|

### Description  
  
None |  |   
  
###  History

Interface |  Introduced with VNA Rev:  
---|---  
The original ICalData Interface was introduced with VNA 1.0 on the
[Calibrator](Calibrator_Object.md) Object.  
ICalData2 |  2.0  
ICalData3 |  3.1  
  
* * *

