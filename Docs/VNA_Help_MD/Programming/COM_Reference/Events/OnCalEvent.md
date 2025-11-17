#####

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnCalEvent

* * *

#### Description

|  Triggered by a calibration event. See a list of [CAL
Events](../../../Support/PNA_Errors.htm#Cal). Note: Some Severe Events are
also used as Error Messages  
---|---  
  
####  VB Syntax

|  Sub app_OnCalEvent(ByVal eventID As Variant, ByVal chanNum As Variant,
ByVal measNum As Variant)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
eventID |  Code number of the event which occurred  
chanNum |  Channel Number of the event  
measNum |  Measurement Number of the event  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Sub pna_OnCalEvent(ByVal eventID As Variant, ByVal channelNumber As
Variant, ByVal measurementNumber As Variant)  
'  
MsgBox ("A Calibration event has occured")  
End Sub  
  
* * *  
  
#### C++ Syntax

|  HRESULT OnCalEvent(VARIANT eventID, VARIANT channelNumber, VARIANT
measurementNumber)  
  
#### Interface

|  IApplication  
  
### Selected Cal Events

512 [naEventID_CAL_QUESTIONABLE](../../../Support/PNA_Errors.md#10512)

513 [naEventID_CAL_STD_NEEDED](../../../Support/PNA_Errors.md#10513)

514
[naEventID_CAL_STATE_NOT_HW_COMPATIBLE](../../../Support/PNA_Errors.md#10514)

515 [naEventID_CAL_REQUIRED](../../../Support/PNA_Errors.md#10515)

516
[naEventID_CAL_CORRECTION_TURNED_OFF](../../../Support/PNA_Errors.md#10516)

517
[naEventID_CAL_CORRECTION_TURNED_OFF_INTERPOLATION_OFF](../../../Support/PNA_Errors.md#10517)

518 [naEventID_CAL_CORRECTION_RESTORED](../../../Support/PNA_Errors.md#10518)

519
[naEventID_CAL_CORRECTION_TURNED_OFF_FREQRANGE_EXCEEDED](../../../Support/PNA_Errors.md#10519)

520 [naEventID_CAL_CALTYPE_SET_TO_NONE](../../../Support/PNA_Errors.md#10520)

521
[naEventID_CAL_CORRECTION_TURNED_OFF_NOT_AN_SPARAM](../../../Support/PNA_Errors.md#10521)

524
[naEventID_SOURCE_POWER_CAL_COMPLETED](../../../Support/PNA_Errors.md#10524)

592
[naEventID_SOURCE_POWER_CAL_NOT_PRESENT](../../../Support/PNA_Errors.md#10592)

593
[naEventID_SOURCE_POWER_CAL_NOT_COMPLETE](../../../Support/PNA_Errors.md#10593)

594
[naEventID_SOURCE_POWER_CAL_REMOVE_TRACE](../../../Support/PNA_Errors.md#10594)

595
[naEventID_SOURCE_POWER_CAL_REMOVE_MEAS](../../../Support/PNA_Errors.md#10595)

596
[naEventID_SOURCE_POWER_CAL_POWER_CHANGED](../../../Support/PNA_Errors.md#10596)

598
[naEventID_INSUFFICIENT_SLIDE_MOVEMENT](../../../Support/PNA_Errors.md#10598)

613 [naEventID_CALSET_NOT_FOUND](../../../Support/PNA_Errors.md#10613)

615 [naEventID_CALSET_CREATED](../../../Support/PNA_Errors.md#10615)

617 [naEventID_CALSET_FILE_NOT_VALID](../../../Support/PNA_Errors.md#10617)

634 [naEventID_CALSET_LOAD_FAILED](../../../Support/PNA_Errors.md#10634)

635 [naEventID_CALSET_SAVE_FAILED](../../../Support/PNA_Errors.md#10635)

636 [naEventID_CALSET_DELETED](../../../Support/PNA_Errors.md#10636)

637
[naEventID_CALSET_FILE_NOT_COMPATIBLE](../../../Support/PNA_Errors.md#10637)

639 [naEventID_NEW_CALSET_FILE_CREATED](../../../Support/PNA_Errors.md#10639)

640 [naEventID_CAL_SET_IN_USE](../../../Support/PNA_Errors.md#10640)

644 [naEventID_CAL_COULD_NOT_TURN_ON](../../../Support/PNA_Errors.md#10644)

693
[naEventID_ERROR_FIXTURING_S2PFILE_CANNOT_OPEN](../../../Support/PNA_Errors.md#10693)

696
[naEventID_ERROR_FIXTURING_TURNED_OFF](../../../Support/PNA_Errors.md#10696)

701 [naEventID_MORE_THRU_PATHS_NEEDED](../../../Support/PNA_Errors.md#10701)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *

