# Liars in the Miller-Rabin primality test
Finding liars in the Miller-Rabin Primality Test with Python. Learn more about the Miller-Rabin primality test [here](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test). Inspired by [Numberphile](https://www.youtube.com/watch?v=_MscGSN5J6o)

## Results (`n` is the number of witnesses, only top 100 liars in certain ranges, feel free to generate more!)
### 1 witness
#### `0 ≤ n < 99`
| Witness | Number of lies |
|---------|----------------|
| 1       | 24             |
| 0       | 21             |
| 74      | 5              |
| 76      | 5              |
| 82      | 5              |
| 38      | 4              |
| 62      | 4              |
| 68      | 4              |
| 79      | 4              |
| 18      | 3              |
| 22      | 3              |
| 26      | 3              |
| 29      | 3              |
| 31      | 3              |
| 34      | 3              |
| 43      | 3              |
| 44      | 3              |
| 46      | 3              |
| 47      | 3              |
| 53      | 3              |
| 57      | 3              |
| 64      | 3              |
| 67      | 3              |
| 69      | 3              |
| 80      | 3              |
| 83      | 3              |
| 86      | 3              |
| 89      | 3              |
| 91      | 3              |
| 92      | 3              |
| 94      | 3              |
| 98      | 3              |
| 13      | 2              |
| 16      | 2              |
| 17      | 2              |
| 19      | 2              |
| 32      | 2              |
| 41      | 2              |
| 50      | 2              |
| 51      | 2              |
| 52      | 2              |
| 55      | 2              |
| 56      | 2              |
| 58      | 2              |
| 59      | 2              |
| 61      | 2              |
| 65      | 2              |
| 66      | 2              |
| 71      | 2              |
| 73      | 2              |
| 77      | 2              |
| 78      | 2              |
| 85      | 2              |
| 88      | 2              |
| 93      | 2              |
| 97      | 2              |
| 7       | 1              |
| 8       | 1              |
| 9       | 1              |
| 10      | 1              |
| 11      | 1              |
| 12      | 1              |
| 14      | 1              |
| 20      | 1              |
| 23      | 1              |
| 24      | 1              |
| 28      | 1              |
| 30      | 1              |
| 33      | 1              |
| 36      | 1              |
| 37      | 1              |
| 39      | 1              |
| 40      | 1              |
| 48      | 1              |
| 49      | 1              |
| 54      | 1              |
| 70      | 1              |
| 72      | 1              |
| 75      | 1              |
| 81      | 1              |
| 84      | 1              |
| 87      | 1              |
| 90      | 1              |
| 95      | 1              |
| 96      | 1              |
| 2       | 0              |
| 3       | 0              |
| 4       | 0              |
| 5       | 0              |
| 6       | 0              |
| 15      | 0              |
| 21      | 0              |
| 25      | 0              |
| 27      | 0              |
| 35      | 0              |
| 42      | 0              |
| 45      | 0              |
| 60      | 0              |
| 63      | 0              |

#### `0 ≤ n < 999`
| Witness | Number of lies |
|---------|----------------|
| 0       | 164            |
| 676     | 18             |
| 901     | 18             |
| 374     | 17             |
| 944     | 16             |
| 766     | 15             |
| 824     | 15             |
| 900     | 15             |
| 946     | 15             |
| 989     | 15             |
| 293     | 14             |
| 307     | 14             |
| 524     | 14             |
| 557     | 14             |
| 584     | 14             |
| 638     | 14             |
| 734     | 14             |
| 526     | 13             |
| 562     | 13             |
| 566     | 13             |
| 568     | 13             |
| 776     | 13             |
| 818     | 13             |
| 874     | 13             |
| 904     | 13             |
| 976     | 13             |
| 256     | 12             |
| 274     | 12             |
| 278     | 12             |
| 316     | 12             |
| 373     | 12             |
| 419     | 12             |
| 460     | 12             |
| 571     | 12             |
| 606     | 12             |
| 631     | 12             |
| 674     | 12             |
| 694     | 12             |
| 704     | 12             |
| 712     | 12             |
| 736     | 12             |
| 782     | 12             |
| 898     | 12             |
| 899     | 12             |
| 926     | 12             |
| 932     | 12             |
| 974     | 12             |
| 991     | 12             |
| 995     | 12             |
| 68      | 11             |
| 149     | 11             |
| 157     | 11             |
| 191     | 11             |
| 230     | 11             |
| 242     | 11             |
| 268     | 11             |
| 302     | 11             |
| 362     | 11             |
| 386     | 11             |
| 398     | 11             |
| 411     | 11             |
| 426     | 11             |
| 451     | 11             |
| 467     | 11             |
| 482     | 11             |
| 494     | 11             |
| 501     | 11             |
| 514     | 11             |
| 521     | 11             |
| 538     | 11             |
| 626     | 11             |
| 628     | 11             |
| 629     | 11             |
| 649     | 11             |
| 652     | 11             |
| 664     | 11             |
| 757     | 11             |
| 781     | 11             |
| 802     | 11             |
| 803     | 11             |
| 809     | 11             |
| 820     | 11             |
| 826     | 11             |
| 841     | 11             |
| 854     | 11             |
| 862     | 11             |
| 881     | 11             |
| 892     | 11             |
| 993     | 11             |
| 998     | 11             |
| 166     | 10             |
| 209     | 10             |
| 211     | 10             |
| 221     | 10             |
| 226     | 10             |
| 244     | 10             |
| 295     | 10             |
| 314     | 10             |
| 352     | 10             |

#### `0 < n < 4999`
| Witness | Number of liars |
|---------|-----------------|
| 0       | 665             |
| 4096    | 70              |
| 256     | 39              |
| 4624    | 36              |
| 4724    | 36              |
| 1432    | 33              |
| 2474    | 33              |
| 4117    | 33              |
| 4952    | 33              |
| 1296    | 32              |
| 1451    | 32              |
| 1918    | 32              |
| 4562    | 32              |
| 3464    | 31              |
| 4124    | 31              |
| 4852    | 31              |
| 4951    | 31              |
| 2414    | 30              |
| 3194    | 30              |
| 3449    | 30              |
| 4726    | 30              |
| 4913    | 30              |
| 1322    | 29              |
| 1576    | 29              |
| 1607    | 29              |
| 2393    | 29              |
| 2582    | 29              |
| 2834    | 29              |
| 3446    | 29              |
| 3466    | 29              |
| 4094    | 29              |
| 4274    | 29              |
| 4454    | 29              |
| 1303    | 28              |
| 1816    | 28              |
| 1844    | 28              |
| 2116    | 28              |
| 2789    | 28              |
| 2971    | 28              |
| 3149    | 28              |
| 3376    | 28              |
| 3536    | 28              |
| 3674    | 28              |
| 4330    | 28              |
| 901     | 27              |
| 1156    | 27              |
| 1207    | 27              |
| 1979    | 27              |
| 2382    | 27              |
| 2729    | 27              |
| 2792    | 27              |
| 3044    | 27              |
| 3106    | 27              |
| 3136    | 27              |
| 3254    | 27              |
| 3314    | 27              |
| 3571    | 27              |
| 3656    | 27              |
| 3926    | 27              |
| 4079    | 27              |
| 4086    | 27              |
| 4232    | 27              |
| 4276    | 27              |
| 4346    | 27              |
| 4558    | 27              |
| 4747    | 27              |
| 4924    | 27              |
| 16      | 26              |
| 374     | 26              |
| 676     | 26              |
| 900     | 26              |
| 1174    | 26              |
| 1832    | 26              |
| 1889    | 26              |
| 2078    | 26              |
| 2174    | 26              |
| 2458    | 26              |
| 2536    | 26              |
| 2806    | 26              |
| 3526    | 26              |
| 3781    | 26              |
| 3826    | 26              |
| 4164    | 26              |
| 4589    | 26              |
| 4713    | 26              |
| 4749    | 26              |
| 4784    | 26              |
| 4934    | 26              |
| 874     | 25              |
| 1101    | 25              |
| 1568    | 25              |
| 1574    | 25              |
| 1699    | 25              |
| 1772    | 25              |
| 2267    | 25              |
| 2836    | 25              |
| 2876    | 25              |
| 2906    | 25              |
| 2974    | 25              |

More results coming soon.
