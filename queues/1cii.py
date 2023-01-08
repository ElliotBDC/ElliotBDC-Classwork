def deQueue():
    if kBuffer.size() == 0:
        return "kBuffer is empty"
    else:
        Tmp = kBuffer[front]
        kBuffer.pop(front)
    return Tmp
    #endif
 #endfunction
