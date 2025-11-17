#####

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnChannelEvent

* * *

#### Description

|  Triggered by a channel event.  
---|---  
  
####  VB Syntax

|  Sub app_OnChannelEvent(ByVal eventID As Variant, ByVal chanNum As Variant)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
eventID |  Code number of the event which occurred  
chanNum |  Channel Number of the event  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Sub pna_OnChannelEvent(ByVal eventID As Variant, ByVal channelNumber As
Variant)  
If eventID=naEventID_CHANNEL_CREATED then  
MsgBox "Channel" \+ chanelNumber + "was created"  
End If  
End Sub  
  
#### C++ Syntax

|  HRESULT OnChannelEvent(VARIANT eventID, VARIANT channelNumber)  
  
#### Interface

|  IApplication  
  
### Selected Channel Events

1792 [naEventID_CHANNEL_SWEEP_COMPLETE](../../../Support/PNA_Errors.md#11792)

1793
[naEventID_CHANNEL_TRIGGER_COMPLETE](../../../Support/PNA_Errors.md#11793)

1796 [naEventID_SET_CHANNEL_DIRTY](../../../Support/PNA_Errors.md#11796)

1797 [naEventID_CLEAR_CHANNEL_DIRTY](../../../Support/PNA_Errors.md#11797)

1801
[naEventID_ALL_SWEEPS_COMPLETED_AND_PROCESSED](../../../Support/PNA_Errors.md#11801)

1805 [naEventID_CHANNEL_CREATED](../../../Support/PNA_Errors.md#11805)

1806 [naEventID_CHANNEL_DELETED](../../../Support/PNA_Errors.md#11806)

1876 [naEventID_NO_SOURCE_ATTEN](../../../Support/PNA_Errors.md#11876)

1879
[naEventID_FREQ_OFFSET_OVERRANGE_SO_TURNED_OFF](../../../Support/PNA_Errors.md#11879)

1883
[naEventID_PORT_NUMBER_OUT_OF_RANGE](../../../Support/PNA_Errors.md#11883)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *

