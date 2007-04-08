%define _ver	2007-03-23
Summary:	A free drift racing simulator with excellent physics and graphics
Summary(pl.UTF-8):	Darmowy symulator wyścigów ze wspaniałą fizyką i grafiką
Name:		vdrift
Version:	%(echo %{_ver} | tr -d -)
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/vdrift/%{name}-%{_ver}-src.tar.bz2
# Source0-md5:	efc5c3c409923382035738798a6392e8
Source1:	http://dl.sourceforge.net/vdrift/%{name}-%{_ver}-data-full.tar.bz2
# Source1-md5:	2136ce2e347a018f2400e3f114e005fd
Patch0:		%{name}-gcc42.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-FHS.patch
URL:		http://vdrift.net/
BuildRequires:	OpenAL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	freealut-devel
BuildRequires:	gettext-devel
BuildRequires:	scons
Requires:	vdrift-car-resources
Requires:	vdrift-track-resources
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

%package data-cars-base
Summary:	Base cars for VDrift
Summary(pl.UTF-8):	Podstawowe samochody dla VDrift
Group:		X11/Applications/Games
Provides:	vdrift-car-resources

%description data-cars-base
Base cars for VDrift.

%description data-cars-base -l pl.UTF-8
Podstawowe samochody dla VDrift.

%package data-cars-extra
Summary:	Extra cars for VDrift
Summary(pl.UTF-8):	Dodatkowe samochody dla VDrift
Group:		X11/Applications/Games
Provides:	vdrift-car-resources

%description data-cars-extra
Extra cars for VDrift.

%description data-cars-extra -l pl.UTF-8
Dodatkowe samochody dla VDrift.

%package data-tracks-base
Summary:	Base tracks for VDrift
Summary(pl.UTF-8):	Podstawowe trasy dla VDrift
Group:		X11/Applications/Games
Provides:	vdrift-track-resources

%description data-tracks-base
Base tracks for VDrift.

%description data-tracks-base -l pl.UTF-8
Podstawowe trasy dla VDrift.

%package data-tracks-extra
Summary:	Extra tracks for VDrift
Summary(pl.UTF-8):	Dodatkowe trasy dla VDrift
Group:		X11/Applications/Games
Provides:	vdrift-track-resources

%description data-tracks-extra
Extra tracks for VDrift.

%description data-tracks-extra -l pl.UTF-8
Dodatkowe trasy dla VDrift.

%prep
%setup -q -c -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv vdrift-%{_ver}-src/data/* build/vdrift-%{_ver}-src/data/

%build
cd build/%{name}-%{_ver}-src
export CC='%{__cc}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
%scons \
	destdir=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	bindir=bin/ \
	datadir=share/games/vdrift/data \
	release=1 \
	os_cc=1 \
	os_cxx=1 \
	os_cxxflags=1 \
	NLS=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cd build/%{name}-%{_ver}-src

export CC='%{__cc}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
%scons install \
	destdir=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	bindir=bin/ \
	os_cc=1 \
	os_cxx=1 \
	os_cxxflags=1 \
	datadir=share/games/vdrift/data \
	NLS=1

install tools/autopackage/vdrift.desktop $RPM_BUILD_ROOT%{_desktopdir}
install data/textures/icons/vdrift-64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/vdrift.png

cd ../..

%find_lang VDrift

%clean
rm -rf $RPM_BUILD_ROOT

%files -f VDrift.lang
%defattr(644,root,root,755)
%doc build/%{name}-%{_ver}-src/docs/{AUTHORS,ChangeLog,NEWS,README,TODO,VAMOS.txt}
%attr(755,root,root) %{_bindir}/vdrift
%dir %{_datadir}/games/vdrift
%dir %{_datadir}/games/vdrift/data
%dir %{_datadir}/games/vdrift/data/cars
%{_datadir}/games/vdrift/data/lists
%{_datadir}/games/vdrift/data/settings
%dir %{_datadir}/games/vdrift/data/skins
%{_datadir}/games/vdrift/data/skins/simple
%{_datadir}/games/vdrift/data/skins/x1
%{_datadir}/games/vdrift/data/sounds
%{_datadir}/games/vdrift/data/textures
%dir %{_datadir}/games/vdrift/data/tracks
%{_desktopdir}/vdrift.desktop
%{_pixmapsdir}/vdrift.png

%files data-cars-base
%defattr(644,root,root,755)
%{_datadir}/games/vdrift/data/cars/CO
%{_datadir}/games/vdrift/data/cars/FF
%{_datadir}/games/vdrift/data/cars/TL2
%{_datadir}/games/vdrift/data/cars/XS

%files data-cars-extra
%defattr(644,root,root,755)
%{_datadir}/games/vdrift/data/cars/3S
%{_datadir}/games/vdrift/data/cars/AX2
%{_datadir}/games/vdrift/data/cars/C7
%{_datadir}/games/vdrift/data/cars/CS
%{_datadir}/games/vdrift/data/cars/CT
%{_datadir}/games/vdrift/data/cars/F1
%{_datadir}/games/vdrift/data/cars/FE
%{_datadir}/games/vdrift/data/cars/G4
%{_datadir}/games/vdrift/data/cars/GT
%{_datadir}/games/vdrift/data/cars/M3
%{_datadir}/games/vdrift/data/cars/M7
%{_datadir}/games/vdrift/data/cars/M8
%{_datadir}/games/vdrift/data/cars/MC
%{_datadir}/games/vdrift/data/cars/MI
%{_datadir}/games/vdrift/data/cars/NS
%{_datadir}/games/vdrift/data/cars/RG
%{_datadir}/games/vdrift/data/cars/RS2
%{_datadir}/games/vdrift/data/cars/SB
%{_datadir}/games/vdrift/data/cars/T73
%{_datadir}/games/vdrift/data/cars/TC
%{_datadir}/games/vdrift/data/cars/TL
%{_datadir}/games/vdrift/data/cars/XG
%{_datadir}/games/vdrift/data/cars/XM
%{_datadir}/games/vdrift/data/cars/Z06

%files data-tracks-base
%defattr(644,root,root,755)
%{_datadir}/games/vdrift/data/tracks/lagunaseca
%{_datadir}/games/vdrift/data/tracks/zandvoort

%files data-tracks-extra
%defattr(644,root,root,755)
%{_datadir}/games/vdrift/data/tracks/barcelona
%{_datadir}/games/vdrift/data/tracks/brands
%{_datadir}/games/vdrift/data/tracks/detroit
%{_datadir}/games/vdrift/data/tracks/dijon
%{_datadir}/games/vdrift/data/tracks/hockenheim
%{_datadir}/games/vdrift/data/tracks/jarama
%{_datadir}/games/vdrift/data/tracks/kyalami
%{_datadir}/games/vdrift/data/tracks/lemans
%{_datadir}/games/vdrift/data/tracks/monaco
%{_datadir}/games/vdrift/data/tracks/monza
%{_datadir}/games/vdrift/data/tracks/mosport
%{_datadir}/games/vdrift/data/tracks/neurburgring_nordschleife
%{_datadir}/games/vdrift/data/tracks/pau
%{_datadir}/games/vdrift/data/tracks/road_atlanta
%{_datadir}/games/vdrift/data/tracks/ruudskogen
%{_datadir}/games/vdrift/data/tracks/spa
%{_datadir}/games/vdrift/data/tracks/weekend
