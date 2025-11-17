##### Write-only

|

##### [About Save/Recall](../../../S5_Output/SaveRecall.md)  
  
---|---  
  
## SaveData Method

* * *

#### Description

|  Stores trace data to the following file types: *.prn, *.cti, *.csv, *.mdf
To save snp files, use
[WriteSnpFileWithSpecifiedPorts](WriteSnpFileWithSpecifiedPorts_Method.md) To
save instrument state and calibration files, use [Save](Save_Method.md). This
command replaces the following: [SaveCitiDataData
Method](SaveCitiDataData_Method.htm) [SaveCitiFormattedData
Method](SaveCitiFormattedData_Method.htm) [CitiContents
Property](../Properties/CitiContents_Property.htm) [CitiFormat
Property](../Properties/CitiFormat_Property.htm) Some saved files can be
recalled using app.[Recall](Recall_Method.md). depending on the content.  
---|---  
  
####  VB Syntax

|  app.SaveData filename,type,scope,format,selector  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
filename |  (string) \- Full path, file name, and extension of the file. Files are typically stored in "D:\"  
all other parameters |  Choose from the following valid parameter combinations for ALL measurement classes: |  |  Parameters  
---|---  
Type of file to save Click to learn about these file types: |  <type>   
(String) |  <scope>   
(String) |  <format>  
(String) |  <selector>  
(Integer)  
[*.prn](../../../S5_Output/SaveRecall.md#prn) |  "PRN Trace Data" |  "Trace" |  "Displayed" |  Measurement number  
Example: app.SaveData "myData.prn","PRN Trace Data","Trace","Displayed",2  
[*.cti](../../../S5_Output/SaveRecall.md#cti) (unformatted) |  "Citifile Data Data" |  "Trace" or "Auto" |  "RI" |  Measurement number  
Example: app.SaveData "myData.cti","Citifile Data Data","AUTO","RI",3  
[*.cti](../../../S5_Output/SaveRecall.md#cti) (unformatted) |  "Citifile Data Data" |  "Displayed" |  "RI" |  -1  
Example: app.SaveData "myData.cti","Citifile Data Data","AUTO","RI",3  
[*.cti](../../../S5_Output/SaveRecall.md#cti) (formatted) |  "Citifile Formatted Data" |  "Trace" or "Auto" |  "RI" or "MA" or "DB" |  Measurement number  
Example: app.SaveData "myData.cti","Citifile Formatted Data","AUTO","MA",3  
[*.cti](../../../S5_Output/SaveRecall.md#cti) (formatted) |  "Citifile Formatted Data" |  "Displayed" |  "RI" or "MA" or "DB" or "Displayed" |  -1  
Example: app.SaveData "myData.cti","Citifile Formatted
Data","DISPLAYED","MA",-1  
[*.csv](../../../S5_Output/SaveRecall.md#csv) |  "CSV Formatted Data" |  "Trace" or "Auto" |  "RI" or "MA" or "DB" or "Displayed" |  Measurement number  
Example: app.SaveData "myData.csv","CSV Formatted Data","Trace","DB",3  
[*.csv](../../../S5_Output/SaveRecall.md#csv) |  "CSV Formatted Data" |  "Displayed" |  "RI" or "MA" or "DB" |  -1  
Example: app.SaveData "myData.csv","CSV Formatted Data","displayed","RI",-1  
[*.mdf](../../../S5_Output/SaveRecall.md#MDIF) |  "MDIF Data" |  "Trace" or "Auto" |  "RI" or "Displayed" |  Measurement number  
Example: app.SaveData "myData.mdf","MDIF Data","trace","displayed",1  
[*.mdf](../../../S5_Output/SaveRecall.md#MDIF) |  "MDIF Data" |  "Displayed" |  "RI" or "Displayed" |  -1  
Example: app.SaveData "myData.mdf","MDIF Data","displayed","displayed",-1  
Notes (for above file types) Use
[meas.Number](../Properties/Number_meas_Property.md) to read the measurement
number of a trace.

### Scope:

"Trace" \- specified measurement number only. **" Channel"** \- all
measurements that are in the channel in which the selected measurement reside
are saved. "Displayed" \- all displayed measurements. "Auto" \- for all
Standard Meas Class (S-parameter) channels:

  * When correction is OFF, saves the specified trace
  * When correction is ON, saves all corrected parameters associated with the calibrated ports in the Cal Set.

"Auto" \- for all other channels:

  * When correction is OFF or ON, saves the specified trace

  
The following parameter combinations save *.csv files in specific formats for
GCA and Swept IMD classes:  
|  Parameters  
|  <type>  
(String) |  <scope>  
(String) |  <format>  
(String) |  <selector>  
(Integer)  
GCA channels ONLY: [Learn more](../../../Applications/Gain_Compression_Application.md#Saving) |  "GCA Sweep Data" |  "Auto" |  "DB" |  GCA channel number  
Example: app.SaveData "myData.csv","GCA Sweep Data","Auto","db",1  
Swept IMD channels ONLY: [Learn more](../../../Applications/Swept_IMD.md#Saving) |  "IMD Sweep Data" |  "Auto" |  "DB" |  Swept IMD channel number  
Example: app.SaveData "myData.csv","IMD Sweep Data","Auto","db",1  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SaveData(BSTR File, BSTR Type, BSTR Scope, BSTR Format, Long
selector);  
  
#### Interface

|  IApplication18  
  
* * *

