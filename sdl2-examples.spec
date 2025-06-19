Name: sdl2-examples
Version: 1.0
Release: alt1
Summary: Collection of SDL2 examples with Makefile and other languages
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/xyproto/sdl2-examples
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-altlinux
BuildRequires: gcc-c++ libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel
BuildRequires: golang python3 python3-module-pygame rust-cargo

%description
A collection of SDL2 examples using Makefile for C/C++ and support for Python, Go, and Rust.

%prep
%setup -q -n %name-%version

%build
for dir in c89 c99 c11 c18 c2x; do
    pushd $dir
    make
    popd
done
for dir in c++98 c++11; do
    pushd $dir
    make
    popd
done
pushd go
for f in *.go; do
    go build "$f"
done
popd
chmod +x python/main.py
pushd rust
cargo build --release
popd

%install
install -d %buildroot%_bindir
install -d %buildroot%_desktopdir

for dir in c89 c99 c11 c18 c2x; do
    install -m 755 $dir/hello %buildroot%_bindir/sdl2-example-$dir-hello
    cat > %buildroot%_desktopdir/sdl2-example-$dir-hello.desktop <<EOF
[Desktop Entry]
Name=SDL2 Example $dir Hello
Exec=%_bindir/sdl2-example-$dir-hello
Icon=application-x-executable
Type=Application
Categories=Game;
EOF
done
for dir in c++98 c++11; do
    install -m 755 $dir/hello %buildroot%_bindir/sdl2-example-$dir-hello
    cat > %buildroot%_desktopdir/sdl2-example-$dir-hello.desktop <<EOF
[Desktop Entry]
Name=SDL2 Example $dir Hello
Exec=%_bindir/sdl2-example-$dir-hello
Icon=application-x-executable
Type=Application
Categories=Game;
EOF
done
install -m 755 go/main %buildroot%_bindir/sdl2-example-go-main
cat > %buildroot%_desktopdir/sdl2-example-go-main.desktop <<EOF
[Desktop Entry]
Name=SDL2 Example Go Main
Exec=%_bindir/sdl2-example-go-main
Icon=application-x-executable
Type=Application
Categories=Game;
EOF
install -m 755 python/main.py %buildroot%_bindir/sdl2-example-python-main
cat > %buildroot%_desktopdir/sdl2-example-python-main.desktop <<EOF
[Desktop Entry]
Name=SDL2 Example Python Main
Exec=python3 %_bindir/sdl2-example-python-main
Icon=application-x-executable
Type=Application
Categories=Game;
EOF
install -m 755 rust/target/release/rust %buildroot%_bindir/sdl2-example-rust
cat > %buildroot%_desktopdir/sdl2-example-rust.desktop <<EOF
[Desktop Entry]
Name=SDL2 Example Rust
Exec=%_bindir/sdl2-example-rust
Icon=application-x-executable
Type=Application
Categories=Game;
EOF

%files
%_bindir/sdl2-example-*
%_desktopdir/sdl2-example-*.desktop

%changelog
* Thu Jun 19 2025 Gleb <pitsentiy@inbox.ru> 1.0-alt1
- Initial build with Makefile-based and Python, Go, Rust SDL2 examples
