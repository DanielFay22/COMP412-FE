    loadI   1024    => r1
    loadI   4       => r5
    add     r1, r5  => r1
    load    r1      => r4
    store   r3      => r1
    lshift  r2, r4 => r2
    lshift  r4, r7   =>      r8
    lshift  r4, r2 => r4
    mult    r3, r3   => r3
    rshift  r6, r3   =>      r7
    loadI   16      =>      r2
    add     r3, r1 => r1
    load    r1 => r2
    add     r4, r2   => r4
    mult    r2, r3   => r4
    store   r4      => r1
    loadI   0       =>      r3
    sub     r1, r5  => r1
    loadI   1024    => r1
    add     r4, r3   =>      r5
    sub     r2, r3   => r3
    loadI   4       => r5
    loadI   4       => r3
    sub     r1, r3 => r1
    mult    r3, r4 => r4
    load    r1 => r4
    loadI   4  => r3
    add     r3, r4   =>      r5
    mult    r3, r2 => r2
    sub     r5, r9   =>      r9
    loadI   166     => r2
    mult    r4, r8   =>      r3
    store   r4      => r1
    rshift  r3, r5   => r3
    store   r4 => r1
    sub     r5, r1   =>      r6
    mult    r2, r2   =>      r4
    store   r9      =>      r1
    loadI   1024 => r1
    store   r2 => r1
    output  1020
    output  1024