Name:           task
Version:        1.9.4
Release:        %mkrel 1
Summary:        A command-line to do list manager

Group:          Office
License:        GPLv2+
URL:            http://taskwarrior.org
Source0:        http://taskwarrior.org/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root


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
%configure2_5x
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 -T scripts/bash/task_completion.sh $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/task

%clean
rm -rf $RPM_BUILD_ROOT


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


