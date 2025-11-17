# CALCulate<cnum>:DTOPology <device>,<topology>

Applicable Models: Multi-port systems with > 4 ports (Read-Write) Maps the
physical VNA ports to a device of balanced and single-ended logical ports for
multi-port systems with greater than 4 ports. The device type is selected
using [CALCulate:FSIMulator:BALun:DEVice](FSimulatorBalun.md#DevType). See
Also:
[CALC:FSIM:BAL:PAR:CAT?](FSimulatorBalun.md#CALCulate:FSIMulator:BALun:PARameter:CATalog)
\- returns the list of measurement parameters available for the currently
selected topology.
[CALC:FSIM:BAL:PAR:CUST:DEFine](FSimulatorBalun.md#CALCulate:FSIMulator:BALun:PARameter:CUSTom:DEFine)
and [CALC:MEAS:PAR](MeasurePARameter.md) \- defines measurement parameter
corresponding to a custom topology for systems where the port count is
expandable beyond 4 ports.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<device> | (String) Device type for the balanced measurement. B means the Balanced port; S means the Single-ended port. Choose from: B  1 port balanced device (2 ports) BB  Balanced - Balanced device (4 ports) BS  Balanced - Single-ended device (3 ports) BSS  Balanced - Single-ended - Single-ended device (3 ports) SB  Single-ended - Balanced device (3 ports) SSB  Single-ended - Single-ended - Balanced device (4 ports)  
<topology> | (Int array) Physical port numbers mapped to the logical ports, separated by ,. B (Balanced) requires 2 physical port numbers: <nPos>, <nNeg>. S (Single-ended) requires 1 physical port number.  
Examples | 'The following example sets up 6 physical ports into 5 logical ports:  
'Logical port 1 is a single ended port mapped to physical port 1  
'Logical port 2 is a single ended port mapped to physical port 2  
'Logical port 3 is a balanced port mapped to physical ports 4 and 5  
'Logical port 4 is a single ended port mapped to physical port 3  
'Logical port 5 is a single ended port mapped to physical port 6  
'Example 1 CALC:FSIM:BAL:DEV CUST  
CALC:DTOP "SSBSS",1,2,4,5,3,6  
CALC:MEAS:PAR "SDD33" 'Example 2 CALC:PAR:COUN 1  
CALC:FSIM:BAL:DEV CUST  
CALC:FSIM:BAL:PAR:STATE ON  
CALC:DTOPology "SSBSS",1,2,4,5,3,6  
CALC:FSIM:BAL:PAR:CUST:DEF "SDD33"  
Query Syntax | CALCulate<cnum>:DTOPology <device>,<topology>?  
Return Type | Int array  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable

