# TODO: optflags
Summary:	WEP cracker which uses the AP to decipher packets
Summary(pl):	£amacz WEP-a u¿ywaj±cy AP do odszyfrowywania pakietów
Name:		chopchop
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Networking
# http://www.netstumbler.org/attachment.php?s=dc6863691ec47fcc72b51c473413807d&attachmentid=2598
Source0:	%{name}-%{version}.zip
# Source0-md5:	c5f97976238058c9de96266e23a6f7e2
URL:		http://www.netstumbler.org/showthread.php?t=12489
BuildRequires:	libpcap-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WEP cracker which uses the AP to decipher packets. Easiest one are
ARP's. Takes 10-20s.

%description -l pl
£amacz WEP-a u¿ywaj±cy AP do odszyfrowywania pakietów. Naj³atwiejsze
to ARP. Zajmuje to 10-20s.

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
