# $Id$

Name: control
Version: 0.6.1
Release: alt1

Summary: A set of scripts to control installed system facilities
License: GPL
Group: System/Base
BuildArch: noarch

Source: %name-%version.tar.gz

Requires: %__subst

%define _controldir %_sysconfdir/control.d/facilities

%description
The scripts included in this package provide a common interface to
control system facilities provided by a number of other packages.
This is intended for use primarily by packages which are providing
a facility that can potentially be dangerous to system security,
to let you enable, disable, or configure the facility independently
from package installation.

%prep
%setup -q

%install
%__mkdir_p $RPM_BUILD_ROOT{%_controldir,%_sbindir,%_man8dir}
%__install -p -m755 control{,-dump,-restore} $RPM_BUILD_ROOT%_sbindir/
%__install -p -m755 functions $RPM_BUILD_ROOT%_sysconfdir/control.d/
%__mkdir_p -m700 $RPM_BUILD_ROOT/var/run/control
%__install -p -m644 control{,-dump,-restore}.8 $RPM_BUILD_ROOT%_man8dir/
%__install -pD -m644 control.macros $RPM_BUILD_ROOT%_sysconfdir/rpm/macros.d/control

# Generate shell functions provides list.
(
	echo '# shell functions provides list'
	for f in $RPM_BUILD_ROOT%_sysconfdir/control.d/*; do
		[ -f "$f" -a -x "$f" ] || continue
		sed -ne 's/^\([A-Za-z][A-Za-z_0-9]*[[:space:]]*\)()$/\1/pg' "$f"
	done |LC_COLLATE=C sort -u
) >$RPM_BUILD_ROOT%_controldir/.provides.sh

%files
%config %_sysconfdir/rpm/macros.d/control
%_sbindir/control*
%config %_sysconfdir/control.d
/var/run/control
%_man8dir/*

%changelog
* Sat Sep 25 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.1-alt1
- functions/{new_help,control_help}:
  new functions for help support.
- functions/control_list:
  new function for use by complex facilities.
- functions/control_fmode:
  don't change files when the new setting is the same.
- Packaged %_sysconfdir/control.d/.provides.sh file.

* Wed Oct 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt2
- functions: use colon instead of dot as user/group name
  separator with invocations of chown(1).
- Added rpm macros file (#2972).

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- Synced with owl-control-0.6:
  * Fri Apr 18 2003 Solar Designer <solar@owl.openwall.com> 0.6-owl1
  - Avoid *roff commands within .SH NAME to not confuse makewhatis
    and apropos(1).

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- control-restore: be more verbose.

* Sun Jan 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- Refined output for facilities with slashes.

* Wed Jan 08 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- Synced with owl-control-0.5:
  * Wed Jan 08 2003 Solar Designer <solar@owl.openwall.com>
  - Wrote control(8) and control-dump(8) manual pages.

* Sun Nov 03 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Synced with owl-control-0.4, including:
  + minor syntax fixes in control, control-dump and control-restore;
  + in control_subst(), don't rewrite files when the new setting is the same.

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- ALT adaptions.
- Added control-dump and control-restore utilities.

* Sun Jul 07 2002 Solar Designer <solar@owl.openwall.com>
- Use grep -q in the provided shell functions.

* Wed Feb 06 2002 Michail Litvak <mci@owl.openwall.com>
- Enforce our new spec file conventions.

* Wed Nov 22 2000 Solar Designer <solar@owl.openwall.com>
- Support extended regexp's in control_subst().

* Fri Aug 11 2000 Solar Designer <solar@owl.openwall.com>
- Various important changes to the provided shell functions.
- Wrote the package description.
- Moved the symlink: /sbin/control is now /usr/sbin/control.

* Thu Aug 10 2000 Solar Designer <solar@owl.openwall.com>
- Initial version.
