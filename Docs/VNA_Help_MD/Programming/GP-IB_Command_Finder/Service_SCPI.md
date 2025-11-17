# Service Commands

* * *

Controls and queries settings related with Service.

SERVice: :DUMMy:DUT:FILE :DUMMy:DUT:NOISe:STATe  
:LOGGing:CLEAR  
---  
  
## SERVice:DUMMy:DUT:FILE <string> \- Superseded

Applicable Models: ALL

(Read-Write) Set/get trace sNp file for dummy DUT. Preset & Save/Recall does
not work for this command.  This command is replaced by
[SYST:SIM:DUT:FILE](System.md#SimDutFil)  
---  
Parameters | <string> sNp file to be set to dummy DUT  
Examples | SERV:DUMM:DUT:FILE?  
service:dummy:dut:file?  
Return Type | string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SERVice:DUMMy:DUT:NOISe:STATe <bool> \- Superseded

Applicable Models: ALL

(Read-Write) Set/get trace noise state for dummy DUT Preset & Save/Recall does
not work for this command This command is replaced by
[SYST:SIM:DUT:NOIS](System.md#SimDutNois)  
---  
Parameters | <bool> Noise state.  
Examples | SERV:DUMM:DUT:NOIS:STAT?  
service:dummy:dut:noise:state?  
Return Type | bool  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SERVice:LOGGing:CLEar

Applicable Models: E5080A/B, M9485A, M98xxA, P50xxA/B

(Write-only) Delete the service error log files stored in the modules and PC.
See [Error Log](../../Support/Tshoot.md#Error_Log).  
---  
Parameters |   
Examples | SERV:LOGG:CLE  
service:logging:clear  
Return Type | N/A  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

