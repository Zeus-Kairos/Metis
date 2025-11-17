##### Write/Read

|

##### [About Citifiles](../../../S5_Output/SaveRecall.md#cti)  
  
---|---  
  
## CitiFormat Property - Superseded

* * *

#### Description

|  This command is replaced with [SaveData
Method](../Methods/SaveData_Method.htm) Specifies the format of subsequent
citifile saves using
app.[SaveCitiFormattedData](../Methods/SaveCitiFormattedData_Method.md)  
---|---  
  
####  VB Syntax

|  pref.CitiFormat = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (string) \- Format in which the citifile will be saved with subsequent save commands. Choose from: "MA" \- Linear Magnitude / degrees "DB" \- Log Mag / degrees "RI" \- Real / Imaginary "Auto" \- Format in which the trace is already displayed. If other than Log Mag, Linear Magnitude, or Real/Imag, then the format will be in Real/Imag.  
  
#### Return Type

|  String  
  
#### Default

|  "Auto"  
  
#### Examples

|  pref.CitiFormat = "MA" 'Write  
format = pref.CitiFormat 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CitiFormat(BSTR *Format)  
HRESULT put_CitiFormat(BSTR Format)  
  
#### Interface

|  IPreferences

