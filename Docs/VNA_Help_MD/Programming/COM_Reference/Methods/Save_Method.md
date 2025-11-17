##### Write-only

|

##### [About Save/Recall](../../../S5_Output/SaveRecall.md)  
  
---|---  
  
## Save Method

* * *

#### Description

| Saves the appropriate content to the hard drive depending on the extension
that is provided. Some saved files can be recalled using
app.[Recall](Recall_Method.md). depending on the content.  
---|---  
  
####  VB Syntax

| app.Save(filename.ext)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | An [Application](../Objects/Application_Object.md) (object)  
filename.ext | (string) \- Full path, file name, and extension of the file. Files are typically stored in "D:\" Use one of the following extensions:

  * .cst \- Saves both Instrument State and Cal Set reference - Recalls a calibrated measurement. (Recallable)
  * .sta \- Saves Instrument State only - recalls the instrument state without calibration. (Recallable)
  * .cal \- Calibration file  saves the active Cal Sets currently in use by any channel. Use this mode for archival purposes only. All Cal Sets are saved to a Cal Set data file. This mode provides a method of safeguarding calibration data. This data can be restored to the list of Cal Sets available in the instrument. (Recallable)
  * .csa \- Saves both instrument state AND actual calibration data, not a reference pointer to the Cal Set.
  * .prn \- Saves active trace in comma-separated format (not recallable)
  * .bmp \- Saves a Bitmap of the screen (not recallable)
  * .s1p \- Saves 1-port measurement data
  * .s2p \- Saves 2-port measurement data
  * .s3p \- Saves 3-port measurement data
  * .s4p \- Saves 4-port measurement data

  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| app.Save("C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\Newfolder\MyState.cst") 'Saves "mystate.cst" to the
specified folder  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT Save(BSTR bstrFile)  
  
#### Interface

| IApplication  
  
* * *

