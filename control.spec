# $Id$

Name: control
Version: 0.3.1
Release: alt1

Summary: A set of scripts to control installed system facilities
License: GPL
Group: System/Base
BuildArch: noarch

Source: %name-%version.tar.bz2

Requires: %__subst

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
%__mkdir_p $RPM_BUILD_ROOT{/etc/control.d/facilities,%_sbindir}
%__install -p -m755 control* $RPM_BUILD_ROOT%_sbindir/
%__install -p -m755 functions $RPM_BUILD_ROOT/etc/control.d/
%__mkdir_p -m700 $RPM_BUILD_ROOT/var/run/control

%files
%_sbindir/control*
/etc/control.d
/var/run/control

%changelog
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
