#####

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnHardwareEvent

* * *

#### Description

|  Triggered by a hardware event. See a list of [Hardware
Events](../../../Support/PNA_Errors.htm#Hardware) Note: Some Severe Events are
also used as Error Messages  
---|---  
  
####  VB Syntax

|  Sub app_OnHardwareEvent(ByVal eventID As Variant)  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
eventID |  Code number of the event which occurred  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  Private Sub pna_OnHardwareEvent(ByVal eventID As Variant)  
MsgBox ("A Hardware event has occured")  
End Sub  
  
* * *  
  
#### C++ Syntax

|  HRESULT OnHardwareEvent(VARIANT eventID)  
  
#### Interface

|  IApplication  
  
### Selected Hardware Events

848 [naEventID_PHASELOCK](../../../Support/PNA_Errors.md#10848)

852 [naEventID_RFPOWEROFF](../../../Support/PNA_Errors.md#10852)

853 [naEventID_RFPOWERON](../../../Support/PNA_Errors.md#10853)

855 [naEventID_UNLEVELED](../../../Support/PNA_Errors.md#10855)

857 [naEventID_OVERLOAD](../../../Support/PNA_Errors.md#10857)

914
[naEventID_TRIGGER_REQUIRES_EDGE_LEVEL_TRIGGER](../../../Support/PNA_Errors.md#10914)

915
[naEventID_TRIGGER_REQUIRES_TRIGGER_OUT](../../../Support/PNA_Errors.md#10915)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *

