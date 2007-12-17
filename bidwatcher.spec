%define name	bidwatcher
%define version 1.3.17
%define release %mkrel 6

Name:		%{name}
Summary:	Free tools to manage e-bay auctions
Version:	%{version}
Release:	%{release}
Source:		http://prdownloads.sourceforge.net/bidwatcher/%{name}-%{version}.tar.bz2
Url:		http://bidwatcher.sourceforge.net
Group:		Networking/Other
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:  curl-devel
License:	GPL

%description
Bidwatcher is a tool for eBay users (eBay is a giant internet auction site, if
you don't know that I'm not sure why you're reading this :-) ).  It is a
stand alone application that can track auctions and perform automated bids
called 'snipes'.  For more information see http://bidwatcher.sourceforge.net

%prep
%setup -q 

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="bidwatcher" \
needs="x11" \
icon="finances_section.png" \
section="More Applications/Finances" \
title="BidWatcher" \
longtitle="Tool For eBay users" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Tool for eBay users
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Finances;Office;Finance;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README INSTALL NEWS COPYING AUTHORS
%{_bindir}/*
%{_mandir}/man1/*
%{_menudir}/*
%{_datadir}/applications/mandriva-%{name}.desktop

