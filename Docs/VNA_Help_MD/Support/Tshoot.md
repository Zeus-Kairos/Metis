# Troubleshooting the VNA

* * *

By running a few checks, you can identify if the analyzer is at fault. Before
calling Keysight Technologies or returning the instrument for service, please
make the following checks.

  * [Check the Basics](Tshoot.md#basics)

  * [VNA Application Terminates Unexpectedly](Tshoot.md#crash)

  * [Check Error Terms](Tshoot.md#error_terms)

  * [Check the Service Guide](Tshoot.md#guide)

  * [Error Log](Tshoot.md#Error_Log)

[Other Support Topics](Support_Overview.md)

Check the Basics

A problem can often be solved by repeating the procedure you were following
when the problem occurred. Before calling Keysight Technologies or returning
the instrument for service, please make the following checks:

Note: Problems with the VNA application (slow or terminates unexpectedly) can
be caused by a faulty Hard Disk Drive (HDD). For more information, see
Preventing VNA SSD Problems and The VNA SSD Recovery Process.

  1. Is there power at the power socket? Is the instrument plugged in?

  2. Is the instrument turned on? Check to see if the front panel line switch and at least one of the LED rings around the test ports glows green. This indicates the power supply is on.

  3. If you are experiencing difficulty with the front-panel keypad or peripherals, the USB bus may be overloaded. Remove the USB devices, restart the VNA, and reconnect the USB devices. See Power-up.

  4. If other equipment, cables, and connectors are being used with the instrument, make sure they are connected properly and operating correctly.

  5. Review the procedure for the measurement being performed when the problem appeared. Are all the settings correct?

  6. If the instrument is not functioning as expected, return the unit to a known state by pressing the Preset key.

  7. Is the measurement being performed, and the results that are expected, within the [specifications](../Specs/ManualChoice.md) and capabilities of the instrument?

  8. If the problem is thought to be due to firmware, check to see if the instrument has the [latest firmware](FW_upgrade.md) before starting the troubleshooting procedure.

  9. Check that the measurement calibration is valid. See [Accurate Measurement Calibrations](../S3_Cals/Accurate.md) for more information.

  10. If the necessary test equipment is available, perform the operator's check and system verification in Chapter 2 of the VNA Service Guide, "System Tests, Verifications, and Adjustments," . You can download a copy of the Service Guide from our Web site: [http://www.Keysight.com](http://www.Keysight.com/find/pna).

  11. Phase lock lost message \- This usually occurs when there is not enough source power to phase lock the VNA. It can occur during an errant [FCA setup](../FreqOffset/FCA_Use.md) or [Source Power Calibration](../S3_Cals/PwrCalibration.md#SourcePowerCal). It can also occur if one of the front panel reference channel loops is not connected. Otherwise, this indicates a hardware problem.

VNA Application Terminates Unexpectedly

If an unexpected and irrecoverable error occurs, Keysight would like to know
about it. The VNA attempts to save pertinent information about the state of
the system. The VNA does NOT send this information to Keysight.

We respect the privacy of our customers. However, access to information that
helps us improve the VNA is a benefit to both Keysight and you. Please take
the time to contact us or email the saved information to
www.keysight.com/find/contactus.

The following procedure shows how to do this:

  1. A message box immediately appears on the screen containing the location of a directory. Please record this message. If you miss the message, you can find the directory location using the Windows Event Log: On the VNA, click Start, Settings, Control Panel, Administrative Tools, Event Viewer. Double-click the top line (most recent event). The location of the directory is seen in the Description.

  2. A dialog box may appear on the screen allowing you to add comments to help us replicate the crash.

  3. Find the directory (described in Step 1) which contains the following files:

  * 835x.dmp which is the 835x.exe capturing the context in which the program crashed.

  * 835x.xml which reports some very basic information ( exception code, OS version, and the list of modules loaded at the time of the crash and their respective version numbers).

  * 835xCrashLog.txt: The text file with your comments (described in Step 2), if submitted.

  4. If your VNA is not connected to LAN or is not configured to send email, copy the files to a PC. Then, please email the files to www.keysight.com/find/contactus.

Check Error Terms

If you print the error terms at set intervals (weekly, monthly, and so forth),
you can compare current error terms to these records. A stable, repeatable
system should generate repeatable error terms over long time intervals, for
example, six months. If a subtle failure or mild performance problem is
suspected, the magnitude of the error terms should be compared against values
generated previously with the same instrument and calibration kit. See the
[procedure for monitoring error terms](../S3_Cals/Errors.md#promouse).

  * A long-term trend often reflects drift, connector and cable wear, or gradual degradation, indicating the need for further investigation and preventative maintenance. Yet, the system may still conform to specifications. The cure is often as simple as cleaning and gaging connectors or inspecting cables.

  * A sudden shift in error terms reflects a sudden shift in systematic errors, and may indicate the need for further troubleshooting.

Consider the following while troubleshooting:

  * All parts of the system, including cables and calibration devices, can contribute to systematic errors and impact the error terms.

  * Connectors must be clean and gauged, and within specification for error term analysis to be meaningful. See the Chapter 2 in the VNA Service Guide for information on cleaning and gaging connectors.

  *     * Avoid unnecessary bending and flexing of the cables following measurement calibration, thus minimizing cable instability errors.

    * Use good connection techniques during the measurement calibration. The connector interface must be repeatable. See the VNA Service Guide for information on connection techniques.

  * It is often worthwhile to perform the procedure twice (using two distinct measurement calibrations) to establish the degree of repeatability. If the results do not seem repeatable, check all connectors and cables.

  * Use error-term analysis to troubleshoot minor, subtle performance problems. See Chapter 3, "Troubleshooting," in the VNA Service Guide if a blatant failure or gross measurement error is evident.

Check the Service Guide

Check the VNA Service Guide for specific troubleshooting procedures to help
identify problems. You can download a copy of the Service Guide from our Web
site: www.keysight.com/manuals/pna

## Error Log

Some VNAs create automatic log of data for troubleshooting purpose. The log
file stores data related to the total power ON time, number of times of power
ON, results of power ON test and so on. For security reasons, if this data
needs to be deleted, then [SERVice:LOGGing:CLEar](../Programming/GP-
IB_Command_Finder/Service_SCPI.htm#SERVice:LOGGing:CLEar) command can be used
to clear the log recorded by the instrument.

* * *

