# SpectrumAnalyzerDFT Object

* * *

### Description

Controls the Spectrum Analyzer Application Discrete Fourier Transform (DFT)
settings.

### Accessing the SpectrumAnalyzer object

CComPtr<ISpectrumAnalyzer4> SA; CComPtr<ISpectrumAnalyzerDFT> sadft;
SA->GetDFT(&sadft);  
---  
  
### Method

|

### Interface

### See History

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[AutoBandwidth](../Properties/AutoBandwidth_Property.md) | ISpectrumAnalyzerDFT | Sets default values for DFT bandwidth.  
[BandwidthNarrowMax](../Properties/BandwidthNarrowMax_Property.md) | ISpectrumAnalyzerDFT | Sets maximum value for narrow DFT bandwidth.  
[BandwidthNarrowMin](../Properties/BandwidthNarrowMin_Property.md) | ISpectrumAnalyzerDFT | Sets minimum value for narrow DFT bandwidth.  
[BandwidthWideMax](../Properties/BandwidthWideMax_Property.md) | ISpectrumAnalyzerDFT | Sets maximum value for wide DFT bandwidth.  
[BandwidthWideMin](../Properties/BandwidthWideMin_Property.md) | ISpectrumAnalyzerDFT | Sets minimum value for wide DFT bandwidth.  
[BinaryFileEnabled](../Properties/BinaryFileEnabled_Property.md) | ISpectrumAnalyzerDFT | Enables binary file output.  
[DataBinCount](../Properties/DataBinCount_Property.md) | ISpectrumAnalyzerDFT | Returns the number of DFT points processed across the total RF span.  
[DataByteSize](../Properties/DataByteSize_Property.md) | ISpectrumAnalyzerDFT | Returns the byte size.  
[DataByteSizeLOW](../Properties/DataByteSizeLSB_Property.md) | ISpectrumAnalyzerDFT | Returns the low part of the byte.  
[DataByteSizeHIGH](../Properties/DataByteSizeMSB_Property.md) | ISpectrumAnalyzerDFT | Returns the high part of the byte.  
[DataBytesPerBin](../Properties/DataBytesPerBin_Property.md) | ISpectrumAnalyzerDFT | Returns the number of bytes per bin.  
[DataExportMarkersEnabled](../Properties/DataExportMarkersEnabled_Property.md) | ISpectrumAnalyzerDFT2 | Enables/disables adding marker data to the text file (*.txt) output.   
[DataExportWindowingFactor](../Properties/DataExportWindowingFactor_Property.md) | ISpectrumAnalyzerDFT2 | Returns the windowing factor for band power computation.  
[DataFirstRFBin](../Properties/DataFirstRFBin_Property.md) | ISpectrumAnalyzerDFT | Returns the frequency of the first RF bin.  
[DataFormat](../Properties/DataFormat_Property.md) | ISpectrumAnalyzerDFT | Sets and returns the data format.  
[DataLevelThreshold](../Properties/DataLevelTreshold_Property.md) | ISpectrumAnalyzerDFT2 | Sets and returns the threshold value (dBm).  
[DataLevelThresholdEnabled](../Properties/DataLevelTresholdEnabled_Property.md) | ISpectrumAnalyzerDFT2 | Enables/disables data level threshold mode.  
[ExportReceiverCount](../Properties/ExportReceiverCount_Property.md) | ISpectrumAnalyzerDFT | Returns the number of exported receivers.  
[ExportReceiverList](../Properties/ExportReceiverList_Property.md) | ISpectrumAnalyzerDFT | Returns the currently exported receiver list.  
[ExportReceiverSetList](../Properties/ExportReceiverSetList_Property.md) | ISpectrumAnalyzerDFT | Sets and returns the list of exported receivers.  
[FIFOEnabled](../Properties/FIFOEnabled_Property.md) | ISpectrumAnalyzerDFT | Enables exporting data to the FIFO (First-IN, First-OUT) data buffer.  
[FileEraseEachSweep](../Properties/FileEraseEachSweep_Property.md) | ISpectrumAnalyzerDFT | Enables output data files to be erased after each sweep.  
[FilePrefix](../Properties/FilePrefix_Property.md) | ISpectrumAnalyzerDFT | Sets and returns the file name prefix and path of the data file.  
[FileVerboseEnabled](../Properties/FileVerboseEnabled_Property.md) | ISpectrumAnalyzerDFT | Enables output of data and frequency.  
[MemShareEnabled](../Properties/MemShareEnabled_Property.md) | ISpectrumAnalyzerDFT | Enables data to be output to shared memory.  
[MemShareName](../Properties/MemShareName_Property.md) | ISpectrumAnalyzerDFT | Assigns a specified name to the shared data.  
[RecordSize](../Properties/RecordSize_Property.md) | ISpectrumAnalyzerDFT | Returns the current DFT record size.  
[Resolution](../Properties/Resolution_Property.md) | ISpectrumAnalyzerDFT | Returns the DFT resolution.  
[TextFileEnabled](../Properties/TextFileEnabled_Property.md) | ISpectrumAnalyzerDFT | Enables text file output.  
[Type](../Properties/Type_Property.md) | ISpectrumAnalyzerDFT | Sets the DFT record size type.  
  
###  SpectrumAnalyzerDFT History

Interface | Introduced with VNA Rev:  
---|---  
ISpectrumAnalyzerDFT | 12.70 and 12.80  
ISpectrumAnalyzerDFT2 | 13.25

