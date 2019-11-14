#!/usr/bin/env python2

from __future__ import print_function
from triton     import ARCH, TritonContext, Instruction, MODE, MemoryAccess, CPUSIZE

import os
import sys

Triton = TritonContext()

instCount = 0
taintCount = 0

def emulate(pc):
    global instCount
    global taintCount

    astCtxt = Triton.getAstContext()
    print('[+] Starting emulation.')
    while pc:
        opcode = Triton.getConcreteMemoryAreaValue(pc, 16)

        instruction = Instruction()
        instruction.setOpcode(opcode)
        instruction.setAddress(pc)

        if instruction.getAddress() == 0x4005ba:
            Triton.taintRegister(Triton.registers.rsi)
            Triton.taintRegister(Triton.registers.rdi)

        Triton.processing(instruction)

        hookingHandler(Triton)

        if "call" in str(instruction):
            print('[call] %s' %(str(instruction)))

            ret_addr = Triton.getConcreteMemoryValue(MemoryAccess(Triton.getConcreteRegisterValue(Triton.registers.rsp), CPUSIZE.QWORD))

            Triton.setConcreteRegisterValue(Triton.registers.rip, ret_addr)

            Triton.setConcreteRegisterValue(Triton.registers.rsp, Triton.getConcreteRegisterValue(Triton.registers.rsp)+CPUSIZE.QWORD)


        instCount += 1
        if instruction.isTainted():
            print('[tainted] %s' %(str(instruction)))
            taintCount += 1
        else:
            #print(instruction)
            pass

        pc = Triton.getConcreteRegisterValue(Triton.registers.rip)

    print('[*] ' + str(instCount) + ' instructions emulated')
    print('[*] ' + str(taintCount) + ' instructions tainted')
    return

def hookingHandler(ctx):
    pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
    for rel in customRelocation:
        if rel[2] == pc:
            # Emulate the routine and the return value
            ret_value = rel[1](ctx)
            if ret_value is not None:
                ctx.setConcreteRegisterValue(ctx.registers.rax, ret_value)

            # Get the return address
            ret_addr = ctx.getConcreteMemoryValue(MemoryAccess(ctx.getConcreteRegisterValue(ctx.registers.rsp), CPUSIZE.QWORD))

            # Hijack RIP to skip the call
            ctx.setConcreteRegisterValue(ctx.registers.rip, ret_addr)

            # Restore RSP (simulate the ret)
            ctx.setConcreteRegisterValue(ctx.registers.rsp, ctx.getConcreteRegisterValue(ctx.registers.rsp)+CPUSIZE.QWORD)
    return

def putsHandler(ctx):
    debug('[+] puts hooked')

    # Get arguments
    arg1 = getMemoryString(ctx, ctx.getConcreteRegisterValue(ctx.registers.rdi))
    sys.stdout.write(arg1 + '\n')

    # Return value
    return len(arg1) + 1

def loadBinary(path):
    import lief
    binary = lief.parse(path)
    phdrs  = binary.segments
    for phdr in phdrs:
        size   = phdr.physical_size
        vaddr  = phdr.virtual_address
        print('[+] Loading 0x%06x - 0x%06x' %(vaddr, vaddr+size))
        Triton.setConcreteMemoryAreaValue(vaddr, phdr.content)
    return

BASE_PLT = 0x10000000
customRelocation = [
    ('puts',              putsHandler,     BASE_PLT + 4),
]

if __name__ == '__main__':
    Triton.setArchitecture(ARCH.X86_64)

    Triton.setMode(MODE.ALIGNED_MEMORY, True)
    Triton.setMode(MODE.ONLY_ON_SYMBOLIZED, True)

    loadBinary(os.path.join(os.path.dirname(__file__), 'baby2'))

    Triton.setConcreteRegisterValue(Triton.registers.rbp, 0x7fffffff)
    Triton.setConcreteRegisterValue(Triton.registers.rsp, 0x6fffffff)

    Triton.setConcreteRegisterValue(Triton.registers.rdi, 0x10000000)

    for index in range(30):
        Triton.symbolizeMemory(MemoryAccess(0x10000000+index, CPUSIZE.BYTE))

    emulate(0x4005b6)

    sys.exit(0)
