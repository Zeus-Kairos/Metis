##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataLevelThreshold Property

* * *

#### Description

| Sets and returns the threshold value (dBm). For text file output with
verbose mode, only the frequencies with power greater than this threshold
setting will be written to the file. This command can be used as a kind of
simple spurious search.  
---|---  
  
#### VB Syntax

| sa.dft.DataLevelThreshold = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft | A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
  
#### Return Type

| Double  
  
#### Default

| -60 dBm  
  
#### Examples

| sa.dft.DataLevelThreshold = -5 dBm  'Write  
value = sa.dft.DataLevelThreshold 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_DataLevelThreshold(double threshold); HRESULT
get_DataLevelThreshold(double* threshold);  
  
#### Interface

| ISpectrumAnalyzerDFT2  
  
* * *

