# MMEMory:TDR Commands

These commands control the loading and storing of eye bit pattern and mask
files.

MMEMory:TDR LOAD | EYE | BPATtern | MASK | STATe STORe | EYE | BPATtern | MASK | FDATa | [ALL](TDR_Memory.md#MMEMoryTDRSTOReFDATaALL) | SNP | STATe  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## MMEMory:TDR:LOAD:EYE:BPATtern <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
loads the specified user bit pattern file. The extension of file should be
.txt. The bit pattern editing is not available through the command.  
---  
Parameters |   
<filename> |  File name of the user bit pattern (.txt)  
Examples |  MMEM:TDR:LOAD:EYE:BPAT "C:\TDR\mybitpattern.txt"  
mmemory:tdr:load:eye:bpattern "c:\tdr\mybitpattern.txt"  
Default |  Not Applicable  
  
* * *

## MMEMory:TDR:LOAD:EYE[:MASK] <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
loads [eye-mask
file](../../Applications/Enhanced_Time_Domain_Analysis/Eye_Diagram_and_Mask_Test/Available_Masks.htm).
The format of the eye mask file should be the same as the format of the
Infiniium DCA (86100C). The extension of the file should be .msk. The MASK
pattern editing is not available through the command.  
---  
Parameters |   
<filename> |  File name of the eye mask (.msk)  
Examples |  MMEM:TDR:LOAD:EYE:MASK "C:\TDR\FC0133.msk"  
mmemory:tdr:load:eye:mask "c:\tdr\FC0133.msk"  
Default |  Not Applicable  
  
* * *

## MMEMory:TDR:LOAD:STATe <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) Loads the
specified instrument state file (.tdr).  
---  
Parameters |   
<filename> |  String - Name of any valid file that does not already exist.  
Examples |  MMEM:TDR:LOAD:STAT 'myState' mmemory:tdr:load:state 'c:\tdr\myState.tdr'  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## MMEMory:TDR:STORe:EYE:BPATtern <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
stores the user bit pattern file. The extension of file should be .txt. The
bit pattern editing is not available through the command.  
---  
Parameters |   
<filename> |  File name of the user bit pattern (.txt)  
Examples |  MMEM:TDR:STOR:EYE:BPAT "C:\TDR\mybitpattern.txt"  
mmemory:tdr:store:eye:bpattern "c:\tdr\mybitpattern.txt"  
Default |  Not Applicable  
  
* * *

## MMEMory:TDR:STORe:EYE[:MASK] <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
stores the eye-mask file. The format of the eye mask file should be the same
as the format of the Infiniium DCA (86100C). The extension of the file should
be .msk. The MASK pattern editing is not available through the command.  
---  
Parameters |   
<filename> |  File name of the eye mask (.msk)  
Examples |  MMEM:TDR:STOR:EYE:MASK "C:\TDR\mymask.msk"  
mmemory:tdr:store:eye:mask "c:\tdr\mymask.msk"  
Default |  Not Applicable  
  
* * *

## MMEMory:TDR:STORe:FDATa <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) Stores the
specified measurement data file of the active trace.  
---  
Parameters |   
<filename> |  String - Name of any valid file that does not already exist.  
Examples |  MMEM:TDR:STOR:FDAT 'myFdata' mmemory:tdr:store:fdata 'c:\tdr\myFdata'  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## MMEMory:TDR:STORe:FDATa:ALL <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) Stores the
specified measurement data file for all traces.  
---  
Parameters |   
<filename> |  String - Name of any valid file that does not already exist.  
Examples |  MMEM:TDR:STOR:FDAT:ALL 'myFdata' mmemory:tdr:store:fdata:all 'c:\tdr\myFdata'  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## MMEMory:TDR:STORe:SNP <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) Stores the
SnP measurement data. [Learn more about SnP
data](../../S5_Output/SaveRecall.htm#An *.s3p).  
---  
Parameters |   
<filename> |  String - Name of any valid file that does not already exist.  
Examples |  MMEM:TDR:STOR:SNP 'mySnp.s4p' mmemory:tdr:store:snp 'mySnp.s2p'  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## MMEMory:TDR:STORe:STATe <filename>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) Stores the
specified instrument state file (.tdr).  
---  
Parameters |   
<filename> |  String - Name of any valid file that does not already exist.  
Examples |  MMEM:TDR:STOR:STAT 'myState' mmemory:tdr:store:state 'c:\tdr\myState.tdr'  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

##

