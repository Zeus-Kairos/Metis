# Route Command

* * *

[Learn about Frequency Offset](../../S1_Settings/Power_Level.md)

[SCPI Command Tree](SCPI_Command_Tree.md)

## ROUTe<cnum>:PATH:LOOP[:R1] <char>

Applicable Models: N522xB, N524xB (Read-Write) Throws internal switch to
reference receiver when the specified channel is measured. N523xA models do
NOT have the R1 reference receiver switch.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<char> |  Position of the switch. Choose from: INTernal \- bypass R1 Loop. Connects the port 1 source directly to the R1 receiver. EXTernal \- flow through R1 Loop. Allows direct access to the R1 receiver through the Reference 1 front-panel connectors.  
Examples |  ROUT:PATH:LOOP INT  
route2:path:loop:r1 external  
Query Syntax |  ROUTe<cnum>:PATH:LOOP:R1?  
Return Type |  Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  INTernal  
  
* * *

