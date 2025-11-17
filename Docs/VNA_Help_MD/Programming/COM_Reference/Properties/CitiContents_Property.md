##### Write/Read

|

##### [About Citifiles](../../../S5_Output/SaveRecall.md#cti)  
  
---|---  
  
## CitiContents Property - Superseded

* * *

#### Description

|  This command is replaced with [SaveData
Method](../Methods/SaveData_Method.htm) Specifies the contents of subsequent
citifile saves using
app.[SaveCitiDataData](../Methods/SaveCitiDataData_Method.md) or
app.[SaveCitiFormattedData](../Methods/SaveCitiFormattedData_Method.md)  
---|---  
  
####  VB Syntax

|  pref.CitiContents = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (string) \- Contents that will be saved with subsequent save commands. Choose from: "Single" \- Single trace "Displayed" \- All displayed traces "Auto" \- All displayed traces  
  
#### Return Type

|  String  
  
#### Default

|  "Auto"  
  
#### Examples

|  pref.CitiContents = "Single" 'Write  
content = pref.CitiContents 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CitiContents(BSTR *Contents)  
HRESULT put_CitiContents(BSTR Contents)  
  
#### Interface

|  IPreferences

