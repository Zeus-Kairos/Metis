# SYSTem:FIFO Commands

* * *

The 4 GB FIFO data buffer is available with Option S93118A/B or Option
S930900A/B on the PNA. (See [VNA Configurations and
Options](../../Support/Configurations.htm).) These commands control data in
and out of FIFO data buffer. The FIFO can be emptied as it is being filled,
which means that the VNA can be used to acquire an infinite amount of data.

The data placed into the FIFO is the raw data after averaging and ratioing has
been applied, but prior to any calibration, formatting, or data analysis
functions.

SYSTem:FIFO [DATA](SystFIFO.md#data) | BYTe? | COUNt? | [CLEar](SystFIFO.md#clear) | [COUNT?](SystFIFO.md#DataCount) [[:STATe]](SystFIFO.md#state)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [FIFO and other Antenna Features](../../IFAccess/FIFO_and_other_Antenna_Features.md)

  * [Fast CW command](Sense/Sweep_SCPI.md#swpTypeFASTCW)

  * [FIFO Example Program](../GPIB_Example_Programs/Setup_FastCW_and_FIFO.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:FIFO:DATA? <dpoints>

Applicable Models: N522xB, N524xB (Read-only) Reads the next specified number
of data points from the FIFO buffer. Each data point is returned as a
real/imaginary pair. Data is cleared as it is read.  
---  
Parameters |   
<dPoints> | Number of data points to read. An error is returned if the amount of requested data is larger than the available data.  
Examples | SYST:FIFO:DATA? 1e6 system:fifo:data? 1e3  
Return Type | Use [FORMat:DATA](Format_SCPI.md#fd) to change the data type (<REAL,32>, <REAL,64> or <ASCii,0>). For best results, use REAL,32 Use [FORMat:BORDer](Format_SCPI.md#fb) to change the byte order. Use NORMal when transferring a binary block from LabView or Vee. For other programming languages, you may need to "SWAP" the byte order. Each data point is returned as a real/imaginary pair.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:FIFO:DATA:BYTe? <X>

Applicable Models: N522xB, N524xB (Read-only) Returns a specific number of
bytes to read.  
---  
Parameters |   
<X> | Number of bytes to read.  
Examples | SYST:FIFO:DATA:BYTe? 4096 system:fifo:data:byte? 4096  
Return Type | IEEE binary block  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:FIFO:DATA:BYTe:COUNt?

Applicable Models: N522xB, N524xB (Read-only) Returns a specific number of
bytes to read.  
---  
Parameters |   
Examples | SYST:FIFO:DATA:BYTe:COUNt? system:fifo:data:byte:count?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:FIFO:DATA:CLEar

Applicable Models: N522xB, N524xB (Write-only) Clears the data from the FIFO
buffer.  
---  
Parameters | None  
Examples | SYST:FIFO:DATA:CLE system:fifo:data:clear  
Return Type | None  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:FIFO:DATA:COUNt?

Applicable Models: N522xB, N524xB (Read-only) Returns the total number of data
points in the FIFO buffer.  
---  
Parameters | None  
Examples | SYST:FIFO:DATA:COUN? ' returns 5.07e6  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:FIFO[:STATe] <bool>

Applicable Models: N522xB, N524xB (Write-Read) Sets and returns the state of
data storage to the FIFO buffer. Syst:Preset or an instrument state recall
also ends storage to the FIFO buffer. The FIFO buffer is cleared when set to
OFF.  
---  
Parameters |   
<bool> | FIFO buffer state. Choose from: ON or 1 Data is stored in the FIFO buffer. OFF or 0 Data is NOT stored in the FIFO buffer.  
Examples | SYST:FIFO 1 system:fifo:state off  
Query Syntax | SYSTem:FIFO[:STATE]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 OFF  
  
* * *

