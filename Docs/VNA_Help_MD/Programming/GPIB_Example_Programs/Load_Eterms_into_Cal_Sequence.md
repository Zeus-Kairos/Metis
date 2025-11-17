# Load Error Terms during a Cal Sequence

* * *

This example requires that you already have a Cal Set named "foo" that
contains a 1-port cal on port 1 and a 1-port cal on port 2.

This example starts a Guided Calibration specifying an Unknown Thru. It loads
the 1-port Cals from the existing "foo" Cal Set, then recalculates the number
of steps required to complete the cal. After loading the 1-port cals, only the
Unknown Thru standard is left to acquire.

SENS:CORR:COLL:GUID:CONN:PORT1 "APC 3.5 female" SENS:CORR:COLL:GUID:CONN:PORT2
"APC 3.5 female" SENS:CORR:COLL:GUID:CKIT:PORT1 "85033D/E"
SENS:CORR:COLL:GUID:CKIT:PORT2 "85033D/E" SENS:CORR:COLL:GUID:METH UNKN '
auto-create user calsets for SCPI SENS:CORR:PREF:CSET:SAVU 1
SENS:CORR:COLL:GUID:INIT ' should return the number 7
SENS:CORR:COLL:GUID:STEPS? ' to port 1, from port 1 in calset
SENS:CORR:COLL:GUID:ETER:LOAD "foo",1,1 ' to port 2, from port 2 in calset
SENS:CORR:COLL:GUID:ETER:LOAD "foo",2,2 ' should now return the number 1
SENS:CORR:COLL:GUID:STEPS? ' measure the unknown thru SENS:CORR:COLL:GUID:ACQ
STAN1 ' save the cal to new user calset SENS:CORR:COLL:GUID:SAVE  
---

