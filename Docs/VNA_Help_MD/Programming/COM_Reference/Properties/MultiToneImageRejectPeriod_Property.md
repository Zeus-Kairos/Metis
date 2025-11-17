##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiTonePeriod Property

* * *

#### Description

| Sets and returns the test signal repetition rate (in seconds). This value is
1/MultiToneImageRejectSpacing.  
---|---  
  
#### VB Syntax

| sa.coherence.MultiTonePeriod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Double)  Test signal repetition rate (in seconds)  
  
#### Return Type

| Double  
  
#### Default

| 1E6  
  
#### Examples

| sa.coherence.MultiTonePeriod = 1E6  'Write  
value = sa.coherence.MultiTonePeriod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_MultiTonePeriod(double freqval); HRESULT
get_MultiTonePeriod(double* freqval);  
  
#### Interface

| ICoherenceSA  
  
* * *

