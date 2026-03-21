# nexus-crypter
x64 pe packer - signal: vertigo.66

## introduction:

nexus-crypter is a custom pe parser and packer written in C. it is designed to be paired with a loader stub that decrypts and executes the packed payload. 

every pe stub/loader gets burned the moment its source becomes public. the only way to stay ahead of this is to write your own custom one. i have included a template for you to fill out with your own code. this packer and stub template has been fully tested with a private fully functional stub, working on putty.exe, strings.exe, various other compiled exe's, as well as being able to pack itself. if you need help feel free to reach out on my signal: vertigo.66

## features:
* basic working compiled rolling xor stub (obfuscation not encryption)
* BYOS (bring your own stub)
* stub template
* extensive debug output (-DDEBUG & --debug flags)
* randomized config marker
* zeroed out optional headers
* secure key generation
* checksum recalculation
* pe section manipulation

## to-do:

my vision for this project is to eventually have a fully featured, working packer that rivals commercial products like themida, vmprotect, and others, but is open source and available to all. here are some features that will be added over the coming months/years:

* integrity checks
* compression
* pyinstaller support
* multiple working stub variants with different types of encryption and anti-debugging
* license support/hardware binding
* virtualization

## usage:
`.\nexus-crypter.exe [--debug] program.exe packed.exe`

<img align="center" width="1000" height="100%" src="img/splash.png" alt="nexus-crypter splashscreen">
<img align="center" width="1000" height="100%" src="img/putty.png" alt="putty debugging output">
<img align="center" width="1000" height="100%" src="img/die.png" alt="detect-it-easy">
<img align="center" width="1000" height="100%" src="img/die2.png" alt="detect-it-easy">

## compile:
**requirements:** 
* mingw64 tool suite available at `https://winlibs.com/`
* windbg or other debugger
* python interpreter for `clean.py`

**commands:**
* `.\gcc.exe stub.c -o stub.o [-DDEBUG] -fno-asynchronous-unwind-tables -fno-ident -fno-stack-protector`
* `.\ld.exe stub.o -o stub.exe -nostdlib --build-id=none -s --entry=_start`
* `.\objcopy.exe -O binary stub.exe stub.bin`
* `.\windres.exe resource.rc -o resource.o`
* `.\gcc.exe nexus-crypter.c resource.o -o nexus-crypter.exe -lbcrypt`

## license:
this software is licensed under a modified ACSL 1.4 license.





