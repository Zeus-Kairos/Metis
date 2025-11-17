##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataExportMarkersEnabled Property

* * *

#### Description

| Enables/disables adding marker data to the text file (*.txt) output.  
---|---  
  
####  VB Syntax

| sa.dft.DataExportMarkersEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft | A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value | (Boolean) Choose from: 0 - OFF \- Disable marker data to the file output. 1 - ON \- Enable marker data to the file output.  
  
#### Return Type

| Boolean  
  
#### Default

| OFF  
  
#### Examples

| sa.dft.DataExportMarkersEnabled = ON 'Write  
value = sa.dft.DataExportMarkersEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DataExportMarkersEnabled(VARIANT_BOOL* enable)  
HRESULT put_DataExportMarkersEnabled(VARIANT_BOOL enable)  
  
#### Interface

| ISpectrumAnalyzerDFT2  
  
* * *

