|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnSCPIEvent

* * *

#### Description

|  Triggered by a SCPI event. Note: Some Severe Events are also used as Error
Messages  
---|---  
  
####  VB Syntax

|  Sub app_OnSCPIEvent(ByVal eventID As Variant)  
  
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

|  Private Sub pna_OnSCPIEvent(ByVal eventID As Variant)  
MsgBox ("A SCPI event has occured")  
End Sub  
  
* * *  
  
#### C++ Syntax

|  HRESULT OnSCPIEvent(VARIANT eventID )  
  
#### Interface

|  IApplication  
  
### Selected SCPI Parser Events

1281 [naEventID_NOTHING_TO_SAY](../../../Support/PNA_Errors.md#11281)

1284
[naEventID_SCPI_STATUS_BYTE_CHANGE](../../../Support/PNA_Errors.md#11284)

1360 [naEventID_BAD_SCPI_EXECUTE](../../../Support/PNA_Errors.md#11360)

1375
[naEventID_CALC_MEASUREMENT_SET_TO_NONE](../../../Support/PNA_Errors.md#11375)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *

