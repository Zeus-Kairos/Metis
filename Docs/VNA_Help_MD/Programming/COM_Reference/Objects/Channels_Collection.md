# Channels Collection

* * *

### Description

A collection object that provides a mechanism for iterating through the
channels

Collections are, by definition, unordered lists of like objects. You cannot
assume that Channels.Item(1) is always Channel 1.

### Accessing the Channels collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim chans As Channels  
Set chans = app.Channels

### See Also:

  * [Channel Object](Channel_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

See History | 

### Description  
  
---|---|---  
[Add](../Methods/Add_channels_Method.md) |  IChannels |  An alternate way to create a measurement.  
[Hold](../Methods/Hold_Method.md) |  IChannels |  Places all channels in Hold trigger mode.  
[Item](../Methods/Item_Method.md) |  IChannels |  Use to get a handle to a channel in the collection.  
[Remove](../Methods/Remove_Method.md) |  IChannels3 |  Delete a channel by specifying the index in the collection.  
[RemoveChannelNumber](../Methods/RemoveChannelNumber_Method.md) |  IChannels3 |  Delete a channel by specifying the channel number.  
[Resume](../Methods/Resume_Method.md) |  IChannels2 |  Resumes the trigger mode of all channels that was in effect before sending the channels.Hold method.  
  
### Properties

|

###

|

### Description  
  
[Count](../Properties/Count_Property.md) |  IChannels |  Returns the number of channels in the analyzer.  
[Parent](../Properties/Parent_Property.md) |  IChannels |  Returns a handle to the current Application.  
[UnusedChannelNumbers](../Properties/UnusedChannelNumbers_Property.md) |  IChannels2 |  Returns an array of channel numbers that are NOT in use.  
[UsedChannelNumbers](../Properties/UsedChannelNumbers_Property.md) |  IChannels2 |  Returns an array of channel numbers that are in use.  
  
### IChannels History

Interface |  Introduced with VNA Rev:  
---|---  
IChannels |  1.0  
IChannels2 |   
IChannels3 |  9.30

