%global _disable_lto 1

# git branches
#------------------------------------------------------------------

%define date 20250331
%define commit 2f8ed1a6bd7a6424e05c4425a647c9eecca13a91
%define commit_short %(echo %{commit} | head -c 7)

#------------------------------------------------------------------
# modules
%bcond_with modules
#------------------------------------------------------------------
%define libpng_ver 1.6.48
%bcond_with libpng_bundled

%define libpng_commit ea127968204cc5d10f3fc9250c306b9e8cbd9b80
%define libpng_short %(echo %{libpng_commit} | head -c 7)

%if %{without libpng_bundled}
%define USE_SYSTEM_LIBPNG USE_SYSTEM_LIBPNG=ON
%else
%define USE_SYSTEM_LIBPNG USE_SYSTEM_LIBPNG=OFF
%endif
#------------------------------------------------------------------
%define hidapi_ver 0.15.0
%bcond_without hidapi_bundled

%define hidapi_commit f42423643ec9011c98cccc0bb790722bbbd3f30b
%define hidapi_short %(echo %{hidapi_commit} | head -c 7)
#------------------------------------------------------------------
%define glslang_ver 15.3.0
%bcond_with use_system_glslang

%define glslang_commit 36d08c0d940cf307a23928299ef52c7970d8cee6
%define glslang_short %(echo %{glslang_commit} | head -c 7)
#------------------------------------------------------------------
%bcond_with use_system_pugixml

%define pugixml_commit ee86beb30e4973f5feffe3ce63bfa4fbadf72f38
%define pugixml_short %(echo %{pugixml_commit} | head -c 7)

%if %{with use_system_pugixml}
%define USE_SYSTEM_PUGIXML USE_SYSTEM_PUGIXML=ON
%else
%define USE_SYSTEM_PUGIXML USE_SYSTEM_PUGIXML=OFF
%endif
#------------------------------------------------------------------
%bcond_with use_system_openal

%define openal_commit dc7d7054a5b4f3bec1dc23a42fd616a0847af948
%define openal_short %(echo %{openal_commit} | head -c 7)

%if %{with use_system_openal}
%define USE_SYSTEM_OPENAL USE_SYSTEM_OPENAL=ON
%else
%define USE_SYSTEM_OPENAL USE_SYSTEM_OPENAL=OFF
%endif
#------------------------------------------------------------------
%define cubeb_commit 70b4e3db7822de4d534959885cda109d6edbee36
%define cubeb_short %(echo %{cubeb_commit} | head -c 7)
#------------------------------------------------------------------
%define asmjit_commit 416f7356967c1f66784dc1580fe157f9406d8bff
%define asmjit_short %(echo %{asmjit_commit} | head -c 7)
#------------------------------------------------------------------
%bcond_without use_system_faudio

%define FAudio_commit 6077ea740a7114a54f76ed9b7abe08cffc0034b6
%define FAudio_short %(echo %{FAudio_commit} | head -c 7)

%if %{with use_system_faudio}
%define USE_SYSTEM_FAUDIO USE_SYSTEM_FAUDIO=ON
%else
%define USE_SYSTEM_FAUDIO USE_SYSTEM_FAUDIO=OFF
%endif
#------------------------------------------------------------------
%define ffmpeg_ver 5.1.2

%bcond_without use_system_ffmpeg

%define ffmpeg_commit ec6367d3ba9d0d57b9d22d4b87da8144acaf428f
%define ffmpeg_short %(echo %{ffmpeg_commit} | head -c 7)

%if %{with use_system_ffmpeg}
%define USE_SYSTEM_FFMPEG USE_SYSTEM_FFMPEG=ON
%else
%define USE_SYSTEM_FFMPEG USE_SYSTEM_FFMPEG=OFF
%endif
#------------------------------------------------------------------
%bcond_with use_system_wolfssl

%define wolfssl_commit b077c81eb635392e694ccedbab8b644297ec0285
%define wolfssl_short %(echo %{wolfssl_commit} | head -c 7)

%if %{with use_system_wolfssl}
%define USE_SYSTEM_WOLFSSL USE_SYSTEM_WOLFSSL=ON
%else
%define USE_SYSTEM_WOLFSSL USE_SYSTEM_WOLFSSL=OFF
%endif
#------------------------------------------------------------------
%define libcurl_ver 8.3.0
# no static libs repository
%bcond_without use_system_curl

%define curl_commit 4dacb79fcdd9364c1083e06f6a011d797a344f47
%define curl_short %(echo %{curl_commit} | head -c 7)

%if %{with use_system_curl}
%define USE_SYSTEM_CURL USE_SYSTEM_CURL=ON
%else
%define USE_SYSTEM_CURL USE_SYSTEM_CURL=OFF
%endif
#------------------------------------------------------------------
%bcond_with soundtouch

%define soundtouch_commit 3982730833b6daefe77dcfb32b5c282851640c17
%define soundtouch_short %(echo %{soundtouch_commit} | head -c 7)
#------------------------------------------------------------------
%bcond_with spirv

#------------------------------------------------------------------
%bcond_with use_system_flatbuffers

%define flatbuffers_commit 595bf0007ab1929570c7671f091313c8fc20644e
#%%define flatbuffers_commit 06c5c7ed0bd987a918cf88caafb094f22cdd1721
%define flatbuffers_short %(echo %{flatbuffers_commit} | head -c 7)

%if %{with use_system_flatbuffers}
%define USE_SYSTEM_FLATBUFFERS USE_SYSTEM_FLATBUFFERS=ON
%else
%define USE_SYSTEM_FLATBUFFERS USE_SYSTEM_FLATBUFFERS=OFF
%endif
#------------------------------------------------------------------
%define yaml_cpp_commit 456c68f452da09d8ca84b375faa2b1397713eaba
%define yaml_cpp_short %(echo %{yaml_cpp_commit} | head -c 7)
#------------------------------------------------------------------
# no static libs repository
%bcond_with miniupnp

%define miniupnp_commit d66872e34d9ff83a07f8b71371b13419b2089953
%define miniupnp_short %(echo %{miniupnp_commit} | head -c 7)
#------------------------------------------------------------------
# Compile with JACK support OFF
%bcond_with rtmidi

%define rtmidi_commit 1e5b49925aa60065db52de44c366d446a902547b
%define rtmidi_short %(echo %{rtmidi_commit} | head -c 7)
#------------------------------------------------------------------
%bcond_without use_system_libusb

%define libusb_commit a61afe5f75d969c4561a1d0ad753aa23cee6329a
%define libusb_short %(echo %{libusb_commit} | head -c 7)

%if %{with use_system_libusb}
%define USE_SYSTEM_LIBUSB USE_SYSTEM_LIBUSB=ON
%else
%define USE_SYSTEM_LIBUSB USE_SYSTEM_LIBUSB=OFF
%endif

#------------------------------------------------------------------
%define zstd_commit f8745da6ff1ad1e7bab384bd1f9d742439278e99
%define zstd_short %(echo %{zstd_commit} | head -c 7)
#------------------------------------------------------------------
%bcond_without use_system_sdl

%define sdl_commit 8d604353a53853fa56d1bdce0363535605ca868f
%define sdl_short %(echo %{sdl_commit} | head -c 7)

%if %{with use_system_sdl}
%define USE_SYSTEM_SDL USE_SYSTEM_SDL=ON
%else
%define USE_SYSTEM_SDL USE_SYSTEM_SDL=OFF
%endif
#------------------------------------------------------------------
%bcond_without use_system_opencv

%define opencv_commit f76628fb5b25746fcb75a7ce85be0d8c6439fc57
%define opencv_short %(echo %{opencv_commit} | head -c 7)

%if %{with use_system_opencv}
%define USE_SYSTEM_OPENCV USE_SYSTEM_OPENCV=ON
%else
%define USE_SYSTEM_OPENCV USE_SYSTEM_OPENCV=OFF
%endif
#------------------------------------------------------------------
%bcond_without use_system_fusion

%define fusion_commit 066d4a63b2c714b20b0a8073a01fda7c5c6763f6
%define fusion_short %(echo %{fusion_commit} | head -c 7)
#------------------------------------------------------------------
# VulkanMemoryAllocator
%define gpuopen_commit 37064843398c69cc0ca7f8cf5b33128c03a2bd74
%define gpuopen_short %(echo %{fusion_commit} | head -c 7)
#------------------------------------------------------------------
%bcond_with clang

Summary:	PS3 emulator/debugger
Name:		rpcs3
Version:	0.0.36
Release:	1.%{date}.0
License:	GPLv2
Group:		Emulators
Url:		https://rpcs3.net/
Source0:	https://github.com/RPCS3/rpcs3/archive/%{commit}.tar.gz?/%{name}-%{version}.tar.gz
%if %{without modules}
Source1:	https://github.com/pnggroup/libpng/archive/%{libpng_commit}.tar.gz?/libpng-%{libpng_short}.tar.gz
Source2:	https://github.com/RPCS3/hidapi/archive/%{hidapi_commit}.tar.gz?/hidapi-%{hidapi_short}.tar.gz
Source4:	https://github.com/mozilla/cubeb/archive/%{cubeb_commit}.tar.gz?/cubeb-%{cubeb_short}.tar.gz
Source5:	https://github.com/asmjit/asmjit/archive/%{asmjit_commit}.tar.gz?/asmjit-%{asmjit_short}.tar.gz
Source6:	https://github.com/FNA-XNA/FAudio/archive/%{FAudio_commit}.tar.gz?/FAudio-%{FAudio_short}.tar.gz
Source7:	https://github.com/RPCS3/ffmpeg-core/archive/%{ffmpeg_commit}.tar.gz?/ffmpeg-%{ffmpeg_short}.tar.gz
Source8:	https://github.com/wolfSSL/wolfssl/archive/%{wolfssl_commit}.tar.gz?/wolfssl-%{wolfssl_short}.tar.gz
Source9:	https://github.com/curl/curl/archive/%{curl_commit}.tar.gz?/curl-%{curl_short}.tar.gz
Source10:	https://github.com/RPCS3/soundtouch/archive/%{soundtouch_commit}.tar.gz?/soundtouch-%{soundtouch_short}.tar.gz
Source11:	https://github.com/google/flatbuffers/archive/%{flatbuffers_commit}.tar.gz?/flatbuffers-%{flatbuffers_short}.tar.gz
Source12:	https://github.com/RPCS3/yaml-cpp/archive/%{yaml_cpp_commit}.tar.gz?/yaml-cpp-%{yaml_cpp_short}.tar.gz
Source13:	https://github.com/miniupnp/miniupnp/archive/%{miniupnp_commit}.tar.gz?/miniupnp-%{miniupnp_short}.tar.gz
Source14:	https://github.com/thestk/rtmidi/archive/%{rtmidi_commit}.tar.gz?/rtmidi-%{rtmidi_short}.tar.gz
Source15:	https://github.com/KhronosGroup/glslang/archive/%{glslang_commit}.tar.gz?/glslang-%{glslang_short}.tar.gz
Source16:	https://github.com/libusb/libusb/archive/%{libusb_commit}.tar.gz?/libusb-%{libusb_short}.tar.gz
Source17:	https://github.com/libsdl-org/SDL/archive/%{sdl_commit}.tar.gz?/sdl-%{sdl_short}.tar.gz
Source18:	https://github.com/zeux/pugixml/archive/%{pugixml_commit}.tar.gz?/pugixml-%{pugixml_short}.tar.gz
Source19:	https://github.com/facebook/zstd/archive/%{zstd_commit}.tar.gz?/zstd-%{zstd_short}.tar.gz
Source20:	https://github.com/kcat/openal-soft/archive/%{openal_commit}.tar.gz?/openal-%{openal_short}.tar.gz
Source21:	https://github.com/Megamouse/opencv_minimal/archive/%{opencv_commit}.tar.gz?/opencv-%{opencv_short}.tar.gz
Source22:	https://github.com/xioTechnologies/Fusion/archive/%{fusion_commit}.tar.gz?/fusion-%{fusion_short}.tar.gz
Source23:	https://github.com/Megamouse/VulkanMemoryAllocator/archive/%{gpuopen_commit}.tar.gz?/gpuopen-%{gpuopen_short}.tar.gz
Source100:	%{name}.rpmlintrc
%endif
Patch0:		rpcs3-stb-headers.patch
BuildRequires:  cmake
BuildRequires:  doxygen
# not have option USE_SYSTEM_ZSTD
#BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(stb)
%if %{with libpng_bundled}
BuildRequires: pkgconfig(libpng) >= %{libpng_ver}
%endif
%if %{without hidapi_bundled}
BuildRequires: hidapi-devel >= %{hidapi_ver}
%endif
%if %{with use_system_glslang}
BuildRequires: glslang-devel >= %{glslang_ver}
%endif
BuildRequires: pkgconfig(libpipewire-0.3)
%if %{with clang}
BuildRequires: clang
%endif
BuildRequires: llvm-devel
%if %{with use_system_ffmpeg}
BuildRequires: ffmpeg-devel > %{ffmpeg_ver}
%endif
%if %{with use_system_faudio}
BuildRequires: pkgconfig(FAudio)
%endif
BuildRequires: pkgconfig(glew)
%if %{with use_system_curl}
BuildRequires: pkgconfig(libcurl) > %{libcurl_ver}
%endif
%if %{with use_system_flatbuffers}
BuildRequires: pkgconfig(flatbuffers)
%endif
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libudev)
%if %{with use_system_libusb}
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: usb1.0-static-devel
%endif
%if %{with miniupnp}
BuildRequires: pkgconfig(miniupnpc)
%endif
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(opengl)
%if %{with use_system_pugixml}
BuildRequires: pkgconfig(pugixml)
%endif
%if %{with rtmidi}
BuildRequires: pkgconfig(rtmidi)
%endif
%if %{with soundtouch}
BuildRequires: pkgconfig(soundtouch)
%endif
BuildRequires: pkgconfig(yaml-cpp)
%if %{with use_system_sdl}
BuildRequires: pkgconfig(sdl2)
%endif
%if %{with use_system_opencv}
BuildRequires: pkgconfig(opencv)
%endif
BuildRequires: pkgconfig(vulkan)
%if %{without spirv}
BuildRequires: spirv-headers
BuildRequires: spirv-tools
%endif
BuildRequires: qt6-cmake
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6MultimediaWidgets)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6SvgWidgets)
BuildRequires: pkgconfig(Qt6Widgets)
ExclusiveArch: %{x86_64}

%description
The world's first free and open-source PlayStation 3 emulator/debugger,
written in C++ for Windows, Linux, macOS and FreeBSD.

%files
%license LICENSE
%doc *.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.{png,svg}
%{_metainfodir}/%{name}.metainfo.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/GuiConfigs
%{_datadir}/%{name}/GuiConfigs/*
%dir %{_datadir}/%{name}/Icons
%{_datadir}/%{name}/Icons/*
%dir %{_datadir}/%{name}/git
%{_datadir}/%{name}/git/*
%dir %{_datadir}/%{name}/test
%{_datadir}/%{name}/test/*

#------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{commit}

%if %{with libpng_bundled}
tar xf %{SOURCE1} --strip-components=1 \
 -C ${PWD}/3rdparty/libpng/libpng
%endif
%if %{with hidapi_bundled}
tar xf %{SOURCE2} --strip-components=1 \
 -C ${PWD}/3rdparty/hidapi/hidapi
%endif
tar xf %{SOURCE4} --strip-components=1 \
 -C ${PWD}/3rdparty/cubeb/cubeb
tar xf %{SOURCE5} --strip-components=1 \
 -C ${PWD}/3rdparty/asmjit/asmjit
%if %{without use_system_faudio}
tar xf %{SOURCE6} --strip-components=1 \
 -C ${PWD}/3rdparty/FAudio
%endif
%if %{without use_system_ffmpeg}
tar xf %{SOURCE7} --strip-components=1 \
 -C ${PWD}/3rdparty/ffmpeg
%endif
%if %{without use_system_wolfssl}
tar xf %{SOURCE8} --strip-components=1 \
 -C ${PWD}/3rdparty/wolfssl/wolfssl
%endif
%if %{without use_system_curl}
tar xf %{SOURCE9} --strip-components=1 \
 -C ${PWD}/3rdparty/curl/curl
%endif
%if %{without soundtouch}
tar xf %{SOURCE10} --strip-components=1 \
 -C ${PWD}/3rdparty/SoundTouch/soundtouch
%endif
%if %{without use_system_flatbuffers}
tar xf %{SOURCE11} --strip-components=1 \
 -C ${PWD}/3rdparty/flatbuffers
%endif
tar xf %{SOURCE12} --strip-components=1 \
 -C ${PWD}/3rdparty/yaml-cpp/yaml-cpp
%if %{without miniupnp}
tar xf %{SOURCE13} --strip-components=1 \
 -C ${PWD}/3rdparty/miniupnp/miniupnp
%endif
%if %{without rtmidi}
tar xf %{SOURCE14} --strip-components=1 \
 -C ${PWD}/3rdparty/rtmidi/rtmidi
%endif
%if %{without use_system_glslang}
tar xf %{SOURCE15} --strip-components=1 \
 -C ${PWD}/3rdparty/glslang/glslang
%endif
%if %{without use_system_libusb}
tar xf %{SOURCE16} --strip-components=1 \
 -C ${PWD}/3rdparty/libusb/libusb
%endif
%if %{without use_system_sdl}
tar xf %{SOURCE17} --strip-components=1 \
 -C ${PWD}/3rdparty/libsdl-org/SDL
%endif
%if %{without use_system_pugixml}
tar xf %{SOURCE18} --strip-components=1 \
 -C ${PWD}/3rdparty/pugixml
%endif

tar xf %{SOURCE19} --strip-components=1 \
 -C ${PWD}/3rdparty/zstd/zstd

%if %{without use_system_openal}
tar xf %{SOURCE20} --strip-components=1 \
 -C ${PWD}/3rdparty/OpenAL/openal-soft
%endif
%if %{without use_system_opencv}
tar xf %{SOURCE21} --strip-components=1 \
 -C ${PWD}/3rdparty/opencv/opencv
%endif
tar xf %{SOURCE22} --strip-components=1 \
 -C ${PWD}/3rdparty/fusion/fusion

tar xf %{SOURCE23} --strip-components=1 \
 -C ${PWD}/3rdparty/GPUOpen/VulkanMemoryAllocator

find . -name ".gitmodules" -delete

%build
%cmake -Wno-dev                         \
%if %{with clang}
 -D CMAKE_C_COMPILER=%(which clang)     \
 -D CMAKE_CXX_COMPILER=%(which clang++) \
%endif
 -D BUILD_SHARED_LIBS=OFF               \
 -D BUILD_STATIC_LIBS=ON                \
 -D %{USE_SYSTEM_FAUDIO}                \
 -D %{USE_SYSTEM_SDL}                   \
 -D %{USE_SYSTEM_LIBUSB}                \
 -D %{USE_SYSTEM_LIBPNG}                \
 -D %{USE_SYSTEM_OPENAL}                \
 -D %{USE_SYSTEM_OPENCV}                \
 -D %{USE_SYSTEM_PUGIXML}               \
 -D %{USE_SYSTEM_WOLFSSL}               \
 -D WITH_LLVM=OFF                       \
 -D BUILD_LLVM=OFF                      \
 -D %{USE_SYSTEM_FFMPEG}                \
 -D %{USE_SYSTEM_CURL}                  \
 -D %{USE_SYSTEM_FLATBUFFERS}

%make_build -s

%install
%make_install -C build

%_fixperms %{buildroot}
