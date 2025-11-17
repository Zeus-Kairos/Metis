# DCStimulus Object

* * *

Description

The DCStimulus object allows you to make DC Source settings for each channel.

### Accessing the DCStimulus Object

You can obtain a handle to a DCStimulus object through the Channel object.

dim app Set app = CreateObject("AgilentPNA835x.Application") dim chan Set chan
= app.ActiveChannel chan.NumberofPoints = 3 dim DC Set DC = chan.DCStimulus
DC.EnableAllOutput = True DC.State("AO1")= True  
---  
  
### See Also

[Learn about DC Source Control](../../../S1_Settings/DC_Control.md)

[Configure an External DC Device](../../../System/Configure_a_DC_Device.md)

[The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Description  
  
---|---  
None |   
  
### Properties

|

### Description  
  
[EnableAllOutput](../Properties/EnableAllOutput_Property.md) |  Sets and returns the ON / OFF state of all DC sources for the channel.  
[LimitMax](../Properties/LimitMax_Property.md) |  Sets and returns the Max DC limit value for a DC Source.  
[LimitMin](../Properties/LimitMin_Property.md) |  Sets and returns the Min DC limit value for a DC Source.  
[ListData](../Properties/ListData_Property.md) |  Sets and returns the stimulus value array of the DC source for the channel.  
[Sources](../Properties/Sources_Property.md) |  Returns the names of the configured DC sources for the channel.  
[Start](../Properties/Start_DC_Property.md) |  Sets and returns start DC value for the specified DC source.  
[State](../Properties/State_DC_Property.md) |  Sets and returns the ON / Off / Port state of the specified DC source.  
[Stop](../Properties/Stop_DC_Property.md) |  Sets and returns Stop DC value for the specified DC source.  
Target |  For future use  
  
### DCStimulus History

Interface |  Introduced with VNA Rev:  
---|---  
IDCStimulus |  9.5  
IDCStimulus2 |  12.80  
  
* * *

