Name:		texlive-pst-arrow
Version:	61069
Release:	1
Summary:	Special arrows for PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-arrow
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-arrow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-arrow.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package has all the code from the package pstricks-add
which was related to arrows, like multiple arrows and so on.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-arrow
%{_texmfdistdir}/tex/generic/pst-arrow
%doc %{_texmfdistdir}/doc/generic/pst-arrow

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
