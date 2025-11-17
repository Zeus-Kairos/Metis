# BalancedStimulus Object

* * *

### Description

These properties set the values that are unique to iTMSA - Opt S93460A/B.

All other properties for iTMSA use the standard VNA commands.

### Accessing the BalancedStimulus object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim balStim As BalancedStimulus  
Set balStim = app.ActiveMeasurement.BalancedMeasurement.BalancedStimulus

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [About iTMSA](../../../S1_Settings/Balanced_Measurements.md)

  * [Example iTMSA Program](../../COM_Example_Programs/Create_an_iTMSA_Measurement.md)

(Bold Methods or Properties provide access to a child object)

### Method

|

###

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[BalancedPortTrueState](../Properties/BalancedPortTrueState_Property.md) | IBalancedStimulus3 | Sets the True Mode state of a balanced port.  
[BalPort1PhaseOffset](../Properties/BalPort1PhaseOffset_Property.md) | IBalancedStimulus | Sets balanced port 1 phase offset  
[BalPort1PowerOffset](../Properties/BalPort1PowerOffset_Property.md) | IBalancedStimulus | Sets balanced port 1 power offset  
[BalPort1StartPhase](../Properties/BalPort1StartPhase_Property.md) | IBalancedStimulus2 | Sets Phase start value for port 1  
[BalPort1StopPhase](../Properties/BalPort1StopPhase_Property.md) | IBalancedStimulus2 | Sets Phase stop value for port 1  
[BalPort2PhaseOffset](../Properties/BalPort2PhaseOffset_Property.md) | IBalancedStimulus | Sets balanced port 2 phase offset  
[BalPort2PowerOffset](../Properties/BalPort2PowerOffset_Property.md) | IBalancedStimulus | Sets balanced port 2 power offset  
[BalPort2StartPhase](../Properties/BalPort2StartPhase_Property.md) | IBalancedStimulus2 | Sets Phase start value for port 2  
[BalPort2StopPhase](../Properties/BalPort2StopPhase_Property.md) | IBalancedStimulus2 | Sets Phase start value for port 2  
[Mode](../Properties/Mode-iTMSA_Property.md) | IBalancedStimulus | Sets Stimulus mode for balanced measurements  
[PhaseAsFixture](../Properties/PhaseAsFixture_Property.md) | IBalancedStimulus | Sets the state of phase offset as a fixture  
[PhaseSwpAsFixture](../Properties/PhaseSwpAsFixture_Property.md) | IBalancedStimulus2 | Enable Phase Sweep as fixture  
[PhaseSwpState](../Properties/PhaseSwpState_Property.md) | IBalancedStimulus2 | Enable Phase Sweep  
[PowerAsFixture](../Properties/PowerAsFixture_Property.md) | IBalancedStimulus | Sets the state of power offset as a fixture  
  
###  IBalancedStimulus History

Interface | Introduced with VNA Rev:  
---|---  
IBalancedStimulus | 8.2  
IBalancedStimulus2 | 8.5  
IBalancedStimulus3 | 14.40  
  
* * *

