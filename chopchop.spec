Summary:	WEP cracker which uses the AP to decipher packets
Summary(pl):	³amacz WEP'a, który u¿ywa AP by odszyfrowaæ pakiety
Name:		chopchop
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	%{name}-%{version}.zip
# Source0-md5:	c5f97976238058c9de96266e23a6f7e2
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ble

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install chopchop $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOC README patch
%attr(755,root,root) %{_bindir}/*
