##### Write/Read

|

##### [About SnP files](../../../S5_Output/SaveRecall.md#An *.s3p)  
  
---|---  
  
## SnPFormat Property

* * *

#### Description

|  Specifies the format of .SnP files. Use either
app.[Save](../Methods/Save_Method.md) (saves data to file) or meas.[Get
SnpDataWithSpecifiedPorts](../Methods/Get_SnpDataWithSpecifiedPorts_Method.htm)
(reads data into variant array).  
---|---  
  
####  VB Syntax

|  pref.SnPFormat = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (string) \- Format of the .S1P, .S2P, .S3P, .S4P data. Choose from: "MA" \- Linear Magnitude / degrees "DB" \- Log Mag / degrees "RI" \- Real / Imaginary "Auto" \- Format in which the trace is already displayed. If other than Log Mag, Linear Magnitude, or Real/Imag, then the format will be in Real/Imag.  
  
#### Return Type

|  String  
  
#### Default

|  "Auto"  
  
#### Examples

|  pref.SnPFormat = "MA" 'Write  
format = pref.SnPFormat 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SnPFormat(BSTR *Format)  
HRESULT put_SnPFormat(BSTR Format)  
  
#### Interface

|  IPreferences  
  
* * *

  

* * *

