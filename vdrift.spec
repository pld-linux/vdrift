%define _ver	2007-03-23
Summary:	A free drift racing simulator with excellent physics and graphics
Summary(pl.UTF-8):	Darmowy symulator wyścigów ze wspaniałą fizyką i grafiką
Name:		vdrift
Version:	%(echo %{_ver} | tr -d -)
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/vdrift/%{name}-%{_ver}-src.tar.bz2
# Source0-md5:	efc5c3c409923382035738798a6392e8
Source1:	http://dl.sourceforge.net/vdrift/%{name}-%{_ver}-data-full.tar.bz2
# Source1-md5:	2136ce2e347a018f2400e3f114e005fd
Patch0:		%{name}-gcc42.patch
URL:		http://vdrift.net/
BuildRequires:	OpenAL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	freealut-devel
BuildRequires:	scons
BuildRequires:	FHS-fixes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind. Currently the game features:
- 19 tracks: Barcelona, Brands Hatch, Detroit, Dijon, Hockenheim,
  Jarama, Kyalami, Laguna Seca, Le Mans, Monaco, Monza, Mosport,
  Nrburgring Nordschleife, Pau, Road Atlanta, Ruudskogen, Spa
  Francorchamps, Weekend Drive, Zandvoort
- 28 cars: 3S, AX2, C7, CO, CS, CT, F1, FE, FF, G4, GT, M3, M7,
  MC, MI, NS, RG, RS2, SB, T73, TC, TL, TL2, XG, XM, XS, Z06
- Compete against AI players
- Simple networked multiplayer mode
- Very realistic physics
- Mouse/joystick/keyboard driven menus
- Much more...

%description -l pl.UTF-8
VDrift jest międzyplatformowym symulatorem jazdy opartym na kodzie
open source. Obecnie gra zapewnia:
- 19 tras: Barcelona, Brands Hatch, Detroit, Dijon, Hockenheim,
  Jarama, Kyalami, Laguna Seca, Le Mans, Monaco, Monza, Mosport,
  Nrburgring Nordschleife, Pau, Road Atlanta, Ruudskogen, Spa
  Francorchamps, Weekend Drive, Zandvoort
- 28 samochodów: 3S, AX2, C7, CO, CS, CT, F1, FE, FF, G4, GT, M3, M7,
  MC, MI, NS, RG, RS2, SB, T73, TC, TL, TL2, XG, XM, XS, Z06
- Wyścig przeciwko komputerowym graczom
- Prosty tryb multiplayer przez sieć
- Bardzo realistyczną fizykę
- Myszka/joystick/klawiatura menu ustawień
- Wiele więcej...

%prep
%setup -q -n %{name}-%{_ver}-src -a0 -a1 -c -T
%patch0 -p1
mv vdrift-%{_ver}-src/data/* ./build/vdrift-%{_ver}-src/data/

%build
cd build/%{name}-%{_ver}-src/
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

cd build/%{name}-%{_ver}-src/
scons install \
	prefix=$RPM_BUILD_ROOT/usr/
ln -s %{_datadir}/games/vdrift/bin/vdrift $RPM_BUILD_ROOT%{_bindir}/vdrift

cd ../..

%find_lang VDrift

%clean
rm -rf $RPM_BUILD_ROOT

%files -f VDrift.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vdrift
# IT HAS TO BE FIXED!!!
%attr(755,root,root) %{_datadir}/games/vdrift/bin/vdrift
%{_datadir}/games/vdrift
