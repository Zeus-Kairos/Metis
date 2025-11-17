# Perform a Guided Cal with C#

* * *

The following example performs a 2-port or 4-port Guided Cal using C#.

Note: Replace <remote host name> with the full computer name of your VNA.

[Learn more about using .NET with the
VNA](../Learning_about_COM/Using_NET.htm)

AgilentPNA835x.IApplication pna; AgilentPNA835x.ICalManager3 calMgr;
AgilentPNA835x.IGuidedCalibration guidedCal; AgilentPNA835x.IChannel chan; int
chanNum; AgilentPNA835x.ICalSet calset; void PerformGuidedCal() { Type pnaType
= Type.GetTypeFromProgID("AgilentPNA835x.Application", "<remote host name>");
pna = (AgilentPNA835x.IApplication) Activator.CreateInstance(pnaType); calMgr
= (AgilentPNA835x.ICalManager3)pna.GetCalManager(); guidedCal =
(AgilentPNA835x.IGuidedCalibration)calMgr.GuidedCalibration; chan =
pna.ActiveChannel; chanNum = chan.channelNumber; // Initialize guided cal to
be performed on the active channel. // The boolean argument of True indicates
to store the cal only // in the channel's calibration register. If instead you
wish // to create a new calset that the new cal will get stored to, // comment
out this next line and uncomment the three lines below it.
guidedCal.Initialize(chanNum, true); calset = calMgr.CreateCalSet(chanNum);
chan.SelectCalSet(calset.GetGUID(), true); guidedCal.Initialize(chanNum,
false); // To perform 2-port cal, Uncomment the following // Then comment the
4-port cal // Do 2-port cal // TwoPortGuidedCal(); // Do 4-port cal
FourPortGuidedCal(); } void TwoPortGuidedCal() { // Select the connectors
guidedCal.set_ConnectorType(1, "APC 3.5 female");
guidedCal.set_ConnectorType(2,"APC 3.5 male"); for (int i = 3; i <=
pna.NumberOfPorts; i++) guidedCal.set_ConnectorType(i, "Not used");
MessageBox.Show("Connectors defined for Ports 1 and 2"); // Select the Cal Kit
for each port being calibrated. guidedCal.set_CalKitType(1,"85052D");
guidedCal.set_CalKitType(2,"85052D"); // To use an ECal module instead,
comment out the above two lines // and uncomment the following two lines. //
Replace N4691-60004 with your own ECAL model followed by 'ECal'. // Your ECal
module must already be connected to a PNA USB port. // guidedCal.CalKitType(1)
= "N4691-60004 ECal" // guidedCal.CalKitType(2) = "N4691-60004 ECal"
MessageBox.Show("Cal kits defined for Ports 1 and 2"); // Initiate the
calibration and query the number of steps int numSteps =
guidedCal.GenerateSteps(); // Measure the standards, compute and apply the cal
MeasureAndComplete(numSteps); } void FourPortGuidedCal() { //Select the
connectors guidedCal.set_ConnectorType(1,"APC 3.5 female");
guidedCal.set_ConnectorType(2,"APC 3.5 female");
guidedCal.set_ConnectorType(3,"APC 3.5 female");
guidedCal.set_ConnectorType(4,"APC 3.5 female"); // If a PNA which has more
than 4 ports for (int i = 5;i<=pna.NumberOfPorts;++i)
guidedCal.set_ConnectorType(i,"Not used"); MessageBox.Show("Connectors defined
for Ports 1 to 4"); // Select the Cal Kit for each port being calibrated.
guidedCal.set_CalKitType(1,"85052D"); guidedCal.set_CalKitType(2,"85052D");
guidedCal.set_CalKitType(3,"85052D"); guidedCal.set_CalKitType(4, "85052D");
// To use an ECal module instead, comment out the above four lines // and
uncomment the following four lines. // Replace N4691-60003 with your own ECAL
model followed by 'ECal'. // Your ECal module must already be connected to a
PNA USB port. //guidedCal.CalKitType(1) = "N4431-60003 ECal";
//guidedCal.CalKitType(2) = "N4431-60003 ECal"; //guidedCal.CalKitType(3) =
"N4431-60003 ECal"; //guidedCal.CalKitType(4) = "N4431-60003 ECal";
MessageBox.Show("Cal kits defined for Ports 1 to 4"); // Initiate the
calibration guidedCal.GenerateSteps(); // If your selected cal kit is not a
4-port ECal module which can // mate to all 4 ports at once, then you may want
to choose which // thru connections to measure for the cal. You must measure
at // least 3 different thru paths for a 4-port cal (for greatest // accuracy
you can choose to measure a thru connection for all 6 // pairings of the 4
ports). If you omit this command, the default // is to measure from port 1 to
port 2, port 1 to port 3, and // port 1 to port 4. For this example we select
to measure // from port 1 to port 2, port 2 to port 3, and port 2 to port 4.
long[] portList = new long[6]{1,2,2,3,2,4}; guidedCal.ThruPortList = portList;
// Re-generate the connection steps to account for the thru changes int
numSteps = guidedCal.GenerateSteps(); // Measure the standards, compute and
apply the cal MeasureAndComplete(numSteps); } void MeasureAndComplete(int
numSteps) { MessageBox.Show("Number of steps is " \+ numSteps.ToString()); //
Measure the standards // The following series of commands shows that standards
// can be measured in any order. These steps acquire // measurement of
standards in reverse order. // It is easiest to iterate through standards
using // a For-Next Loop. for (int i = numSteps; i >= 1; --i) { string
strPrompt = guidedCal.GetStepDescription(i); MessageBox.Show(strPrompt);
guidedCal.AcquireStep(i); } // Conclude the calibration
guidedCal.GenerateErrorTerms(); MessageBox.Show("Cal is done!"); }  
---

