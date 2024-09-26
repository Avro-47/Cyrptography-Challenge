import binascii
import math
import struct
from os import close
from shlex import join
from typing import Counter
from venv import create

Frequency_Table = {
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
    }

def English_Test(mystr: str):
    c = Counter(mystr.lower())
    total_characters = len(mystr)

    # This *Should* be the fancy math bs that I keep finding
    coefficient = sum(math.sqrt(Frequency_Table.get(char, 0) * y/total_characters) for char, y in c.items())
    return coefficient

def English_Check(results: str):
    sorter = [(English_Test(r[0]), r[0], r[0]) for r in results]
    sorter.sort(key=lambda x: x[0], reverse=True)
    winner = sorter[0]

    return winner

def Xor_Check(encoded: str, number: int):
    mystr = bytes.fromhex(encoded)
    for xor_key in range(256):
        decoded = ''.join(chr(b ^ xor_key) for b in mystr)
        # trying to chekc the value englishness of text
        English_Check(decoded)

        if decoded.isprintable() and decoded.isascii():



            # my work around for printing the key, line that the cipher was on, plus decoded message in one line
            OUTPUT = ''.join(str(xor_key))
            OUTPUT += ''.join("  ")
            OUTPUT += ''.join(str(i))
            OUTPUT += ''.join("  ")
            OUTPUT += ''.join(decoded)
            OUTPUT += '\n'
            #print(OUTPUT)
            OutputData.write(OUTPUT)           
#TODO                                             
#Print a space between sets of strings. Still not done, but a reasonable alternative has been implemented.  

OutputData = open(r"Challenge4Output","w")

# lines = len(Data.readlines())
with open('D:\Code files\GItRepo\Cyrptography-Challenge\Set 1\Challenge4data') as f: #This goes through ALL lines
    Current_Winner = None       #Start of new code attempting to sort though results 
    Current_Winner_Score = 0    #Start of new code attempting to sort though results 

    for i, line in enumerate(f, start=1):                                            #This goes through ALL lines
        Xor_Check(line, i)
        



f.close()
OutputData.close()

# FILE IS NOT COMPLETED. WILL NOT RUN. HAS BEEN ABANDONED IN FAVOR OF NEW APROACH. 
#          LAST VALID RESULTS ARE AS FOLLOWS
#       97  197  ^z;U^b)SxZt])NvdXNc~>h2Hm-"PJW
#       98  197  ]y8V]a*P{Yw^*Mug[M`}=k1Kn.!SIT
#       99  197  \x9W\`+QzXv_+LtfZLa|<j0Jo/ RHU
#       101  197  Z~?QZf-W|^pY-Jr`\Jgz:l6Li)&TNS
#       103  197  X|=SXd/U~\r[/Hpb^Hex8n4Nk+$VLQ
#       105  197  Vr3]Vj![pR|U!F~lPFkv6`:@e%*XB_
#       107  197  Tp1_Th#YrP~W#D|nRDit4b8Bg'(Z@]
#       108  197  Sw6XSo$^uWyP$C{iUCns3e?E` /]GZ
#       109  197  Rv7YRn%_tVxQ%BzhTBor2d>Da!.\F[
#       110  197  Qu4ZQm&\wU{R&AykWAlq1g=Gb"-_EX
#       111  197  Pt5[Pl']vTzS'@xjV@mp0f<Fc#,^DY
#       112  197  Ok*DOs8BiKeL8_guI_ro/y#Y|<3A[F
#       113  197  Nj+ENr9ChJdM9^ftH^sn.x"X}=2@ZG
#       114  197  Mi(FMq:@kIgN:]ewK]pm-{![~>1CYD
#       116  197  Ko.@Kw<FmOaH<[cqM[vk+}']x87E_B
#       117  197  Jn/AJv=GlN`I=ZbpLZwj*|&\y96D^C
#       119  197  Hl-CHt?EnLbK?X`rNXuh(~$^{;4F\A
#       120  197  Gc"LG{0JaCmD0Wo}AWzg'q+Qt4;ISN
#       121  197  Fb#MFz1K`BlE1Vn|@V{f&p*Pu5:HRO
#       123  197  D`!ODx3Ib@nG3Tl~BTyd$r(Rw78JPM
#       126  197  Ae$JA}6LgEkB6Qi{GQ|a!w-Wr2=OUH
#       127  197  @d%K@|7MfDjC7PhzFP}` v,Vs3<NTI
#       96  227  W1[Mj.^2qWJZaS,=1cl&&^W6IlmnrB
#       97  227  V0ZLk/_3pVK[`R-<0bm''_V7HmlosC
#       98  227  U3YOh,\0sUHXcQ.?3an$$\U4Knolp@
#       99  227  T2XNi-]1rTIYbP/>2`o%%]T5JonmqA
#       100  227  S5_In*Z6uSN^eW(95gh""ZS2MhijvF
#       101  227  R4^Ho+[7tRO_dV)84fi##[R3LihkwG
#       102  227  Q7]Kl(X4wQL\gU*;7ej  XQ0OjkhtD
#       103  227  P6\Jm)Y5vPM]fT+:6dk!!YP1NkjiuE
#       104  227  _9SEb&V:y_BRi[$59kd..V_>AdefzJ
#       105  227  ^8RDc'W;x^CShZ%48je//W^?@edg{K
#       106  227  ];QG`$T8{]@PkY&7;if,,T]<CfgdxH
#       107  227  \:PFa%U9z\AQjX'6:hg--U\=BgfeyI
#       108  227  [=WAf"R>}[FVm_ 1=o`**R[:E`ab~N
#       111  227  X>TBe!Q=~XEUn\#2>lc))QX9Fcba}M
#       112  227  G!K]z>N"aGZJqC<-!s|66NG&Y|}~bR
#       116  227  C%OY~:J&eC^NuG8)%wx22JC"]xyzfV
#       118  227  A'M[|8H$gA\LwE:+'uz00HA _z{xdT
#       119  227  @&LZ}9I%f@]MvD;*&t{11I@!^{zyeU
#       120  227  O)CUr6F*iORByK4%){t>>FO.QtuvjZ
#       121  227  N(BTs7G+hNSCxJ5$(zu??GN/Putwk[
#       122  227  M+AWp4D(kMP@{I6'+yv<<DM,SvwthX
#       123  227  L*@Vq5E)jLQAzH7&*xw==EL-RwvuiY
#       125  227  J,FPw3C/lJWG|N1 ,~q;;CJ+Tqpso_
#       127  227  H.DRu1A-nHUE~L3".|s99AH)Vsrqm]
#       96  232  urWqyellq"D:`/cV0(xPCjyEh<zwGF
#       97  232  tsVpxdmmp#E;a.bW1)yQBkxDi={vFG
#       98  232  wpUs{gnns F8b-aT2*zRAh{Gj>xuED
#       99  232  vqTrzfoor!G9c,`U3+{S@izFk?ytDE
#       100  232  qvSu}ahhu&@>d+gR4,|TGn}Al8~sCB
#       105  232  |{^xpleex+M3i&j_9!qYJcpLa5s~NO
#       107  232  ~y\zrnggz)O1k$h];#s[HarNc7q|LM
#       108  232  y~[}ui``}.H6l#oZ<$t\OfuId0v{KJ
#       111  232  z}X~vjcc~-K5o lY?'w_LevJg3uxHI
#       112  232  ebGaiu||a2T*p?sF 8h@SziUx,jgWV
#       113  232  dcF`ht}}`3U+q>rG!9iAR{hTy-kfVW
#       114  232  g`Eckw~~c0V(r=qD":jBQxkWz.heUT
#       116  232  afCemqxxe6P.t;wB$<lDW~mQ|(ncSR
#       118  232  cdAgoszzg4R,v9u@&>nFU|oS~*laQP
#       120  232  mjOia}tti:\"x7{N(0`H[ra]p$bo_^
#       121  232  lkNh`|uuh;]#y6zO)1aIZs`\q%cn^_
#       123  232  niLjb~wwj9_!{4xM+3cKXqb^s'al\]
#       125  232  hoJldxqql?Y'}2~K-5eM^wdXu!gjZ[
#       126  232  klIog{rro<Z$~1}H.6fN]tg[v"diYX
#       98  297  T+C}Cf4g|Kmy.:/e+@nJiH21}DKc2\
#       99  297  U*B|Bg5f}Jlx/;.d*AoKhI30|EJb3]
#       101  297  S,DzDa3`{Lj~)=(b,GiMnO56zCLd5[
#       102  297  P/GyGb0cxOi}*>+a/DjNmL65y@Og6X
#       103  297  Q.FxFc1byNh|+?*`.EkOlM74xANf7Y
#       104  297  ^!IwIl>mvAgs$0%o!Jd@cB8;wNAi8V
#       105  297  _ HvHm?lw@fr%1$n KeAbC9:vO@h9W
#       106  297  \#KuKn<otCeq&2'm#HfBa@:9uLCk:T
#       107  297  ]"JtJo=nuBdp'3&l"IgC`A;8tMBj;U
#       108  297  Z%MsMh:irEcw 4!k%N`DgF<?sJEm<R
#       109  297  [$LrLi;hsDbv!5 j$OaEfG=>rKDl=S
#       110  297  X'OqOj8kpGau"6#i'LbFeD>=qHGo>P
#       111  297  Y&NpNk9jqF`t#7"h&McGdE?<pIFn?Q
#       113  297  G8PnPu'toX~j=)<v8S}Yz[!"nWXp!O
#       114  297  D;SmSv$wl[}i>*?u;P~ZyX"!mT[s"L
#       117  297  C<TjTq#pk\zn9-8r<Wy]~_%&jS\t%K
#       118  297  @?WiWr sh_ym:.;q?Tz^}\&%iP_w&H
#       119  297  A>VhVs!ri^xl;/:p>U{_|]'$hQ^v'I
#       121  297  O0XfX}/|gPvb5!4~0[uQrS)*f_Px)G
#       124  297  J5]c]x*ybUsg0$1{5^pTwV,/cZU},B
#       125  297  K4\b\y+xcTrf1%0z4_qUvW-.b[T|-C
#       127  297  I6^`^{)zaVpd3'2x6]sWtU/,`YV~/A
