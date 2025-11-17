# LXI Command

* * *

[SCPI Command Tree](SCPI_Command_Tree.md)

## LXI:IDENtify[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B (Read-Write) Sets and
returns the status of the LXI LAN status indicator on the [LAN Status
dialog](../../S0_Start/LXI_Compliance.htm).  
---  
Parameters |   
<bool> | Choose from: OFF or 0 \- Changes the LXI Status indicator to NORMAL and closes the dialog if it was opened by this command. ON or 1 \- Changes the LXI Status indicator to IDENTIFY and opens the dialog if it was not already open.  
Examples | LXI:IDEN 1  
lxi:identify:state off  
Query Syntax | LXI:IDENtify[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF

