# Triton Scripts
Scripts for the dynamic binary analysis tool Triton

## Example 1: taint_baby2.py

Example of binary taint analysis using triton on the `baby2` challenge from UMDCTF2017. Finds all the instructions tainted by user input in the main function.

```
[+] Loading 0x400040 - 0x400238
[+] Loading 0x400238 - 0x400254
[+] Loading 0x400000 - 0x40f0d4
[+] Loading 0x60fe10 - 0x610048
[+] Loading 0x60fe28 - 0x60fff8
[+] Loading 0x400254 - 0x400298
[+] Loading 0x40efa8 - 0x40efdc
[+] Loading 0x000000 - 0x000000
[+] Loading 0x60fe10 - 0x610000
[+] Starting emulation.
[tainted] 0x4005c1: mov dword ptr [rbp - 0x1f44], edi
[tainted] 0x4005c7: mov qword ptr [rbp - 0x1f50], rsi
[call] 0x4005d3: call 0x400470
[call] 0x4005dd: call 0x400470
[call] 0x4005e7: call 0x400470
[call] 0x4005f1: call 0x400470
[call] 0x4005fb: call 0x400470
[call] 0x400605: call 0x400470
[call] 0x40060f: call 0x400470
[call] 0x400619: call 0x400470
[call] 0x400623: call 0x400470
[call] 0x40062d: call 0x400470
[call] 0x400637: call 0x400470
[call] 0x400641: call 0x400470
[call] 0x40064b: call 0x400470
[call] 0x400655: call 0x400470
[call] 0x40065f: call 0x400470
[call] 0x400669: call 0x400470
[call] 0x400673: call 0x400470
[call] 0x40067d: call 0x400470
[call] 0x400687: call 0x400470
[tainted] 0x403154: cmp dword ptr [rbp - 0x1f44], 2
[tainted] 0x40315b: je 0x40316e
[call] 0x403162: call 0x400470
[+] 1051 instructions emulated
[+] 4 instructions tainted
```

## Example 2: taint_hash.py

Another example of binary taint analysis script using Triton. Traces the instructions that are affected by user input throughout the hash function in the `hashmenot` binary. It discovers 364 tainted instructions.

```
chase@chase:~/github/triton-scripts/taint$ ./taint_hash.py 
[+] Loading 0x400040 - 0x400238
[+] Loading 0x400238 - 0x400254
[+] Loading 0x400000 - 0x400ea4
[+] Loading 0x601e10 - 0x602090
[+] Loading 0x601e28 - 0x601ff8
[+] Loading 0x400254 - 0x400298
[+] Loading 0x400d50 - 0x400d8c
[+] Loading 0x000000 - 0x000000
[+] Loading 0x601e10 - 0x602000
[+] Starting emulation.
[tainted] 0x400a78: mov dword ptr [rbp - 0x44], edi
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[tainted] 0x400aab: mov ecx, dword ptr [rbp - 0x44]
[tainted] 0x400ab3: mov eax, ecx
[tainted] 0x400ab5: mul edx
[tainted] 0x400ab7: shr edx, 1
[tainted] 0x400ab9: mov eax, edx
[tainted] 0x400abb: add eax, eax
[tainted] 0x400abd: add eax, edx
[tainted] 0x400abf: sub ecx, eax
[tainted] 0x400ac1: mov edx, ecx
[tainted] 0x400ac3: mov edx, edx
[tainted] 0x400ac9: add rax, rdx
[tainted] 0x400ad6: mov eax, dword ptr [rbp - 0x44]
[tainted] 0x400ad9: add eax, 1
[tainted] 0x400ae1: mul edx
[tainted] 0x400ae3: mov eax, edx
[tainted] 0x400ae5: shr eax, 1
[tainted] 0x400ae7: mov dword ptr [rbp - 0x44], eax
[tainted] 0x400aee: cmp dword ptr [rbp - 0x44], 0
[tainted] 0x400af2: jne 0x400aab
[call] 0x400bba: call 0x4007c0
skipping...
[call] 0x400bd2: call 0x400760
skipping...
[*] 3144 instructions emulated
[*] 364 instructions tainted

```


