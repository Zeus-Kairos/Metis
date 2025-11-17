# Fixturing Object

* * *

### Description

Contains the properties for Embedding and De-embedding test fixtures.

### Accessing the Fixturing object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim fixt as Fixturing  
Set fixt = chan.Fixturing

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * About Fixturing

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[AutoPortExtMeasure](../Methods/AutoPortExtMeasure_Method.md) | IFixturing2 | Measures either an OPEN or SHORT standard.  
[AutoPortExtReset](../Methods/AutoPortExtReset_Method.md) | IFixturing2 | Clears old port extension delay and loss data.  
[NetworkPortMap](../Methods/NetworkPortMap_Method.md) | IFixturing2 | Set the port mapping for a 4-port SNP file to be embedded.  
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[AutoPortExtConfig](../Properties/AutoPortExtConfig_Property.md) | IFixturing2 | Sets the frequency span that is used to calculate Automatic Port Extension.  
[AutoPortExtDCOffset](../Properties/AutoPortExtDCOffset_Property.md) | IFixturing2 | Specifies whether or not to include DC Offset as part of Automatic port extension.  
[AutoPortExtLoss](../Properties/AutoPortExtLoss_Property.md) | IFixturing2 | Specifies whether or not to include loss correction as part of Automatic Port Extension.  
[AutoPortExtSearchStart](../Properties/AutoPortExtSearchStart_Property.md) | IFixturing2 | Set the start frequency for custom user span.  
[AutoPortExtSearchStop](../Properties/AutoPortExtSearchStop_Property.md) | IFixturing2 | Set the stop frequency for custom user span.  
[AutoPortExtState](../Properties/AutoPortExtState_Property.md) | IFixturing2 | Enables and disables automatic port extensions on the specified port.  
[CmnModeZConvPortImag](../Properties/CmnModeZConvPortImag_Property.md) | IFixturing2 | Sets imaginary value for common port impedance conversion.  
[CmnModeZConvPortReal](../Properties/CmnModeZConvPortReal_Property.md) | IFixturing2 | Sets real value for common port impedance conversion.  
[CmnModeZConvState](../Properties/CmnModeZConvState_Property.md) | IFixturing2 | Turns ON/OFF common port impedance conversion.  
[CmnModeZConvPortZ0](../Properties/CmnModeZConvPortZ0_Property.md) | IFixturing2 | Sets impedance value for common port impedance conversion.  
[DiffPortMatch_C](../Properties/DiffPortMatch_C_Property.md) | IFixturing2 | Sets Capacitance value of the differential matching circuit.  
[DiffPortMatch_G](../Properties/DiffPortMatch_G_Property.md) | IFixturing2 | Sets Conductance value of the differential matching circuit.  
[DiffPortMatch_L](../Properties/DiffPortMatch_L_Property.md) | IFixturing2 | Sets Inductance value of the differential matching circuit.  
[DiffPortMatch_R](../Properties/DiffPortMatch_R_Property.md) | IFixturing2 | Sets Resistance value of the differential matching circuit.  
[DiffPortMatchMode](../Properties/DiffPortMatchMode_Property.md) | IFixturing2 | Sets type of circuit to embed.  
[DiffPortMatchUserFilename](../Properties/DiffPortMatchUserFilename_Property.md) | IFixturing2 | Specifies the 4-port touchstone file for user-defined differential matching circuit.  
[DiffPortMatchState](../Properties/DiffPortMatchState_Property.md) | IFixturing2 | Turns ON/OFF differential matching circuit function.  
[DiffZConvPortImag](../Properties/DiffZConvPortImag_Property.md) | IFixturing2 | Sets imaginary value for differential port impedance conversion.  
[DiffZConvPortReal](../Properties/DiffZConvPortReal_Property.md) | IFixturing2 | Sets real value for differential port impedance conversion.  
[DiffZConvPortZ0](../Properties/DiffZConvPortZ0_Property.md) | IFixturing2 | Sets impedance value for differential port impedance conversion.  
[DiffZConvState](../Properties/DiffZConvState_Property.md) | IFixturing2 | Turns ON/OFF differential port impedance conversion.  
[Embed4PortA](../Properties/Embed4PortA_Property.md) | IFixturing2 | Returns VNA portA connections.  
[Embed4PortB](../Properties/Embed4PortB_Property.md) | IFixturing2 | Returns VNA portB connections.  
[Embed4PortC](../Properties/Embed4PortC_Property.md) | IFixturing2 | Returns VNA portC connections.  
[Embed4PortD](../Properties/Embed4PortD_Property.md) | IFixturing2 | Returns VNA portD connections.  
[Embed4PortList](../Properties/Embed4PortList_Property.md) | IFixturing2 | Specifies all VNA port connections.  
[Embed4PortNetworkFilename](../Properties/Embed4PortNetworkFilename_Property.md) | IFixturing2 | Specifies *.s4p filename.  
[Embed4PortNetworkMode](../Properties/Embed4PortNetworkMode_Property.md) | IFixturing2 | Specify embed, de-embed, or none.  
[Embed4PortState](../Properties/Embed4PortState_Property.md) | IFixturing2 | Turns ON or OFF 4-port Network Embed/De-embed.  
[Embed4PortTopology](../Properties/Embed4PortTopology_Property.md) | IFixturing2 | Specifies the VNA / DUT topology.  
[EnablePowerCompensation](../Properties/EnablePowerCompensation_Property.md) | IFixturing5 | Compensates source power for combined loss through all fixturing functions.  
[EnableSnPDataExtrapolation](../Properties/EnableSnPDataExtrapolation_Property.md) | IFixturing6 | Turns ON and OFF SNP file extrapolation for both 2-port and 4-port embedding/de-embedding.  
[FixturingState](../Properties/FixturingState_Property.md) | IFixturing | Turns Fixturing ON and OFF on this channel.  
[NetworkPortMapA](../Properties/NetworkPortMapA_Property.md) | IFixturing6 | Read the port mapping of in A port for a 4-port SNP file to be embedded.  
[NetworkPortMapB](../Properties/NetworkPortMapB_Property.md) | IFixturing6 | Read the port mapping of in B port for a 4-port SNP file to be embedded.  
[NetworkPortMapC](../Properties/NetworkPortMapC_Property.md) | IFixturing6 | Read the port mapping of out A port for a 4-port SNP file to be embedded.  
[NetworkPortMapD](../Properties/NetworkPortMapD_Property.md) | IFixturing6 | Read the port mapping of out B port for a 4-port SNP file to be embedded.  
[Port2PdeembedCktModel](../Properties/Port2PdeembedCktModel_Property.md) | IFixturing | Sets and returns the 2 port De-embedding circuit model for the specified port number.  
[Port2PdeembedState](../Properties/Port2PdeembedState_Property.md) | IFixturing | Turns 2 port de-embedding ON and OFF on this channel.  
[PortArbzImag](../Properties/PortArbzImag_Property.md) | IFixturing3 | Sets and returns the imaginary impedance value for the specified single-ended port number.  
[PortArbzReal](../Properties/PortArbzReal_Property.md) | IFixturing3 | Sets and returns the real impedance value for the specified single-ended port number.  
[PortArbzState](../Properties/PortArbzState_Property.md) | IFixturing | Turns single-ended port impedance ON and OFF on the specified channel.  
[PortArbzZ0](../Properties/PortArbzZ0_Property.md) | IFixturing3 | Sets and returns the real and imaginary impedance value for the specified single-ended port number.  
[PortCoupleToSystemMedia](../Properties/PortCoupleToSystemMedia_Property.md) | IFixturing4 | Couples to system Media type  
[PortCoupleToSystemVelocity](../Properties/PortCoupleToSystemVelocity_Property.md) | IFixturing4 | Couples to system Velocity Factor  
[PortDelay](../Properties/PortDelay_Property.md) | IFixturing | Sets and returns the Port Delay value for the specified port number.  
[PortDistance](../Properties/PortDistance_Property.md) | IFixturing4 | Sets Port Ext in distance  
[PortNADistanceUnit](../Properties/PortDistanceUnit_Property.md) | IFixturing4 | Sets distance units  
[PortExtState](../Properties/PortExtState_Property.md) | IFixturing | Turns Port Extension ON and OFF on this channel.  
[PortExtUse1](../Properties/PortExtUse1_Property.md) | IFixturing | Sets and returns the USE1 ON/OFF state for the Loss1 and Freq1 values for the specified port number.  
[PortExtUse2](../Properties/PortExtUse2_Property.md) | IFixturing | Sets and returns the USE2 ON/OFF state for the Loss2 and Freq2 values for the specified port number.  
[PortFreq1](../Properties/PortFreq1_Property.md) | IFixturing | Sets and returns the 1st Port Frequency value for the specified port number.  
[PortFreq2](../Properties/PortFreq2_Property.md) | IFixturing | Sets and returns the 2nd Port Frequency value for the specified port number.  
[PortLoss1](../Properties/PortLoss1_Property.md) | IFixturing | Sets and returns the 1st Port Loss value for the specified port number.  
[PortLoss2](../Properties/PortLoss2_Property.md) | IFixturing | Sets and returns the 2nd Port Loss value for the specified port number.  
[PortLossDC](../Properties/PortLossDC_Property.md) | IFixturing | Sets and returns the Port Loss at DC value for the specified port number.  
[PortMatching_C](../Properties/PortMatching_C_Property.md) | IFixturing7 | Sets and returns the Capacitance, 'C' value for the specified port number.  
[PortMatching_G](../Properties/PortMatching_G_Property.md) | IFixturing7 | Sets and returns the Conductance, 'G' value for the specified port number.  
[PortMatching_L](../Properties/PortMatching_L_Property.md) | IFixturing7 | Sets and returns the Inductance, 'L' value for the specified port number.  
[PortMatching_R](../Properties/PortMatching_R_Property.md) | IFixturing7 | Sets and returns the Resistance, 'R' value for the specified port number.  
[PortMatchingCktModel](../Properties/PortMatchingCktModel_Property.md) | IFixturing | Sets and returns the Port Matching circuit model for the specified port number.  
[PortMatchingState](../Properties/PortMatchingState_Property.md) | IFixturing | Turns Port Matching ON and OFF on this channel.  
[PortMedium](../Properties/PortMedium_Property.md) | IFixturing4 | Sets Media per port  
[PortVelocityFactor](../Properties/PortVelocityFactor_Property.md) | IFixturing4 | Set Velocity Factor per port  
[PortWGCutoffFreq](../Properties/PortWGCutoffFreq_Property.md) | IFixturing4 | Sets waveguide cutoff frequency per port  
[Reverse2PortAdapter](../Properties/Reverse2PortAdapter_Property.md) | IFixturing6 | Set and read whether or not to reverse ports on a 2-port fixture or adapter to be de-embedded.  
[strPort2Pdeembed_S2PFile](../Properties/strPort2Pdeembed_S2PFile_Property.md) | IFixturing | Sets and returns the 2 port De-embedding 'S2P' file name for the specified port number.  
[strPortMatch_S2PFile](../Properties/strPortMatch_S2PFile_Property.md) | IFixturing | Sets and returns the Port Matching 'S2P' file name for the specified port number.  
  
###  IFixturing History

Interface | Introduced with VNA Rev:  
---|---  
IFixturing | 5.0  
IFixturing2 | 5.2  
IFixturing3 | 5.25  
IFixturing4 | 8.50  
IFixturing5 | 9.20  
IFixturing6 | 9.33  
IFixturing7 | 12.70

