Name:		texlive-tlc-article
Version:	51431
Release:	2
Summary:	A LaTeX document class for formal documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tlc-article
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlc-article.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlc-article.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LaTeX document class that orchestrates a
logical arrangement for document header, footer, author,
abstract, table of contents, and margins. It standardizes a
document layout intended for formal documents. The tlc_article
GitHub repository uses a SCRUM framework adapted to standard
GitHub tooling. tlc_article is integrated with Travis-ci.org
for continuous integration and AllanConsulting.slack.com for
centralized notification.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tlc-article
%doc %{_texmfdistdir}/doc/latex/tlc-article

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
