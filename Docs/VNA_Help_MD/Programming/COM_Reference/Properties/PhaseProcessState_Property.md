##### Write/Read

|

##### [About Phase Coherent
Measurements](../../../S1_Settings/Phase_Coherent_Measurements.htm)  
  
---|---  
  
# PhaseProcessState Property

* * *

#### Description

| Enables/disables phase computing.  
---|---  
  
####  VB Syntax

| sa.coherence.PhaseProcessState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Boolean) Choose from: 0 - OFF \- Phase computing disabled. 1 - ON \- Phase computing enabled.  
  
#### Return Type

| Boolean  
  
#### Default

| OFF  
  
#### Examples

| sa.coherence.PhaseProcessState = ON 'Write  
value = sa.coherence.PhaseProcessState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PhaseProcessState(VARIANT_BOOL* enable)  
HRESULT put_PhaseProcessState(VARIANT_BOOL enable)  
  
#### Interface

| ICoherenceSA2  
  
* * *

