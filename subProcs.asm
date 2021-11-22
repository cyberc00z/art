title The subProcs.asm Subroutine (subProcs.asm)
;Description: Calling asm procedures in C with different calling conventions
; Date
.386P
.model flat ;No convention
.stack 4096

.code 

ProcC_CallWithParameterList PROC C, x:DWORD, y:DWORD

   mov  eax, x
   sub  eax, y
   ret

PorcC_CallWithParameterList endp

_ProcC_CallWithStackFrame PROC near

  push    ebp
  mov     ebp, esp

  mov     eax,[ebp+8]
  sub     eax, [ebp+12]

  pop     ebp
  ret

_ProcC_CallWithStackFrame endp

ProcSTD_CallWithParameterList  PROC stdcall, x:DWORD, y:DWORD

  mov   eax, x
  sub   eax, y
  ret

ProcC_CallWithParameterList  endp

_ProcSTD_CallWithStack@8 PROC near

  push  ebp
  mov   ebp, esp

  mov   eax,[ebp+8]
  sub   eax,[ebp+12]

  pop   ebp
  ret  8

_ProcSTD_CallWithStackFrame@8 endp

ReadFromConsole  PROTO C, by:BYTE
DisplayToConsole PROTO C, s:PTR BYTE, n:DWORD

DoSubtraction  PROC C

.data
   text2Disp BYTE 'X-Y =', 0
   diff     DWORD ?
.code 

  INVOKE  ReadFromConsole, 'X'
  mov diff, eax
  INVOKE ReadFromConsole, 'Y'
  sub diff, eax
  INVOKE DisplayToConsole, OFFSET text2Disp, diff
  ret

DoSubtraction endp

end
