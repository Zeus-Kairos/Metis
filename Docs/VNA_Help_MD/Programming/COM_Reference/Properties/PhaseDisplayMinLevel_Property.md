##### Write/Read

|

##### [About Phase Coherent
Measurements](../../../S1_Settings/Phase_Coherent_Measurements.htm)  
  
---|---  
  
# PhaseDisplayMinLevel Property

* * *

#### Description

| Set and read the phase display minimum level.  
---|---  
  
#### VB Syntax

| sa.coherence.PhaseDisplayMinLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Double) Phase display minimum level (in dBm).  
  
#### Return Type

| Double  
  
#### Default

| -50 dBm  
  
#### Examples

| sa.coherence.PhaseDisplayMinLevel = -50 dBm  Write  
value = sa.coherence.PhaseDisplayMinLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_PhaseDisplayMinLevel(double level); HRESULT
get_PhaseDisplayMinLevel(double* levell);  
  
#### Interface

| ICoherenceSA2  
  
* * *

