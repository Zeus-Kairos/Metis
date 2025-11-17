##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiToneHarmonicRejection Property

* * *

#### Description

| Sets and returns the number of test signal harmonics you want to be
protected against. This adds constraints to the list of LOs used to cover the
span.  
---|---  
  
#### VB Syntax

| sa.coherence.MultiToneHarmonicRejection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Long)  Number of test signal harmonics to be protected. The more this number is increased, the more constraints are added on the span LOs setting.  
  
#### Return Type

| Long  
  
#### Default

| 0  
  
#### Examples

| sa.coherence.MultiToneHarmonicRejection = 0  'Write  
value = sa.coherence.MultiToneHarmonicRejection 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_MultiToneHarmonicRejection(long value); HRESULT
get_MultiToneHarmonicRejection(long* value);  
  
#### Interface

| ICoherenceSA  
  
* * *

