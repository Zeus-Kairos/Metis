##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiToneSpacing Property

* * *

#### Description

| Sets and returns the tone spacing of the multitone signal (in Hz). This
value is 1/MultiToneImageRejectPeriod.  
---|---  
  
#### VB Syntax

| sa.coherence.MultiToneSpacing = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Double)  Frequency spacing of multitone signal (in Hz)  
  
#### Return Type

| Double  
  
#### Default

| 1000000  
  
#### Examples

| sa.coherence.MultiToneSpacing = 1E6  'Write  
value = sa.coherence.MultiToneSpacing 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_MultiToneSpacing(double freqval); HRESULT
get_MultiToneSpacing(double* freqval);  
  
#### Interface

| ICoherenceSA  
  
* * *

