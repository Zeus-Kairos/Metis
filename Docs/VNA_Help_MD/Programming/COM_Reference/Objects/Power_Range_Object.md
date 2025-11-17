# Power Range Object

Description

These methods and properties provide access to data sheet specified and
typical, max and min power levels (in dBm). Max power refers to the maximum
leveled source power at the specified port. Min power is calculated by
subtracting the power sweep range from the max leveled power. This information
is stored by frequency band in a power specification file. This object
provides access to the files contents and provides an interface to configure
the port number and RF signal path of interest.

Power data is available as either the most restrictive value across a range of
frequencies (when [RangeGetMaxPower](../Methods/RangeGetMaxPower_Method.md)
and [RangeGetMinPower](../Methods/RangeGetMinPower_Method.md) are used) or
for discrete CW frequencies (when
[DiscreteGetMaxPower](../Methods/DiscreteGetMaxPower_Method.md) and
[DiscreteGetMinPower](../Methods/DiscreteGetMinPower_Method.md) are used).

No measurement of instrument-specific dynamic range is performed; all power
levels are equivalent to power data published in device data sheets. Power
levels are valid only for measurement configurations where the front panel
jumpers are in their standard positions, as originally shipped. Internal
source attenuation and any calibrated external path loss/gain due to cables,
fixtures, switches or booster amplifiers are not included in the reported
min/max leveled power values. It remains the users responsibility to
transform the reported factory power range data to a value corresponding to
the specific calibration plane of their setups.

The power range data files contain both specified min/max leveled power values
and the corresponding typical values. Some paths, that are not part of the
specifications of the instrument may only have typical data. Only the
Specified power range data is guaranteed for an instrument with an up-to-
date calibration certificate.

### Accessing the Power Range object

Dim app As AgilentPNA835x.Application Set app =
CreateObject(AgilentPNA835x.Applicaiton, <analyzerName>) Dim pwrRange As
PowerRange Set pwrRange = app.Capabilities.PowerRange  
---  
  
### See Also:

  * [ALC](../../../S1_Settings/Power_Level.md#Leveling)

  * [Source Unleveled](../../../S1_Settings/Power_Level.md#Unleveled)

  * [Capabilities Object](Capabilities_Object.md)

  * [The PNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/Power_Range_Example.md)

### Methods

|

### Interface

See History | 

###  
  
---|---|---  
[DiscreteGetMaxPower](../Methods/DiscreteGetMaxPower_Method.md) |  IPowreRange |  Returns a single max leveled power value (in dBm) indicating the most restrictive maximum for all discrete maximum powers (the minimum of all max leveled powers).  
[DiscreteGetMaxPowerArray](../Methods/DiscreteGetMaxPowerArray_Method.md) |  IPowreRange |  Returns an array of max leveled power values (in dBm), where each element corresponds to the maximum leveled power possible for CW stimulus at the corresponding frequency set by the DiscreteFrequencies property.  
[DiscreteGetMinPower](../Methods/DiscreteGetMinPower_Method.md) |  IPowreRange |  Returns a single minimum power value (in dBm) indicating the most restrictive minimum for all discrete minimum powers (the maximum of all minimum powers).  
[DiscreteGetMinPowerArray](../Methods/DiscreteGetMinPowerArray_Method.md) |  IPowreRange |  Returns an array of minimum power values (in dBm), where each element corresponds to the minimum power possible for CW stimulus at the corresponding frequency set by the DiscreteFrequencies property.  
[RangeGetMaxPower](../Methods/RangeGetMaxPower_Method.md) |  IPowreRange |  Set minimum of all max leveled power values from RangeStartFrequency to RangeStopFrequency (inclusive).  
[RangeGetMinPower](../Methods/RangeGetMinPower_Method.md) |  IPowreRange |  Set maximum of all min power values from RangeStartFrequency to RangeStopFrequency (inclusive).  
[Reset](../Methods/Reset_\(Power_Range\)_Method.md) |  IPowreRange |  Resets all PowerRange properties to default values, as if the instrument had been preset.  
  
### Properties

|

###

|

### Description  
  
[DiscreteFrequencies](../Properties/DiscreteFrequencies_Property.md) |  IPowreRange | An array of frequencies (in Hertz); each element of the array corresponds to a power returned by DiscreteGetMaxPowerArray or DiscreteGetMinPowerArray.  
[PathElement](../Properties/PathElement_Property.md) |  IPowreRange | Given the name of a path element, returns a handle to the PathElement interface corresponding to the given name.  
[PathElements](../Properties/PathElements_Property.md) |  IPowreRange | Returns an array with the names of all RF path elements that may be configured.  
[PortNumber](../Properties/PortNumber_Property.md) |  IPowreRange | Set port number for power data.  
[PowerRangeType](../Properties/PowerRangeType_Property.md) |  IPowreRange | Select warranted or typical power performance.  
[RangeStartFrequency](../Properties/RangeStartFrequency_\(PowerRange\)_Property.md) |  IPowreRange | Set lower bound of the frequency range (in Hertz).  
[RangeStopFrequency](../Properties/RangeStopFrequency_\(PowerRange\)_Property.md) |  IPowreRange | Set upper bound of the frequency range (in Hertz).  
  
### ICapabilities History

Interface |  Introduced with VNA Rev:  
---|---  
IPowerRange |  12.70  
  
* * *

