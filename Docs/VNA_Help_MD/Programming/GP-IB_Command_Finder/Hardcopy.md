# Hardcopy Command

* * *

Controls printing of the VNA screen and optional data to a printer or a file.

HCOPy: [DPRinter](Hardcopy.md#dPrinter) [FILE](Hardcopy.md#file) [[IMMediate]](Hardcopy.md#IMM) ITEM | [AWINdow](Hardcopy.md#Awindow) | [CTABle](Hardcopy.md#ctable) | [GPFail](Hardcopy.md#GPfail) | [LOGO](Hardcopy.md#logo) | [MKRData](Hardcopy.md#MkrData) | [PNUMber](Hardcopy.md#PNum) | [SEGData](Hardcopy.md#segData) | [SWINdow](Hardcopy.md#sWind) | [TIME](Hardcopy.md#time) | [TTABle](Hardcopy.md#tTable) | [WFRaction](Hardcopy.md#wFraction) | [WINDows](Hardcopy.md#windows) PAGE | DIMension | [LLEFt](Hardcopy.md#lLeft) | [URIGht](Hardcopy.md#uRight) | [ORIentation](Hardcopy.md#Orient) | [SIZE](Hardcopy.md#size) SDUMP | [DATA?](Hardcopy.md#sdump) | [FORMat](Hardcopy.md#SdumpFormat) [PRINters?](Hardcopy.md#printers)  
---  
  
Click on a keyword to view the command details.

Blue commands are superseded or obsolete.

******S** ee Also****

  * [Learn more about VNA Printing](../../S5_Output/Print.md)

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

* * *

## HCOPy:DPRinter <string>

Applicable Models: All (Read-Write) Sets the default printer and selects as
the current printer. Use [HCOPy:PRINters?](Hardcopy.md#printers) to return a
list of locally installed printers. This setting survives instrument preset
and VNA application restart.  
---  
Parameters |   
<string> | Name of the printer to become the default.  
Examples | HCOP:DPR "MyPrinter" hcopy:dprinter "YourPrinter"  
Query Syntax | HCOPy:DPRinter?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## HCOPy:FILE <filename>

Applicable Models: All (Write-only) Saves the screen image to a file. The
image does NOT include the optional print data invoked by many HCOPy commands.  
---  
Parameters |   
<filename> | Name of the file to save the screen to. The file is saved to the current working directory unless a valid full path name is specified. Use one of the following suffixes: .bmp - not recommended due to large file size .jpg - not recommended due to poor quality .png - recommended  
Examples | HCOPY:FILE "myFile.png" hcopy:file "c:/data/myfile.png"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## HCOPy[:IMMediate]

Applicable Models: All (Write-only) Prints the screen to the default printer.  
---  
Examples | HCOP  
hcopy:immediate  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## HCOPy:ITEM:AWINdow[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints only the Active window.
When OFF, prints all windows. This setting survives instrument preset and VNA
application restart.  
---  
Parameters |   
<bool> | Active window state. Chose from: OFF or (0) - Print ALL windows. ON or (1) - Print Active window only.  
Examples | HCOP:ITEM:AWIN 1 hcopy:item:awindow:state off  
Query Syntax | HCOPy:ITEM:AWINdow[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:CTABle[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints the channel settings
table. This setting survives instrument preset and VNA application restart.  
---  
Parameters |   
<bool> | Channel table print state. Chose from: OFF or (0) - Does NOT print the channel settings table. ON or (1) - Prints channel settings table.  
Examples | HCOP:ITEM:CTAB 1 hcopy:item:ctable:state off  
Query Syntax | HCOPy:ITEM:CTABle[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:GPFail[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints the [Global
Pass/Fail](../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag) status
in the page header. This setting survives instrument preset and VNA
application restart.  
---  
Parameters |   
<bool> | Pass / Fail print state. Chose from: OFF or (0) - Does NOT print Pass / Fail status. ON or (1) - Print Pass / Fail status  
Examples | HCOP:ITEM:GPF 1 hcopy:item:gpfail:state off  
Query Syntax | HCOPy:ITEM:GPFail[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:LOGO[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints the Keysight Technologies
logo in the page header. This setting survives instrument preset and VNA
application restart.  
---  
Parameters |   
<bool> | Keysight logo print state. Chose from: OFF or (0) - Prints the Keysight logo. ON or (1) - Does NOT print the Keysight logo.  
Examples | HCOP:ITEM:LOGO 1 hcopy:item:logo:state off  
Query Syntax | HCOPy:ITEM:LOGO[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:MKRData[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, includes marker data as part of
the [trace attributes table](Hardcopy.md#tTable). To print marker data,
[HCOP:ITEM:TTABle](Hardcopy.md#tTable) must also be set to ON. This setting
does not affect the limited [marker readout
data](../../S4_Collect/Markers.htm#DisplayDiag) that can be displayed in the
measurement window. This setting survives instrument preset and VNA
application restart.  
---  
Parameters |   
<bool> | Marker data print state. Chose from: OFF or (0) - Does NOT print Marker data. ON or (1) - Print Marker data.  
Examples | HCOP:ITEM:MKRD 1 hcopy:item:mkrdata:state off  
Query Syntax | HCOPy:ITEM:MKRData[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:PNUMber[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints page numbers (1 of n) in
the header at the top of each page. This setting survives instrument preset
and VNA application restart.  
---  
Parameters |   
<bool> | Page number print state. Chose from: OFF or (0) - Does NOT print page numbers. ON or (1) - Print page numbers.  
Examples | HCOP:ITEM:PNUM 1 hcopy:item:pnumber:state off  
Query Syntax | HCOPy:ITEM:PNUMber[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:SEGData[:STATe] <bool> \- Obsolete

Note: This command no longer works beginning with A.09.40 (Read-Write) When
ON, includes ALL segment data as part of the [channel settings
table](Hardcopy.htm#ctable). To print ALL segment data,
[HCOP:ITEM:CTAB](Hardcopy.md#ctable) must also be set to ON. This setting
survives instrument preset and VNA application restart.  
---  
Parameters |   
<bool> | Expanded segment data print state. Chose from: OFF or (0) - Does NOT print expanded segment data, but summary data is printed. ON or (1) - Print expanded segment data.  
Examples | HCOP:ITEM:SEGD 1 hcopy:item:segdata:state off  
Query Syntax | HCOPy:ITEM:SEGData[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:SWINdow[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints a single measurement
window per page. When OFF, prints up to four measurement windows per page.
This setting survives instrument preset and VNA application restart.  
---  
Parameters |   
<bool> | Single window print state. Chose from: OFF or (0) - Print up to four windows per page. ON or (1) - Print only one window per page.  
Examples | HCOP:ITEM:SWIN 1 hcopy:item:swindow:state off  
Query Syntax | HCOPy:ITEM:SWINdow[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:TIME[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints the VNA computer date and
time in the header. This setting survives instrument preset and VNA
application restart.  
---  
Parameters |   
<bool> | Time stamp print state. Chose from: OFF or (0) - Does NOT print time stamp. ON or (1) - Print time stamp.  
Examples | HCOP:ITEM:TIME 1 hcopy:item:time:state off  
Query Syntax | HCOPy:ITEM:TIME:[STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:TTABle[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints the trace attributes
table. This setting survives instrument preset and VNA application restart.  
---  
Parameters |   
<bool> | Trace attributes table print state. Chose from: OFF or (0) - Does NOT print the trace attributes table. ON or (1) - Print the trace attributes table.  
Examples | HCOP:ITEM:TTABle 1 hcopy:item:ttable:state off  
Query Syntax | HCOPy:ITEM:TTABle[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:ITEM:WFRaction <value>

Applicable Models: All (Read-Write) Sets the vertical amount of a page that is
filled by the measurement windows. This setting survives instrument preset and
VNA application restart.  
---  
Parameters |   
<value> | Window size as a fraction of the page. Chose a value from .4 (40%) to 1.0 (100%)  
Examples | HCOP:ITEM:WFR .8 hcopy:item:wfraction .5  
Query Syntax | HCOPy:ITEM:WFRaction?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .4  
  
* * *

## HCOPy:ITEM:WINDows[:STATe] <bool>

Applicable Models: All (Read-Write) When ON, prints measurement windows. Use
[HCOPy:ITEM:AWINdow](Hardcopy.md#Awindow) to specify all windows or only the
active window. This setting survives instrument preset and VNA application
restart.  
---  
Parameters |   
<bool> | Windows print state. Chose from: OFF or (0) - Does not print measurement windows. ON or (1) - Print measurement windows.  
Examples | HCOP:ITEM:WIND 1 hcopy:item:windows:state off  
Query Syntax | HCOPy:ITEM:WINDows[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## HCOPy:PAGE:DIMensions:LLEFt <left, lower>

Applicable Models: All (Read-Write) Sets the left and lower page margins. This
setting survives instrument preset and VNA application restart.  
---  
Parameters |   
<left> | Left page margin as a percentage of entire page width. Value must be between 0 and 1.  
<lower> | Lower page margin as a percentage of entire page length. Value must be between 0 and 1.  
Examples | HCOP:PAGE:DIM:LLEF .10,.10 hcopy:page:dimensions:lleft .5,.7  
Query Syntax | HCOPy:PAGE:DIMensions:LLEFt?  
Return Type | Numeric, Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depends on selected page size  
  
* * *

## HCOPy:PAGE:DIMensions:URIGht <right, upper>

Applicable Models: All (Read-Write) Sets the right and upper page margins.
This setting survives instrument preset and VNA application restart.  
---  
Parameters |   
<right> | Right page margin as a percentage of entire page width. Value must be between 0 and 1.  
<upper> | Upper page margin as a percentage of entire page length. Value must be between 0 and 1.  
Examples | HCOP:PAGE:DIM:URIG .10,.10 hcopy:page:dimensions:uright .5,.7  
Query Syntax | HCOPy:PAGE:DIMensions:URIGht?  
Return Type | Numeric, Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depends on selected page size  
  
* * *

## HCOPy:PAGE:ORIentation <char>

Applicable Models: All (Read-Write) Sets the page orientation. This setting
survives instrument preset and VNA application restart.  
---  
Parameters |   
<char> | Choose from:

  * PORTrait
  * LANDscape

  
Examples | HCOP:PAGE:ORI PORT hcopy:page:orientation landscape  
Query Syntax | HCOPy:PAGE:ORIentation?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | PORTrait  
  
* * *

## HCOPy:PAGE:SIZE <int>

Applicable Models: (Read-Write) Sets the paper type, which implies the page
size. This setting survives instrument preset and VNA application restart.  
---  
Parameters |   
<int> | Choose from:I | Integer | Description  
---|---  
1 | Letter 8 1/2 x 11 in  
2 | Letter Small 8 1/2 x 11 in  
3 | Tabloid 11 x 17 in  
4 | Ledger 17 x 11 in  
5 | Legal 8 1/2 x 14 in  
6 | Statement 5 1/2 x 8 1/2 in  
7 | Executive 7 1/4 x 10 1/2 in  
8 | A3 297 x 420 mm  
9 | A4 210 x 297 mm  
10 | A4 Small 210 x 297 mm  
11 | A5 148 x 210 mm  
12 | B4 (JIS) 250 x 354  
13 | B5 (JIS) 182 x 257 mm  
  
For more paper type choices, see Microsoft's "wingdi.h" file, which can be
downloaded as part of the Platform SDK.  
  
Examples | HCOP:PAGE:SIZE 2 hcopy:page:size 5  
Query Syntax | HCOPy:PAGE:SIZE?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## HCOPy:SDUMp:DATA?

Applicable Models: All (Read-only) Returns the display image in a definite-
length arbitrary binary block. The format of the data is PNG by default. Use
[HCOP:SDUMp:DATA:FORMat](Hardcopy.md#SdumpFormat) to change the format. This
command is equivalent to saving an image to the VNA
([HCOPy:FILE](Hardcopy.md#file)) and then using
[MMEM:TRAN](Memory.md#Transfer) to transfer the file to the computer.  
---  
Examples | HCOP:SDUM? hcopy:sdump?  
Return Type | A definite-length arbitrary binary block  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## HCOPy:SDUMp:DATA:FORMat <char>

Applicable Models: All (Read-Write) Sets the graphic format for
[HCOPy:SDUMp:DATA?](Hardcopy.md#SdumpFormat)  
---  
Parameters |   
<char> | Choose from: JPG | BMP | PNG  
Examples | HCOP:SDUMp:DATA:FORMat BMP  
Query Syntax | HCOPy:SDUMp:DATA:FORMat?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | PNG  
  
* * *

## HCOPy:PRINters?

Applicable Models: All (Read-only) Returns a comma-separated list of printers
installed on the VNA. Select a printer using
[HCOPy:DPRinter](Hardcopy.md#dPrinter). This setting survives instrument
preset and VNA application restart.  
---  
Examples | HCOP:PRIN? hcopy:printers?  
Query Syntax | HCOPy:PRINters?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

