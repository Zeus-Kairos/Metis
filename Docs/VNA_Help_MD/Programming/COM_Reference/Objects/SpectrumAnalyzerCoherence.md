# SpectrumAnalyzerCoherence

### Description

Controls the Spectrum Analyzer Application Coherence and modulation distortion
settings.

### Accessing the SpectrumAnalyzerCoherence object

CComPtr<ISpectrumAnalyzer4> SA; CComPtr<ICoherenceSA> sacoherence;
SA->GetCoherence(&sacoherence);  
---  
  
### Method

|

### Interface

### See History

|

### Description  
  
---|---|---  
|  |   
  
### Property

|

### Interface

|

### Description  
  
[MultiToneDataDisplay](../Properties/MultiToneImageRejectDataDisplay_Property.md) |  ICoherenceSA |  Sets and returns the data display mode.  
[MultiToneEnable](../Properties/MultiToneImageRejectEnable_Property.md) |  ICoherenceSA |  Enables/disables multitone image rejection.  
[MultiToneHarmonicRejection](../Properties/MultiToneImageRejectHarmonic_Property.md) |  ICoherenceSA |  Sets and returns the multitone harmonic rejection.  
[MultiToneNyquistProtection](../Properties/MultiToneNyquistProtection_Property.md) |  ICoherenceSA2 |  Sets and returns the Nyquist protection level.  
[MultiTonePeriod](../Properties/MultiToneImageRejectPeriod_Property.md) |  ICoherenceSA |  Sets and returns the multitone image rejection period.  
[MultiToneReference](../Properties/MultiToneImageRejectReference_Property.md) |  ICoherenceSA |  Sets and returns the multitone image rejection offset frequency.  
[MultiToneSettingsValid](../Properties/MultitoneSettingsValid_Property.md) |  ICoherenceSA2 |  Returns the current multitone settings and determine if they are valid or not.  
[MultiToneSpacing](../Properties/MultiToneImageRejectSpacing_Property.md) |  ICoherenceSA |  Sets and returns the tone spacing of the multitone signal.  
[PhaseDisplayMinLevel](../Properties/PhaseDisplayMinLevel_Property.md) |  ICoherenceSA2 |  Sets and returns the phase display minimum level.  
[PhaseProcessState](../Properties/PhaseProcessState_Property.md) |  ICoherenceSA2 |  Enables/disables phase computing.  
[VectorAverageEnable](../Properties/VectorAverageEnable_Property.md) |  ICoherenceSA |  Sets and returns the ON/OFF state of the vector averaging.  
[VectorAverageValue](../Properties/VectorAverageValue_Property.md) |  ICoherenceSA |  Sets and returns the vector averaging value.  
[VectorAverageValueMax](../Properties/VectorAverageMax.md) |  ICoherenceSA |  Returns the current maximum available vector averaging value.  
  
###  SpectrumAnalyzerCoherence History

Interface |  Introduced with VNA Rev:  
---|---  
ICoherenceSA |  12.80  
ICoherenceSA2 |  12.90

