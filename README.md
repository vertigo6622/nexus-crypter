/*
*
*   __  _  ____ __  __ __ __  ____  ____ _____ __  _______  _____  ____ _____ 
*  |  \| || ===|\ \/ /|  |  |(_ (_`/ (__`| () )\ \/ /| ()_)|_   _|| ===|| () )
*  |_|\__||____|/_/\_\ \___/.__)__)\____)|_|\_\ |__| |_|     |_|  |____||_|\_\ v8
*   x64 pe packer - signal: vertigo.66
*
*   Features:
*   * BYOS (bring your own stub)
*   * Stub template available
*   * Extensive debug output (-DDEBUG & --debug flags)
*   * Randomized config marker
*
*   Compile:
*   .\gcc.exe stub.c -o stub.o [-DDEBUG] -fno-asynchronous-unwind-tables -fno-ident -fno-stack-protector
*   .\ld.exe stub.o -o stub.exe -nostdlib --build-id=none -s --entry=_start
*   .\objcopy.exe -O binary stub.exe stub.bin
*   .\windres.exe resource.rc -o resource.o 
*   .\gcc.exe nexus-crypter.c resource.o -o nexus-crypter.exe -lbcrypt
*
*/
