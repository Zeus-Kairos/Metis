# Format Commands

* * *

Specifies the way that data will be transferred when moving large amounts of
data.

![](../../assets/images/Programming/format.gif)

Click on a keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## FORMat:BORDer <char>

Applicable Models: All (Read-Write) Set the byte order used for GPIB data
transfer. Some computers read data from the analyzer in the reverse order.
This command is only implemented if FORMAT:DATA is set to :REAL. If
FORMAT:DATA is set to :ASCII, the swapped command is ignored.  
---  
Parameters |   
<char> |  Choose from: NORMal \- Use when your controller is anything other than an IBM compatible computers. SWAPped - for IBM compatible computers. Note: Use NORMal if you are using VEE, LabView, or T&M Tool kit.  
Examples |  FORM:BORD SWAP  
format:border normal  
Query Syntax | 

     FORMat:BORDer?  
Return Type |  Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Normal  
  
* * *

## FORMat[:DATA] <char>

Applicable Models: All (Read-Write) Sets the data format for transferring
measurement data and frequency data.

  * To transfer measurement data, use [CALC:MEAS:DATA](Calculate/MeasureDATA.md).
  * To transfer Cal Set data, use [SENS:CORR:CSET:DATA](Sense/CorrCset.md#data)
  * To transfer Source Power correction data, use:
  * [SOURce:POWer:CORRection:COLLect:TABLe:DATA](SourceCorrection.md#tdata)
  * [SOURce:POWer:CORRection:COLLect:TABLe:FREQuency](SourceCorrection.md#RWfreq)
  * [SOURce:POWer:CORRection:DATA](SourceCorrection.md#corrdata)
  * To transfer FIFO buffer data, use [SYST:FIFO:DATA?](SystFIFO.md#data)

The following commands transfer frequency data. Use <REAL, 64>

  * [CALC:MEAS:DATA:SNP?](Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:SNP:PORTs)
  * [CALC:MEAS:X?](Calculate/MeasureX.md)
  * [SENS:X?](Sense/X-Axis.md)

Use FORMat:BORDer to change the byte order. Use NORMal when transferring a
binary block from LabView or Vee. For other programming languages, you may
need to SWAP the byte order.  
---  
Parameters |   
<char> |  In the VNA, measurement data is stored as 32 bit and frequencies stored as 64 bit. Therefore, use REAL,32 when getting data and REAL,64 when getting frequencies. That way you are guaranteed to avoid losing any precision as well as getting the maximum speed on the data transfer. Choose from:

  * REAL,32 \- (default value for REAL) Best for transferring large amounts of measurement data. Can cause rounding errors in frequency data.
  * REAL,64 \- Slower but has more significant digits than REAL,32. REQUIRED to accurately represent frequency data. See above list for commands which transfer frequency information.
  * ASCii,0 \- The easiest to implement, but very slow. Use when you have small amounts of data to transfer.

Note The REAL,32 and REAL,64 arguments transfer data in block format as
explained in [Transferring Measurement
Data](../Learning_about_GPIB/Getting_Data_from_the_Analyzer.htm).  
Examples |  FORM REAL,64  
format:data ascii  
Query Syntax |  FORMat:DATA?  
Return Type |  Character,Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ASCii,0 Syst:Preset does NOT reset this command. However, *RST does reset this command to ASCii,0  
  
* * *

