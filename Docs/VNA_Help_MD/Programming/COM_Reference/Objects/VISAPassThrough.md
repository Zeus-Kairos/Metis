# VISAPassThrough Object

* * *

Description

VISA (Virtual Instrument Software Architecture) is used to communicate with
most instrumentation buses including the following:

  * GPIB
  * USB
  * Serial
  * Ethernet

### Accessing the VISAPassThrough object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim vPass As VISAPassThrough  
Set vPass = app.VISAPassThrough

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[Close](../Methods/Close_VISAPassthrough_Method.md) |  IVISAPassthrough |  Closes the remote VISA session  
[Find](../Methods/Find_VISAPassthrough_Method.md) |  IVISAPassthrough |  Returns a comma separated list of either visa address strings or aliases  
[GetVISATimeout](../Methods/GetVISATimeout_Method.md) |  IVISAPassthrough |  Returns the timeout value (in milliseconds) for subsequent VISA pass-through commands  
[Open](../Methods/Open_VISAPassthrough_Method.md) |  IVISAPassthrough |  Initiates a VISA pass-through session  
[ReadBinary](../Methods/ReadBinary_Method.md) |  IVISAPassthrough |  Reads data from the VISA pass-through device as a Safe Array of variants.  
[ReadBinaryCompact](../Methods/ReadBinaryCompact_Method.md) |  IVISAPassthrough |  Reads binary data in a more compact form of Safe Array.  
[ReadString](../Methods/ReadString_VISAPassthrough_Method.md) |  IVISAPassthrough |  Reads string data from the VISA pass-through device.  
[Reset](../Methods/Reset_VISAPassthrough_Method.md) |  IVISAPassthrough |  Closes all currently open remote VISA sessions  
[SetVISATimeout](../Methods/SetVISATimeout_Method.md) |  IVISAPassthrough |  Sends the timeout value (in milliseconds) for subsequent VISA pass-through commands  
[WriteBinary](../Methods/WriteBinary.md) |  IVISAPassthrough |  Write data to the VISA pass-through device - without header.  
[WriteString](../Methods/WriteString_VISAPassthrough_Method.md) |  IVISAPassthrough | Write string data to the VISA pass-through device.

