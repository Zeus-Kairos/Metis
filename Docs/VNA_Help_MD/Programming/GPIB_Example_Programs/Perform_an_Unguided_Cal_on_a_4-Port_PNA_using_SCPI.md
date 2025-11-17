# Perform an Unguided Cal on a 4-Port VNA

* * *

This topic describes how to perform an unguided calibration on a multiport
network analyzer using SCPI. The objective here is to make clear the
relationship between the physical port on which a standard is being measured,
the actual device in the cal kit, and the SCPI command used to acquire the
device.

There are two sets of SCPI commands that acquire calibrations. One set is used
for guided cal, the other for unguided. The SCPI commands that provide remote
access to unguided cal are in the SENS:CORR:COLL block:

  * SENS:CORR:COLL:METHod

  * SENS:CORR:COLL:ACQuire

  * SENS:CORR:COLL:SAVE

On a four port network analyzer, the remote programmer needs to be aware of
the relationship between the physical port and the calibration kit class
assignments. The example program (below) illustrates the usage by performing
three unique 2 port cals, taking care to acquire the appropriate standards.

Calibration standards classes are categories of standard types. To perform a
2 port calibration, the cal wizard requires the user to measure:

3 reflection standards on the forward port:

  * Class S11A typically an open

  * Class S11B typically a short

  * Class S11C typically a load

Likewise, 3 reflection standards are required for the reverse port:

  * Class S22A typically an open

  * Class S22B typically a short

  * Class S22C typically a load

There is also a transmission standard that is measured in both directions:

  * Class S21T typically a thru

The following illustrates the relationship between cal kit physical standards
and calibration classes.

Here is a list of the physical devices in my calibration kit.

Standard #1 = "3.5 mm male short"

Standard #2 = "3.5 mm male open"

Standard #3 = "3.5 mm male broadband load"

Standard #4 = "Insertable thru standard"

Standard #5 = "3.5 mm male sliding load"

Standard #6 = "3.5 mm male lowband load"

Standard #7 = "3.5 mm female short"

Standard #8 = "female to female characterized thru adapter"

Standard #9 = "0-2 Load"

Standard #10 = "Open"

Standard #11 = "Non-insertable thru"

Standard #12 = "3.5 mm female lowband load"

Standard #13 = "3.5 mm female sliding load"

Standard #14 = "3.5 mm female broadband load"

Standard #15 = "3.5 mm female open"

When you perform a calibration remotely using SCPI, you dont specify the
device number directly. Rather, you specify the class you want to measure.
Each device in the calibration kit is assigned to a class. And since more than
one device can be assigned to the same class, each class contains an ordered
list of devices. The class assignments are user-settable using the Advanced
Modify Cal Kit dialog or the SCPI command:

[SENS:CORR:COLL:CKIT:ORDer](../GP-
IB_Command_Finder/Sense/CorrCollCKIT.htm#sccco)<class>, <std>, <std>, <std>,
<std>,<std>,<std>,<std>

The 85052B kit used in the example program had the following standard list for
each class: The list was obtained by issuing the corresponding SCPI query:

[SENS:CORR:COLL:CKIT:OLIST1?](../GP-
IB_Command_Finder/Sense/CorrCollCKIT.htm#olist) S11A = +2,+15,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST2? S11B = +1,+7,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST3? S11C = +6,+5,+3,+12,+13,+14,+0

SENS:CORR:COLL:CKIT:OLIST4? S21T = +4,+8,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST5? S22A = +2,+15,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST6? S22B = +1,+7,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST7? S22C = +6,+5,+3,+12,+13,+14,+0

SENS:CORR:COLL:CKIT:OLIST8? S12T = +4,+8,+0,+0,+0,+0,+0

When you perform the calibration, you acquire data by issuing the ACQuire
command:

[SENS:CORR:COLL:ACQ <class>[, <subst> ]](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#scca)

For example:

[SENS:CORR:COLL:SFOR](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#sforward) 1

SENS:CORR:COLL:ACQ STANA, SST2

The SFOR command tells the wizard to make the next acquisition in the forward
direction. The ACQuire command specifies that we are measuring the 2nd device
in the list for STANA. And since we are measuring SFORward, STANA refers to
class #1 or S11A. The list of devices for this class are specified in the
OLIST1 query above. The associations are shown in red.

Alternately, you could modify the device order for the S11A class to move
device #15 into the first position (SENS:CORR:COLL:CKIT:ORDER1). When the
desired device is in the first position, you neednt specify the order number
in the ACQuire command. The default is the first device in the OLIST. This
worked well for two port network analyzers where the order for S11A,B,C
classes were setup for port 1 and the order for S22A,B,C was set up for port
2. With the kit setup in the proper order, you could eliminate the
specification of the substandard number (SST<n>).

When performing 2 port calibrations on 4 Port Network Analyzers, the wizard
applies S11A,B,C standards to the lower numbered port, S22A,B,C standards to
the higher numbered port. Since the two classes (S11A,B,C and S22A,B,C) are
applied to multiple ports, the programmer must take into account the ports
being measured and take greater care when specifying the ACQuire command to
ensure that the correct device is being measured.

Port to class relationship

Ports |  S11A Port |  S22A Port  
---|---|---  
1,2 |  1 |  2  
1,3 |  1 |  3  
1,4 |  1 |  4  
2,3 |  2 |  3  
2,4 |  2 |  4  
3,4 |  3 |  4  
  
The following example program shows one method of handling two port cals on a
multiport network analyzer. The connectors at the measurement plane are
assumed to be (1) male, (2) female, (3) male, and (4) male. In the example,
three cals are performed: 1-2 (insertable male to female), 2-3 (insertable
female to male), and 3-4 (noninsertable using an characterized adapter).

option explicit  
public scpi  
public pna  
' assume a 4 port VNA with the following connectors:  
' the standard measured on these ports will be the opposite gender  
' PORT 1 = 3.5 male  
' PORT 2 = 3.5 female  
' PORT 3 = 3.5 male  
' PORT 4 = 3.5 male  
'To perform 2 port calibrations between 1-2, 2-3, and 3-4 you need to do the
following  
  
call main  
  
sub main  
set pna = CreateObject("AgilentPnA835x.Application")  
set scpi = pna.ScpiStringParser  
pna.Preset  
' select a kit to use for this demonstration  
' kit #1 for the N5230A is the 85052B 3.5mm kit with sliding load  
scpi.execute("SENS:CORR:COLL:CKIT:SELECT 1" )  
PrintKitStandardInfo 1  
PrintKitOlist 1  
  
' \--------------------------------------------  
' CALIBRATE PORTS 1 and 2, insertable cal  
' \--------------------------------------------  
wscript.echo  
wscript.echo "Calibrating ports 1 and 2"  
scpi.execute("SYST:PRES;")  
scpi.execute("calc:par:sel CH1_S11_1")  
scpi.execute("SENS:CORR:TST:STATE 0")  
scpi.execute("SENS:CORR:COLL:METHod SPARSOLT")  
scpi.execute("SENS:CORR:SFOR 1")  
MeasureFemaleStandards 1  
scpi.execute("SENS:CORR:SFOR 0")  
MeasureMaleStandards 2  
MeasureTransmissionStandards 1,2  
scpi.execute("SENS:CORR:COLL:SAVE")  
  
' \--------------------------------------------  
' CALIBRATE PORTS 2 and 3, insertable cal  
' \--------------------------------------------  
wscript.echo  
wscript.echo "Calibrating ports 2 and 3"  
scpi.execute("SYST:PRES;")  
scpi.execute("calc:par:sel CH1_S11_1")  
scpi.execute("calc:par:mod S23")  
scpi.execute("SENS:CORR:TST:STATE 0")  
scpi.execute("SENS:CORR:COLL:METHod SPARSOLT")  
scpi.execute("SENS:CORR:SFOR 1")  
MeasureMaleStandards 2  
scpi.execute("SENS:CORR:SFOR 0")  
MeasureFemaleStandards 3  
MeasureTransmissionStandards 2,3  
scpi.execute("SENS:CORR:COLL:SAVE")  
  
' \--------------------------------------------  
' CALIBRATE PORTS 3 and 4, non-insertable cal  
' \--------------------------------------------  
wscript.echo  
wscript.echo "Calibrating ports 3 and 4"  
scpi.execute("SYST:PRES;")  
scpi.execute("calc:par:sel CH1_S11_1")  
scpi.execute("calc:par:mod S43")  
scpi.execute("SENS:CORR:COLL:METHod SPARSOLT")  
scpi.execute("SENS:CORR:SFOR 1")  
MeasureFemaleStandards 3  
scpi.execute("SENS:CORR:SFOR 0")  
MeasureFemaleStandards 4  
MeasureAdapter 3, 4  
scpi.execute("SENS:CORR:COLL:SAVE")  
end sub  
  
sub MeasureMaleStandards ( portNumber )  
dim portstr  
portstr = formatnumber(portNumber,0)  
Promptconnect1 1, 1, portNumber  
scpi.execute("SENS:CORR:COLL:ACQ STAN1;*OPC?")  
  
Promptconnect1 2, 1, portNumber  
scpi.execute("SENS:CORR:COLL:ACQ STAN2;*OPC?")  
Promptconnect1 3, 3, portNumber  
scpi.execute("SENS:CORR:COLL:ACQ STAN3,SST3;*OPC?")  
end sub  
  
sub MeasureFemaleStandards (portNumber)  
dim portstr  
portstr = formatnumber(portNumber,0)  
Promptconnect1 1, 2, portNumber  
scpi.execute("SENS:CORR:COLL:ACQ STAN1,SST2;*OPC?")  
Promptconnect1 2, 2, portNumber  
scpi.execute("SENS:CORR:COLL:ACQ STAN2,SST2;*OPC?")  
Promptconnect1 3, 6, portNumber  
scpi.execute("SENS:CORR:COLL:ACQ STAN3,SST6;*OPC?")  
end sub  
  
sub MeasureTransmissionStandards( port1, port2)  
dim p1str  
dim p2str  
p1str = formatnumber( port1, 0)  
p2str = formatnumber( port2, 0)  
  
Promptconnect2 4, 1, port1, port2  
scpi.execute("SENS:CORR:COLL:ACQ STAN4;*OPC?")  
end sub  
  
sub MeasureAdapter( port1, port2)  
dim p1str  
dim p2str  
p1str = formatnumber( port1, 0)  
p2str = formatnumber( port2, 0)  
  
Promptconnect2 4, 2, port1, port2  
scpi.execute("SENS:CORR:COLL:ACQ STAN4,SST2;*OPC?")  
end sub  
  
' return the nth item in the comma separated list  
Function GetItemNumber( list, n)  
dim strVector  
strVector = split(list,",",-1,1)  
GetItemNumber = strVector(n-1)  
end function  
' remove the trailing newline from str  
function chop( str )  
dim tmp  
tmp = str  
' remove the appended newline  
dim pos  
pos = InStrRev(tmp,vblf)  
if (pos >0) then  
tmp = mid(tmp,1,pos-1)  
end if  
chop = tmp  
end function  
  
'return the label for the nth standard assigned to the class described by
class_index.  
' if class_index = 1, class is S11A (STAN1)  
' if class_index = 2, class is S11B (STAN2), etc  
function GetStandardLabel( class_index, nth)  
dim olist  
dim stdnum  
dim resp  
olist = scpi.execute("SENS:CORR:COLL:CKIT:OLIST" \+
formatnumber(class_index,0)+"?")  
stdnum = GetItemNumber( olist, nth)  
scpi.execute("SENS:CORR:COLL:CKIT:STAN " \+ formatnumber(stdnum,0))  
resp = scpi.execute("SENS:CORR:COLL:CKIT:STAN:LABel?")  
GetStandardLabel = chop(resp)  
end function  
  
sub PromptConnect1( class_index, nth, port)  
wscript.echo "CONNECT " \+ GetStandardLabel( class_index, nth) + " to port "
\+ formatnumber(port,0)  
end sub  
  
sub PromptConnect2( class_index, nth, port1, port2)  
wscript.echo "CONNECT " \+ GetStandardLabel( class_index, nth) + " between
ports " \+ formatnumber(port1,0) + " and " \+ formatnumber(port2,0)  
end sub  
  
' Print the order of standards per class for this kit  
sub PrintKitOlist( kit )  
dim i  
dim cmd  
dim resp  
wscript.echo  
dim olistcmd  
olistcmd = "SENS:CORR:COLL:CKIT:OLIST"  
' list the sub standards for each of the following classes  
' S11A, S11B, S11C, FWD TRANS, FWD ISOL, S22A, S22B, S22C, REV TRANS, REV ISOL  
for i = 1 to 8  
cmd = olistcmd + formatNumber(i,0) + "?"  
resp = scpi.execute(cmd)  
wscript.echo cmd + "= " \+ chop(resp)  
next  
end sub  
  
sub PrintKitStandardInfo( kit )  
wscript.echo scpi.execute("SENS:CORR:COLL:CKIT:NAME?")  
dim i  
for i = 1 to 30  
dim slabel  
dim snum  
snum = formatNumber(i,0)  
scpi.execute("SENS:CORR:COLL:CKIT:STAN " \+ snum)  
slabel=scpi.execute("SENS:CORR:COLL:CKIT:STAN:LABel?")  
wscript.echo "Standard #"+snum+ " = " \+ chop(slabel)  
next  
end sub  
  

The output from this program is as follows:

Microsoft (R) Windows Script Host Version 5.6

Copyright (C) Microsoft Corporation 1996-2001. All rights reserved.

"85052B 3.5 mm with sliding load"

Standard #1 = "3.5 mm male short"

Standard #2 = "3.5 mm male open"

Standard #3 = "3.5 mm male broadband load"

Standard #4 = "Insertable thru standard"

Standard #5 = "3.5 mm male sliding load"

Standard #6 = "3.5 mm male lowband load"

Standard #7 = "3.5 mm female short"

Standard #8 = "female to female characterized thru adapter"

Standard #9 = "0-2 Load"

Standard #10 = "Open"

Standard #11 = "Non-insertable thru"

Standard #12 = "3.5 mm female lowband load"

Standard #13 = "3.5 mm female sliding load"

Standard #14 = "3.5 mm female broadband load"

Standard #15 = "3.5 mm female open"

Standard #16 = "Open"

Standard #17 = "Open"

Standard #18 = "Open"

Standard #19 = "Open"

Standard #20 = "Open"

Standard #21 = "Open"

Standard #22 = "Open"

Standard #23 = "Open"

Standard #24 = "Open"

Standard #25 = "Open"

Standard #26 = "Open"

Standard #27 = "Open"

Standard #28 = "Open"

Standard #29 = "Open"

Standard #30 = "Open"

SENS:CORR:COLL:CKIT:OLIST1?= +2,+15,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST2?= +1,+7,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST3?= +6,+5,+3,+12,+13,+14,+0

SENS:CORR:COLL:CKIT:OLIST4?= +4,+8,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST5?= +2,+15,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST6?= +1,+7,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST7?= +6,+5,+3,+12,+13,+14,+0

SENS:CORR:COLL:CKIT:OLIST8?= +4,+8,+0,+0,+0,+0,+0

Calibrating ports 1 and 2

CONNECT "3.5 mm female open" to port 1

CONNECT "3.5 mm female short" to port 1

CONNECT "3.5 mm female broadband load" to port 1

CONNECT "3.5 mm male open" to port 2

CONNECT "3.5 mm male short" to port 2

CONNECT "3.5 mm male broadband load" to port 2

CONNECT "Insertable thru standard" between ports 1 and 2

Calibrating ports 2 and 3

CONNECT "3.5 mm male open" to port 2

CONNECT "3.5 mm male short" to port 2

CONNECT "3.5 mm male broadband load" to port 2

CONNECT "3.5 mm female open" to port 3

CONNECT "3.5 mm female short" to port 3

CONNECT "3.5 mm female broadband load" to port 3

CONNECT "Insertable thru standard" between ports 2 and 3

Calibrating ports 3 and 4

CONNECT "3.5 mm female open" to port 3

CONNECT "3.5 mm female short" to port 3

CONNECT "3.5 mm female broadband load" to port 3

CONNECT "3.5 mm female open" to port 4

CONNECT "3.5 mm female short" to port 4

CONNECT "3.5 mm female broadband load" to port 4

CONNECT "female to female characterized thru adapter" between ports 3 and 4

