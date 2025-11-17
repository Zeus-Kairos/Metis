##### Write-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# ImportCSVfile Method

* * *

#### Description

| Imports segment data to a CSV file.  
---|---  
  
####  VB Syntax

| segs.ImportCSVfile(bstrFile)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
bstrFile | (string) \- Full path, file name, and extension of the file.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| segs.ImportCSVfile("D:\MyFile.csv") 'Imports "myfile.csv"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT ImportCSVfile(BSTR bstrFile)  
  
#### Interface

| ISegments6

