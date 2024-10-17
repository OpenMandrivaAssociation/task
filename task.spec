Name:           task
Version:        2.1.2
Release:        2
Summary:        A command-line to do list manager

Group:          Office
License:        GPLv2+
URL:            https://taskwarrior.org
Source0:        http://taskwarrior.org/download/%{name}-%{version}.tar.gz

buildrequires:  cmake

%description
Task is a command-line to do list manager. It has
support for GTD functionality and includes the
following features: tags, colorful tabular output,
reports and graphs, lots of manipulation commands,
low-level API, abbreviations for all commands and
options, multi-user file locking, recurring tasks.

%prep
%setup -q


%build
%cmake
%make


%install
%makeinstall_std -C build
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 -T scripts/bash/task.sh $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/task


%files
%defattr(-,root,root,-)
%doc /usr/share/doc/task/
%{_bindir}/task
%{_mandir}/man1/task.1.*
%{_mandir}/man5/taskrc.5.*
%{_mandir}/man5/task-tutorial.5.*
%{_mandir}/man5/task-color.5.*
%{_mandir}/man5/task-faq.5.*
%{_mandir}/man5/task-sync.5.*
%config(noreplace) %{_sysconfdir}/bash_completion.d




%changelog
* Fri Jul 22 2011 Götz Waschk <waschk@mandriva.org> 1.9.4-1mdv2012.0
+ Revision: 690916
- import task

