# Remotely Specifying a Source Port

* * *

In the 'not-too-distant past', it was a simple task to specify a VNA source
port. It was either port 1 or port 2. Now, for the following reasons, it is
not so simple:

  * Internal 2nd sources are now offered on various VNA models. However, some source ports do not have a port number. One example is the second source on the PNA-X 2-port model (option 224). [Learn more about Internal Second Sources](../S0_Start/Internal_Second_Source.md).

  * External sources can now be controlled by the VNA as though they are internal sources. External sources do not have a source port number, but use String names as identifiers.

  *     * For FCA ONLY: Once configured using the [Configuration dialog](../System/Configure_an_External_Device.md#ext_source_config), an external source can be selected remotely and controlled by the VNA by specifying the LOName using [SCPI](GP-IB_Command_Finder/Sense/MIXerSCPI.md#name) or [COM](COM_Reference/Properties/LOName_Property.md).

    * All other uses for External sources: The external source must be configured and selected from the [External Source](../System/Configure_an_External_Device.md) dialog. You can then save an [Instrument State file](../S5_Output/SaveRecall.md#file_save), then recall that state file remotely.

  * Multiport test sets choose between ports 1 through port N, where N is the number of ports on the test set. You still use a port number, but this port number refers to a logical port. The Port mapping feature maps the logical port to a physical port. [Learn more about Multiport test sets.](../System/External_Testset_Control.md)

  * iTMSA (Opt S93460A/B) When this option is present, the string names for balanced source ports are returned with the appropriate COM and SCPI commands. For example, "SE Port 1" is used to access 'Single-ended Port 1".

### Source Port String Names

The VNA User Interface (UI) makes it easy to configure and select the sources
and ports. Remotely however, string names are used now, in addition to port
numbers, to specify a Source port.

COM \- The existing COM commands specify source ports as numbers and they are
still used. It is necessary to learn the port number from the string using the
[GetPortNumber Method](COM_Reference/Methods/GetPortNumber_Method.md). Port
numbers are assigned dynamically depending on whether [external sources are
selected](../System/Configure_an_External_Device.htm#SelectExtSource) and the
number of ports of the VNA.

  * [SourcePortNames Property](COM_Reference/Properties/SourcePortNames_Property.md)

  * [GetPortNumber Method](COM_Reference/Methods/GetPortNumber_Method.md)

  * [SourcePortCount Property](COM_Reference/Properties/SourcePortCount_Property.md).

An example:

dim app  
set app = CreateObject("Agilentpna835x.application")  
dim channel  
set channel = app.Channel  
dim portnum  
portnum = Channel.GetPortNumber("Src2 Out1")  
app.CreateMeasurement 1,"A",portnum

SCPI \- ALL of the existing SCPI commands that specify a source port are
extended to also allow the source port to be specified using string names. For
example, send the following command to set the power on Src2 Out1:

  * [SOUR:POW 5, Src2 Out1](GP-IB_Command_Finder/source.md#pwrval)

  * Use [Source:Cat?](GP-IB_Command_Finder/source.md#Cat) to list the available source port string names.

* * *

