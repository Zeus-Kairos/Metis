# Windows Operating System

This topic describes the Microsoft Windows Operating System, configuration and
the settings used with the Keysight instrument software. It includes
information about changing some of the system settings. And it describes the
Windows operating system configuration and the software installations that are
present on the Disk Drive when the instrument leaves the factory.

It is possible to use the front panel and touchscreen for changing operating
system configuration items, but it is easier to perform these tasks with a USB
mouse and external keyboard.

Note: This topic does not cover Windows Operation System features that can be
found in the Windows OS Help (for example, keyboard shortcuts, etc.).

## Microsoft Windows

Your instrument has Microsoft Windows installed at the factory. Keysight has
already configured many of the settings in Microsoft Windows for optimal
behavior in your instrument. This topic contains details about many of these
settings.

## Installed Software

#### Vector network analyzer software

The Vector Network Analyzer Measurement Application software is installed in
the vector network analyzer. Additional measurement applications are
available. Each application requires a license to execute the software. All of
these applications are installed by the factory at the time of manufacture,
even if the licenses have not been purchased. You may purchase additional
licenses at a later date.

## Customer Information of Software

#### 3rd party software verified by Keysight

Keysight has verified that the following programs are compatible with the
instrument's applications:

  * MathWorks MATLAB

#### Installation of other 3rd party software

The Vector Network Analyzer platform is an Open Windows environment, so you
can install software on the instrument. However, installation of non-approved
software may affect instrument performance. Keysight does not warrant the
performance of the analyzers with non-approved software installed.

Note: Before installing any additional programs on the instrument, you should
exit the Vector Network Analyzer application. Also, you must not remove any
applications or programs that were installed on the instrument when it was
shipped from the factory.

If you install programs other than those that Keysight has tested, it could
cause problems with the instrument's applications. If this happens, you should
try uninstalling the program that has caused the problem, or try changing the
program's configuration. If this does not correct the problem, you may have to
use the Instrument Recovery system to reinstall the instrument's system
software.

## User Accounts

Refer to [VNA User Accounts and Passwords](NewUsers.md).

## Keysight VNA Licensing Options

For information on VNA licensing options, refer to the
[ht](https://www.keysight.com/us/en/assets/9018-04534/installation-
guides/9018-04534.pdf)tps:[//www](http://www.keysight.com/us/en/assets/9018-04534/installation-
guides/90).k[eysight.com/us/en/assets/9018-04534/installation-
guides/9018-04534.pdf](http://www.keysight.com/us/en/assets/9018-04534/installation-
guides/90) (N5242-90024).

## Licensing New Measurement Application Software - After Initial Purchase

For information on VNA licensing options, refer to the
[ht](https://www.keysight.com/us/en/assets/9018-04534/installation-
guides/9018-04534.pdf)tps:[//www](http://www.keysight.com/us/en/assets/9018-04534/installation-
guides/90).k[eysight.com/us/en/assets/9018-04534/installation-
guides/9018-04534.pdf](http://www.keysight.com/us/en/assets/9018-04534/installation-
guides/90) (N5242-90024).

## Windows Configuration

The Windows settings have been optimized for the best measurement performance.
Any modifications to these settings may degrade instrument performance and
measurement speed. In general, most Windows System settings (typically set
through the Windows Control Panel) should not be modified. Those that can be
safely modified are listed below.

CAUTION: To recover from problems caused by changing Windows Systems settings,
you may have to reinstall the Windows system and instrument applications using
the Instrument Recovery process.

#### Settings that can be changed

You may change the following Windows settings or administrative tasks
(available from the Windows Control Panel) to suit your own personal
preferences. It is recommended that you document any changes to the
instruments configuration in case an Instrument Recovery is performed and the
configuration is reset.

Note: Some of these actions can only be performed with Administrator
privileges. Refer to the Windows OS Help for how to set the permissions to
Administrator.

You May Use This Feature: |  To Do This:  
---|---  
Windows Update |  Configure Microsoft Windows Automatic Updates. Microsoft recommends that you always get the latest critical Windows updates to ensure that the instrument's Windows operating system is protected. If the instrument has Internet access, the instrument default is set to automatically check for critical Windows Updates and notify you.  
User Accounts |  Set up new user accounts. CAUTION: Do not delete or modify the "KeysightOnly" user account. Doing so may prevent Keysight from servicing the instrument.  
Network and Sharing Center |  Add the instrument to a network.  
Devices and Printers |  Install and configure a printer.  
Date and Time |  Set the time and date.  
System |  If you click on Advanced System Settings a dialog will open called System Properties. On this dialog there is an Advanced tab, which opens up a dialog with a number of settings options. One of these is Performance, and if you click on the Settings button under Performance, you will see another dialog with a number of settings options. The default is Let Windows choose whats best for my computer. You can also select Adjust for best performance. You should leave the remaining selections unchanged.  
  
#### Settings that must not be changed

Avoid changing the settings described below (available from the Windows
Control Panel). Changes to these settings may degrade instrument performance,
screen displays, and measurement speed.

Do NOT Use This Feature: |  To Do This:  
---|---  
Power Options |  Do not change power options.  
System  |  If you click on Advanced System Settings a dialog will open called System Properties. On this dialog there is a tab calledHardware. You should not modify any settings under the Hardware tab. On this dialog there is also a tab called Advanced. You should not modify any settings under the Advanced tab except as described above under Settings that can be changed.  
Fonts |  Do not remove installed fonts.  
Display |  Do not change the following settings:

  * Screen Saver settings (under Personalization)
  * Screen resolution (under Adjust Resolution)
  * DPI setting (underSet custom text size)

  
Region and Language |  Do not change any settings under Region and Language or the instrument keyboard and display may not operate properly.  
User Accounts |  Do not delete or modify the "KeysightOnly" user account.  
  
In addition, Do Not:

  * Add, delete, or modify disk drive partitions.

  * Delete or modify Keysight registry entries.

  * Change the contents of any directories containing the name Keysight.

  * Stop the IIS server.

  * Tamper with any virtual directories (or their contents) that came configured with the instrument.

  * Uninstall these libraries, interfaces, or programs:

    * The I/O Libraries

    * The .NET Framework or any Hot fixes or Service Packs for the .NET Framework

    * The Microsoft Visual J# .NET Redistributable Package1.1

    * Programs that begin with Keysight  The Adobe Acrobat reader

  * Modify: 
    * The I/O Library GPIB27, GPIB28 interfaces shown as configured Instrument I/O in the Connection Expert or I/O Config

#### Autoplay / Autorun

Since the introduction of Windows XP, the term Autoplay (sometimes also called
Autorun) has come to be associated with the feature which assists users in
selecting appropriate actions when new media and devices are detected.

The Autoplay/Autorun feature is turned off in the instrument, by default, for
heightened security, unless the Administrator account is running.

If you wish to re-enable Autoplay/Autorun, you may use the Auto Play function
in the Control Panel. However, be aware that if you do this you may be more
subject to virus attack from portable media such as USB flash drives.

## Configuring Printers

Refer to [Windows Considerations](Windows_Considerations.md#Printing).

## Configuring LAN

Refer to [Windows Considerations](Windows_Considerations.md#LAN).

## Windows Security

Microsoft recommends the following to ensure the instrument's Windows
operating system is protected:

  * Use an internet firewall
  * Get the latest critical Windows updates.
  * Use up-to-date antivirus software.

#### Windows Firewall

The instrument is shipped with the Windows Firewall enabled. You can verify
the status of Windows Firewall by going to the Control Panel and clicking on
System and Security, Windows Firewall.

Windows Firewall Exceptions for programs and ports have been added to allow
proper operation of the instrument over a network. Modifying these settings
may cause the instrument to not operate properly.

#### Automatic Updates

Microsoft recommends that you always get the latest critical Windows updates
to ensure that the instrument's Windows operating system is protected. If the
instrument has internet access, the instrument default is set to automatically
check for critical Windows Updates and notify you.

You can change the configuration of the Microsoft Automatic Updates. You can
choose not to have automatic updates. However, if you do this then you should
manually update Windows periodically.

#### Virus and Firewall Protection

No third-party antivirus software is shipped with the analyzer. It is
recommended that you install antivirus software if your analyzer is connected
to the LAN. Check with your IT department to see what they recommend. The
analyzer is shipped with the Windows firewall and Windows Defender enabled.

Do not modify the default network settings as this may cause problems with the
operating system of the analyzer.

To adjust Windows Defender settings, log in as administrator and minimize the
Application and click on the Start button and type: defender

Then click on Windows Defender from the Best match column.

#### Spyware Protection

There is no third-party anti-spyware software installed on the instrument.
This should not be a problem if you do not use the instrument for a lot of
internet browsing. Having spyware in the instrument could have an impact on
the instrument performance.

## System Maintenance

[Refer to](http://mktwww.srs.is.keysight.com/field/service/network/pna/)
[http://mktwww.srs.is.keysight.com/field/service/network/pna/.](http://mktwww.srs.is.keysight.com/field/service/network/pna/)

## USB Connections

Refer to [Windows Considerations](Windows_Considerations.md#USB).

## Disk Drive Partitioning and Use

The drive is partitioned into 3 sections:C:, D: and E:

  * The C: partition contains the Windows 10 operating system and software installed by Keysight. This is an Open System which means you can install additional software, and these should be installed on the C: drive. However, only a limited set of software applications are tested for use with the Keysight measurement software. The installation and/or use of other software is not warranted and could interfere with the operation of the measurement software. If instrument repair is ever needed, the Keysight version of the C: drive is the only part of the instrument software that is restored by the Instrument Recovery process. You must reload any other software that you have added in the instrument.

  * The D: partition is reserved for data storage. The User Accounts that are configured by Keysight have their My Documents folder mapped to the D: drive. This is for the convenience of backing-up the measurement data. You should always back-up the data on the D: drive to an external device. This allows you to restore the data if you ever need to replace the disk drive.
  * The E: partition is reserved for Keysights use. The primary use of the E: drive is for housing the Calibration and Alignment data. Do not change or overwrite the files on this drive. This could cause your instrument to not meet specifications, or even to stop functioning correctly. Do not use this drive for data storage.

## Disk Drive Recovery Process

Refer to The VNA SSD Recovery Process.

## Problems with Windows OS

The Microsoft Windows operating system settings have been optimized for the
best performance. Modification of these settings may degrade instrument
performance and measurement speed.

The VNA Vector Network Analyzers operate in an open Windows environment, so
you can install software on the instrument. However, installation of non-
approved software may affect instrument performance. Keysight does not warrant
the performance with non-approved software installed.

